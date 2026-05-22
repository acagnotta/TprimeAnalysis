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
parser.add_option(      "--era",                    dest="era",                         type=str,     default="2023",                                   help="Please enter the era, e.g. 2022, 2022EE, etc.")
parser.add_option(      '--TopCategory',            dest='TopCategory',                 type=str,     default="Mixed",                                  help='Top category for the histograms: Resolved, Mixed or Merged')
(opt, args)             = parser.parse_args()
era                     = opt.era
TopCategory             = opt.TopCategory

outputfolder            = config["TrotaScaleFactor"]["outputfolder"][TopCategory][era]
outName                 = f"TrotaScaleFactors_{era}_{TopCategory}"
inFilePath              = f"{outputfolder}/ScaleFactors/{outName}.json"
corrLibFolder           = config["corrlibfolder"][era]
outFilePath             = f"{corrLibFolder}/CorrLib_{outName}.json"

os.makedirs(corrLibFolder, exist_ok=True)
with open(inFilePath, "r") as json_file:
    TrotaScaleFactors_dict = json.load(json_file)


def values_to_return(values, tagcat):
    vals = list(values)
    if tagcat == "other":
        vals[3] = vals[2]
    return vals


def CreateCorrectionLibFile(TrotaScaleFactors_dict):

    corr = cs.Correction(
        name="TrotaScaleFactors",
        version=1,
        inputs=[
            cs.Variable(name="TopCat",          type="string", description="Top category: Resolved, Mixed, Merged"),
            cs.Variable(name="wp_cat",          type="string", description="working point category"),
            cs.Variable(name="TagCat",          type="string", description="Tag category: topmatched, nonmatched, other"),
            cs.Variable(name="channel",         type="string", description="insert: pass, fail"),
            cs.Variable(name="type",            type="string", description="insert: value, error"),
            cs.Variable(name="TopCandidate_pt", type="real",   description="Top candidate pt"),
        ],
        output=cs.Variable(
            name="TrotaScaleFactor",
            type="real",
            description="Trota Top tagger scale factor"
        ),
        data=cs.Category(
            nodetype="category",
            input="TopCat",
            content=[
                {
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
                                                                        content=values_to_return(
                                                                            TrotaScaleFactors_dict[TopCat][wp_cat][TagCat][channel]["value"],
                                                                            TagCat
                                                                        ),
                                                                        flow="clamp"
                                                                    )
                                                                },
                                                                {
                                                                    "key": "error",
                                                                    "value": cs.Binning(
                                                                        nodetype="binning",
                                                                        input="TopCandidate_pt",
                                                                        edges=[0, 200, 400, 600, 1000],
                                                                        content=values_to_return(
                                                                            TrotaScaleFactors_dict[TopCat][wp_cat][TagCat][channel]["error"],
                                                                            TagCat
                                                                        ),
                                                                        flow="clamp"
                                                                    )
                                                                }
                                                            ]
                                                        )
                                                    } for channel in TrotaScaleFactors_dict[TopCat][wp_cat][TagCat].keys()
                                                ]
                                            )
                                        } for TagCat in TrotaScaleFactors_dict[TopCat][wp_cat].keys()
                                    ]
                                )
                            } for wp_cat in TrotaScaleFactors_dict[TopCat].keys()
                        ]
                    )
                } for TopCat in TrotaScaleFactors_dict.keys()
            ]
        )
    )

    cset = cs.CorrectionSet(schema_version=2, corrections=[corr])

    with open(outFilePath, "w") as f:
        json.dump(cset.dict(), f, indent=2)

    return 0


CreateCorrectionLibFile(TrotaScaleFactors_dict)