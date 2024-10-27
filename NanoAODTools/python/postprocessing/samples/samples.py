import ROOT
import os
#import json_reader as jr

path = os.path.dirname(os.path.abspath(__file__))

class sample:
    def __init__(self, color, style, fill, leglabel, label):
        self.color = color
        self.style = style
        self.fill = fill
        self.leglabel = leglabel
        self.label = label

#da controllare i tag aggiungere la QCD

tag_2016 = 'RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8'
tag_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8'
tag2_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8'
tag_2018 = 'RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21'

################################ WJets ################################
altXSUp=0
kFactorsQCD={
    "WJetsHT100to200" : 1.21,
    "WJetsHT200to400" : 1.21,
    "WJetsHT400to600" : 1.21,
    "WJetsHT600to800" : 1.21,
    "WJetsHT800to1200" : 1.21,
    "WJetsHT1200to2500" : 1.21,
    "WJetsHT2500toInf" : 1.21
}

###############################################################################################################################
##########################################                                           ##########################################
##########################################                    2018                   ##########################################
##########################################                                           ##########################################
###############################################################################################################################

################################ QCD ################################
QCDHT_100to200_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_100to200_2018")
QCDHT_100to200_2018.sigma   = 27990000 #23590000 #pb
QCDHT_100to200_2018.year    = 2018
QCDHT_100to200_2018.dataset = '/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_100to200_2018.process = 'QCD_2018'
QCDHT_100to200_2018.unix_code = 21000

QCDHT_200to300_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_200to300_2018")
QCDHT_200to300_2018.sigma   = 1712000#1555000 #pb
QCDHT_200to300_2018.year    = 2018
QCDHT_200to300_2018.dataset = '/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_200to300_2018.process = 'QCD_2018'
QCDHT_200to300_2018.unix_code = 21001

QCDHT_300to500_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_300to500_2018")
QCDHT_300to500_2018.sigma   = 347700 #324500 #pb
QCDHT_300to500_2018.year    = 2018
QCDHT_300to500_2018.dataset = '/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_300to500_2018.process = 'QCD_2018'
QCDHT_300to500_2018.unix_code = 21002
# QCDHT_300to500_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD_HT300to500_2018_Skim.root"

QCDHT_500to700_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_500to700_2018")
QCDHT_500to700_2018.sigma   = 32100 #30310 #pb
QCDHT_500to700_2018.year    = 2018
QCDHT_500to700_2018.dataset = '/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_500to700_2018.process = 'QCD_2018'
QCDHT_500to700_2018.unix_code = 21003
# QCDHT_500to700_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD_HT500to700_2018_Skim.root"

QCDHT_700to1000_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_700to1000_2018")
QCDHT_700to1000_2018.sigma   = 6832 #6444 #pb
QCDHT_700to1000_2018.year    = 2018
QCDHT_700to1000_2018.dataset = '/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_700to1000_2018.process = 'QCD_2018'
QCDHT_700to1000_2018.unix_code = 21004
# QCDHT_700to1000_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD_HT700to1000_2018_Skim.root"

QCDHT_1000to1500_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1000to1500_2018")
QCDHT_1000to1500_2018.sigma   = 1207 #1127 #pb
QCDHT_1000to1500_2018.year    = 2018
QCDHT_1000to1500_2018.dataset = '/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_1000to1500_2018.process = 'QCD_2018'
QCDHT_1000to1500_2018.unix_code = 21005
# QCDHT_1000to1500_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD_HT1000_Skim.root"

QCDHT_1500to2000_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1500to2000_2018")
QCDHT_1500to2000_2018.sigma   = 119.9 #109.8 #pb
QCDHT_1500to2000_2018.year    = 2018
QCDHT_1500to2000_2018.dataset = '/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_1500to2000_2018.process = 'QCD_2018'
QCDHT_1500to2000_2018.unix_code = 21006
# QCDHT_1500to2000_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD-HT1500to2000_2018_Skim.root"

QCDHT_2000toInf_2018         = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_2000toInf_2018")
QCDHT_2000toInf_2018.sigma   = 25.24 #21.98 #pb   #####
QCDHT_2000toInf_2018.year    = 2018
QCDHT_2000toInf_2018.dataset = '/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
QCDHT_2000toInf_2018.process = 'QCD_2018'
QCDHT_2000toInf_2018.unix_code = 21007
# QCDHT_2000toInf_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/QCD-HT2000toInf_2018_Skim.root"

QCD_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2018")
QCD_2018.year = 2018
QCD_2018.components = [QCDHT_100to200_2018, QCDHT_200to300_2018,
                       QCDHT_300to500_2018, QCDHT_500to700_2018, 
                       QCDHT_700to1000_2018, QCDHT_1000to1500_2018, 
                       QCDHT_1500to2000_2018, QCDHT_2000toInf_2018]

#QCD_2018.components = [QCDHT_300to500_2018, QCDHT_500to700_2018, QCDHT_1000to1500_2018, QCDHT_1500to2000_2018, QCDHT_2000toInf_2018]

################################ TTbar ################################

TT_hadr_2018         = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_hadr_2018")
TT_hadr_2018.sigma   = 380.94 #687.1 #pb
TT_hadr_2018.year    = 2018
TT_hadr_2018.dataset = '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
TT_hadr_2018.process = 'TT_2018'
TT_hadr_2018.unix_code = 21101
# TT_hadr_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/TT_Hadr_2018_Skim.root"

TT_Mtt700to1000_2018         = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt700to1000_2018")
TT_Mtt700to1000_2018.sigma   = 80.5 #pb
TT_Mtt700to1000_2018.year    = 2018
TT_Mtt700to1000_2018.dataset = '/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
TT_Mtt700to1000_2018.process = 'TT_2018'
TT_Mtt700to1000_2018.unix_code = 21102
# TT_Mtt700to1000_2018.local_path= "/eos/home-a/acagnott/DarkMatter/topcandidate_file/TT_Mtt-700to1000_2018_Skim.root"

TT_Mtt1000toInf_2018         = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt1000toInf_2018")
TT_Mtt1000toInf_2018.sigma   = 21.3 #pb
TT_Mtt1000toInf_2018.year    = 2018
TT_Mtt1000toInf_2018.dataset = '/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
TT_Mtt1000toInf_2018.process = 'TT_2018'
TT_Mtt1000toInf_2018.unix_code = 21103
# TT_Mtt1000toInf_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/TT_Mtt-1000toInf_2018_Skim.root"

TT_semilep_2018         = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2018")
TT_semilep_2018.sigma   = 364.51 #pb
TT_semilep_2018.year    = 2018
TT_semilep_2018.dataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
TT_semilep_2018.process = 'TT_2018'
TT_semilep_2018.unix_code = 21104
# TT_semilep_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/TT_SemiLep_2018_Skim.root"

TT_2018             = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_2018")
TT_2018.year        = 2018
TT_2018.components  = [TT_hadr_2018, TT_semilep_2018, TT_Mtt1000toInf_2018, TT_Mtt700to1000_2018]

################################ ZJetsToNuNu ################################
ZJetsToNuNu_HT100to200_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT100to200_2018")
ZJetsToNuNu_HT100to200_2018.sigma   = 280.35 * 1.37 #267.0	 #pb 
ZJetsToNuNu_HT100to200_2018.year    = 2018
ZJetsToNuNu_HT100to200_2018.dataset = '/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT100to200_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT100to200_2018.unix_code = 21200
# ZJetsToNuNu_HT100to200_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT100to200_2018_Skim.root'

ZJetsToNuNu_HT200to400_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT200to400_2018")
ZJetsToNuNu_HT200to400_2018.sigma   = 77.67*1.52 #73.08 #pb
ZJetsToNuNu_HT200to400_2018.year    = 2018
ZJetsToNuNu_HT200to400_2018.dataset = '/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT200to400_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT200to400_2018.unix_code = 21201
# ZJetsToNuNu_HT200to400_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT200to400_2018_Skim.root'

ZJetsToNuNu_HT400to600_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT400to600_2018")
ZJetsToNuNu_HT400to600_2018.sigma   = 10.73*1.37 #9.904	 #pb
ZJetsToNuNu_HT400to600_2018.year    = 2018
ZJetsToNuNu_HT400to600_2018.dataset = '/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT400to600_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT400to600_2018.unix_code = 21202
# ZJetsToNuNu_HT400to600_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT400to600_2018_Skim.root'

ZJetsToNuNu_HT600to800_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT600to800_2018")
ZJetsToNuNu_HT600to800_2018.sigma   = 2.56*1.04 #2.413 #pb
ZJetsToNuNu_HT600to800_2018.year    = 2018
ZJetsToNuNu_HT600to800_2018.dataset = '/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT600to800_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT600to800_2018.unix_code = 21203
# ZJetsToNuNu_HT600to800_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT600to800_2018_Skim.root'

ZJetsToNuNu_HT800to1200_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT800to1200_2018")
ZJetsToNuNu_HT800to1200_2018.sigma   = 1.18*1.14 #1.071 #pb
ZJetsToNuNu_HT800to1200_2018.year    = 2018
ZJetsToNuNu_HT800to1200_2018.dataset = '/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT800to1200_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT800to1200_2018.unix_code = 21204
# ZJetsToNuNu_HT800to1200_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT800to1200_2018_Skim.root'

ZJetsToNuNu_HT1200to2500_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT1200to2500_2018")
ZJetsToNuNu_HT1200to2500_2018.sigma   = 0.29*0.88 #0.2497 #pb
ZJetsToNuNu_HT1200to2500_2018.year    = 2018
ZJetsToNuNu_HT1200to2500_2018.dataset = '/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT1200to2500_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT1200to2500_2018.unix_code = 21205
# ZJetsToNuNu_HT1200to2500_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT1200to2500_2018_Skim.root'

ZJetsToNuNu_HT2500toInf_2018         = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT2500toInf_2018")
ZJetsToNuNu_HT2500toInf_2018.sigma   = 0.007*0.88 #0.005618	 #pb
ZJetsToNuNu_HT2500toInf_2018.year    = 2018
ZJetsToNuNu_HT2500toInf_2018.dataset = '/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
ZJetsToNuNu_HT2500toInf_2018.process = 'ZJetsToNuNu_2018'
ZJetsToNuNu_HT2500toInf_2018.unix_code = 21206
# ZJetsToNuNu_HT2500toInf_2018.local_path = '/eos/home-a/acagnott/DarkMatter/topcandidate_file/ZJetsToNuNu_HT2500toInf_2018_Skim.root'

ZJetsToNuNu_2018            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2018")
ZJetsToNuNu_2018.year       = 2018
ZJetsToNuNu_2018.components = [ZJetsToNuNu_HT100to200_2018, ZJetsToNuNu_HT200to400_2018, 
                               ZJetsToNuNu_HT400to600_2018, ZJetsToNuNu_HT600to800_2018, 
                               ZJetsToNuNu_HT800to1200_2018, ZJetsToNuNu_HT1200to2500_2018, 
                               ZJetsToNuNu_HT2500toInf_2018]

#ZJetsToNuNu_2018.components = [ZJetsToNuNu_HT100to200_2018, ZJetsToNuNu_HT200to400_2018, ZJetsToNuNu_HT400to600_2018, ZJetsToNuNu_HT600to800_2018, ZJetsToNuNu_HT1200to2500_2018, ZJetsToNuNu_HT2500toInf_2018]

################################ WJets ################################

WJetsHT70to100_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT70to100_2018")
WJetsHT70to100_2018.sigma   = 1353.0 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT70to100_2018.year    = 2018
WJetsHT70to100_2018.dataset = '/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
WJetsHT70to100_2018.process = 'WJets_2018'
WJetsHT70to100_2018.unix_code = 21200

WJetsHT100to200_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT100to200_2018")
WJetsHT100to200_2018.sigma   = 1345 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT100to200_2018.year    = 2018
WJetsHT100to200_2018.dataset = '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
WJetsHT100to200_2018.process = 'WJets_2018'
WJetsHT100to200_2018.unix_code = 21201

WJetsHT200to400_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT200to400_2018")
WJetsHT200to400_2018.sigma   = 359.7 * kFactorsQCD["WJetsHT200to400"] #pb
WJetsHT200to400_2018.year    = 2018
WJetsHT200to400_2018.dataset = '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'
WJetsHT200to400_2018.process = 'WJets_2018'
WJetsHT200to400_2018.unix_code = 21202

WJetsHT400to600_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT400to600_2018")
WJetsHT400to600_2018.sigma   = 48.91 * kFactorsQCD["WJetsHT400to600"] #pb
WJetsHT400to600_2018.year    = 2018
WJetsHT400to600_2018.dataset = '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM'
WJetsHT400to600_2018.process = 'WJets_2018' 
WJetsHT400to600_2018.unix_code = 21203

WJetsHT600to800_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT600to800_2018")
WJetsHT600to800_2018.sigma   = 12.05 * kFactorsQCD["WJetsHT600to800"] #pb
WJetsHT600to800_2018.year    = 2018
WJetsHT600to800_2018.dataset = '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM'
WJetsHT600to800_2018.process = 'WJets_2018'
WJetsHT600to800_2018.unix_code = 21204

WJetsHT800to1200_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT800to1200_2018")
WJetsHT800to1200_2018.sigma   = 5.501 * kFactorsQCD["WJetsHT800to1200"] #pb
WJetsHT800to1200_2018.year    = 2018
WJetsHT800to1200_2018.dataset = '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM'
WJetsHT800to1200_2018.process = 'WJets_2018' 
WJetsHT800to1200_2018.unix_code = 21205

WJetsHT1200to2500_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT1200to2500_2018")
WJetsHT1200to2500_2018.sigma   = 1.329 * kFactorsQCD["WJetsHT1200to2500"] #pb
WJetsHT1200to2500_2018.year    = 2018
WJetsHT1200to2500_2018.dataset = '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM'
WJetsHT1200to2500_2018.process = 'WJets_2018' 
WJetsHT1200to2500_2018.unix_code = 21206

WJetsHT2500toInf_2018         = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJetsHT2500toInf_2018")
WJetsHT2500toInf_2018.sigma   = 0.03216 * kFactorsQCD["WJetsHT2500toInf"] #pb
WJetsHT2500toInf_2018.year    = 2018
WJetsHT2500toInf_2018.dataset = '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM'
WJetsHT2500toInf_2018.process = 'WJets_2018'
WJetsHT2500toInf_2018.unix_code = 21207

WJets_2018 = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2018")
WJets_2018.year = 2018
WJets_2018.components = [#WJetsHT70to100_2018, 
                         WJetsHT100to200_2018, WJetsHT200to400_2018, 
                         WJetsHT400to600_2018, WJetsHT600to800_2018, 
                         WJetsHT800to1200_2018, WJetsHT1200to2500_2018, 
                         WJetsHT2500toInf_2018]

################################ Signal tDM ################################

tDM_mPhi1000_mChi1_2018 = sample(ROOT.kGreen+2, 1, 1001, "DM (m_{#Phi}=1000)", "tDM_mPhi1000_mChi1_2018")
tDM_mPhi1000_mChi1_2018.sigma = 24.99 *0.00001 #*100    #pb  aggiunto*100 per i plot
tDM_mPhi1000_mChi1_2018.year = 2018
tDM_mPhi1000_mChi1_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/tDM_mPhi1000_mChi1_Skim.root"
tDM_mPhi1000_mChi1_2018.unix_code = 22100

tDM_mPhi500_mChi1_2018 = sample(ROOT.kGreen+1, 1, 1001, "DM (m_{#Phi}=500)", "tDM_mPhi500_mChi1_2018")
tDM_mPhi500_mChi1_2018.year = 2018
tDM_mPhi500_mChi1_2018.sigma = 43.85 *0.0001  #pb
tDM_mPhi500_mChi1_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/tDM_mPhi500_mChi1_Skim.root"
tDM_mPhi500_mChi1_2018.unix_code = 22101

tDM_mPhi50_mChi1_2018= sample(ROOT.kGreen, 1, 1001, "DM (m_{#Phi}=50)", "tDM_mPhi50_mChi1_2018")
tDM_mPhi50_mChi1_2018.year = 2018
tDM_mPhi50_mChi1_2018.sigma = 0.7  #pb
tDM_mPhi50_mChi1_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/tDM_mPhi50_mChi1_Skim.root"
tDM_mPhi50_mChi1_2018.unix_code = 22102

################################ Signal Tprime ################################

TprimeToTZ_1800_2018         = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1800GeV", "TprimeToTZ_1800_2018")
TprimeToTZ_1800_2018.sigma   = 0.00045 #pb
TprimeToTZ_1800_2018.year    = 2018
TprimeToTZ_1800_2018.dataset = '/TprimeBToTZ_M-1800_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM'
TprimeToTZ_1800_2018.unix_code = 22000
# TprimeToTZ_1800_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/"+TprimeToTZ_1800_2018.label +"_Skim.root"

TprimeToTZ_1000_2018         = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow TZ M1000GeV", "TprimeToTZ_1000_2018")
TprimeToTZ_1000_2018.sigma   = 0.01362 #pb
TprimeToTZ_1000_2018.year    = 2018
TprimeToTZ_1000_2018.dataset = '/TprimeBToTZ_M-1000_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM'
TprimeToTZ_1000_2018.unix_code = 22001
# TprimeToTZ_1000_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/"+TprimeToTZ_1000_2018.label +"_Skim.root"

TprimeToTZ_700_2018         = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M700GeV", "TprimeToTZ_700_2018")
TprimeToTZ_700_2018.sigma   = 0.07804 #pb
TprimeToTZ_700_2018.year    = 2018
TprimeToTZ_700_2018.dataset = '/TprimeBToTZ_M-700_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM'
TprimeToTZ_700_2018.unix_code = 22002
# TprimeToTZ_700_2018.local_path = "/eos/home-a/acagnott/DarkMatter/topcandidate_file/"+TprimeToTZ_700_2018.label +"_Skim.root"

###############################################################################################################################
##########################################                                           ##########################################
##########################################       samples for tagger studies          ##########################################
##########################################                                           ##########################################
###############################################################################################################################
Zprime4top_500_2018          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M500GeV", "Zprime4top_500_2018")
Zprime4top_500_2018.sigma    = 1 #pb
Zprime4top_500_2018.year     = 2018
Zprime4top_500_2018.dataset  = '/TTZprimeToTT_M-500_Width4_TuneCP5_13TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-500_Width4_nanoaod_hotvr_UL2018v1_230510-00000000000000000000000000000000/USER'

Zprime4top_1000_2018          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M1000GeV", "Zprime4top_1000_2018")
Zprime4top_1000_2018.sigma    = 1 #pb
Zprime4top_1000_2018.year     = 2018
Zprime4top_1000_2018.dataset  = '/TTZprimeToTT_M-1000_Width4_TuneCP5_13TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-1000_Width4_nanoaod_hotvr_UL2018v1_230510-00000000000000000000000000000000/USER'

Zprime4top_2000_2018          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M2000GeV", "Zprime4top_2000_2018")
Zprime4top_2000_2018.sigma    = 1 #pb
Zprime4top_2000_2018.year     = 2018
Zprime4top_2000_2018.dataset  = '/TTZprimeToTT_M-2000_Width4_TuneCP5_13TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-2000_Width4_nanoaod_hotvr_UL2018v1_230510-00000000000000000000000000000000/USER'

###############################################################################################################################
##########################################                                           ##########################################
##########################################                    2022                   ##########################################
##########################################                                           ##########################################
###############################################################################################################################
#  EraCD (preEE) più avanti descrizione completa

################################ QCD ################################
# QCD_HT40to70_2022               = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT40to70_2022")
# QCD_HT40to70_2022.sigma         = 311.7*(10**6) #pb
# QCD_HT40to70_2022.year          = 2022
# QCD_HT40to70_2022.dataset       = "/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-JMENano12p5_132X_mcRun3_2022_realistic_v3-v1/NANOAODSIM"
# QCD_HT40to70_2022.process       = "QCD_2022"
# QCD_HT40to70_2022.unix_code     = 31000
# QCD_HT40to70_2022.EE            = 0
QCD_HT70to100_2022              = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT70to100_2022")
QCD_HT70to100_2022.sigma        = 58.6*(10**6) #pb
QCD_HT70to100_2022.year         = 2022
QCD_HT70to100_2022.dataset      = "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT70to100_2022.process      = "QCD_2022"
QCD_HT70to100_2022.unix_code    = 31001
QCD_HT70to100_2022.EE           = 0
QCD_HT100to200_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT100to200_2022")
QCD_HT100to200_2022.sigma       = 25.1*(10**6) #pb
QCD_HT100to200_2022.year        = 2022
QCD_HT100to200_2022.dataset     = "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT100to200_2022.process     = "QCD_2022"
QCD_HT100to200_2022.unix_code   = 31002
QCD_HT100to200_2022.EE          = 0
QCD_HT200to400_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT200to400_2022")
QCD_HT200to400_2022.sigma       = 1.96*(10**6) #pb
QCD_HT200to400_2022.year        = 2022
QCD_HT200to400_2022.dataset     = "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT200to400_2022.process     = "QCD_2022"
QCD_HT200to400_2022.unix_code   = 31003
QCD_HT200to400_2022.EE          = 0
QCD_HT400to600_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT400to600_2022")
QCD_HT400to600_2022.sigma       = 96.0*(10**3) #pb
QCD_HT400to600_2022.year        = 2022
QCD_HT400to600_2022.dataset     = "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT400to600_2022.process     = "QCD_2022"
QCD_HT400to600_2022.unix_code   = 31004
QCD_HT400to600_2022.EE          = 0
QCD_HT600to800_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT600to800_2022")
QCD_HT600to800_2022.sigma       = 13.5*(10**3) #pb
QCD_HT600to800_2022.year        = 2022
QCD_HT600to800_2022.dataset     = "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT600to800_2022.process     = "QCD_2022"
QCD_HT600to800_2022.unix_code   = 31005
QCD_HT600to800_2022.EE          = 0
QCD_HT800to1000_2022            = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT800to1000_2022")
QCD_HT800to1000_2022.sigma      = 3.03*(10**3) #pb
QCD_HT800to1000_2022.year       = 2022
QCD_HT800to1000_2022.dataset    = "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT800to1000_2022.process    = "QCD_2022"
QCD_HT800to1000_2022.unix_code  = 31006
QCD_HT800to1000_2022.EE         = 0
QCD_HT1000to1200_2022           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1000to1200_2022")
QCD_HT1000to1200_2022.sigma     = 884 #pb
QCD_HT1000to1200_2022.year      = 2022
QCD_HT1000to1200_2022.dataset   = "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT1000to1200_2022.process   = "QCD_2022"
QCD_HT1000to1200_2022.unix_code = 31007
QCD_HT1000to1200_2022.EE        = 0
QCD_HT1200to1500_2022           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1200to1500_2022")
QCD_HT1200to1500_2022.sigma     = 384 #pb 
QCD_HT1200to1500_2022.year      = 2022
QCD_HT1200to1500_2022.dataset   = "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT1200to1500_2022.process   = "QCD_2022"
QCD_HT1200to1500_2022.unix_code = 31007
QCD_HT1200to1500_2022.EE        = 0
QCD_HT1500to2000_2022           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1500to2000_2022")
QCD_HT1500to2000_2022.sigma     = 125 #pb
QCD_HT1500to2000_2022.year      = 2022
QCD_HT1500to2000_2022.dataset   = "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT1500to2000_2022.process   = "QCD_2022"
QCD_HT1500to2000_2022.unix_code = 31008
QCD_HT1500to2000_2022.EE        = 0
QCD_HT2000_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT2000_2022")
QCD_HT2000_2022.sigma           = 26.5 #pb
QCD_HT2000_2022.year            = 2022
QCD_HT2000_2022.dataset         = "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT2000_2022.process         = "QCD_2022"
QCD_HT2000_2022.unix_code       = 31009
QCD_HT2000_2022.EE              = 0
QCD_2022                        = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2022")
QCD_2022.year                   = 2022
QCD_2022.components             = [ 
                                    # QCD_HT40to70_2022, 
                                    QCD_HT70to100_2022, QCD_HT100to200_2022, QCD_HT200to400_2022,
                                    QCD_HT400to600_2022, QCD_HT600to800_2022, QCD_HT800to1000_2022, 
                                    QCD_HT1000to1200_2022, QCD_HT1200to1500_2022,
                                    QCD_HT1500to2000_2022, QCD_HT2000_2022
                                ]


################################ TTbar ################################
TT_semilep_2022             = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2022")
TT_semilep_2022.sigma       = 404.0 #pb
TT_semilep_2022.year        = 2022
TT_semilep_2022.dataset     = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
TT_semilep_2022.process     = 'TT_2022'
TT_semilep_2022.unix_code   = 31100
TT_semilep_2022.EE          = 0

TT_hadr_2022                = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_hadr_2022")
TT_hadr_2022.sigma          = 422.3
TT_hadr_2022.year           = 2022
TT_hadr_2022.dataset        = "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
TT_hadr_2022.process        = 'TT_2022'
TT_hadr_2022.unix_code      = 31101
TT_hadr_2022.EE             = 0

TT_2022                     = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_2022")
TT_2022.year                = 2022
TT_2022.components          = [TT_semilep_2022, TT_hadr_2022]

################################ ZJets ################################

ZJetsToNuNu_HT100to200_2022             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT100to200_2022")
ZJetsToNuNu_HT100to200_2022.sigma       = 273.7 #pb
ZJetsToNuNu_HT100to200_2022.year        = 2022
ZJetsToNuNu_HT100to200_2022.dataset     = "/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT100to200_2022.process     = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT100to200_2022.unix_code   = 31200
ZJetsToNuNu_HT100to200_2022.EE          = 0

ZJetsToNuNu_HT200to400_2022             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT200to400_2022")
ZJetsToNuNu_HT200to400_2022.sigma       = 75.96 #pb
ZJetsToNuNu_HT200to400_2022.year        = 2022
ZJetsToNuNu_HT200to400_2022.dataset     = "/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT200to400_2022.process     = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT200to400_2022.unix_code   = 31201
ZJetsToNuNu_HT200to400_2022.EE          = 0

ZJetsToNuNu_HT400to800_2022             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT400to800_2022")
ZJetsToNuNu_HT400to800_2022.sigma       = 13.19 #pb
ZJetsToNuNu_HT400to800_2022.year        = 2022
ZJetsToNuNu_HT400to800_2022.dataset     = "/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT400to800_2022.process     = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT400to800_2022.unix_code   = 31202
ZJetsToNuNu_HT400to800_2022.EE          = 0

ZJetsToNuNu_HT800to1500_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT800to1500_2022")
ZJetsToNuNu_HT800to1500_2022.sigma      = 1.364 #pb
ZJetsToNuNu_HT800to1500_2022.year       = 2022
ZJetsToNuNu_HT800to1500_2022.dataset    = "/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT800to1500_2022.process    = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT800to1500_2022.unix_code  = 31203
ZJetsToNuNu_HT800to1500_2022.EE         = 0

ZJetsToNuNu_HT1500to2500_2022           = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT1500to2500_2022")
ZJetsToNuNu_HT1500to2500_2022.sigma     = 0.09865 #pb
ZJetsToNuNu_HT1500to2500_2022.year      = 2022
ZJetsToNuNu_HT1500to2500_2022.dataset   = "/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT1500to2500_2022.process   = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT1500to2500_2022.unix_code = 31204
ZJetsToNuNu_HT1500to2500_2022.EE        = 0

ZJetsToNuNu_HT2500_2022                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT2500_2022")
ZJetsToNuNu_HT2500_2022.sigma           = 0.006699 #pb
ZJetsToNuNu_HT2500_2022.year            = 2022
ZJetsToNuNu_HT2500_2022.dataset         = "/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT2500_2022.process         = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT2500_2022.unix_code       = 31205
ZJetsToNuNu_HT2500_2022.EE              = 0

ZJetsToNuNu_2022                        = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2022")
ZJetsToNuNu_2022.year                   = 2022
ZJetsToNuNu_2022.components             = [
                                            ZJetsToNuNu_HT100to200_2022,
                                            ZJetsToNuNu_HT200to400_2022,
                                            ZJetsToNuNu_HT400to800_2022,
                                            ZJetsToNuNu_HT800to1500_2022,
                                            ZJetsToNuNu_HT1500to2500_2022,
                                            ZJetsToNuNu_HT2500_2022 
                                            ]

ZJetsToNuNu_2jets_PT40to100_1J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_1J_2022")
ZJetsToNuNu_2jets_PT40to100_1J_2022.sigma      = 929.8	
ZJetsToNuNu_2jets_PT40to100_1J_2022.year       = 2022
ZJetsToNuNu_2jets_PT40to100_1J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_1J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT40to100_1J_2022.unix_code  = 31206
ZJetsToNuNu_2jets_PT40to100_1J_2022.EE         = 0

ZJetsToNuNu_2jets_PT100to200_1J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_1J_2022")
ZJetsToNuNu_2jets_PT100to200_1J_2022.sigma      = 86.38
ZJetsToNuNu_2jets_PT100to200_1J_2022.year       = 2022
ZJetsToNuNu_2jets_PT100to200_1J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_1J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT100to200_1J_2022.unix_code  = 31207
ZJetsToNuNu_2jets_PT100to200_1J_2022.EE         = 0

ZJetsToNuNu_2jets_PT200to400_1J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_1J_2022")
ZJetsToNuNu_2jets_PT200to400_1J_2022.sigma      = 6.354	
ZJetsToNuNu_2jets_PT200to400_1J_2022.year       = 2022
ZJetsToNuNu_2jets_PT200to400_1J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_1J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT200to400_1J_2022.unix_code  = 31208
ZJetsToNuNu_2jets_PT200to400_1J_2022.EE         = 0

ZJetsToNuNu_2jets_PT400to600_1J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_1J_2022")
ZJetsToNuNu_2jets_PT400to600_1J_2022.sigma      = 0.2188
ZJetsToNuNu_2jets_PT400to600_1J_2022.year       = 2022
ZJetsToNuNu_2jets_PT400to600_1J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_1J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT400to600_1J_2022.unix_code  = 31209
ZJetsToNuNu_2jets_PT400to600_1J_2022.EE         = 0

ZJetsToNuNu_2jets_PT600_1J_2022                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_1J_2022")
ZJetsToNuNu_2jets_PT600_1J_2022.sigma           = 0.02583
ZJetsToNuNu_2jets_PT600_1J_2022.year            = 2022
ZJetsToNuNu_2jets_PT600_1J_2022.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_1J_2022.process         = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT600_1J_2022.unix_code       = 31210
ZJetsToNuNu_2jets_PT600_1J_2022.EE              = 0

ZJetsToNuNu_2jets_PT40to100_2J_2022             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_2J_2022")
ZJetsToNuNu_2jets_PT40to100_2J_2022.sigma       = 335.5
ZJetsToNuNu_2jets_PT40to100_2J_2022.year        = 2022
ZJetsToNuNu_2jets_PT40to100_2J_2022.dataset     = "/Zto2Nu-2Jets_PTNuNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_2J_2022.process     = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT40to100_2J_2022.unix_code   = 31211
ZJetsToNuNu_2jets_PT40to100_2J_2022.EE          = 0

ZJetsToNuNu_2jets_PT100to200_2J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_2J_2022")
ZJetsToNuNu_2jets_PT100to200_2J_2022.sigma      = 100.4
ZJetsToNuNu_2jets_PT100to200_2J_2022.year       = 2022
ZJetsToNuNu_2jets_PT100to200_2J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_2J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT100to200_2J_2022.unix_code  = 31212
ZJetsToNuNu_2jets_PT100to200_2J_2022.EE         = 0

ZJetsToNuNu_2jets_PT200to400_2J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_2J_2022")
ZJetsToNuNu_2jets_PT200to400_2J_2022.sigma      = 13.86
ZJetsToNuNu_2jets_PT200to400_2J_2022.year       = 2022
ZJetsToNuNu_2jets_PT200to400_2J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_2J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT200to400_2J_2022.unix_code  = 31213
ZJetsToNuNu_2jets_PT200to400_2J_2022.EE         = 0

ZJetsToNuNu_2jets_PT400to600_2J_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_2J_2022")
ZJetsToNuNu_2jets_PT400to600_2J_2022.sigma      = 0.7816
ZJetsToNuNu_2jets_PT400to600_2J_2022.year       = 2022
ZJetsToNuNu_2jets_PT400to600_2J_2022.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_2J_2022.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT400to600_2J_2022.unix_code  = 31214
ZJetsToNuNu_2jets_PT400to600_2J_2022.EE         = 0

ZJetsToNuNu_2jets_PT600_2J_2022                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_2J_2022")
ZJetsToNuNu_2jets_PT600_2J_2022.sigma           = 0.1311
ZJetsToNuNu_2jets_PT600_2J_2022.year            = 2022
ZJetsToNuNu_2jets_PT600_2J_2022.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_2J_2022.process         = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT600_2J_2022.unix_code       = 31215
ZJetsToNuNu_2jets_PT600_2J_2022.EE              = 0

ZJetsToNuNu_2jets_2022 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_2022")
ZJetsToNuNu_2jets_2022.year = 2022
ZJetsToNuNu_2jets_2022.components = [
                                        ZJetsToNuNu_2jets_PT40to100_1J_2022,
                                        ZJetsToNuNu_2jets_PT100to200_1J_2022,
                                        ZJetsToNuNu_2jets_PT200to400_1J_2022,
                                        ZJetsToNuNu_2jets_PT400to600_1J_2022,
                                        ZJetsToNuNu_2jets_PT600_1J_2022,
                                        ZJetsToNuNu_2jets_PT40to100_2J_2022,
                                        ZJetsToNuNu_2jets_PT100to200_2J_2022,
                                        ZJetsToNuNu_2jets_PT200to400_2J_2022,
                                        ZJetsToNuNu_2jets_PT400to600_2J_2022,
                                        ZJetsToNuNu_2jets_PT600_2J_2022
                                    ]

################################ WJets ################################
WJets_HT120to200_2022               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT120to200_2022") 
WJets_HT120to200_2022.dataset       = "/WtoLNu-4Jets_MLNu-120to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT120to200_2022.sigma         = 167
WJets_HT120to200_2022.year          = 2022
WJets_HT120to200_2022.process       = "WJets_2022"
WJets_HT120to200_2022.unix_code     = 31300
WJets_HT120to200_2022.EE            = 0

WJets_HT200to400_2022               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT200to400_2022") 
WJets_HT200to400_2022.dataset       = "/WtoLNu-4Jets_MLNu-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT200to400_2022.sigma         = 20.3	
WJets_HT200to400_2022.year          = 2022
WJets_HT200to400_2022.process       = "WJets_2022"
WJets_HT200to400_2022.unix_code     = 31301
WJets_HT200to400_2022.EE            = 0

WJets_HT400to800_2022               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT400to800_2022") 
WJets_HT400to800_2022.dataset       = "/WtoLNu-4Jets_MLNu-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT400to800_2022.sigma         = 1.596
WJets_HT400to800_2022.year          = 2022
WJets_HT400to800_2022.process       = "WJets_2022"
WJets_HT400to800_2022.unix_code     = 31302
WJets_HT400to800_2022.EE            = 0

WJets_HT800to1500_2022              = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT800to1500_2022") 
WJets_HT800to1500_2022.dataset      = "/WtoLNu-4Jets_MLNu-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT800to1500_2022.sigma        = 0.1095	
WJets_HT800to1500_2022.year         = 2022
WJets_HT800to1500_2022.process      = "WJets_2022"
WJets_HT800to1500_2022.unix_code    = 31303
WJets_HT800to1500_2022.EE           = 0

WJets_HT1500to2500_2022             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT1500to2500_2022") 
WJets_HT1500to2500_2022.dataset     = "/WtoLNu-4Jets_MLNu-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT1500to2500_2022.sigma       = 0.006365
WJets_HT1500to2500_2022.year        = 2022
WJets_HT1500to2500_2022.process     = "WJets_2022"
WJets_HT1500to2500_2022.unix_code   = 31304
WJets_HT1500to2500_2022.EE          = 0

WJets_HT2500to4000_2022             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT2500to4000_2022") 
WJets_HT2500to4000_2022.dataset     = "/WtoLNu-4Jets_MLNu-2500to4000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT2500to4000_2022.sigma       = 0.0003463
WJets_HT2500to4000_2022.year        = 2022
WJets_HT2500to4000_2022.process     = "WJets_2022"
WJets_HT2500to4000_2022.unix_code   = 31305
WJets_HT2500to4000_2022.EE          = 0

WJets_HT4000to6000_2022             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT4000to6000_2022") 
WJets_HT4000to6000_2022.dataset     = "/WtoLNu-4Jets_MLNu-4000to6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT4000to6000_2022.sigma       = 0.00001075
WJets_HT4000to6000_2022.year        = 2022
WJets_HT4000to6000_2022.process     = "WJets_2022"
WJets_HT4000to6000_2022.unix_code   = 31306
WJets_HT4000to6000_2022.EE          = 0

WJets_HT6000_2022                   = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT6000_2022") 
WJets_HT6000_2022.dataset           = "/WtoLNu-4Jets_MLNu-6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
WJets_HT6000_2022.sigma             = 4.182e-7	
WJets_HT6000_2022.year              = 2022
WJets_HT6000_2022.process           = "WJets_2022"
WJets_HT6000_2022.unix_code         = 31307
WJets_HT6000_2022.EE                = 0

WJets_2022                  = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2022")
WJets_2022.year             = 2022
WJets_2022.components       = [WJets_HT120to200_2022, WJets_HT200to400_2022, WJets_HT400to800_2022, WJets_HT800to1500_2022, WJets_HT1500to2500_2022, WJets_HT2500to4000_2022, WJets_HT4000to6000_2022, WJets_HT6000_2022]

WJets_2jets0J_2022           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets0J_2022")
WJets_2jets0J_2022.dataset   = "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM"
WJets_2jets0J_2022.sigma     = 55760 
WJets_2jets0J_2022.year      = 2022
WJets_2jets0J_2022.process   = "WJets_2jets_2022"
WJets_2jets0J_2022.unix_code = 31308
WJets_2jets0J_2022.EE        = 0

WJets_2jets1J_2022           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets1J_2022")
WJets_2jets1J_2022.dataset   = "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
WJets_2jets1J_2022.sigma     = 9529 
WJets_2jets1J_2022.year      = 2022
WJets_2jets1J_2022.process   = "WJets_2jets_2022"
WJets_2jets1J_2022.unix_code = 31309
WJets_2jets1J_2022.EE        = 0

WJets_2jets2J_2022           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets2J_2022")
WJets_2jets2J_2022.dataset   = "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
WJets_2jets2J_2022.sigma     = 3532 
WJets_2jets2J_2022.year      = 2022
WJets_2jets2J_2022.process   = "WJets_2jets_2022"
WJets_2jets2J_2022.unix_code = 31310
WJets_2jets2J_2022.EE        = 0

WJets_2jets_2022             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_2022")
WJets_2jets_2022.year        = 2022
WJets_2jets_2022.components  = [WJets_2jets0J_2022, WJets_2jets1J_2022, WJets_2jets2J_2022]

#######################################   VLQ T signals   #######################################
TprimeToTZ_700_2022           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M700GeV", "TprimeToTZ_700_2022")
TprimeToTZ_700_2022.sigma     = 0.07804 #pb  # questa è 2018 non 2022
TprimeToTZ_700_2022.year      = 2022
TprimeToTZ_700_2022.dataset   = '/TprimeBtoTZ_M-700_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM'
TprimeToTZ_700_2022.unix_code = 32000
TprimeToTZ_700_2022.EE        = 0

TprimeToTZ_800_2022           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M800GeV", "TprimeToTZ_800_2022")
TprimeToTZ_800_2022.sigma     = 0.04155 #pb  # questa è 2018 non 2022
TprimeToTZ_800_2022.year      = 2022
TprimeToTZ_800_2022.dataset   = '/TprimeBtoTZ_M-800_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM'
TprimeToTZ_800_2022.unix_code = 32001
TprimeToTZ_800_2022.EE        = 0

TprimeToTZ_900_2022           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M900GeV", "TprimeToTZ_900_2022")
TprimeToTZ_900_2022.sigma     = 0.02335 #pb  # questa è 2018 non 2022
TprimeToTZ_900_2022.year      = 2022
TprimeToTZ_900_2022.dataset   = '/TprimeBtoTZ_M-900_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM'
TprimeToTZ_900_2022.unix_code = 32002
TprimeToTZ_900_2022.EE        = 0

TprimeToTZ_1000_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1000GeV", "TprimeToTZ_1000_2022")
TprimeToTZ_1000_2022.sigma     = 0.01362 #pb  # questa è 2018 non 2022
TprimeToTZ_1000_2022.year      = 2022
TprimeToTZ_1000_2022.dataset   = '/TprimeBtoTZ_M-1000_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM' 
TprimeToTZ_1000_2022.unix_code = 32003
TprimeToTZ_1000_2022.EE        = 0

TprimeToTZ_1100_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1100GeV", "TprimeToTZ_1100_2022")
TprimeToTZ_1100_2022.sigma     = 0.008228 #pb  # questa è 2018 non 2022
TprimeToTZ_1100_2022.year      = 2022
TprimeToTZ_1100_2022.dataset   = '/TprimeBtoTZ_M-1100_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM' 
TprimeToTZ_1100_2022.unix_code = 32003
TprimeToTZ_1100_2022.EE        = 0

TprimeToTZ_1200_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1200GeV", "TprimeToTZ_1200_2022")
TprimeToTZ_1200_2022.sigma     = 0.005113 #pb  # questa è 2018 non 2022
TprimeToTZ_1200_2022.year      = 2022
TprimeToTZ_1200_2022.dataset   = '/TprimeBtoTZ_M-1200_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM' 
TprimeToTZ_1200_2022.unix_code = 32003
TprimeToTZ_1200_2022.EE        = 0

TprimeToTZ_1300_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1300GeV", "TprimeToTZ_1300_2022")
TprimeToTZ_1300_2022.sigma     = 0.003256 #pb  # questa è 2018 non 2022
TprimeToTZ_1300_2022.year      = 2022
TprimeToTZ_1300_2022.dataset   = '/TprimeBtoTZ_M-1300_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM' 
TprimeToTZ_1300_2022.unix_code = 32003
TprimeToTZ_1300_2022.EE        = 0

TprimeToTZ_1400_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1400GeV", "TprimeToTZ_1400_2022")
TprimeToTZ_1400_2022.sigma     = 0.002121 #pb  # questa è 2018 non 2022
TprimeToTZ_1400_2022.year      = 2022
TprimeToTZ_1400_2022.dataset   = '/TprimeBtoTZ_M-1400_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM' 
TprimeToTZ_1400_2022.unix_code = 32003
TprimeToTZ_1400_2022.EE        = 0

TprimeToTZ_1500_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1500GeV", "TprimeToTZ_1500_2022")
TprimeToTZ_1500_2022.sigma     = 0.001407 #pb  # questa è 2018 non 2022
TprimeToTZ_1500_2022.year      = 2022
TprimeToTZ_1500_2022.dataset   = '/TprimeBtoTZ_M-1500_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM' 
TprimeToTZ_1500_2022.unix_code = 32003
TprimeToTZ_1500_2022.EE        = 0

TprimeToTZ_1600_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1600GeV", "TprimeToTZ_1600_2022")
TprimeToTZ_1600_2022.sigma     = 0.0009456 #pb  # questa è 2018 non 2022
TprimeToTZ_1600_2022.year      = 2022
TprimeToTZ_1600_2022.dataset   = '/TprimeBtoTZ_M-1600_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM' 
TprimeToTZ_1600_2022.unix_code = 32003
TprimeToTZ_1600_2022.EE        = 0

TprimeToTZ_1700_2022           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1700GeV", "TprimeToTZ_1700_2022")
TprimeToTZ_1700_2022.sigma     = 0.0006454 #pb  # questa è 2018 non 2022
TprimeToTZ_1700_2022.year      = 2022
TprimeToTZ_1700_2022.dataset   = '/TprimeBtoTZ_M-1700_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM' 
TprimeToTZ_1700_2022.unix_code = 32003
TprimeToTZ_1700_2022.EE        = 0

TprimeToTZ_1800_2022           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1800GeV", "TprimeToTZ_1800_2022")
TprimeToTZ_1800_2022.sigma     = 0.0004463 #pb
TprimeToTZ_1800_2022.year      = 2022
TprimeToTZ_1800_2022.dataset   = '/TprimeBtoTZ_M-1800_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM'
TprimeToTZ_1800_2022.unix_code = 22000
TprimeToTZ_1800_2022.EE        = 0


###############################################################################################################################
##########################################                                           ##########################################
##########################################       samples for tagger studies          ##########################################
##########################################                                           ##########################################
###############################################################################################################################
Zprime4top_500_2022          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M500GeV", "Zprime4top_500_2022")
Zprime4top_500_2022.sigma    = 1 #pb
Zprime4top_500_2022.year     = 2022
Zprime4top_500_2022.dataset  = '/TopPhilic_ttzp_13p6TeV_m500_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-500_Width4_nanoaod_hotvr_UL2022v1_230510-00000000000000000000000000000000/USER'
Zprime4top_500_2022.EE       = 0

Zprime4top_1000_2022          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M1000GeV", "Zprime4top_1000_2022")
Zprime4top_1000_2022.sigma    = 1 #pb
Zprime4top_1000_2022.year     = 2022
Zprime4top_1000_2022.dataset  = '/TopPhilic_ttzp_13p6TeV_m1000_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-1000_Width4_nanoaod_hotvr_UL2022v1_230510-00000000000000000000000000000000/USER'
Zprime4top_1000_2022.EE       = 0

Zprime4top_2000_2022          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M2000GeV", "Zprime4top_2000_2022")
Zprime4top_2000_2022.sigma    = 1 #pb
Zprime4top_2000_2022.year     = 2022
Zprime4top_2000_2022.dataset  = '/TopPhilic_ttzp_13p6TeV_m2000_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-2000_Width4_nanoaod_hotvr_UL2022v1_230510-00000000000000000000000000000000/USER'
Zprime4top_2000_2022.EE       = 0


###############################################################################################################################
##########################################                                           ##########################################
##########################################                   2022EE                  ##########################################
##########################################                                           ##########################################
###############################################################################################################################
# Era EFG del 2022 hanno avuto un proble water leak (controlla bene?) per cui vanno sotto una tag diversa 
# rispetto a era CD, per questo finora abbiamo usato la tag Run3Summer22 e da qui rifacciamo i sample con
# 2022EE --> Run3Summer22EE, ci sono correzioni diverse per i due pezzi quindi invece di cambiare l'anno
# aggiungerò un .EE che sarà True solo per i 2022EE, False per i 2022 e per gli altri anni non definito
# NB per i dati le ere hanno tutti year 2022 perché il golden JSON è lo stesso per tutti
################################ QCD ################################
# QCD_HT40to70_2022EE               = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT40to70_2022EE")
# QCD_HT40to70_2022EE.sigma         = 311.7*(10**6) #pb
# QCD_HT40to70_2022EE.year          = 2022
# QCD_HT40to70_2022EE.dataset       = # NO DATASET
# QCD_HT40to70_2022EE.process       = "QCD_2022EE"
# QCD_HT40to70_2022EE.unix_code     = 41000
# QCD_HT40to70_2022EE.EE            = 1
QCD_HT70to100_2022EE              = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT70to100_2022EE")
QCD_HT70to100_2022EE.sigma        = 58.6*(10**6) #pb 3.117e+08
QCD_HT70to100_2022EE.year         = 2022
QCD_HT70to100_2022EE.dataset      = "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT70to100_2022EE.process      = "QCD_2022EE"
QCD_HT70to100_2022EE.unix_code    = 41001
QCD_HT70to100_2022EE.EE           = 1

QCD_HT100to200_2022EE             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT100to200_2022EE")
QCD_HT100to200_2022EE.sigma       = 25.1*(10**6) #pb
QCD_HT100to200_2022EE.year        = 2022
QCD_HT100to200_2022EE.dataset     = "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT100to200_2022EE.process     = "QCD_2022EE"
QCD_HT100to200_2022EE.unix_code   = 41002
QCD_HT100to200_2022EE.EE          = 1

QCD_HT200to400_2022EE             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT200to400_2022EE")
QCD_HT200to400_2022EE.sigma       = 1.96*(10**6) #pb
QCD_HT200to400_2022EE.year        = 2022
QCD_HT200to400_2022EE.dataset     = "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT200to400_2022EE.process     = "QCD_2022EE"
QCD_HT200to400_2022EE.unix_code   = 41003
QCD_HT200to400_2022EE.EE          = 1

QCD_HT400to600_2022EE             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT400to600_2022EE")
QCD_HT400to600_2022EE.sigma       = 96.0*(10**3) #pb
QCD_HT400to600_2022EE.year        = 2022
QCD_HT400to600_2022EE.dataset     = "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT400to600_2022EE.process     = "QCD_2022EE"
QCD_HT400to600_2022EE.unix_code   = 41004
QCD_HT400to600_2022EE.EE          = 1

QCD_HT600to800_2022EE             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT600to800_2022EE")
QCD_HT600to800_2022EE.sigma       = 13.5*(10**3) #pb
QCD_HT600to800_2022EE.year        = 2022
QCD_HT600to800_2022EE.dataset     = "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT600to800_2022EE.process     = "QCD_2022EE"
QCD_HT600to800_2022EE.unix_code   = 41005
QCD_HT600to800_2022EE.EE          = 1

QCD_HT800to1000_2022EE            = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT800to1000_2022EE")
QCD_HT800to1000_2022EE.sigma      = 3.03*(10**3) #pb
QCD_HT800to1000_2022EE.year       = 2022
QCD_HT800to1000_2022EE.dataset    = "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT800to1000_2022EE.process    = "QCD_2022EE"
QCD_HT800to1000_2022EE.unix_code  = 41006
QCD_HT800to1000_2022EE.EE         = 1

QCD_HT1000to1200_2022EE           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1000to1200_2022EE")
QCD_HT1000to1200_2022EE.sigma     = 884 #pb
QCD_HT1000to1200_2022EE.year      = 2022
QCD_HT1000to1200_2022EE.dataset   = "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT1000to1200_2022EE.process   = "QCD_2022EE"
QCD_HT1000to1200_2022EE.unix_code = 41007
QCD_HT1000to1200_2022EE.EE        = 1

QCD_HT1200to1500_2022EE           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1200to1500_2022EE")
QCD_HT1200to1500_2022EE.sigma     = 384 #pb
QCD_HT1200to1500_2022EE.year      = 2022
QCD_HT1200to1500_2022EE.dataset   = "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT1200to1500_2022EE.process   = "QCD_2022EE"
QCD_HT1200to1500_2022EE.unix_code = 41007
QCD_HT1200to1500_2022EE.EE        = 1

QCD_HT1500to2000_2022EE           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1500to2000_2022EE")
QCD_HT1500to2000_2022EE.sigma     = 125 #pb
QCD_HT1500to2000_2022EE.year      = 2022
QCD_HT1500to2000_2022EE.dataset   = "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT1500to2000_2022EE.process   = "QCD_2022EE"
QCD_HT1500to2000_2022EE.unix_code = 41008
QCD_HT1500to2000_2022EE.EE        = 1

QCD_HT2000_2022EE                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT2000_2022EE")
QCD_HT2000_2022EE.sigma           = 26.5 #pb
QCD_HT2000_2022EE.year            = 2022
QCD_HT2000_2022EE.dataset         = "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
QCD_HT2000_2022EE.process         = "QCD_2022EE"
QCD_HT2000_2022EE.unix_code       = 41009
QCD_HT2000_2022EE.EE              = 1

QCD_2022EE                        = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2022EE")
QCD_2022EE.year                   = 2022
QCD_2022EE.components             = [ 
                                    # QCD_HT40to70_2022EE, 
                                    QCD_HT70to100_2022EE, QCD_HT100to200_2022EE, QCD_HT200to400_2022EE,
                                    QCD_HT400to600_2022EE, QCD_HT600to800_2022EE, QCD_HT800to1000_2022EE, 
                                    QCD_HT1000to1200_2022EE,QCD_HT1200to1500_2022EE,
                                    QCD_HT1500to2000_2022EE, QCD_HT2000_2022EE
                                ]


# /QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-JMENano12p5_132X_mcRun3_2022_realistic_postEE_v4-v2/NANOAODSIM


################################ TTbar ################################
TT_semilep_2022EE             = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2022EE")
TT_semilep_2022EE.sigma       = 405.7 #pb 
TT_semilep_2022EE.year        = 2022
TT_semilep_2022EE.dataset     = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"
TT_semilep_2022EE.process     = 'TT_2022EE'
TT_semilep_2022EE.unix_code   = 41100
TT_semilep_2022EE.EE          = 1

TT_hadr_2022EE                = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_hadr_2022EE")
TT_hadr_2022EE.sigma          = 419.8
TT_hadr_2022EE.year           = 2022
TT_hadr_2022EE.dataset        = "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM"
TT_hadr_2022EE.process        = 'TT_2022EE'
TT_hadr_2022EE.unix_code      = 41101
TT_hadr_2022EE.EE             = 1

TT_2022EE                     = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_2022EE")
TT_2022EE.year                = 2022
TT_2022EE.components          = [TT_semilep_2022EE, TT_hadr_2022EE]

################################ ZJets ################################

ZJetsToNuNu_HT100to200_2022EE             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT100to200_2022EE")
ZJetsToNuNu_HT100to200_2022EE.sigma       = 273.6 #pb
ZJetsToNuNu_HT100to200_2022EE.year        = 2022
ZJetsToNuNu_HT100to200_2022EE.dataset     = "/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
ZJetsToNuNu_HT100to200_2022EE.process     = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT100to200_2022EE.unix_code   = 41200
ZJetsToNuNu_HT100to200_2022EE.EE          = 1

ZJetsToNuNu_HT200to400_2022EE             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT200to400_2022EE")
ZJetsToNuNu_HT200to400_2022EE.sigma       = 76.14 #pb
ZJetsToNuNu_HT200to400_2022EE.year        = 2022
ZJetsToNuNu_HT200to400_2022EE.dataset     = "/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
ZJetsToNuNu_HT200to400_2022EE.process     = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT200to400_2022EE.unix_code   = 41201
ZJetsToNuNu_HT200to400_2022EE.EE          = 1

ZJetsToNuNu_HT400to800_2022EE             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT400to800_2022EE")
ZJetsToNuNu_HT400to800_2022EE.sigma       = 13.18 #pb
ZJetsToNuNu_HT400to800_2022EE.year        = 2022
ZJetsToNuNu_HT400to800_2022EE.dataset     = "/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
ZJetsToNuNu_HT400to800_2022EE.process     = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT400to800_2022EE.unix_code   = 41202
ZJetsToNuNu_HT400to800_2022EE.EE          = 1

ZJetsToNuNu_HT800to1500_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT800to1500_2022EE")
ZJetsToNuNu_HT800to1500_2022EE.sigma      = 1.366 #pb
ZJetsToNuNu_HT800to1500_2022EE.year       = 2022
ZJetsToNuNu_HT800to1500_2022EE.dataset    = "/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM"
ZJetsToNuNu_HT800to1500_2022EE.process    = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT800to1500_2022EE.unix_code  = 41203
ZJetsToNuNu_HT800to1500_2022EE.EE         = 1

ZJetsToNuNu_HT1500to2500_2022EE           = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT1500to2500_2022EE")
ZJetsToNuNu_HT1500to2500_2022EE.sigma     = 0.09852 #pb
ZJetsToNuNu_HT1500to2500_2022EE.year      = 2022
ZJetsToNuNu_HT1500to2500_2022EE.dataset   = "/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
ZJetsToNuNu_HT1500to2500_2022EE.process   = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT1500to2500_2022EE.unix_code = 41204
ZJetsToNuNu_HT1500to2500_2022EE.EE        = 1

ZJetsToNuNu_HT2500_2022EE                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT2500_2022EE")
ZJetsToNuNu_HT2500_2022EE.sigma           = 0.006699 #pb
ZJetsToNuNu_HT2500_2022EE.year            = 2022
ZJetsToNuNu_HT2500_2022EE.dataset         = "/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
ZJetsToNuNu_HT2500_2022EE.process         = 'ZJetsToNuNu_2022EE'
ZJetsToNuNu_HT2500_2022EE.unix_code       = 41205
ZJetsToNuNu_HT2500_2022EE.EE              = 1

ZJetsToNuNu_2022EE                        = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2022EE")
ZJetsToNuNu_2022EE.year                   = 2022
ZJetsToNuNu_2022EE.components             = [
                                            ZJetsToNuNu_HT100to200_2022EE, ZJetsToNuNu_HT200to400_2022EE, ZJetsToNuNu_HT400to800_2022EE,
                                            ZJetsToNuNu_HT800to1500_2022EE, ZJetsToNuNu_HT1500to2500_2022EE, ZJetsToNuNu_HT2500_2022EE 
                                            ]

ZJetsToNuNu_2jets_PT40to100_1J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_1J_2022EE")
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.sigma      = 929.8	
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.process    = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.unix_code  = 41207
ZJetsToNuNu_2jets_PT40to100_1J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT100to200_1J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_1J_2022EE")
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.sigma      = 86.38
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.process    = 'ZJetsToNuNu_2jets_2022EE'
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.unix_code  = 41208
ZJetsToNuNu_2jets_PT100to200_1J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT200to400_1J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_1J_2022EE")
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.sigma      = 6.354	
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.unix_code  = 41209
ZJetsToNuNu_2jets_PT200to400_1J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT400to600_1J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_1J_2022EE")
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.sigma      = 0.2188
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.unix_code  = 41210
ZJetsToNuNu_2jets_PT400to600_1J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT600_1J_2022EE                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_1J_2022EE")
ZJetsToNuNu_2jets_PT600_1J_2022EE.sigma           = 0.02583
ZJetsToNuNu_2jets_PT600_1J_2022EE.year            = 2022
ZJetsToNuNu_2jets_PT600_1J_2022EE.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_1J_2022EE.process         = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT600_1J_2022EE.unix_code       = 41211
ZJetsToNuNu_2jets_PT600_1J_2022EE.EE              = 1

ZJetsToNuNu_2jets_PT40to100_2J_2022EE             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT40to100_2J_2022EE")
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.sigma       = 335.5
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.year        = 2022
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.dataset     = "/Zto2Nu-2Jets_PTNuNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.process     = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.unix_code   = 41212
ZJetsToNuNu_2jets_PT40to100_2J_2022EE.EE          = 1

ZJetsToNuNu_2jets_PT100to200_2J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT100to200_2J_2022EE")
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.sigma      = 100.4
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.unix_code  = 41213
ZJetsToNuNu_2jets_PT100to200_2J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT200to400_2J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT200to400_2J_2022EE")
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.sigma      = 13.86
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM"
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.unix_code  = 41214
ZJetsToNuNu_2jets_PT200to400_2J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT400to600_2J_2022EE            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT400to600_2J_2022EE")
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.sigma      = 0.7816
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.year       = 2022
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.dataset    = "/Zto2Nu-2Jets_PTNuNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.process    = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.unix_code  = 41215
ZJetsToNuNu_2jets_PT400to600_2J_2022EE.EE         = 1

ZJetsToNuNu_2jets_PT600_2J_2022EE                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_PT600_2J_2022EE")
ZJetsToNuNu_2jets_PT600_2J_2022EE.sigma           = 0.1311
ZJetsToNuNu_2jets_PT600_2J_2022EE.year            = 2022
ZJetsToNuNu_2jets_PT600_2J_2022EE.dataset         = "/Zto2Nu-2Jets_PTNuNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
ZJetsToNuNu_2jets_PT600_2J_2022EE.process         = 'ZJetsToNuNu_2jets_2022'
ZJetsToNuNu_2jets_PT600_2J_2022EE.unix_code       = 41216
ZJetsToNuNu_2jets_PT600_2J_2022EE.EE              = 1

ZJetsToNuNu_2jets_2022EE = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2jets_2022EE")
ZJetsToNuNu_2jets_2022EE.year = 2022
ZJetsToNuNu_2jets_2022EE.components = [
                                        ZJetsToNuNu_2jets_PT40to100_1J_2022EE,
                                        ZJetsToNuNu_2jets_PT100to200_1J_2022EE,
                                        ZJetsToNuNu_2jets_PT200to400_1J_2022EE,
                                        ZJetsToNuNu_2jets_PT400to600_1J_2022EE,
                                        ZJetsToNuNu_2jets_PT600_1J_2022EE,
                                        ZJetsToNuNu_2jets_PT40to100_2J_2022EE,
                                        ZJetsToNuNu_2jets_PT100to200_2J_2022EE,
                                        ZJetsToNuNu_2jets_PT200to400_2J_2022EE,
                                        ZJetsToNuNu_2jets_PT400to600_2J_2022EE,
                                        ZJetsToNuNu_2jets_PT600_2J_2022EE
                                    ]
################################ WJets ################################

WJets_HT120to200_2022EE               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT120to200_2022EE") 
WJets_HT120to200_2022EE.dataset       = "/WtoLNu-4Jets_MLNu-120to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT120to200_2022EE.sigma         = 167
WJets_HT120to200_2022EE.year          = 2022
WJets_HT120to200_2022EE.process       = "WJets_2022"
WJets_HT120to200_2022EE.unix_code     = 41300
WJets_HT120to200_2022EE.EE            = 1

WJets_HT200to400_2022EE               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT200to400_2022EE") 
WJets_HT200to400_2022EE.dataset       = "/WtoLNu-4Jets_MLNu-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT200to400_2022EE.sigma         = 20.3
WJets_HT200to400_2022EE.year          = 2022
WJets_HT200to400_2022EE.process       = "WJets_2022"
WJets_HT200to400_2022EE.unix_code     = 41301
WJets_HT200to400_2022EE.EE            = 1

WJets_HT400to800_2022EE               = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT400to800_2022EE") 
WJets_HT400to800_2022EE.dataset       = "/WtoLNu-4Jets_MLNu-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT400to800_2022EE.sigma         = 1.596	
WJets_HT400to800_2022EE.year          = 2022
WJets_HT400to800_2022EE.process       = "WJets_2022"
WJets_HT400to800_2022EE.unix_code     = 41302
WJets_HT400to800_2022EE.EE            = 1

WJets_HT800to1500_2022EE              = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT800to1500_2022EE") 
WJets_HT800to1500_2022EE.dataset      = "/WtoLNu-4Jets_MLNu-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT800to1500_2022EE.sigma        = 0.1095
WJets_HT800to1500_2022EE.year         = 2022
WJets_HT800to1500_2022EE.process      = "WJets_2022"
WJets_HT800to1500_2022EE.unix_code    = 41303
WJets_HT800to1500_2022EE.EE           = 1

WJets_HT1500to2500_2022EE             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT1500to2500_2022EE") 
WJets_HT1500to2500_2022EE.dataset     = "/WtoLNu-4Jets_MLNu-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
WJets_HT1500to2500_2022EE.sigma       = 0.006365
WJets_HT1500to2500_2022EE.year        = 2022
WJets_HT1500to2500_2022EE.process     = "WJets_2022"
WJets_HT1500to2500_2022EE.unix_code   = 41304
WJets_HT1500to2500_2022EE.EE          = 1

WJets_HT2500to4000_2022EE             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT2500to4000_2022EE") 
WJets_HT2500to4000_2022EE.dataset     = "/WtoLNu-4Jets_MLNu-2500to4000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT2500to4000_2022EE.sigma       = 0.0003463
WJets_HT2500to4000_2022EE.year        = 2022
WJets_HT2500to4000_2022EE.process     = "WJets_2022"
WJets_HT2500to4000_2022EE.unix_code   = 41305
WJets_HT2500to4000_2022EE.EE          = 1

WJets_HT4000to6000_2022EE             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT4000to6000_2022EE") 
WJets_HT4000to6000_2022EE.dataset     = "/WtoLNu-4Jets_MLNu-4000to6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT4000to6000_2022EE.sigma       = 0.00001075
WJets_HT4000to6000_2022EE.year        = 2022
WJets_HT4000to6000_2022EE.process     = "WJets_2022"
WJets_HT4000to6000_2022EE.unix_code   = 41306
WJets_HT4000to6000_2022EE.EE          = 1

WJets_HT6000_2022EE                   = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_HT6000_2022EE") 
WJets_HT6000_2022EE.dataset           = "/WtoLNu-4Jets_MLNu-6000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM"
WJets_HT6000_2022EE.sigma             = 4.182e-7
WJets_HT6000_2022EE.year              = 2022
WJets_HT6000_2022EE.process           = "WJets_2022"
WJets_HT6000_2022EE.unix_code         = 41307
WJets_HT6000_2022EE.EE                = 1

WJets_2022EE                  = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2022EE")
WJets_2022EE.year             = 2022
WJets_2022EE.components       = [WJets_HT120to200_2022EE, WJets_HT200to400_2022EE, WJets_HT400to800_2022EE, WJets_HT800to1500_2022EE, WJets_HT1500to2500_2022EE, WJets_HT2500to4000_2022EE, WJets_HT4000to6000_2022EE, WJets_HT6000_2022EE]


WJets_2jets0J_2022EE           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets0J_2022EE")
WJets_2jets0J_2022EE.dataset   = "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM"
WJets_2jets0J_2022EE.sigma     = 55760
WJets_2jets0J_2022EE.year      = 2022
WJets_2jets0J_2022EE.process   = "WJets_2jets_2022"
WJets_2jets0J_2022EE.unix_code = 41308
WJets_2jets0J_2022EE.EE        = 1

WJets_2jets1J_2022EE           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets1J_2022EE")
WJets_2jets1J_2022EE.dataset   = "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
WJets_2jets1J_2022EE.sigma     = 9529
WJets_2jets1J_2022EE.year      = 2022
WJets_2jets1J_2022EE.process   = "WJets_2jets_2022"
WJets_2jets1J_2022EE.unix_code = 41309
WJets_2jets1J_2022EE.EE        = 1

WJets_2jets2J_2022EE           = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets2J_2022EE")
WJets_2jets2J_2022EE.dataset   = "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM"
WJets_2jets2J_2022EE.sigma     = 3532
WJets_2jets2J_2022EE.year      = 2022
WJets_2jets2J_2022EE.process   = "WJets_2jets_2022"
WJets_2jets2J_2022EE.unix_code = 41310
WJets_2jets2J_2022EE.EE        = 1

WJets_2jets_2022EE             = sample(ROOT.kGreen-3, 1, 1001, "W + Jets", "WJets_2jets_2022EE")
WJets_2jets_2022EE.year        = 2022
WJets_2jets_2022EE.components  = [WJets_2jets0J_2022EE, WJets_2jets1J_2022EE, WJets_2jets2J_2022EE]

#######################################   VLQ T signals   #######################################
TprimeToTZ_700_2022EE           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M700GeV", "TprimeToTZ_700_2022EE")
TprimeToTZ_700_2022EE.sigma     = 0.07804 #pb  # questa è 2018 non 2022
TprimeToTZ_700_2022EE.year      = 2022
TprimeToTZ_700_2022EE.dataset   = '/TprimeBtoTZ_M-700_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM'
TprimeToTZ_700_2022EE.unix_code = 42000
TprimeToTZ_700_2022EE.EE        = 1

TprimeToTZ_800_2022EE           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M800GeV", "TprimeToTZ_800_2022EE")
TprimeToTZ_800_2022EE.sigma     = 0.041545 #pb  # questa è 2018 non 2022
TprimeToTZ_800_2022EE.year      = 2022
TprimeToTZ_800_2022EE.dataset   = '/TprimeBtoTZ_M-800_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM'
TprimeToTZ_800_2022EE.unix_code = 42000
TprimeToTZ_800_2022EE.EE        = 1

TprimeToTZ_900_2022EE           = sample(ROOT.kGreen, 1, 1001, "T#rightarrow tZ M900GeV", "TprimeToTZ_900_2022EE")
TprimeToTZ_900_2022EE.sigma     = 0.023345 #pb  # questa è 2018 non 2022
TprimeToTZ_900_2022EE.year      = 2022
TprimeToTZ_900_2022EE.dataset   = '/TprimeBtoTZ_M-900_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM'
TprimeToTZ_900_2022EE.unix_code = 42000
TprimeToTZ_900_2022EE.EE        = 1

TprimeToTZ_1000_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1000GeV", "TprimeToTZ_1000_2022EE")
TprimeToTZ_1000_2022EE.sigma     = 0.01362 #pb  # questa è 2018 non 2022
TprimeToTZ_1000_2022EE.year      = 2022
TprimeToTZ_1000_2022EE.dataset   = '/TprimeBtoTZ_M-1000_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM' 
TprimeToTZ_1000_2022EE.unix_code = 42001
TprimeToTZ_1000_2022EE.EE        = 1

TprimeToTZ_1100_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1100GeV", "TprimeToTZ_1100_2022EE")
TprimeToTZ_1100_2022EE.sigma     = 0.008228 #pb  # questa è 2018 non 2022
TprimeToTZ_1100_2022EE.year      = 2022
TprimeToTZ_1100_2022EE.dataset   = '/TprimeBtoTZ_M-1100_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM' 
TprimeToTZ_1100_2022EE.unix_code = 42001
TprimeToTZ_1100_2022EE.EE        = 1

TprimeToTZ_1200_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1200GeV", "TprimeToTZ_1200_2022EE")
TprimeToTZ_1200_2022EE.sigma     = 0.005113 #pb  # questa è 2018 non 2022
TprimeToTZ_1200_2022EE.year      = 2022
TprimeToTZ_1200_2022EE.dataset   = '/TprimeBtoTZ_M-1200_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM' 
TprimeToTZ_1200_2022EE.unix_code = 42001
TprimeToTZ_1200_2022EE.EE        = 1

TprimeToTZ_1300_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1300GeV", "TprimeToTZ_1300_2022EE")
TprimeToTZ_1300_2022EE.sigma     = 0.003256 #pb  # questa è 2018 non 2022
TprimeToTZ_1300_2022EE.year      = 2022
TprimeToTZ_1300_2022EE.dataset   = '/TprimeBtoTZ_M-1300_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM' 
TprimeToTZ_1300_2022EE.unix_code = 42001
TprimeToTZ_1300_2022EE.EE        = 1

TprimeToTZ_1400_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1400GeV", "TprimeToTZ_1400_2022EE")
TprimeToTZ_1400_2022EE.sigma     = 0.002121 #pb  # questa è 2018 non 2022
TprimeToTZ_1400_2022EE.year      = 2022
TprimeToTZ_1400_2022EE.dataset   = '/TprimeBtoTZ_M-1400_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM' 
TprimeToTZ_1400_2022EE.unix_code = 42001
TprimeToTZ_1400_2022EE.EE        = 1

TprimeToTZ_1500_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1500GeV", "TprimeToTZ_1500_2022EE")
TprimeToTZ_1500_2022EE.sigma     = 0.001407 #pb  # questa è 2018 non 2022
TprimeToTZ_1500_2022EE.year      = 2022
TprimeToTZ_1500_2022EE.dataset   = '/TprimeBtoTZ_M-1500_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM' 
TprimeToTZ_1500_2022EE.unix_code = 42001
TprimeToTZ_1500_2022EE.EE        = 1

TprimeToTZ_1600_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1600GeV", "TprimeToTZ_1600_2022EE")
TprimeToTZ_1600_2022EE.sigma     = 0.0008456 #pb  # questa è 2018 non 2022
TprimeToTZ_1600_2022EE.year      = 2022
TprimeToTZ_1600_2022EE.dataset   = '/TprimeBtoTZ_M-1600_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM' 
TprimeToTZ_1600_2022EE.unix_code = 42001
TprimeToTZ_1600_2022EE.EE        = 1

TprimeToTZ_1700_2022EE           = sample(ROOT.kGreen+2, 1, 1001, "T#rightarrow tZ M1700GeV", "TprimeToTZ_1700_2022EE")
TprimeToTZ_1700_2022EE.sigma     = 0.0006454 #pb  # questa è 2018 non 2022
TprimeToTZ_1700_2022EE.year      = 2022
TprimeToTZ_1700_2022EE.dataset   = '/TprimeBtoTZ_M-1700_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM' 
TprimeToTZ_1700_2022EE.unix_code = 42001
TprimeToTZ_1700_2022EE.EE        = 1

TprimeToTZ_1800_2022EE           = sample(ROOT.kGreen+4, 1, 1001, "T#rightarrow tZ M1800GeV", "TprimeToTZ_1800_2022EE")
TprimeToTZ_1800_2022EE.sigma     = 0.0004463 #pb
TprimeToTZ_1800_2022EE.year      = 2022
TprimeToTZ_1800_2022EE.dataset   = '/TprimeBtoTZ_M-1800_LH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM'
TprimeToTZ_1800_2022EE.unix_code = 42002
TprimeToTZ_1800_2022EE.EE        = 1

###############################################################################################################################
##########################################                                           ##########################################
##########################################       samples for tagger studies          ##########################################
##########################################                                           ##########################################
###############################################################################################################################
Zprime4top_500_2022EE          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M500GeV", "Zprime4top_500_2022EE")
Zprime4top_500_2022EE.sigma    = 1 #pb
Zprime4top_500_2022EE.year     = 2022
Zprime4top_500_2022EE.dataset  = '/TopPhilic_ttzp_13p6TeV_m500_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-500_Width4_nanoaod_hotvr_UL2022_EEv1_230510-00000000000000000000000000000000/USER'
Zprime4top_500_2022EE.EE       = 1

Zprime4top_1000_2022EE          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M1000GeV", "Zprime4top_1000_2022EE")
Zprime4top_1000_2022EE.sigma    = 1 #pb
Zprime4top_1000_2022EE.year     = 2022
Zprime4top_1000_2022EE.dataset  = '/TopPhilic_ttzp_13p6TeV_m1000_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-1000_Width4_nanoaod_hotvr_UL2022_EEv1_230510-00000000000000000000000000000000/USER'
Zprime4top_1000_2022EE.EE       = 1

Zprime4top_2000_2022EE          = sample(ROOT.kGreen+2, 1, 1001, "Zprime4top M2000GeV", "Zprime4top_2000_2022EE")
Zprime4top_2000_2022EE.sigma    = 1 #pb
Zprime4top_2000_2022EE.year     = 2022
Zprime4top_2000_2022EE.dataset  = '/TopPhilic_ttzp_13p6TeV_m2000_relwidth4_TuneCP5_13p6TeV-madgraph-pythia8/gmilella-crab_TTZprimeToTT_M-2000_Width4_nanoaod_hotvr_UL2022_EEv1_230510-00000000000000000000000000000000/USER'
Zprime4top_2000_2022EE.EE       = 1




###############################################################################################################################
########################### DATA 2018 ############################################
###############################################################################################################################
DataMETA_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETA_2018")
DataMETA_2018.runP      = 'A'
DataMETA_2018.year      = 2018
DataMETA_2018.dataset   = '/MET/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD' #'/MET/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataMETA_2018.process   = "DataMET_2018"
DataMETA_2018.unix_code = 20000
DataMETB_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETB_2018")
DataMETB_2018.runP      = 'B'
DataMETB_2018.year      = 2018
DataMETB_2018.dataset   = '/MET/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD' #'/MET/Run2018B-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataMETB_2018.process   = "DataMET_2018"
DataMETB_2018.unix_code = 20001
DataMETC_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETC_2018")
DataMETC_2018.runP      = 'C'
DataMETC_2018.year      = 2018
DataMETC_2018.dataset   = '/MET/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'#'/MET/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMETC_2018.process   = "DataMET_2018"
DataMETC_2018.unix_code = 20002
DataMETD_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETD_2018")
DataMETD_2018.runP      = 'D'
DataMETD_2018.year      = 2018
DataMETD_2018.dataset   = '/MET/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'#'/MET/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMETD_2018.process   = "DataMET_2018"
DataMETD_2018.unix_code = 20003

DataMET_2018            = sample(ROOT.kBlack, 1, 1001, "Data", "DataMET_2018")
DataMET_2018.year       = 2018
DataMET_2018.components = [DataMETA_2018, DataMETB_2018, 
                          DataMETC_2018, DataMETD_2018
                          ]

DataSingleMuA_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataSingleMuA_2018")
DataSingleMuA_2018.runP      = 'A'
DataSingleMuA_2018.year      = 2018
DataSingleMuA_2018.dataset   = '/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'
DataSingleMuA_2018.process   = "DataSingleMu_2018"
DataSingleMuA_2018.unix_code = 20100
DataSingleMuB_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataSingleMuB_2018")
DataSingleMuB_2018.runP      = 'B'
DataSingleMuB_2018.year      = 2018
DataSingleMuB_2018.dataset   = '/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'
DataSingleMuB_2018.process   = "DataSingleMu_2018"
DataSingleMuB_2018.unix_code = 20101
DataSingleMuC_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataSingleMuC_2018")
DataSingleMuC_2018.runP      = 'C'
DataSingleMuC_2018.year      = 2018
DataSingleMuC_2018.dataset   = '/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'
DataSingleMuC_2018.process   = "DataSingleMu_2018"
DataSingleMuC_2018.unix_code = 20102
DataSingleMuD_2018           = sample(ROOT.kBlack, 1, 1001, "Data", "DataSingleMuD_2018")
DataSingleMuD_2018.runP      = 'D'
DataSingleMuD_2018.year      = 2018
DataSingleMuD_2018.dataset   = '/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'
DataSingleMuD_2018.process   = "DataSingleMu_2018"
DataSingleMuD_2018.unix_code = 20103

DataSingleMu_2018            = sample(ROOT.kBlack, 1, 1001, "Data", "DataSingleMu_2018")
DataSingleMu_2018.year       = 2018
DataSingleMu_2018.components = [DataSingleMuA_2018, DataSingleMuB_2018, 
                                DataSingleMuC_2018, DataSingleMuD_2018
                               ]


# DataMETA_2018          = sample(ROOT.kBlack, 1, 1001, "Data", "DataMETA_2018")
# DataMETA_2018.runP     = 'A'
# DataMETA_2018.year     = 2018
# DataMETA_2018.dataset  = '/MET/Run2018A-02Apr2020-v1/NANOAOD' #ReRECO 2018 A

########################### DATA 2022 ############################################

DataJetMETC_2022            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC_2022")
DataJetMETC_2022.runP       = 'C'
DataJetMETC_2022.year       = 2022
DataJetMETC_2022.dataset    = '/JetMET/Run2022C-22Sep2023-v1/NANOAOD' #/JetMET/Run2022C-JMENano12p5-v1/NANOAOD da capire quale vogliono che usiamo
DataJetMETC_2022.unix_code  = 30000
DataJetMETC_2022.EE         = 0
DataJetMETD_2022            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETD_2022")
DataJetMETD_2022.runP       = 'D'
DataJetMETD_2022.year       = 2022
DataJetMETD_2022.dataset    = '/JetMET/Run2022D-22Sep2023-v1/NANOAOD'
DataJetMETD_2022.unix_code  = 30001
DataJetMETD_2022.EE         = 0
DataJetMET_2022             = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMET_2022")
DataJetMET_2022.year        = 2022
DataJetMET_2022.components  = [DataJetMETC_2022, DataJetMETD_2022]

DataJetMETE_2022EE            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETE_2022EE")
DataJetMETE_2022EE.runP       = 'E'
DataJetMETE_2022EE.year       = 2022
DataJetMETE_2022EE.dataset    = '/JetMET/Run2022E-22Sep2023-v1/NANOAOD'
DataJetMETE_2022EE.unix_code  = 30002
DataJetMETE_2022EE.EE         = 1
DataJetMETF_2022EE            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETF_2022EE")
DataJetMETF_2022EE.runP       = 'F'
DataJetMETF_2022EE.year       = 2022
DataJetMETF_2022EE.dataset    = '/JetMET/Run2022F-22Sep2023-v2/NANOAOD'
DataJetMETF_2022EE.unix_code  = 30003
DataJetMETF_2022EE.EE         = 1
DataJetMETG_2022EE            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETG_2022EE")
DataJetMETG_2022EE.runP       = 'G'
DataJetMETG_2022EE.year       = 2022
DataJetMETG_2022EE.dataset    = '/JetMET/Run2022G-22Sep2023-v2/NANOAOD'
DataJetMETG_2022EE.unix_code  = 30004
DataJetMETG_2022EE.EE         = 1
DataJetMET_2022EE             = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMET_2022EE")
DataJetMET_2022EE.year        = 2022
DataJetMET_2022EE.components  = [DataJetMETE_2022EE, DataJetMETF_2022EE, DataJetMETG_2022EE]

DataMuonC_2022              = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonC_2022")
DataMuonC_2022.runP         = 'C'
DataMuonC_2022.year         = 2022
DataMuonC_2022.dataset      = '/Muon/Run2022C-22Sep2023-v1/NANOAOD'
DataMuonC_2022.unix_code    = 30100
DataMuonC_2022.EE           = 0
DataMuonD_2022              = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonD_2022")
DataMuonD_2022.runP         = 'D'
DataMuonD_2022.year         = 2022
DataMuonD_2022.dataset      = '/Muon/Run2022C-22Sep2023-v1/NANOAOD'
DataMuonD_2022.unix_code    = 30101
DataMuonD_2022.EE           = 0
DataMuon_2022               = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuon_2022")
DataMuon_2022.year          = 2022
DataMuon_2022.components    = [DataMuonC_2022, DataMuonD_2022]

DataMuonE_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonE_2022EE")
DataMuonE_2022EE.runP         = 'E'
DataMuonE_2022EE.year         = 2022
DataMuonE_2022EE.dataset      = '/Muon/Run2022E-22Sep2023-v1/NANOAOD'
DataMuonE_2022EE.unix_code    = 30102
DataMuonE_2022EE.EE           = 1
DataMuonF_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonF_2022EE")
DataMuonF_2022EE.runP         = 'F'
DataMuonF_2022EE.year         = 2022
DataMuonF_2022EE.dataset      = '/Muon/Run2022F-22Sep2023-v2/NANOAOD'
DataMuonF_2022EE.unix_code    = 30103
DataMuonF_2022EE.EE           = 1
DataMuonG_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuonG_2022EE")
DataMuonG_2022EE.runP         = 'G'
DataMuonG_2022EE.year         = 2022
DataMuonG_2022EE.dataset      = '/Muon/Run2022G-22Sep2023-v1/NANOAOD'
DataMuonG_2022EE.unix_code    = 30104
DataMuonG_2022EE.EE           = 1
DataMuon_2022EE               = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuon_2022EE")
DataMuon_2022EE.year          = 2022
DataMuon_2022EE.components    = [DataMuonE_2022EE, DataMuonF_2022EE, DataMuonG_2022EE]

DataEGammaC_2022              = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaC_2022")
DataEGammaC_2022.year         = 2022
DataEGammaC_2022.dataset      = "/EGamma/Run2022C-22Sep2023-v1/NANOAOD"
DataEGammaC_2022.runP         = 'C'
DataEGammaC_2022.unix_code    = 30200
DataEGammaC_2022.EE           = 0
DataEGammaD_2022              = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaD_2022")
DataEGammaD_2022.year         = 2022
DataEGammaD_2022.dataset      = "/EGamma/Run2022D-22Sep2023-v1/NANOAOD"
DataEGammaD_2022.runP         = 'C'
DataEGammaD_2022.unix_code    = 30201
DataEGammaD_2022.EE           = 0
DataEGamma_2022               = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGamma_2022")
DataEGamma_2022.year          = 2022
DataEGamma_2022.components    = [DataEGammaC_2022, DataEGammaD_2022]

DataEGammaE_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaE_2022EE")
DataEGammaE_2022EE.year         = 2022
DataEGammaE_2022EE.dataset      = "/EGamma/Run2022E-22Sep2023-v1/NANOAOD"
DataEGammaE_2022EE.runP         = 'E'
DataEGammaE_2022EE.unix_code    = 30202
DataEGammaE_2022EE.EE           = 1
DataEGammaF_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaF_2022EE")
DataEGammaF_2022EE.year         = 2022
DataEGammaF_2022EE.dataset      = "/EGamma/Run2022F-22Sep2023-v1/NANOAOD"
DataEGammaF_2022EE.runP         = 'F'
DataEGammaF_2022EE.unix_code    = 30203
DataEGammaF_2022EE.EE           = 1
DataEGammaG_2022EE              = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGammaG_2022EE")
DataEGammaG_2022EE.year         = 2022
DataEGammaG_2022EE.dataset      = "/EGamma/Run2022G-22Sep2023-v2/NANOAOD"
DataEGammaG_2022EE.runP         = 'G'
DataEGammaG_2022EE.unix_code    = 30204
DataEGammaG_2022EE.EE           = 1

DataEGamma_2022EE               = sample(ROOT.kBlack, 1, 1001, "Data", "DataEGamma_2022EE")
DataEGamma_2022EE.year          = 2022
DataEGamma_2022EE.components    = [DataEGammaE_2022EE, DataEGammaF_2022EE, DataEGammaG_2022EE]


############### UNIX code meanings ################
# XXXXX  5 digits for each sample
# 1st digit: 0 for 2016, 1 for 2017, 2 for 2018, 3 for 2022, 4 for 2022EE, 5 for 2023, 6 for 2023BP
# 2nd digit: 0 for data, 1 for MC bkg, 2 for MC signal
# 3rd digit: for the process (QCD = 0, TT = 1, ZJets = 2, WJets = 3, 
#                             Tprime = 0, tDM = 1, 
#                             Data_MET = 0, Data_SingleMu = 1,...)
# 3rd digit and 4th digit: 2 digits identifies the sample 

# example: QCDHT_100to200_2018 == 21000, QCDHT_200to300_2018 == 21001
#          DATAHTA_2018 == 20600, DATAHTB_2018 == 20601, DATAHTC_2018 == 20602, DATAHTD_2018 == 20603  
### non diamo un codice ai sample con le components --> da capire se serve aggiungerlo


sample_dict = {

    # 'DataHTA_2018': DataHTA_2018,

    ################################## RUN II
    # Data MET 2018   
    'DataMET_2018': DataMET_2018, 'DataMETA_2018': DataMETA_2018, 'DataMETB_2018': DataMETB_2018,
    'DataMETC_2018': DataMETC_2018, 'DataMETD_2018': DataMETD_2018, 
    # 'DataMETA_2018': DataMETA_2018,
    # Data Single Muon 2018
    'DataSingleMu_2018':DataSingleMu_2018, 'DataSingleMuA_2018':DataSingleMuA_2018, 'DataSingleMuB_2018':DataSingleMuB_2018, 
    'DataSingleMuC_2018':DataSingleMuC_2018, 'DataSingleMuD_2018':DataSingleMuD_2018,
    # BKGs 2018
    'QCDHT_100to200_2018':QCDHT_100to200_2018, 'QCDHT_200to300_2018':QCDHT_200to300_2018, 
    'QCDHT_300to500_2018':QCDHT_300to500_2018, 'QCDHT_500to700_2018':QCDHT_500to700_2018, 
    'QCDHT_700to1000_2018':QCDHT_700to1000_2018, 'QCDHT_1000to1500_2018':QCDHT_1000to1500_2018, 
    'QCDHT_1500to2000_2018':QCDHT_1500to2000_2018, 'QCDHT_2000toInf_2018':QCDHT_2000toInf_2018, 
    'QCD_2018':QCD_2018,
    'TT_Mtt700to1000_2018':TT_Mtt700to1000_2018, 'TT_Mtt1000toInf_2018':TT_Mtt1000toInf_2018, 
    'TT_semilep_2018':TT_semilep_2018, 'TT_hadr_2018':TT_hadr_2018,
    'TT_2018':TT_2018,
    'ZJetsToNuNu_HT100to200_2018':ZJetsToNuNu_HT100to200_2018, 'ZJetsToNuNu_HT200to400_2018':ZJetsToNuNu_HT200to400_2018, 
    'ZJetsToNuNu_HT400to600_2018':ZJetsToNuNu_HT400to600_2018, 'ZJetsToNuNu_HT600to800_2018':ZJetsToNuNu_HT600to800_2018, 
    'ZJetsToNuNu_HT800to1200_2018':ZJetsToNuNu_HT800to1200_2018, 'ZJetsToNuNu_HT1200to2500_2018':ZJetsToNuNu_HT1200to2500_2018, 
    'ZJetsToNuNu_HT2500toInf_2018':ZJetsToNuNu_HT2500toInf_2018, 
    'ZJetsToNuNu_2018':ZJetsToNuNu_2018,
    'WJetsHT70to100_2018':WJetsHT70to100_2018,'WJetsHT100to200_2018':WJetsHT100to200_2018,
    'WJetsHT200to400_2018':WJetsHT200to400_2018,'WJetsHT400to600_2018':WJetsHT400to600_2018,
    'WJetsHT600to800_2018':WJetsHT600to800_2018,'WJetsHT800to1200_2018':WJetsHT800to1200_2018,
    'WJetsHT1200to2500_2018':WJetsHT1200to2500_2018,'WJetsHT2500toInf_2018':WJetsHT2500toInf_2018,
    'WJets_2018':WJets_2018,    
    # signals 2018
    'TprimeToTZ_1800_2018' : TprimeToTZ_1800_2018, 
    'TprimeToTZ_1000_2018' : TprimeToTZ_1000_2018, 
    'TprimeToTZ_700_2018' : TprimeToTZ_700_2018,

    'tDM_mPhi50_mChi1_2018' : tDM_mPhi50_mChi1_2018, 'tDM_mPhi500_mChi1_2018' : tDM_mPhi500_mChi1_2018, 'tDM_mPhi1000_mChi1_2018' : tDM_mPhi1000_mChi1_2018,
    

    "Zprime4top_500_2018":Zprime4top_500_2018, "Zprime4top_1000_2018":Zprime4top_1000_2018, "Zprime4top_2000_2018":Zprime4top_2000_2018, 
    
    #######################################
    ############# RUN III ################
    #######################################

    #####################2022
    ############ QCD
    'QCD_2022' : QCD_2022,
    # "QCD_HT40to70_2022": QCD_HT40to70_2022, 
    "QCD_HT70to100_2022": QCD_HT70to100_2022, 
    "QCD_HT100to200_2022": QCD_HT100to200_2022, "QCD_HT200to400_2022": QCD_HT200to400_2022, 
    "QCD_HT400to600_2022": QCD_HT400to600_2022, "QCD_HT600to800_2022": QCD_HT600to800_2022, 
    "QCD_HT800to1000_2022": QCD_HT800to1000_2022, "QCD_HT1000to1200_2022": QCD_HT1000to1200_2022, 
    "QCD_HT1200to1500_2022": QCD_HT1200to1500_2022, "QCD_HT1500to2000_2022": QCD_HT1500to2000_2022, "QCD_HT2000_2022": QCD_HT2000_2022,
    ########### TT
    'TT_2022': TT_2022, 'TT_semilep_2022' : TT_semilep_2022, 'TT_hadr_2022' : TT_hadr_2022,
    ########## WJets
    "WJets_2jets_2022": WJets_2jets_2022, 
    "WJets_2jets0J_2022": WJets_2jets0J_2022, "WJets_2jets1J_2022": WJets_2jets1J_2022, "WJets_2jets2J_2022": WJets_2jets2J_2022,

    "WJets_2022":WJets_2022, 
    "WJets_HT120to200_2022":WJets_HT120to200_2022, "WJets_HT200to400_2022":WJets_HT200to400_2022, 
    "WJets_HT400to800_2022":WJets_HT400to800_2022, "WJets_HT800to1500_2022":WJets_HT800to1500_2022, 
    "WJets_HT1500to2500_2022":WJets_HT1500to2500_2022, "WJets_HT2500to4000_2022":WJets_HT2500to4000_2022, 
    "WJets_HT4000to6000_2022":WJets_HT4000to6000_2022, "WJets_HT6000_2022":WJets_HT6000_2022,
    ########## ZJetsToNuNu
    "ZJetsToNuNu_2022":ZJetsToNuNu_2022, "ZJetsToNuNu_HT100to200_2022":ZJetsToNuNu_HT100to200_2022, 
    "ZJetsToNuNu_HT200to400_2022":ZJetsToNuNu_HT200to400_2022, "ZJetsToNuNu_HT400to800_2022":ZJetsToNuNu_HT400to800_2022, 
    "ZJetsToNuNu_HT800to1500_2022":ZJetsToNuNu_HT800to1500_2022, "ZJetsToNuNu_HT1500to2500_2022":ZJetsToNuNu_HT1500to2500_2022, 
    "ZJetsToNuNu_HT2500_2022":ZJetsToNuNu_HT2500_2022,

    "ZJetsToNuNu_2jets_2022":ZJetsToNuNu_2jets_2022,
    "ZJetsToNuNu_2jets_PT40to100_1J_2022":ZJetsToNuNu_2jets_PT40to100_1J_2022, "ZJetsToNuNu_2jets_PT100to200_1J_2022":ZJetsToNuNu_2jets_PT100to200_1J_2022,
    "ZJetsToNuNu_2jets_PT200to400_1J_2022":ZJetsToNuNu_2jets_PT200to400_1J_2022, "ZJetsToNuNu_2jets_PT400to600_1J_2022":ZJetsToNuNu_2jets_PT400to600_1J_2022,
    "ZJetsToNuNu_2jets_PT600_1J_2022":ZJetsToNuNu_2jets_PT600_1J_2022, "ZJetsToNuNu_2jets_PT40to100_2J_2022":ZJetsToNuNu_2jets_PT40to100_2J_2022,
    "ZJetsToNuNu_2jets_PT100to200_2J_2022":ZJetsToNuNu_2jets_PT100to200_2J_2022, "ZJetsToNuNu_2jets_PT200to400_2J_2022":ZJetsToNuNu_2jets_PT200to400_2J_2022,
    "ZJetsToNuNu_2jets_PT400to600_2J_2022":ZJetsToNuNu_2jets_PT400to600_2J_2022, "ZJetsToNuNu_2jets_PT600_2J_2022":ZJetsToNuNu_2jets_PT600_2J_2022,
                                    
    ########## SIGNALS
    "TprimeToTZ_700_2022":TprimeToTZ_700_2022,
    "TprimeToTZ_800_2022":TprimeToTZ_800_2022,
    "TprimeToTZ_900_2022":TprimeToTZ_900_2022,
    "TprimeToTZ_1000_2022":TprimeToTZ_1000_2022,
    "TprimeToTZ_1100_2022":TprimeToTZ_1100_2022,
    "TprimeToTZ_1200_2022":TprimeToTZ_1200_2022,
    "TprimeToTZ_1300_2022":TprimeToTZ_1300_2022,
    "TprimeToTZ_1400_2022":TprimeToTZ_1400_2022,
    "TprimeToTZ_1500_2022":TprimeToTZ_1500_2022,
    "TprimeToTZ_1600_2022":TprimeToTZ_1600_2022,
    "TprimeToTZ_1700_2022":TprimeToTZ_1700_2022,
    "TprimeToTZ_1800_2022":TprimeToTZ_1800_2022,

    #####################Tagger studies 4 top samples
    "Zprime4top_500_2022" : Zprime4top_500_2022, "Zprime4top_1000_2022" : Zprime4top_1000_2022, "Zprime4top_2000_2022" : Zprime4top_2000_2022,

    #####################2022EE
    ############ QCD
    'QCD_2022EE' : QCD_2022EE,
    # "QCD_HT40to70_2022EE": QCD_HT40to70_2022EE, 
    "QCD_HT70to100_2022EE": QCD_HT70to100_2022EE, 
    "QCD_HT100to200_2022EE": QCD_HT100to200_2022EE, "QCD_HT200to400_2022EE": QCD_HT200to400_2022EE, 
    "QCD_HT400to600_2022EE": QCD_HT400to600_2022EE, "QCD_HT600to800_2022EE": QCD_HT600to800_2022EE, 
    "QCD_HT800to1000_2022EE": QCD_HT800to1000_2022EE, "QCD_HT1000to1200_2022EE": QCD_HT1000to1200_2022EE, 
    "QCD_HT1200to1500_2022EE": QCD_HT1200to1500_2022EE, "QCD_HT1500to2000_2022EE": QCD_HT1500to2000_2022EE, "QCD_HT2000_2022EE": QCD_HT2000_2022EE,
    ########### TT
    'TT_2022EE': TT_2022EE, 'TT_semilep_2022EE' : TT_semilep_2022EE, 'TT_hadr_2022EE' : TT_hadr_2022EE,
    ########## WJets
    "WJets_2jets_2022EE": WJets_2jets_2022EE, 
    "WJets_2jets0J_2022EE": WJets_2jets0J_2022EE, "WJets_2jets1J_2022EE": WJets_2jets1J_2022EE, "WJets_2jets2J_2022EE": WJets_2jets2J_2022EE,

    "WJets_2022EE":WJets_2022EE, 
    "WJets_HT120to200_2022EE":WJets_HT120to200_2022EE, "WJets_HT200to400_2022EE":WJets_HT200to400_2022EE, 
    "WJets_HT400to800_2022EE":WJets_HT400to800_2022EE, "WJets_HT800to1500_2022EE":WJets_HT800to1500_2022EE, 
    "WJets_HT1500to2500_2022EE":WJets_HT1500to2500_2022EE, "WJets_HT2500to4000_2022EE":WJets_HT2500to4000_2022EE, 
    "WJets_HT4000to6000_2022EE":WJets_HT4000to6000_2022EE, "WJets_HT6000_2022EE":WJets_HT6000_2022EE,
    ########## ZJetsToNuNu
    "ZJetsToNuNu_2022EE":ZJetsToNuNu_2022EE, "ZJetsToNuNu_HT100to200_2022EE":ZJetsToNuNu_HT100to200_2022EE, 
    "ZJetsToNuNu_HT200to400_2022EE":ZJetsToNuNu_HT200to400_2022EE, "ZJetsToNuNu_HT400to800_2022EE":ZJetsToNuNu_HT400to800_2022EE, 
    "ZJetsToNuNu_HT800to1500_2022EE":ZJetsToNuNu_HT800to1500_2022EE, "ZJetsToNuNu_HT1500to2500_2022EE":ZJetsToNuNu_HT1500to2500_2022EE, 
    "ZJetsToNuNu_HT2500_2022EE":ZJetsToNuNu_HT2500_2022EE,

    "ZJetsToNuNu_2jets_2022EE":ZJetsToNuNu_2jets_2022EE,
    "ZJetsToNuNu_2jets_PT40to100_1J_2022EE":ZJetsToNuNu_2jets_PT40to100_1J_2022EE, "ZJetsToNuNu_2jets_PT100to200_1J_2022EE":ZJetsToNuNu_2jets_PT100to200_1J_2022EE,
    "ZJetsToNuNu_2jets_PT200to400_1J_2022EE":ZJetsToNuNu_2jets_PT200to400_1J_2022EE, "ZJetsToNuNu_2jets_PT400to600_1J_2022EE":ZJetsToNuNu_2jets_PT400to600_1J_2022EE,
    "ZJetsToNuNu_2jets_PT600_1J_2022EE":ZJetsToNuNu_2jets_PT600_1J_2022EE, "ZJetsToNuNu_2jets_PT40to100_2J_2022EE":ZJetsToNuNu_2jets_PT40to100_2J_2022EE,
    "ZJetsToNuNu_2jets_PT100to200_2J_2022EE":ZJetsToNuNu_2jets_PT100to200_2J_2022EE, "ZJetsToNuNu_2jets_PT200to400_2J_2022EE":ZJetsToNuNu_2jets_PT200to400_2J_2022EE,
    "ZJetsToNuNu_2jets_PT400to600_2J_2022EE":ZJetsToNuNu_2jets_PT400to600_2J_2022EE, "ZJetsToNuNu_2jets_PT600_2J_2022EE":ZJetsToNuNu_2jets_PT600_2J_2022EE,
    ########## SIGNALS
    "TprimeToTZ_700_2022EE":TprimeToTZ_700_2022EE,
    "TprimeToTZ_800_2022EE":TprimeToTZ_800_2022EE,
    "TprimeToTZ_900_2022EE":TprimeToTZ_900_2022EE,
    "TprimeToTZ_1000_2022EE":TprimeToTZ_1000_2022EE,
    "TprimeToTZ_1100_2022EE":TprimeToTZ_1100_2022EE,
    "TprimeToTZ_1200_2022EE":TprimeToTZ_1200_2022EE,
    "TprimeToTZ_1300_2022EE":TprimeToTZ_1300_2022EE,
    "TprimeToTZ_1400_2022EE":TprimeToTZ_1400_2022EE,
    "TprimeToTZ_1500_2022EE":TprimeToTZ_1500_2022EE,
    "TprimeToTZ_1600_2022EE":TprimeToTZ_1600_2022EE,
    "TprimeToTZ_1700_2022EE":TprimeToTZ_1700_2022EE,
    "TprimeToTZ_1800_2022EE":TprimeToTZ_1800_2022EE,

    #####################Tagger studies 4 top samples
    "Zprime4top_500_2022EE" : Zprime4top_500_2022EE, "Zprime4top_1000_2022EE" : Zprime4top_1000_2022EE, "Zprime4top_2000_2022EE" : Zprime4top_2000_2022EE,

    ############################################# DATA 
    'DataJetMET_2022': DataJetMET_2022, 'DataJetMETC_2022':DataJetMETC_2022, 'DataJetMETD_2022':DataJetMETD_2022, 
    'DataJetMET_2022EE': DataJetMET_2022EE,
    'DataJetMETE_2022EE':DataJetMETE_2022EE, 'DataJetMETF_2022EE':DataJetMETF_2022EE, 'DataJetMETG_2022EE':DataJetMETG_2022EE,

    "DataMuon_2022":DataMuon_2022, "DataMuonC_2022":DataMuonC_2022, "DataMuonD_2022":DataMuonD_2022, 
    "DataMuon_2022EE":DataMuon_2022EE,
    "DataMuonE_2022EE":DataMuonE_2022EE, "DataMuonF_2022EE":DataMuonF_2022EE, "DataMuonG_2022EE":DataMuonG_2022EE,

    "DataEGamma_2022":DataEGamma_2022, "DataEGammaC_2022":DataEGammaC_2022, "DataEGammaD_2022":DataEGammaD_2022,
    "DataEGamma_2022EE":DataEGamma_2022EE, 
    "DataEGammaE_2022EE":DataEGammaE_2022EE, "DataEGammaF_2022EE":DataEGammaF_2022EE, "DataEGammaG_2022EE":DataEGammaG_2022EE,
    }
