import ROOT
import argparse
import sys
import cmsstyle as CMS
import array

ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat(".2f")


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input",        required=True,                help="Input fitDiagnostics.root file containing the RooFitResult")
parser.add_argument("-p", "--parameters",   required=True,                help="Comma-separated parameter names")
parser.add_argument("-o", "--outname",      default="corr_matrix",        help="Output name without extension")
args = parser.parse_args()


# -------------------------
# Open RooFitResult
# -------------------------
fitDiagnostics_FilePath = args.input
f                       = ROOT.TFile.Open(fitDiagnostics_FilePath)
fit                     = f.Get("fit_s")

# -------------------------
# Parameters
# -------------------------
poisNames   = args.parameters.split(",")
n           = len(poisNames)
pars        = fit.floatParsFinal()
cov         = fit.covarianceMatrix()
allNames    = [pars.at(i).GetName() for i in range(pars.getSize())]


# -------------------------
# Fill correlation matrix
# -------------------------
h = ROOT.TH2F("correlation_matrix", "", n, 0, n, n, 0, n)

for i, p1 in enumerate(poisNames):
    for j, p2 in enumerate(poisNames):
        h.SetBinContent(i + 1, j + 1, fit.correlation(p1, p2))

    h.GetXaxis().SetBinLabel(i + 1, p1)
    h.GetYaxis().SetBinLabel(i + 1, p1)

h.SetStats(0)
h.GetZaxis().SetRangeUser(-1.0, 1.0)
h.GetZaxis().SetTitle("Correlation")

# h.GetXaxis().LabelsOption("v")
h.GetXaxis().SetLabelSize(0.035)
h.GetYaxis().SetLabelSize(0.035)
h.GetZaxis().SetLabelSize(0.030)

h.SetMarkerSize(1.0 if n <= 8 else 0.75)


# -------------------------
# CMS style
# -------------------------
CMS.setCMSStyle()
CMS.SetExtraText("Work in Progress")
CMS.SetLumi("")
CMS.SetEnergy(13.6)
# CMS.SetCMSPalette()

# -------------------------
# Draw
# -------------------------
c = CMS.cmsCanvas(
    "c",
    0, 3,
    0, 3,
    "",
    "",
    square=CMS.kRectangular,
    iPos=0,
    with_z_axis=True
)

c.SetLeftMargin(0.22)
c.SetRightMargin(0.16)
c.SetBottomMargin(0.24)
c.SetTopMargin(0.10)

h.Draw("COLZ TEXT")

CMS.CMS_lumi(c, 0, scaleLumi=0.65) # reduce lumi/energy text
CMS.UpdatePalettePosition(h, c)
CMS.UpdatePad(c)

CMS.SaveCanvas(c, f"{args.outname}.pdf", close=False)
CMS.SaveCanvas(c, f"{args.outname}.png", close=False)

out = ROOT.TFile(f"{args.outname}.root", "RECREATE")
h.Write()
out.Close()

print("Saved:")
print(f"  {args.outname}.pdf")
print(f"  {args.outname}.png")
print(f"  {args.outname}.root")