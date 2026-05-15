import json
import argparse
import ROOT
import cmsstyle as CMS
ROOT.gROOT.SetBatch()
ROOT.gStyle.SetOptStat(0)

parser = argparse.ArgumentParser()
parser.add_argument("json_file")
parser.add_argument("--category",   default="Mixed",    choices=["Mixed", "Merged", "Resolved"])
parser.add_argument("--wp",         default="Loose",    choices=["Loose", "Tight", "LooseButNotTight"])
parser.add_argument("--channel",    default="pass",     choices=["pass", "fail"])
parser.add_argument("--output",     default="sf_map")
args = parser.parse_args()

with open(args.json_file) as f:
    data = json.load(f)

block = data[args.category][args.wp]

xlabels = ["[0,200[", "[200,400[", "[400,600[", "[600,1000)"]
matchings = ["topmatched", "nonmatched", "other"]
ylabels = ["topmatched", "nonmatched", "other"]

CMS.SetExtraText("Work in Progress")
CMS.SetLumi("")
c = CMS.cmsCanvas(
    "c",
    0, 4,
    0, 3,
    "",
    "",
    square=CMS.kRectangular,
    iPos=0,
    with_z_axis=True
)
c.SetLeftMargin(0.18)    # this is the main fix: your y labels are being cut
c.SetRightMargin(0.16)   # leave room for the color palette
c.SetBottomMargin(0.18)

h = ROOT.TH2F("h", "", 4, 0, 4, 3, 0, 3)

for ix, lab in enumerate(xlabels, start=1):
    h.GetXaxis().SetBinLabel(ix, lab)

for iy, lab in enumerate(ylabels, start=1):
    h.GetYaxis().SetBinLabel(iy, lab)

for iy, m in enumerate(matchings, start=1):
    values = block[m][args.channel]["value"]
    errors = block[m][args.channel]["error"]
    for ix in range(4):
        h.SetBinContent(ix + 1, iy, values[ix])

h.SetMinimum(0.0)
h.SetMaximum(2.0)

h.GetXaxis().SetTitle("p_{T} [GeV]")
h.GetXaxis().SetTitleOffset(1.3)
h.GetXaxis().SetTitleSize(0.05)
h.GetXaxis().SetLabelSize(0.045)

h.GetYaxis().SetTitleOffset(1.4)
h.GetYaxis().SetTitleSize(0.05)
h.GetYaxis().SetLabelSize(0.045)

h.GetZaxis().SetTitle("SF")
h.GetZaxis().SetTitleSize(0.045)
h.GetZaxis().SetLabelSize(0.045)

c.cd()
h.Draw("COLZ")

latex = ROOT.TLatex()
latex.SetTextAlign(22)
latex.SetTextSize(0.020)

for iy, m in enumerate(matchings, start=1):
    values = block[m][args.channel]["value"]
    errors = block[m][args.channel]["error"]
    for ix in range(4):
        latex.DrawLatex(ix + 0.5, iy - 0.5, f"{values[ix]:.3f} #pm {errors[ix]:.3f}")

CMS.UpdatePalettePosition(h, c)
c.SaveAs(args.output + ".png")
c.SaveAs(args.output + ".pdf")