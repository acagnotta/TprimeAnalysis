import ROOT
import cmsstyle as CMS

ROOT.EnableImplicitMT()
ROOT.gROOT.SetBatch(True)

sample      = "TT_semilep_2023" # or e.g. "TT_semilep_2023" or "QCD_HT2000_2023"
fname       = f"/eos/user/l/lfavilla/RDF_DManalysis/results_wTrotaScaleFactor/run2023_wTrotaScaleFactor_AllTopCategories/weight_g0p2_l8p0/snap_{sample}.root"
tree_name   = "events_nominal"
df          = ROOT.RDataFrame(tree_name, fname)
nbins, xmin, xmax = 50, -0.5, 4.5

Var1        = "w_nominal"
Var2        = "w_nominal_woTrota"


h1 = df.Histo1D(
    (f"h_{Var1}", f";{Var1};Events", nbins, xmin, xmax),
    Var1
)

h2 = df.Histo1D(
    (f"h_{Var2}", f";{Var2};Events", nbins, xmin, xmax),
    Var2
)


# compute means directly from the RDataFrame (avoids any histogram/binning effects)
mean_values = [
    df.Mean(Var1).GetValue(),
    df.Mean(Var2).GetValue(),
]

histos = [
    h1.GetValue(),
    h2.GetValue(),
]


labels = [
    "w_nominal",
    "w_nominal_woTrota",
]

colors = [
    ROOT.kRed,
    ROOT.kBlue,
]

# Optional CMS text
CMS.SetExtraText("Work in Progress")
CMS.SetLumi(None)        # or e.g. CMS.SetLumi(59.8, unit="fb", run="Run 2")
CMS.SetEnergy(13.6)


ymin = 0.0
ymax = max(h.GetMaximum() for h in histos) * 1.4

# cmsCanvas creates a CMS-style canvas with axes
c = CMS.cmsCanvas(
    "c_w_nominal",
    xmin, xmax,
    ymin, ymax,
    "w_nominal",
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
leg = CMS.cmsLeg(0.52, 0.68, 0.78, 0.88)
for h, mean, lab in zip(histos, mean_values, labels):
    leg.AddEntry(h, f"{lab} (#mu={mean:.3f})", "l")
latex = ROOT.TLatex()
latex.SetTextFont(52)
latex.SetTextSize(0.03)
latex.DrawLatexNDC(0.15, 0.85, sample) # x, y, text

# Save
CMS.SaveCanvas(c, f"wnominal_{sample}.pdf")