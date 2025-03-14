#!/bin/bash
cd /afs/cern.ch/user/l/lfavilla/
source analysis_TPrime.sh
mkdir -p /tmp/lfavilla/TprimeToTZ_1800_2022/file12/
cd /tmp/lfavilla/TprimeToTZ_1800_2022/file12/
pwd
python3 /afs/cern.ch/user/l/lfavilla/TprimeAnalysis/NanoAODTools/condor/tmp//TprimeToTZ_1800_2022/file12/crab_script.py
pwd
hadd -f tree_hadd_12.root tree.root hist.root
pwd
davix-put tree_hadd_12.root davs://stwebdav.pi.infn.it:8443/cms/store/user/lfavilla/Run3Analysis_Tprime/TprimeToTZ_1800_2022/20250310_124216/tree_hadd_12.root -E $1 --capath /cvmfs/cms.cern.ch/grid/etc/grid-security/certificates/
