#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.15476e-34,'m^3/(mol*s)'), n=11.0745, w0=(789.787,'kJ/mol'), E0=(169.581,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08172892276683458, var=74.95943274505365, Tref=1000.0, N=54, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 54 training reactions at node Root
    Total Standard Deviation in ln(k): 17.562168072504694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 54 training reactions at node Root
Total Standard Deviation in ln(k): 17.562168072504694""",
    longDesc = 
"""
BM rule fitted to 54 training reactions at node Root
Total Standard Deviation in ln(k): 17.562168072504694
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.96447e-35,'m^3/(mol*s)'), n=11.2259, w0=(883.537,'kJ/mol'), E0=(170.969,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10821473249855351, var=70.07037256573693, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 27 training reactions at node Root_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 17.053142269424065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 17.053142269424065""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 17.053142269424065
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.72424e-07,'m^3/(mol*s)'), n=3.69682, w0=(696.037,'kJ/mol'), E0=(164.04,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5840980150380004, var=49.78898298881509, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 15.613256037200161"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 15.613256037200161""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 15.613256037200161
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.90423e-28,'m^3/(mol*s)'), n=9.38229, w0=(857.781,'kJ/mol'), E0=(229.946,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3648863569251471, var=56.88238267732761, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 16 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 16.036594070403225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 16.036594070403225""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 16.036594070403225
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO",
    kinetics = ArrheniusBM(A=(1.05567e-22,'m^3/(mol*s)'), n=7.37058, w0=(975,'kJ/mol'), E0=(141.907,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14661968076699874, var=42.78346295919519, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO',), comment="""BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO
    Total Standard Deviation in ln(k): 13.48117664044032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 13.48117664044032""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 13.48117664044032
""",
)

entry(
    index = 6,
    label = "Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO",
    kinetics = ArrheniusBM(A=(2.87817e-06,'m^3/(mol*s)'), n=3.38296, w0=(876,'kJ/mol'), E0=(180.066,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0949338630999086, var=144.9829780170569, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO
    Total Standard Deviation in ln(k): 29.402442975146933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 29.402442975146933""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 29.402442975146933
""",
)

entry(
    index = 7,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(2.51138e-07,'m^3/(mol*s)'), n=3.71209, w0=(700.692,'kJ/mol'), E0=(164.286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5919046454428077, var=50.79742726958659, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 15.77540837145971"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 15.77540837145971""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 15.77540837145971
""",
)

entry(
    index = 8,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(5.93272e-05,'m^3/(mol*s)'), n=2.63647, w0=(575,'kJ/mol'), E0=(143.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.93159e-28,'m^3/(mol*s)'), n=9.42943, w0=(858.5,'kJ/mol'), E0=(230.298,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3578619839032855, var=57.04063534299807, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 10 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 16.039962698470028"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 16.039962698470028""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 16.039962698470028
""",
)

entry(
    index = 10,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2029.21,'m^3/(mol*s)'), n=0.783866, w0=(852.75,'kJ/mol'), E0=(253.649,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.126609618875, var=30.766180113608787, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 18.97552119011026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 18.97552119011026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 18.97552119011026
""",
)

entry(
    index = 11,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(116.282,'m^3/(mol*s)'), n=1.10103, w0=(858.5,'kJ/mol'), E0=(260.264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4680389968819654, var=12.95644142745942, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.904595571097973"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.904595571097973""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.904595571097973
""",
)

entry(
    index = 12,
    label = "Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.80176e-25,'m^3/(mol*s)'), n=7.83563, w0=(975,'kJ/mol'), E0=(143.806,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20533757333877672, var=18.04780270524786, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C
    Total Standard Deviation in ln(k): 9.032580550208982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C
Total Standard Deviation in ln(k): 9.032580550208982""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C
Total Standard Deviation in ln(k): 9.032580550208982
""",
)

entry(
    index = 13,
    label = "Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.6637e-19,'m^3/(mol*s)'), n=6.79375, w0=(975,'kJ/mol'), E0=(129.226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11741340389427635, var=0.0567495025426796, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.7725796317056649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.7725796317056649""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.7725796317056649
""",
)

entry(
    index = 14,
    label = "Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(2.57016e+31,'m^3/(mol*s)'), n=-7.53001, w0=(847,'kJ/mol'), E0=(355.217,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(5.2755e-06,'m^3/(mol*s)'), n=3.32168, w0=(881.8,'kJ/mol'), E0=(177.155,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9719807556927889, var=151.28357790264528, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 29.612443605330217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 29.612443605330217""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 29.612443605330217
""",
)

entry(
    index = 16,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(0.415781,'m^3/(mol*s)'), n=1.8082, w0=(693,'kJ/mol'), E0=(204.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20327960161332745, var=13.653664786599373, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 7.918422436031062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 7.918422436031062""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 7.918422436031062
""",
)

entry(
    index = 17,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(2.05454e-44,'m^3/(mol*s)'), n=14.5196, w0=(718,'kJ/mol'), E0=(15.6244,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.3417543692465057, var=32.657229020841896, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 17.340165029368872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 17.340165029368872""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 17.340165029368872
""",
)

entry(
    index = 18,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O",
    kinetics = ArrheniusBM(A=(5.2637e-32,'m^3/(mol*s)'), n=10.6207, w0=(858.5,'kJ/mol'), E0=(200.708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07231419073951285, var=1.4282536985917886, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O
    Total Standard Deviation in ln(k): 2.57754418906105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O
Total Standard Deviation in ln(k): 2.57754418906105""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O
Total Standard Deviation in ln(k): 2.57754418906105
""",
)

entry(
    index = 19,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.46193e-33,'m^3/(mol*s)'), n=10.7298, w0=(858.5,'kJ/mol'), E0=(237.378,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3124924811373262, var=130.07431715666766, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O
    Total Standard Deviation in ln(k): 23.6491862226386"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O
Total Standard Deviation in ln(k): 23.6491862226386""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O
Total Standard Deviation in ln(k): 23.6491862226386
""",
)

entry(
    index = 20,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(3.60487e+39,'m^3/(mol*s)'), n=-9.93467, w0=(847,'kJ/mol'), E0=(360.535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(3.14941,'m^3/(mol*s)'), n=1.63113, w0=(858.5,'kJ/mol'), E0=(244.653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(125.267,'m^3/(mol*s)'), n=1.1096, w0=(858.5,'kJ/mol'), E0=(261.872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.242182665399847, var=22.542687620902537, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 15.151934584585028"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 15.151934584585028""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 15.151934584585028
""",
)

entry(
    index = 23,
    label = "Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.55901e-25,'m^3/(mol*s)'), n=7.85908, w0=(975,'kJ/mol'), E0=(146.424,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2192330987969802, var=13.57969341746177, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 7.938413106341768"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 7.938413106341768""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 7.938413106341768
""",
)

entry(
    index = 24,
    label = "Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.75808e-23,'m^3/(mol*s)'), n=7.59676, w0=(975,'kJ/mol'), E0=(140.227,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R",
    kinetics = ArrheniusBM(A=(1.67217e-06,'m^3/(mol*s)'), n=3.47122, w0=(887.625,'kJ/mol'), E0=(174.765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1716505252830856, var=175.12452690083705, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R
    Total Standard Deviation in ln(k): 31.98599460914318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R
Total Standard Deviation in ln(k): 31.98599460914318""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R
Total Standard Deviation in ln(k): 31.98599460914318
""",
)

entry(
    index = 26,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s",
    kinetics = ArrheniusBM(A=(0.0059331,'m^3/(mol*s)'), n=2.39407, w0=(657,'kJ/mol'), E0=(201.372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20958383171166042, var=23.18946613824187, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 10.180482957287225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 10.180482957287225""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 10.180482957287225
""",
)

entry(
    index = 27,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s",
    kinetics = ArrheniusBM(A=(12854.1,'m^3/(mol*s)'), n=0.363006, w0=(711,'kJ/mol'), E0=(209.858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13092446396769106, var=2.1888461270229813, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s',), comment="""BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 3.2949112675647987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 3.2949112675647987""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 3.2949112675647987
""",
)

entry(
    index = 28,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s",
    kinetics = ArrheniusBM(A=(1.05542e-40,'m^3/(mol*s)'), n=13.4925, w0=(709.5,'kJ/mol'), E0=(11.844,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-15.39377220837538, var=629.3066547495009, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 88.96857415220366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 88.96857415220366""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 88.96857415220366
""",
)

entry(
    index = 29,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s",
    kinetics = ArrheniusBM(A=(2.90039e-47,'m^3/(mol*s)'), n=15.3086, w0=(720.833,'kJ/mol'), E0=(14.2023,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.410497455426888, var=107.124839089586, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 36.85601211004605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 36.85601211004605""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 36.85601211004605
""",
)

entry(
    index = 30,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C",
    kinetics = ArrheniusBM(A=(4.7072e-32,'m^3/(mol*s)'), n=10.6641, w0=(858.5,'kJ/mol'), E0=(205.722,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1015084452188434, var=0.9739776605708755, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
    Total Standard Deviation in ln(k): 2.233525538042274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
Total Standard Deviation in ln(k): 2.233525538042274""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
Total Standard Deviation in ln(k): 2.233525538042274
""",
)

entry(
    index = 31,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2.426e-34,'m^3/(mol*s)'), n=11.2313, w0=(858.5,'kJ/mol'), E0=(184.207,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.37546e-33,'m^3/(mol*s)'), n=10.7369, w0=(858.5,'kJ/mol'), E0=(237.436,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3044352812623908, var=130.38283965688808, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 23.65604146966272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 23.65604146966272""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 23.65604146966272
""",
)

entry(
    index = 33,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F",
    kinetics = ArrheniusBM(A=(8.19918,'m^3/(mol*s)'), n=1.36893, w0=(858.5,'kJ/mol'), E0=(229.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0484539841974525, var=1.7251977549761428, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
    Total Standard Deviation in ln(k): 2.754898721807278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 2.754898721807278""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 2.754898721807278
""",
)

entry(
    index = 34,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(4.49727,'m^3/(mol*s)'), n=1.54397, w0=(858.5,'kJ/mol'), E0=(265.753,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.09665e-26,'m^3/(mol*s)'), n=8.06194, w0=(975,'kJ/mol'), E0=(147.323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.81675e-24,'m^3/(mol*s)'), n=7.58858, w0=(975,'kJ/mol'), E0=(146.107,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_4COCdCddCtO2d->CO_Ext-4CO-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_5R!H->Br",
    kinetics = ArrheniusBM(A=(24.851,'m^3/(mol*s)'), n=1.25249, w0=(858.5,'kJ/mol'), E0=(239.116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_5R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_5R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br",
    kinetics = ArrheniusBM(A=(9.02824e-16,'m^3/(mol*s)'), n=6.21668, w0=(897.333,'kJ/mol'), E0=(125.84,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.52340934110155, var=133.3584349621319, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br
    Total Standard Deviation in ln(k): 39.54134137214265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br
Total Standard Deviation in ln(k): 39.54134137214265""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br
Total Standard Deviation in ln(k): 39.54134137214265
""",
)

entry(
    index = 39,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(0.00284363,'m^3/(mol*s)'), n=2.5143, w0=(657,'kJ/mol'), E0=(210.075,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27209909721695563, var=35.40550332689003, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 12.612345729037084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 12.612345729037084""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 12.612345729037084
""",
)

entry(
    index = 40,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(7.85783,'m^3/(mol*s)'), n=1.416, w0=(657,'kJ/mol'), E0=(183.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(513.48,'m^3/(mol*s)'), n=0.745458, w0=(711,'kJ/mol'), E0=(208.015,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17663466498596408, var=3.301652146401163, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 4.086499326894868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.086499326894868""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.086499326894868
""",
)

entry(
    index = 42,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.25792e+07,'m^3/(mol*s)'), n=-0.707937, w0=(711,'kJ/mol'), E0=(214.596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12884410618931497, var=0.8149614610182481, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 2.1335078298515295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1335078298515295""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1335078298515295
""",
)

entry(
    index = 43,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_3CtO2d->O2d",
    kinetics = ArrheniusBM(A=(2.01929e-06,'m^3/(mol*s)'), n=3.68936, w0=(773.5,'kJ/mol'), E0=(107.273,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_3CtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_3CtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_N-3CtO2d->O2d",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=-8.46126e-09, w0=(645.5,'kJ/mol'), E0=(276.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_N-3CtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_N-3CtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_N-3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_N-3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R",
    kinetics = ArrheniusBM(A=(23.95,'m^3/(mol*s)'), n=1.57664, w0=(699.5,'kJ/mol'), E0=(220.022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11479703517840713, var=2.2200481478296603, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R
    Total Standard Deviation in ln(k): 3.2754551443634323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R
Total Standard Deviation in ln(k): 3.2754551443634323""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R
Total Standard Deviation in ln(k): 3.2754551443634323
""",
)

entry(
    index = 46,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(6.69769e-21,'m^3/(mol*s)'), n=7.80389, w0=(763.5,'kJ/mol'), E0=(85.9267,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-9.156981682821304, var=216.45374797489794, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 52.501890218251425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.501890218251425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.501890218251425
""",
)

entry(
    index = 47,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(6.67386e-32,'m^3/(mol*s)'), n=10.6691, w0=(858.5,'kJ/mol'), E0=(206.019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(3.32008e-32,'m^3/(mol*s)'), n=10.6591, w0=(858.5,'kJ/mol'), E0=(205.424,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_5R!H->O_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C",
    kinetics = ArrheniusBM(A=(9.8916e-58,'m^3/(mol*s)'), n=17.4051, w0=(858.5,'kJ/mol'), E0=(198.206,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07637184010214733, var=22.640529637986447, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C
    Total Standard Deviation in ln(k): 9.73083263555755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C
Total Standard Deviation in ln(k): 9.73083263555755""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C
Total Standard Deviation in ln(k): 9.73083263555755
""",
)

entry(
    index = 50,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.66847e-33,'m^3/(mol*s)'), n=11.0895, w0=(858.5,'kJ/mol'), E0=(198.089,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9343938068723406, var=6.692105230709256, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C
    Total Standard Deviation in ln(k): 7.533793081374045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C
Total Standard Deviation in ln(k): 7.533793081374045""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C
Total Standard Deviation in ln(k): 7.533793081374045
""",
)

entry(
    index = 51,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4.45749,'m^3/(mol*s)'), n=1.21594, w0=(858.5,'kJ/mol'), E0=(218.95,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_Ext-4CdCddCt-R",
    kinetics = ArrheniusBM(A=(14.8208,'m^3/(mol*s)'), n=1.21604, w0=(858.5,'kJ/mol'), E0=(215.271,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_Ext-4CdCddCt-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_Ext-4CdCddCt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_Ext-4CdCddCt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_Ext-4CdCddCt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(7.80335e-09,'m^3/(mol*s)'), n=4.28272, w0=(975,'kJ/mol'), E0=(135.897,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_3CdO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_3CdO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_N-3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(86.7945,'m^3/(mol*s)'), n=1.05027, w0=(858.5,'kJ/mol'), E0=(210.87,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_N-3CdO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_N-3CdO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-4COCdCddCtO2d->CO_N-3COCdCddCtO2d->Ct_Ext-4CdCddCt-R_N-5R!H->Br_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.18878,'m^3/(mol*s)'), n=1.76475, w0=(657,'kJ/mol'), E0=(181.27,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.215889,'m^3/(mol*s)'), n=1.97486, w0=(657,'kJ/mol'), E0=(231.46,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15132300640431584, var=27.931226864745206, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.975233796505476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.975233796505476""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.975233796505476
""",
)

entry(
    index = 57,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(24408,'m^3/(mol*s)'), n=0.242664, w0=(711,'kJ/mol'), E0=(208.95,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15340377141403394, var=3.4199119490513086, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl
    Total Standard Deviation in ln(k): 4.0927939810607805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.0927939810607805""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.0927939810607805
""",
)

entry(
    index = 58,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.10391,'m^3/(mol*s)'), n=1.64361, w0=(711,'kJ/mol'), E0=(221.034,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.25612e+07,'m^3/(mol*s)'), n=-0.637747, w0=(711,'kJ/mol'), E0=(216.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.97967e+06,'m^3/(mol*s)'), n=-0.518739, w0=(711,'kJ/mol'), E0=(212.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.6085e+08,'m^3/(mol*s)'), n=-0.88707, w0=(711,'kJ/mol'), E0=(213.432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(40.7026,'m^3/(mol*s)'), n=1.65435, w0=(699.5,'kJ/mol'), E0=(224.765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_3CtO2d->O2d",
    kinetics = ArrheniusBM(A=(1.09358e-06,'m^3/(mol*s)'), n=3.74071, w0=(827.5,'kJ/mol'), E0=(116.096,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_3CtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_3CtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d",
    kinetics = ArrheniusBM(A=(1.62705,'m^3/(mol*s)'), n=1.85266, w0=(699.5,'kJ/mol'), E0=(214.967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(4.21028e-60,'m^3/(mol*s)'), n=17.9382, w0=(858.5,'kJ/mol'), E0=(197.688,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.42879e-56,'m^3/(mol*s)'), n=17.219, w0=(858.5,'kJ/mol'), E0=(195.721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(12.1292,'m^3/(mol*s)'), n=1.44664, w0=(858.5,'kJ/mol'), E0=(294.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(3.43748e-35,'m^3/(mol*s)'), n=11.6721, w0=(858.5,'kJ/mol'), E0=(192.275,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.7345113684574365, var=93.49305391065592, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 36.305028398918694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 36.305028398918694""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 36.305028398918694
""",
)

entry(
    index = 69,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.825331,'m^3/(mol*s)'), n=1.69758, w0=(657,'kJ/mol'), E0=(221.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(3.63667,'m^3/(mol*s)'), n=1.59996, w0=(657,'kJ/mol'), E0=(251.549,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(25762.3,'m^3/(mol*s)'), n=0.211089, w0=(711,'kJ/mol'), E0=(206.552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1695120686349818, var=13.236969088359478, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
    Total Standard Deviation in ln(k): 7.719666326447856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.719666326447856""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.719666326447856
""",
)

entry(
    index = 72,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.59096e+06,'m^3/(mol*s)'), n=-0.339093, w0=(711,'kJ/mol'), E0=(221.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.87929e-35,'m^3/(mol*s)'), n=11.696, w0=(858.5,'kJ/mol'), E0=(192.335,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.845888739012175, var=158.76614346500185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 47.48600180442769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 47.48600180442769""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_N-5R!H->O_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 47.48600180442769
""",
)

entry(
    index = 74,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4061.27,'m^3/(mol*s)'), n=0.468602, w0=(711,'kJ/mol'), E0=(200.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18985986566819657, var=36.555013946038876, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.59781198602482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.59781198602482""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.59781198602482
""",
)

entry(
    index = 75,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.0823032,'m^3/(mol*s)'), n=1.92336, w0=(711,'kJ/mol'), E0=(212.188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

