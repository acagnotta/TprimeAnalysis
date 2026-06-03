import ROOT
import cmsstyle as CMS

ROOT.EnableImplicitMT()
ROOT.gROOT.SetBatch(True)

sample      = "TT_semilep_2023" # or e.g. "TT_semilep_2023" or "QCD_HT2000_2023"
fname       = f"/eos/user/l/lfavilla/RDF_DManalysis/results_wTrotaScaleFactor/run2023_wTrotaScaleFactor_AllTopCategories/weight_g0p2_l8p0/snap_{sample}.root"
tree_name   = "events_nominal"
df          = ROOT.RDataFrame(tree_name, fname)
ResolvedVar = "TopResolved_TrotaSF"
MixedVar    = "TopMixed_TrotaSF"
MergedVar   = "TopMerged_TrotaSF"
logy        = True
nbins, xmin, xmax = 1000, 0.0, max(df.Max(ResolvedVar).GetValue(), df.Max(MixedVar).GetValue(), df.Max(MergedVar).GetValue(), df.Max("TotalTrotaEventWeight").GetValue())



h_Resolved = df.Histo1D(
    (f"h_{ResolvedVar}", f";{ResolvedVar};Events", nbins, xmin, xmax),
    ResolvedVar
)

h_Mixed = df.Histo1D(
    (f"h_{MixedVar}", f";{MixedVar};Events", nbins, xmin, xmax),
    MixedVar
)

h_Merged = df.Histo1D(
    (f"h_{MergedVar}", f";{MergedVar};Events", nbins, xmin, xmax),
    MergedVar
)


# compute means directly from the RDataFrame (avoids any histogram/binning effects)
mean_values = [
    df.Mean(ResolvedVar).GetValue(),
    df.Mean(MixedVar).GetValue(),
    df.Mean(MergedVar).GetValue(),
]

histos = [
    h_Resolved.GetValue(),
    h_Mixed.GetValue(),
    h_Merged.GetValue(),
]


labels = [
    "Resolved",
    "Mixed",
    "Merged",
]

colors = [
    ROOT.kAzure+10,
    ROOT.kOrange,
    ROOT.kRed+1,
]

# Optional CMS text
CMS.SetExtraText("Work in Progress")
CMS.SetLumi(None)        # or e.g. CMS.SetLumi(59.8, unit="fb", run="Run 2")
CMS.SetEnergy(13.6)


ymin = 0.0
ymax = max(h.GetMaximum() for h in histos) * 1.4

# cmsCanvas creates a CMS-style canvas with axes
c = CMS.cmsCanvas(
    "c_trota_sf",
    xmin, xmax,
    ymin, ymax,
    "Trota SF",
    "Events",
    square=False,
    iPos=0,
)

axis_hist = c.GetPrimitive("hframe")
axis_hist.GetXaxis().SetTitleOffset(1.4)
axis_hist.GetYaxis().SetTitleOffset(1.4)
axis_hist.GetXaxis().SetLabelSize(0.030)
axis_hist.GetYaxis().SetLabelSize(0.030)
axis_hist.GetXaxis().SetTitleSize(0.035)
axis_hist.GetYaxis().SetTitleSize(0.035)

# Draw histograms
for i, h in enumerate(histos):
    h.SetDirectory(0)
    CMS.cmsDraw(
        h,
        "HIST",
        lcolor=colors[i],
        lwidth=2,
        fstyle=0,
    )

# Legend
leg = CMS.cmsLeg(0.62, 0.68, 0.88, 0.88)
for h, mean, lab in zip(histos, mean_values, labels):
    leg.AddEntry(h, f"{lab} (#mu={mean:.3f})", "l")
latex = ROOT.TLatex()
latex.SetTextFont(52)
latex.SetTextSize(0.03)
latex.DrawLatexNDC(0.15, 0.85, sample) # x, y, text

# Save
# CMS.SaveCanvas(c, "TrotaNumberOfCandidatesConsidered.png")
CMS.SaveCanvas(c, f"Trota_ScaleFactors_{sample}.pdf")