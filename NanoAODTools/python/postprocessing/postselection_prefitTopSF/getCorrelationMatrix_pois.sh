#!/bin/bash
python3 drawCorrelationMatrix_pois.py \
        -i /eos/user/l/lfavilla/RDF_DManalysis/TopSF/results/run2023_SemiLep_systematics_study/workspace_MixedTight/MT_W/fitDiagnostics_pt0to200.root \
        -p SF_topmatched,SF_nonmatched,SF_other \
        -o /eos/user/l/lfavilla/RDF_DManalysis/TopSF/results/run2023_SemiLep_systematics_study/ScaleFactors/corrMatrix_pt0to200
python3 drawCorrelationMatrix_pois.py \
        -i /eos/user/l/lfavilla/RDF_DManalysis/TopSF/results/run2023_SemiLep_systematics_study/workspace_MixedTight/MT_W/fitDiagnostics_pt200to400.root \
        -p SF_topmatched,SF_nonmatched,SF_other \
        -o /eos/user/l/lfavilla/RDF_DManalysis/TopSF/results/run2023_SemiLep_systematics_study/ScaleFactors/corrMatrix_pt200to400
python3 drawCorrelationMatrix_pois.py \
        -i /eos/user/l/lfavilla/RDF_DManalysis/TopSF/results/run2023_SemiLep_systematics_study/workspace_MixedTight/MT_W/fitDiagnostics_pt400to600.root \
        -p SF_topmatched,SF_nonmatched,SF_other \
        -o /eos/user/l/lfavilla/RDF_DManalysis/TopSF/results/run2023_SemiLep_systematics_study/ScaleFactors/corrMatrix_pt400to600
python3 drawCorrelationMatrix_pois.py \
        -i /eos/user/l/lfavilla/RDF_DManalysis/TopSF/results/run2023_SemiLep_systematics_study/workspace_MixedTight/MT_W/fitDiagnostics_pt600to1000.root \
        -p SF_topmatched,SF_nonmatched,SF_other \
        -o /eos/user/l/lfavilla/RDF_DManalysis/TopSF/results/run2023_SemiLep_systematics_study/ScaleFactors/corrMatrix_pt600to1000