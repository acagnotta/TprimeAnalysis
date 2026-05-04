#!/usr/bin/env python3
"""Generate LaTeX tables from Trota scale-factor JSON files.

Expected JSON structure:
{
  "2023": {
    "Mixed": {
      "topmatched": {
        "pass": {"value": [...], "error": [...]},
        "fail": {"value": [...], "error": [...]}
      },
      ...
    },
    "Resolved": {...},
    "Merged": {...}
  }
}

By default, the script looks for the categories Resolved, Mixed, and Merged.
For each era/category found, it prints one LaTeX table in the same style as the
one requested in the chat.

The working-point label is inferred from the input filename. For example:
- TrotaScaleFactors_Loose.json -> Loose
- TrotaScaleFactors_Tight.json -> Tight
- TrotaScaleFactors_LooseButNotTight.json -> LooseButNotTight
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

DEFAULT_CATEGORIES = ["Resolved", "Mixed", "Merged"]
DEFAULT_BIN_LABELS = ["[0,200[", "[200,400[", "[400,600[", "[600,1000)"]
DEFAULT_CHANNELS = ["pass", "fail"]
LATEX_NL = r"\\"
FILENAME_PREFIX = "TrotaScaleFactors_"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a Trota scale-factor JSON into LaTeX tables."
    )
    parser.add_argument("input_json", help="Path to the input JSON file")
    parser.add_argument(
        "-o",
        "--output",
        help="Optional output .tex file. If omitted, print to stdout.",
    )
    parser.add_argument(
        "--categories",
        default=",".join(DEFAULT_CATEGORIES),
        help=(
            "Comma-separated category names to export. "
            f"Default: {','.join(DEFAULT_CATEGORIES)}"
        ),
    )
    parser.add_argument(
        "--bin-labels",
        default=";".join(DEFAULT_BIN_LABELS),
        help=(
            "Semicolon-separated pT bin labels. Must match the number of values in each "
            "channel. Example: [0,200[;[200,400[;[400,600[;[600,1000)"
        ),
    )
    parser.add_argument(
        "--precision",
        type=int,
        default=6,
        help="Number of digits after the decimal point. Default: 6",
    )
    parser.add_argument(
        "--working-point",
        help=(
            "Optional override for the working-point label shown in the table title and "
            "caption. By default it is inferred from the input filename."
        ),
    )
    parser.add_argument(
        "--standalone",
        action="store_true",
        help="Wrap the output in a minimal standalone LaTeX document.",
    )
    return parser.parse_args()


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def normalize_requested_categories(raw: str) -> list[str]:
    categories = [item.strip() for item in raw.split(",") if item.strip()]
    if not categories:
        raise ValueError("No categories were provided.")
    return categories


def normalize_bin_labels(raw: str) -> list[str]:
    labels = [item.strip() for item in raw.split(";") if item.strip()]
    if not labels:
        raise ValueError("No bin labels were provided.")
    return labels


def resolve_categories(requested: Iterable[str], available: dict[str, object]) -> tuple[list[str], list[str]]:
    lower_to_actual = {name.lower(): name for name in available}
    found: list[str] = []
    missing: list[str] = []
    for name in requested:
        actual = lower_to_actual.get(name.lower())
        if actual is None:
            missing.append(name)
        else:
            found.append(actual)
    return found, missing


def format_float(value: float, precision: int) -> str:
    return f"{value:.{precision}f}"


def infer_working_point_label(input_path: Path) -> str:
    stem = input_path.stem
    if stem.startswith(FILENAME_PREFIX) and len(stem) > len(FILENAME_PREFIX):
        return stem[len(FILENAME_PREFIX) :]
    return stem


def sanitize_label_component(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def build_table(
    era: str,
    category: str,
    category_data: dict,
    bin_labels: list[str],
    precision: int,
    working_point: str,
) -> str:
    lines: list[str] = []
    title = f"{era} {category} {working_point}" if working_point else f"{era} {category}"
    caption = (
        f"Trota scale factors for the {working_point} working point in the {era} {category} category."
        if working_point
        else f"Trota scale factors for the {era} {category} category."
    )

    label_parts = ["tab", "trota", "sf", sanitize_label_component(era), sanitize_label_component(category)]
    if working_point:
        label_parts.append(sanitize_label_component(working_point))
    label = "_".join(part for part in label_parts if part)

    lines.append(r"\begin{table}[htbp]")
    lines.append(r"\centering")
    lines.append(r"\begin{tabular}{llccc}")
    lines.append(r"\hline")
    lines.append(rf"\multicolumn{{5}}{{c}}{{{latex_escape(title)}}} {LATEX_NL}")
    lines.append(r"\hline")
    lines.append(rf"Matching & Channel & $p_T$ bin & Value & Error {LATEX_NL}")
    lines.append(r"\hline")
    lines.append("")

    matching_items = list(category_data.items())
    for match_index, (matching, matching_data) in enumerate(matching_items):
        if not isinstance(matching_data, dict):
            raise ValueError(f"'{era}/{category}/{matching}' is not a dictionary.")

        total_rows = 0
        for channel in DEFAULT_CHANNELS:
            if channel in matching_data:
                channel_values = matching_data[channel].get("value", [])
                total_rows += len(channel_values)

        if total_rows == 0:
            continue

        first_row_of_matching = True
        for channel_index, channel in enumerate(DEFAULT_CHANNELS):
            if channel not in matching_data:
                continue

            channel_payload = matching_data[channel]
            if not isinstance(channel_payload, dict):
                raise ValueError(f"'{era}/{category}/{matching}/{channel}' is not a dictionary.")

            values = channel_payload.get("value", [])
            errors = channel_payload.get("error", [])
            if len(values) != len(errors):
                raise ValueError(
                    f"Mismatch in '{era}/{category}/{matching}/{channel}': "
                    f"{len(values)} values but {len(errors)} errors."
                )
            if len(values) != len(bin_labels):
                raise ValueError(
                    f"Mismatch in '{era}/{category}/{matching}/{channel}': "
                    f"{len(values)} entries but {len(bin_labels)} bin labels."
                )

            channel_rows = len(values)
            for row_index, (bin_label, value, error) in enumerate(zip(bin_labels, values, errors)):
                parts: list[str] = []
                if first_row_of_matching:
                    parts.append(rf"\multirow{{{total_rows}}}{{*}}{{{latex_escape(matching)}}}")
                    first_row_of_matching = False
                else:
                    parts.append("")

                if row_index == 0:
                    parts.append(rf"\multirow{{{channel_rows}}}{{*}}{{{latex_escape(channel)}}}")
                else:
                    parts.append("")

                parts.extend([
                    bin_label,
                    format_float(value, precision),
                    format_float(error, precision),
                ])
                lines.append(" & ".join(parts) + f" {LATEX_NL}")

            has_later_channel = any(next_ch in matching_data for next_ch in DEFAULT_CHANNELS[channel_index + 1 :])
            if has_later_channel:
                lines.append(r"\cdashline{2-5}")

        if match_index < len(matching_items) - 1:
            lines.append(r"\hline")
            lines.append("")

    lines.append(r"\hline")
    lines.append(r"\end{tabular}")
    lines.append(rf"\caption{{{latex_escape(caption)}}}")
    lines.append(rf"\label{{{label}}}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def build_document(body: str) -> str:
    return "\n".join(
        [
            r"\documentclass{article}",
            r"\usepackage{multirow}",
            r"\usepackage{arydshln}",
            r"\begin{document}",
            body,
            r"\end{document}",
        ]
    )


def main() -> int:
    args = parse_args()
    input_path = Path(args.input_json)
    if not input_path.exists():
        print(f"Error: file not found: {input_path}", file=sys.stderr)
        return 1

    try:
        requested_categories = normalize_requested_categories(args.categories)
        bin_labels = normalize_bin_labels(args.bin_labels)
        working_point = args.working_point.strip() if args.working_point else infer_working_point_label(input_path)
        with input_path.open() as handle:
            data = json.load(handle)
    except Exception as exc:
        print(f"Error while reading input: {exc}", file=sys.stderr)
        return 1

    if not isinstance(data, dict):
        print("Error: the JSON root must be a dictionary.", file=sys.stderr)
        return 1

    tables: list[str] = []
    warnings: list[str] = []

    for era, era_data in data.items():
        if not isinstance(era_data, dict):
            warnings.append(f"Skipping era '{era}' because its content is not a dictionary.")
            continue

        categories_found, categories_missing = resolve_categories(requested_categories, era_data)
        for missing in categories_missing:
            warnings.append(f"Category '{missing}' not found in era '{era}', skipping it.")

        for category in categories_found:
            category_data = era_data.get(category)
            if not isinstance(category_data, dict):
                warnings.append(
                    f"Skipping '{era}/{category}' because its content is not a dictionary."
                )
                continue
            try:
                tables.append(
                    build_table(
                        str(era),
                        category,
                        category_data,
                        bin_labels,
                        args.precision,
                        working_point,
                    )
                )
            except Exception as exc:
                print(f"Error while processing '{era}/{category}': {exc}", file=sys.stderr)
                return 1

    if not tables:
        print("Error: no tables were produced.", file=sys.stderr)
        return 1

    output_text = "\n\n".join(tables)
    if args.standalone:
        output_text = build_document(output_text)

    if args.output:
        Path(args.output).write_text(output_text)
    else:
        print(output_text)

    for warning in warnings:
        print(f"Warning: {warning}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
