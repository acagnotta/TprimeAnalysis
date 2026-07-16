# B2G-25-006 Analysis
Analysis code for T'→tZ search, where t→bqq' and Z→νν

## Overview
This repository contains the analysis code for the B2G-25-006 analysis, focusing on the T'→tZ decay channel with hadronic top quark decay and invisible Z boson decay.  
### CMS Internal links:  
[CADI line](https://cms.cern.ch/iCMS/analysisadmin/cadilines?line=B2G-25-006)  
[Analysis Note](https://cmsfence.cern.ch/alcm/note/show-note-details?noteID=CMS%20AN-2024%2F018)  
[PubTalk discussion](https://cms-pub-talk.web.cern.ch/c/b2g/b2g-25-006/828)  
[Twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2G25006Review)  

### Most relevant internal talks
- Last VHF update: [1st June 2026](https://indico.cern.ch/event/1687506/#68-update-on-the-trota-scale-f)
- Last B2G update: [14th April 2026](https://indico.cern.ch/event/1671232/#3-analysis-update-b2g-25-006-v)
- [27th October 2025](https://indico.cern.ch/event/1588426/#68-b2g-25-006-status-update-of) 
- [23rd June 2025](https://indico.cern.ch/event/1557401/#66-t-tz-update)
- [30th Sept 2024](https://indico.cern.ch/event/1459687/#66-update-on-t-tz-z-vv)
- [22nd Jan 2024](https://indico.cern.ch/event/1355727/#42-update-on-the-preselection)

## Analysis Workflow
1. **Skimming**: Central NanoAOD skimming + top quark candidate score evaluation with TROTA
2. **Histogram Production**: Using RDataFrame and Vary method
3. **Statistical Analysis**: Using [TprimeStats](https://github.com/acagnotta/TprimeStats)

## Prerequisites
Before running the analysis, make sure you have:
- NanoAOD tools
- Required dependencies installed
- Access to input datasets

## Installation
```bash
# Personal environment setup + JMECalculators lib installation
source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_107 x86_64-el9-gcc13-opt
python3 -m venv /afs/cern.ch/user/{u}/{username}/myvenv_lcg107
source /afs/cern.ch/user/{u}/{username}/myvenv_lcg107/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install git+https://gitlab.cern.ch/cms-analysis/general/CMSJMECalculators.git
python3 -m pip install tf-keras             # [only if needed]
python3 -m pip install "cmsstyle==0.4.3"    # [for plotting]


# Clone the repository
git clone git@github.com:acagnotta/TprimeAnalysis.git

# NanoAOD Tools standalone
cd TprimeAnalysis/NanoAODTools/
bash standalone/env_standalone.sh build
source standalone/env_standalone.sh
```


## Usage
### Step 0: env setup
```bash
# analysis_TPrime.sh 
source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_107 x86_64-el9-gcc13-opt
cd /afs/cern.ch/user/{u}/{username}
source myvenv_lcg107/bin/activate
export TF_USE_LEGACY_KERAS=1
cd /afs/cern.ch/user/{u}/{username}/TprimeAnalysis/NanoAODTools
source standalone/env_standalone.sh
```

### Step 1: Skimming
```bash
cd condor/
python3 postproc_submitter.py -d *dataset_name* --syst (to include jes and jer calc) --s (submit jobs) --r (resubmit failed jobs) --status (running jobs report) --tier bari ("bari" and "pisa" are the only ones supported)
```
When jobs are successfull ended, you need to include the file to the dict_file.json with

```bash
python3 getoutputs.py -d *dataset_name* -o *output_json_file_name*
```

### Step 2: Histograms Production
In order to produce the histograms, you can run the `postSelector_submitter.py` script as follows:
```bash
cd TprimeAnalysis/NanoAODTools/python/postprocessing/postselection/
python3 postSelector_submitter.py -d *dataset_name* --syst
```

#### config file
The configuration file for the histogram production and plotting can be found at `TprimeAnalysis/NanoAODTools/python/postprocessing/config/config.yaml`.
You can modify the settings in this file to customize the folder to save the plots to, as well as other parameters like which samples to use in the stacks production, the systematics to include, etc. In particular:
- `outputfolder/postselector_results`: folder where the output histograms will be stored, per each era;
- `dict_samples`: which dict_samples.json file to use for the histogram production, per each era (this is the json file produced at Step 1);
- `plotting/folder_dict`: folder where the input plots for producing stacks are stored, per each era;
- `plotting/folder_www_dict`: folder where the final plots will be saved, per each era;
- `plotting/datasets_to_plot`: list of samples to plot, per each era;
- `plotting/systematics`: list of systematics to include in the stacks, per each era (if no systematics are needed, just leave the list empty - by default it will only draw statistical uncertainties);
- `plotting/scale_signals`: factor to scale the signal samples in the stacks (set to 1 for no scaling).

Here there is a template example of config.yaml file for the 2022 era:
```yaml
outputfolder:
  postselector_results: { 
    "2022":         "",
    "2022EE":       "",
    "2023":         "",
    "2023postBPix": "",
    }
  triggerSF_results: { 
    "2022":         "",
    "2022EE":       "",
    "2023":         "",
    "2023postBPix": "",
    }

dict_samples:
  "2022":             "../samples/dict_samples_2022.json"
  "2023":             "../samples/dict_samples_2023.json"
  "Full2022":         "."
  "Full2023":         "."
  "Full2022_Full2023": ["../samples/dict_samples_2022.json", "../samples/dict_samples_2023.json"]

plotting:
  lumi_dict:
    {
      "2022":           7.980,
      "2022EE":         26.672,
      "2023":           18.063,
      "2023postBPix":   9.693
    }

  folder_dict:
    {
      "2022":               "",
      "2022EE":             "",
      "2023":               "",
      "2023postBPix":       "",
      "Full2022":           "",
      "Full2023":           "",
      "Full2022_Full2023":  "",
    }

  folder_www_dict:
    {
      "2022":               "",
      "2022EE":             "",
      "2023":               "",
      "2023postBPix":       "",
      "Full2022":           "",
      "Full2023":           "",
      "Full2022_Full2023":  "",
    }

  datasets_to_plot:
    {
      "2022":
              [
                  "DataJetMET_2022",
                  "TT_2022",
                  "TW_2022",
                  "QCD_2022",
                  "ZJetsToNuNu_2jets_2022",
                  "WJets_2jets_2022",
                  "TprimeToTZ_700_2022",
                  "TprimeToTZ_1000_2022",
                  "TprimeToTZ_1800_2022"
              ],
      "2022EE":
              [
                  "DataJetMET_2022EE",
                  "TT_2022EE",
                  "TW_2022EE",
                  "QCD_2022EE",
                  "ZJetsToNuNu_2jets_2022EE",
                  "WJets_2jets_2022EE",
                  "TprimeToTZ_700_2022EE",
                  "TprimeToTZ_1000_2022EE",
                  "TprimeToTZ_1800_2022EE"
              ],
      "2023":
              [
                  "DataJetMET_2023",
                  "TT_2023",
                  "TW_2023",
                  "QCD_2023",
                  "ZJetsToNuNu_2jets_2023",
                  "WJets_2jets_2023",
                  "TprimeToTZ_700_2023",
                  "TprimeToTZ_1000_2023",
                  "TprimeToTZ_1800_2023"
              ],
      "2023postBPix":
              [
                  "DataJetMET_2023postBPix",
                  "TT_2023postBPix",
                  "TW_2023postBPix",
                  "QCD_2023postBPix",
                  "ZJetsToNuNu_2jets_2023postBPix",
                  "WJets_2jets_2023postBPix",
                  "TprimeToTZ_700_2023postBPix",
                  "TprimeToTZ_1000_2023postBPix",
                  "TprimeToTZ_1800_2023postBPix"
              ],
    }
    
  systematics:
    {
      "2022":           [],
      "2022EE":         [],
      "2023":           [],
      "2023postBPix":   []
    }

  scale_signals: 100

TrotaScaleFactor:
  outputfolder: {
    "Resolved": {
                  "2022":         "",
                  "2022EE":       "",
                  "2023":         "",
                  "2023postBPix": "",
                },
    "Mixed": {
                  "2022":         "",
                  "2022EE":       "",
                  "2023":         "",
                  "2023postBPix": "",
                },
    "Merged": {
                  "2022":         "",
                  "2022EE":       "",
                  "2023":         "",
                  "2023postBPix": "",
                },
    }
    
  fit_variable: {
    "ResolvedLoose":                "MT_W",
    "ResolvedLooseButNotTight":     "MT_W",
    "ResolvedTight":                "MT_W",
    "MixedLoose":                   "MT_W",
    "MixedLooseButNotTight":        "MT_W",
    "MixedTight":                   "MT_W",
    "MergedLoose":                  "MT_W",
    "MergedLooseButNotTight":       "MT_W",
    "MergedTight":                  "MT_W",
  }

  corrlibfolder: {
    "2022":         "",
    "2022EE":       "",
    "2023":         "/eos/user/l/lfavilla/RDF_DManalysis/TopSF/corrections/2023_NewWPs_TopPtReweightingTheory/",
    "2023postBPix": "",
  }

  systematics:
    {
      "2022":           [],
      "2022EE":         [],
      "2023":           ["TrotaResolved", "TrotaMixed", "TrotaMerged"],  # "QCDScale"
      "2023postBPix":   []
    }

  scale_signals: 100
```

If you want to check if the output files have been correctly produced, i.e. they contain the histograms in the right format, for all component and so on, you can run:
```bash
cd TprimeAnalysis/NanoAODTools/python/postprocessing/postselection/
python3 jobChecker.py -d *plots_folder* --year *era*
```
where *plots_folder* is the folder where all the output histograms are stored and *era* can be something like `2022`, `2022EE`, etc.

### Step 3: Statistical Analysis
For the statistical analysis, please refer to the [TprimeStats repository](https://github.com/acagnotta/TprimeStats).
