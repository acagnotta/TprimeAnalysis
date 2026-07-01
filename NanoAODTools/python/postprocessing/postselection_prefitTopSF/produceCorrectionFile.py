import json
import correctionlib.schemav2 as cs
import yaml
import sys
import os
import optparse

config = {}
config_paths = os.environ.get('PWD')+'/../config/config.yaml'
if os.path.exists(config_paths):
    with open(config_paths, "r") as _f:
        config = yaml.safe_load(_f) or {}
    print(f"Loaded config file from {config_paths}")
else:
    print(f"Config file not found in {config_paths}, exiting")
    sys.exit(1)

usage                   = "python3 produceCorrectionFile.py --era <era> --TopCategory <TopCategory>"
parser                  = optparse.OptionParser(usage)
parser.add_option(
                    "--era",
                    dest="era",
                    type=str,
                    default="2023",
                    help="Please enter the era, e.g. 2022, 2022EE, etc.",
                )

parser.add_option(
                    "--TopCategory",
                    dest="TopCategory",
                    type=str,
                    default="Mixed",
                    help="Top category for the histograms: Resolved, Mixed or Merged",
                )
(opt, args)             = parser.parse_args()
era                     = opt.era
TopCategory             = opt.TopCategory

outputfolder            = config["TrotaScaleFactor"]["outputfolder"][TopCategory][era]
inJsonName              = f"TrotaScaleFactors_{era}_{TopCategory}"
inFilePath              = f"{outputfolder}/ScaleFactors/{inJsonName}.json"
outJsonName             = f"TrotaScaleFactors_{era}"
corrLibFolder           = config["TrotaScaleFactor"]["corrlibfolder"][era]
outFilePath             = f"{corrLibFolder}/CorrLib_{outJsonName}.json"

def select_correct_sf(inputJsonFile, TopCat, wp_cat, TagCat, channel, type):
    output_sf_list = [1.0, 1.0, 1.0, 1.0] if type=="value" else [0.0, 0.0, 0.0, 0.0]  # Default values for the 4 bins
    if TopCat == "Resolved":
        if wp_cat in ["Loose", "Tight"]:
            if TagCat == "topmatched":
                output_sf_list[0] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][0]
                output_sf_list[1] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][1]
                output_sf_list[2] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][5]
                output_sf_list[3] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][5]
            elif TagCat == "nonmatched":
                output_sf_list[0] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][0]
                output_sf_list[1] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][1]
                output_sf_list[2] = output_sf_list[2]
                output_sf_list[3] = output_sf_list[3]
            elif TagCat == "other":
                output_sf_list[0] = output_sf_list[0]
                output_sf_list[1] = output_sf_list[1]
                output_sf_list[2] = output_sf_list[2]
                output_sf_list[3] = output_sf_list[3]

    if TopCat == "Mixed":
        if wp_cat in ["Loose", "Tight"]:
            if TagCat == "topmatched":
                output_sf_list[0] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][0]
                output_sf_list[1] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][1]
                output_sf_list[2] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][5]
                output_sf_list[3] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][5]
            elif TagCat == "nonmatched":
                output_sf_list[0] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][0]
                output_sf_list[1] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][1]
                output_sf_list[2] = output_sf_list[2]
                output_sf_list[3] = output_sf_list[3]
            elif TagCat == "other":
                output_sf_list[0] = output_sf_list[0]
                output_sf_list[1] = output_sf_list[1]
                output_sf_list[2] = output_sf_list[2]
                output_sf_list[3] = output_sf_list[3]

    if TopCat == "Merged":
        if wp_cat in ["Loose", "Tight"]:
            if TagCat == "topmatched":
                output_sf_list[0] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][4]
                output_sf_list[1] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][4]
                output_sf_list[2] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][5]
                output_sf_list[3] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][5]
            elif TagCat == "nonmatched":
                output_sf_list[0] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][4]
                output_sf_list[1] = inputJsonFile[TopCat][wp_cat][TagCat][channel][type][4]
                output_sf_list[2] = output_sf_list[2]
                output_sf_list[3] = output_sf_list[3]
            elif TagCat == "other":
                output_sf_list[0] = output_sf_list[0]
                output_sf_list[1] = output_sf_list[1]
                output_sf_list[2] = output_sf_list[2]
                output_sf_list[3] = output_sf_list[3]


    return output_sf_list

def produce_TrotaScaleFactors_dict(inputJsonFile):
    TrotaScaleFactors_dict = {}
    for TopCat in inputJsonFile.keys():
        TrotaScaleFactors_dict[TopCat] = {}
        for wp_cat in inputJsonFile[TopCat].keys():
            TrotaScaleFactors_dict[TopCat][wp_cat] = {}
            for TagCat in inputJsonFile[TopCat][wp_cat].keys():
                TrotaScaleFactors_dict[TopCat][wp_cat][TagCat] = {}
                for channel in inputJsonFile[TopCat][wp_cat][TagCat].keys():
                    TrotaScaleFactors_dict[TopCat][wp_cat][TagCat][channel] = {
                        "value": select_correct_sf(inputJsonFile, TopCat, wp_cat, TagCat, channel, "value"),
                        "error": select_correct_sf(inputJsonFile, TopCat, wp_cat, TagCat, channel, "error"),
                    }
    return TrotaScaleFactors_dict

os.makedirs(corrLibFolder, exist_ok=True)
with open(inFilePath, "r") as json_file:
    inputJsonFile       = json.load(json_file)
TrotaScaleFactors_dict  = produce_TrotaScaleFactors_dict(inputJsonFile)

def make_topcat_content(TrotaScaleFactors_dict, TopCat):
    return {
        "key": TopCat,
        "value": cs.Category(
            nodetype="category",
            input="wp_cat",
            content=[
                {
                    "key": wp_cat,
                    "value": cs.Category(
                        nodetype="category",
                        input="TagCat",
                        content=[
                            {
                                "key": TagCat,
                                "value": cs.Category(
                                    nodetype="category",
                                    input="channel",
                                    content=[
                                        {
                                            "key": channel,
                                            "value": cs.Category(
                                                nodetype="category",
                                                input="type",
                                                content=[
                                                    {
                                                        "key": "value",
                                                        "value": cs.Binning(
                                                            nodetype="binning",
                                                            input="TopCandidate_pt",
                                                            edges=[0, 200, 400, 600, 1000],
                                                            content=TrotaScaleFactors_dict[TopCat][wp_cat][TagCat][channel]["value"],
                                                            flow="clamp",
                                                        ),
                                                    },
                                                    {
                                                        "key": "error",
                                                        "value": cs.Binning(
                                                            nodetype="binning",
                                                            input="TopCandidate_pt",
                                                            edges=[0, 200, 400, 600, 1000],
                                                            content=TrotaScaleFactors_dict[TopCat][wp_cat][TagCat][channel]["error"],
                                                            flow="clamp",
                                                        ),
                                                    },
                                                ],
                                            ),
                                        }
                                        for channel in TrotaScaleFactors_dict[TopCat][wp_cat][TagCat].keys()
                                    ],
                                ),
                            }
                            for TagCat in TrotaScaleFactors_dict[TopCat][wp_cat].keys()
                        ],
                    ),
                }
                for wp_cat in TrotaScaleFactors_dict[TopCat].keys()
            ],
        ).dict(),
    }


def make_correction_set(TrotaScaleFactors_dict, TopCategory):
    corr = cs.Correction(
        name="TrotaScaleFactors",
        version=1,
        inputs=[
            cs.Variable(name="TopCat",          type="string", description="Top category: Resolved, Mixed, Merged"),
            cs.Variable(name="wp_cat",          type="string", description="working point category: Loose, LooseButNotTight, Tight"),
            cs.Variable(name="TagCat",          type="string", description="Tag category: topmatched, nonmatched, other"),
            cs.Variable(name="channel",         type="string", description="insert: pass, fail"),
            cs.Variable(name="type",            type="string", description="insert: value, error"),
            cs.Variable(name="TopCandidate_pt", type="real",   description="Top candidate pt"),
        ],
        output=cs.Variable(
            name="TrotaScaleFactor",
            type="real",
            description="Trota Top tagger scale factor",
        ),
        data=cs.Category(
            nodetype="category",
            input="TopCat",
            content=[
                make_topcat_content(TrotaScaleFactors_dict, TopCategory)
            ],
        ),
    )

    cset = cs.CorrectionSet(schema_version=2, corrections=[corr])
    return cset.dict()

def get_correction_by_name(cset_dict, correction_name):

    for correction in cset_dict["corrections"]:

        if correction["name"] == correction_name:

            return correction

    raise RuntimeError(f"Correction '{correction_name}' not found")
    
def insert_or_replace_topcat(cset_dict, new_topcat_content, TopCategory):
    corr            = get_correction_by_name(cset_dict, "TrotaScaleFactors")
    topcat_content  = corr["data"]["content"]

    for i, item in enumerate(topcat_content):
        if item["key"] == TopCategory:
            topcat_content[i] = new_topcat_content
            print(f"Replaced existing TopCat key: {TopCategory}")
            return cset_dict

    topcat_content.append(new_topcat_content)
    print(f"Added new TopCat key: {TopCategory}")

    return cset_dict


def create_or_update_correctionlib_file(TrotaScaleFactors_dict, outFilePath, TopCategory):
    if TopCategory not in TrotaScaleFactors_dict:
        print(f"ERROR: {TopCategory} not found in input JSON.")
        print(f"Available keys: {list(TrotaScaleFactors_dict.keys())}")
        sys.exit(1)

    new_topcat_content = make_topcat_content(TrotaScaleFactors_dict, TopCategory)

    if os.path.exists(outFilePath):
        print(f"Loading existing correctionlib file: {outFilePath}")

        with open(outFilePath, "r") as f:
            cset_dict = json.load(f)

        cset_dict = insert_or_replace_topcat(
            cset_dict,
            new_topcat_content,
            TopCategory,
        )

    else:
        print(f"Creating new correctionlib file: {outFilePath}")

        cset_dict = make_correction_set(
            TrotaScaleFactors_dict,
            TopCategory,
        )

    with open(outFilePath, "w") as f:
        json.dump(cset_dict, f, indent=2)

    print(f"Saved correctionlib file: {outFilePath}")


create_or_update_correctionlib_file(TrotaScaleFactors_dict, outFilePath, TopCategory)