#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.24816e-48,'m^3/(mol*s)'), n=15.3193, w0=(800.129,'kJ/mol'), E0=(157.901,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21582258178615796, var=96.30429463252042, Tref=1000.0, N=66, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 66 training reactions at node Root
    Total Standard Deviation in ln(k): 20.215685669300235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 20.215685669300235""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 20.215685669300235
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(3.72269e-05,'m^3/(mol*s)'), n=3.05336, w0=(706.947,'kJ/mol'), E0=(161.419,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8962206536736665, var=71.4847451458987, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 19 training reactions at node Root_2Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 21.714138294843043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_2Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 21.714138294843043""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_2Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 21.714138294843043
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(7.88434e-49,'m^3/(mol*s)'), n=15.3751, w0=(837.798,'kJ/mol'), E0=(158.137,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21743527561228915, var=95.24623174127787, Tref=1000.0, N=47, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 47 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 20.11136657023114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 47 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 20.11136657023114""",
    longDesc = 
"""
BM rule fitted to 47 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 20.11136657023114
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(4.90034e-05,'m^3/(mol*s)'), n=3.03143, w0=(714.278,'kJ/mol'), E0=(162.314,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0476884714337045, var=77.36833287414832, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 18 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 22.778449426847036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 22.778449426847036""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 22.778449426847036
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCl1sF1sH->Cl1s_N-1Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(5.93272e-05,'m^3/(mol*s)'), n=2.63647, w0=(575,'kJ/mol'), E0=(143.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_N-1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_N-1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s",
    kinetics = ArrheniusBM(A=(8.63093e-09,'m^3/(mol*s)'), n=4.14685, w0=(670.125,'kJ/mol'), E0=(165.449,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7450516087326802, var=73.87463949305052, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s',), comment="""BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s
    Total Standard Deviation in ln(k): 19.102758620230695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s
Total Standard Deviation in ln(k): 19.102758620230695""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s
Total Standard Deviation in ln(k): 19.102758620230695
""",
)

entry(
    index = 7,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s",
    kinetics = ArrheniusBM(A=(3.95074e-49,'m^3/(mol*s)'), n=15.4585, w0=(872.192,'kJ/mol'), E0=(158.39,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21940449434642317, var=93.85570881063148, Tref=1000.0, N=39, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s',), comment="""BM rule fitted to 39 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s
    Total Standard Deviation in ln(k): 19.97297181815734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 39 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s
Total Standard Deviation in ln(k): 19.97297181815734""",
    longDesc = 
"""
BM rule fitted to 39 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s
Total Standard Deviation in ln(k): 19.97297181815734
""",
)

entry(
    index = 8,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(12854.1,'m^3/(mol*s)'), n=0.363006, w0=(711,'kJ/mol'), E0=(209.858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13092446396769106, var=2.1888461270229813, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 12 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 3.2949112675647987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 3.2949112675647987""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 3.2949112675647987
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(2.90039e-47,'m^3/(mol*s)'), n=15.3086, w0=(720.833,'kJ/mol'), E0=(14.2023,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.410497455426888, var=107.124839089586, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 36.85601211004605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 36.85601211004605""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 36.85601211004605
""",
)

entry(
    index = 10,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=-8.46126e-09, w0=(645.5,'kJ/mol'), E0=(276.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(4.72478e-08,'m^3/(mol*s)'), n=3.93599, w0=(673.643,'kJ/mol'), E0=(165.69,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7007994105589191, var=74.63427504504561, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 19.079935595527683"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 19.079935595527683""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 19.079935595527683
""",
)

entry(
    index = 12,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d",
    kinetics = ArrheniusBM(A=(7.21194e-08,'m^3/(mol*s)'), n=3.97622, w0=(975,'kJ/mol'), E0=(139.614,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.001382118662282, var=42.866628764538596, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d
    Total Standard Deviation in ln(k): 23.179248034851632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d
Total Standard Deviation in ln(k): 23.179248034851632""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d
Total Standard Deviation in ln(k): 23.179248034851632
""",
)

entry(
    index = 13,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d",
    kinetics = ArrheniusBM(A=(4.73093e-49,'m^3/(mol*s)'), n=15.435, w0=(866.635,'kJ/mol'), E0=(158.958,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21606851330334706, var=93.18725731547622, Tref=1000.0, N=37, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d',), comment="""BM rule fitted to 37 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d
    Total Standard Deviation in ln(k): 19.89530452992968"""),
    rank = 11,
    shortDesc = """BM rule fitted to 37 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d
Total Standard Deviation in ln(k): 19.89530452992968""",
    longDesc = 
"""
BM rule fitted to 37 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d
Total Standard Deviation in ln(k): 19.89530452992968
""",
)

entry(
    index = 14,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(513.48,'m^3/(mol*s)'), n=0.745458, w0=(711,'kJ/mol'), E0=(208.015,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17663466498596408, var=3.301652146401163, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R',), comment="""BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R
    Total Standard Deviation in ln(k): 4.086499326894868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.086499326894868""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.086499326894868
""",
)

entry(
    index = 15,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.25792e+07,'m^3/(mol*s)'), n=-0.707937, w0=(711,'kJ/mol'), E0=(214.596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12884410618931497, var=0.8149614610182481, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 2.1335078298515295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1335078298515295""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1335078298515295
""",
)

entry(
    index = 16,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CtO2d-R",
    kinetics = ArrheniusBM(A=(23.95,'m^3/(mol*s)'), n=1.57664, w0=(699.5,'kJ/mol'), E0=(220.022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11479703517840713, var=2.2200481478296603, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CtO2d-R
    Total Standard Deviation in ln(k): 3.2754551443634323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CtO2d-R
Total Standard Deviation in ln(k): 3.2754551443634323""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CtO2d-R
Total Standard Deviation in ln(k): 3.2754551443634323
""",
)

entry(
    index = 17,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(6.69769e-21,'m^3/(mol*s)'), n=7.80389, w0=(763.5,'kJ/mol'), E0=(85.9267,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-9.156981682821304, var=216.45374797489794, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 52.501890218251425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.501890218251425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.501890218251425
""",
)

entry(
    index = 18,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R",
    kinetics = ArrheniusBM(A=(0.00284363,'m^3/(mol*s)'), n=2.5143, w0=(657,'kJ/mol'), E0=(210.075,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27209909721695563, var=35.40550332689003, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R
    Total Standard Deviation in ln(k): 12.612345729037084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R
Total Standard Deviation in ln(k): 12.612345729037084""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R
Total Standard Deviation in ln(k): 12.612345729037084
""",
)

entry(
    index = 19,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.7873e-06,'m^3/(mol*s)'), n=3.49893, w0=(715.25,'kJ/mol'), E0=(131.107,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.2301511701470322, var=184.2860607506378, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 32.81807494417064"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 32.81807494417064""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 32.81807494417064
""",
)

entry(
    index = 20,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d_4COCdCddCtO2d->Cdd",
    kinetics = ArrheniusBM(A=(7.80335e-09,'m^3/(mol*s)'), n=4.28272, w0=(975,'kJ/mol'), E0=(135.897,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d_4COCdCddCtO2d->Cdd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d_4COCdCddCtO2d->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d_4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d_4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d_N-4COCdCddCtO2d->Cdd",
    kinetics = ArrheniusBM(A=(0.140494,'m^3/(mol*s)'), n=1.80918, w0=(975,'kJ/mol'), E0=(171.141,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d_N-4COCdCddCtO2d->Cdd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d_N-4COCdCddCtO2d->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d_N-4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_3COCdCddCtO2d->O2d_N-4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(2.43777e-53,'m^3/(mol*s)'), n=16.7896, w0=(841.917,'kJ/mol'), E0=(226.506,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28986545847467304, var=24.242992565774152, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 24 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 10.599054059465256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 10.599054059465256""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 10.599054059465256
""",
)

entry(
    index = 23,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(1.11979e-77,'m^3/(mol*s)'), n=23.5476, w0=(912.269,'kJ/mol'), E0=(17.2119,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3429479887068476, var=24.832050374597156, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 13 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 13.364190375637355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 13.364190375637355""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 13.364190375637355
""",
)

entry(
    index = 24,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(24408,'m^3/(mol*s)'), n=0.242664, w0=(711,'kJ/mol'), E0=(208.95,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15340377141403394, var=3.4199119490513086, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl
    Total Standard Deviation in ln(k): 4.0927939810607805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.0927939810607805""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.0927939810607805
""",
)

entry(
    index = 25,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.10391,'m^3/(mol*s)'), n=1.64361, w0=(711,'kJ/mol'), E0=(221.034,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.25612e+07,'m^3/(mol*s)'), n=-0.637747, w0=(711,'kJ/mol'), E0=(216.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.97967e+06,'m^3/(mol*s)'), n=-0.518739, w0=(711,'kJ/mol'), E0=(212.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.6085e+08,'m^3/(mol*s)'), n=-0.88707, w0=(711,'kJ/mol'), E0=(213.432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(40.7026,'m^3/(mol*s)'), n=1.65435, w0=(699.5,'kJ/mol'), E0=(224.765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3CtO2d->O2d",
    kinetics = ArrheniusBM(A=(1.09358e-06,'m^3/(mol*s)'), n=3.74071, w0=(827.5,'kJ/mol'), E0=(116.096,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3CtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3CtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d",
    kinetics = ArrheniusBM(A=(1.62705,'m^3/(mol*s)'), n=1.85266, w0=(699.5,'kJ/mol'), E0=(214.967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.18878,'m^3/(mol*s)'), n=1.76475, w0=(657,'kJ/mol'), E0=(181.27,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.215889,'m^3/(mol*s)'), n=1.97486, w0=(657,'kJ/mol'), E0=(231.46,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15132300640431584, var=27.931226864745206, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.975233796505476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.975233796505476""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.975233796505476
""",
)

entry(
    index = 34,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdO2d->O2d",
    kinetics = ArrheniusBM(A=(2.01929e-06,'m^3/(mol*s)'), n=3.68936, w0=(773.5,'kJ/mol'), E0=(107.273,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdO2d->O2d",
    kinetics = ArrheniusBM(A=(7.85783,'m^3/(mol*s)'), n=1.416, w0=(657,'kJ/mol'), E0=(183.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H",
    kinetics = ArrheniusBM(A=(2.55251e-54,'m^3/(mol*s)'), n=17.255, w0=(804.929,'kJ/mol'), E0=(232.344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3378389656107327, var=24.340751529801928, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H',), comment="""BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H
    Total Standard Deviation in ln(k): 10.73947220018833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H
Total Standard Deviation in ln(k): 10.73947220018833""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H
Total Standard Deviation in ln(k): 10.73947220018833
""",
)

entry(
    index = 37,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H",
    kinetics = ArrheniusBM(A=(4.42641e-51,'m^3/(mol*s)'), n=15.5591, w0=(857.147,'kJ/mol'), E0=(206.117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1297844831267025, var=62.63362485320676, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H',), comment="""BM rule fitted to 17 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H
    Total Standard Deviation in ln(k): 18.70441018120212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H
Total Standard Deviation in ln(k): 18.70441018120212""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H
Total Standard Deviation in ln(k): 18.70441018120212
""",
)

entry(
    index = 38,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.97474e-42,'m^3/(mol*s)'), n=13.5854, w0=(858.5,'kJ/mol'), E0=(161.917,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20107692261158752, var=14.45879954764573, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 8.128169041826094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 8.128169041826094""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 8.128169041826094
""",
)

entry(
    index = 39,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R",
    kinetics = ArrheniusBM(A=(9.95432e-21,'m^3/(mol*s)'), n=6.90457, w0=(975,'kJ/mol'), E0=(138.41,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12283329380841891, var=51.59854342092964, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R
    Total Standard Deviation in ln(k): 14.709064656855658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 14.709064656855658""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 14.709064656855658
""",
)

entry(
    index = 40,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_3COCdCt->CO",
    kinetics = ArrheniusBM(A=(4.10659e-19,'m^3/(mol*s)'), n=6.96069, w0=(975,'kJ/mol'), E0=(116.396,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_3COCdCt->CO',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_3COCdCt->CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_3COCdCt->CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_3COCdCt->CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_N-3COCdCt->CO",
    kinetics = ArrheniusBM(A=(2.4889e-27,'m^3/(mol*s)'), n=9.43559, w0=(858.5,'kJ/mol'), E0=(152.455,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_N-3COCdCt->CO',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_N-3COCdCt->CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_N-3COCdCt->CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_N-3COCdCt->CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(25762.3,'m^3/(mol*s)'), n=0.211089, w0=(711,'kJ/mol'), E0=(206.552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1695120686349818, var=13.236969088359478, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
    Total Standard Deviation in ln(k): 7.719666326447856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.719666326447856""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.719666326447856
""",
)

entry(
    index = 43,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.59096e+06,'m^3/(mol*s)'), n=-0.339093, w0=(711,'kJ/mol'), E0=(221.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.825331,'m^3/(mol*s)'), n=1.69758, w0=(657,'kJ/mol'), E0=(221.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C_Ext-3COCdO2d-R",
    kinetics = ArrheniusBM(A=(3.63667,'m^3/(mol*s)'), n=1.59996, w0=(657,'kJ/mol'), E0=(251.549,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C_Ext-3COCdO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C_Ext-3COCdO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C_Ext-3COCdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_2Br1sF1sH->Br1s_N-3COCdCddCtO2d->Ct_Ext-3COCdO2d-R_N-5R!H->C_Ext-3COCdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO",
    kinetics = ArrheniusBM(A=(2.14724e-58,'m^3/(mol*s)'), n=18.326, w0=(871.5,'kJ/mol'), E0=(178.057,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30061588011694546, var=0.5722653870348785, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO
    Total Standard Deviation in ln(k): 2.2718627737241284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO
Total Standard Deviation in ln(k): 2.2718627737241284""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO
Total Standard Deviation in ln(k): 2.2718627737241284
""",
)

entry(
    index = 47,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO",
    kinetics = ArrheniusBM(A=(1.85075e-45,'m^3/(mol*s)'), n=14.7888, w0=(755,'kJ/mol'), E0=(287.703,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5395100778065165, var=0.883096676543653, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO
    Total Standard Deviation in ln(k): 3.239467137423894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO
Total Standard Deviation in ln(k): 3.239467137423894""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO
Total Standard Deviation in ln(k): 3.239467137423894
""",
)

entry(
    index = 48,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R",
    kinetics = ArrheniusBM(A=(7.20811e-53,'m^3/(mol*s)'), n=16.0576, w0=(857.542,'kJ/mol'), E0=(204.432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8451162384919282, var=50.00590892959261, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R
    Total Standard Deviation in ln(k): 16.29986291400305"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 16.29986291400305""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 16.29986291400305
""",
)

entry(
    index = 49,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_3COCdCt->Ct",
    kinetics = ArrheniusBM(A=(2.57016e+31,'m^3/(mol*s)'), n=-7.53001, w0=(847,'kJ/mol'), E0=(355.217,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_3COCdCt->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_3COCdCt->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_3COCdCt->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_3COCdCt->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct",
    kinetics = ArrheniusBM(A=(172.261,'m^3/(mol*s)'), n=0.999091, w0=(858.5,'kJ/mol'), E0=(234.51,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3350239841489637, var=9.480572883570447, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct
    Total Standard Deviation in ln(k): 9.527018965413813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct
Total Standard Deviation in ln(k): 9.527018965413813""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct
Total Standard Deviation in ln(k): 9.527018965413813
""",
)

entry(
    index = 51,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O",
    kinetics = ArrheniusBM(A=(4.93796e-37,'m^3/(mol*s)'), n=12.0432, w0=(858.5,'kJ/mol'), E0=(182.197,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0035364533158091928, var=10.377038359071403, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
    Total Standard Deviation in ln(k): 6.466821022094472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
Total Standard Deviation in ln(k): 6.466821022094472""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
Total Standard Deviation in ln(k): 6.466821022094472
""",
)

entry(
    index = 52,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.55859e-82,'m^3/(mol*s)'), n=25.2195, w0=(858.5,'kJ/mol'), E0=(23.9269,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03283016705380347, var=76.10005297222277, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
    Total Standard Deviation in ln(k): 17.57086332998869"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
Total Standard Deviation in ln(k): 17.57086332998869""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
Total Standard Deviation in ln(k): 17.57086332998869
""",
)

entry(
    index = 53,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.80176e-25,'m^3/(mol*s)'), n=7.83563, w0=(975,'kJ/mol'), E0=(143.806,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20533757333877672, var=18.04780270524786, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 9.032580550208982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.032580550208982""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.032580550208982
""",
)

entry(
    index = 54,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R",
    kinetics = ArrheniusBM(A=(7.07779e-19,'m^3/(mol*s)'), n=6.81918, w0=(975,'kJ/mol'), E0=(129.012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4061.27,'m^3/(mol*s)'), n=0.468602, w0=(711,'kJ/mol'), E0=(200.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18985986566819657, var=36.555013946038876, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.59781198602482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.59781198602482""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.59781198602482
""",
)

entry(
    index = 56,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO_Ext-3CO-R",
    kinetics = ArrheniusBM(A=(4.80889e-59,'m^3/(mol*s)'), n=18.4557, w0=(871.5,'kJ/mol'), E0=(175.558,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2652657885549679, var=0.19494374366575662, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO_Ext-3CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO_Ext-3CO-R
    Total Standard Deviation in ln(k): 1.5516362900268013"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO_Ext-3CO-R
Total Standard Deviation in ln(k): 1.5516362900268013""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO_Ext-3CO-R
Total Standard Deviation in ln(k): 1.5516362900268013
""",
)

entry(
    index = 57,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.04962e-41,'m^3/(mol*s)'), n=13.4604, w0=(755,'kJ/mol'), E0=(294.409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6076187389410694, var=1.2801434831407437, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 3.794906196000192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.794906196000192""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.794906196000192
""",
)

entry(
    index = 58,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R",
    kinetics = ArrheniusBM(A=(1.19014e-55,'m^3/(mol*s)'), n=16.8258, w0=(858.5,'kJ/mol'), E0=(201.585,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.289861590267406, var=30.361474388512462, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R
    Total Standard Deviation in ln(k): 11.774635752394728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 11.774635752394728""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 11.774635752394728
""",
)

entry(
    index = 59,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F",
    kinetics = ArrheniusBM(A=(116.282,'m^3/(mol*s)'), n=1.10103, w0=(858.5,'kJ/mol'), E0=(260.264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4680389968819654, var=12.95644142745942, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F
    Total Standard Deviation in ln(k): 10.904595571097973"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F
Total Standard Deviation in ln(k): 10.904595571097973""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F
Total Standard Deviation in ln(k): 10.904595571097973
""",
)

entry(
    index = 60,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(2029.21,'m^3/(mol*s)'), n=0.783866, w0=(852.75,'kJ/mol'), E0=(253.649,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.126609618875, var=30.766180113608787, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F
    Total Standard Deviation in ln(k): 18.97552119011026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F
Total Standard Deviation in ln(k): 18.97552119011026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F
Total Standard Deviation in ln(k): 18.97552119011026
""",
)

entry(
    index = 61,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(186.02,'m^3/(mol*s)'), n=0.98704, w0=(858.5,'kJ/mol'), E0=(235.96,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6430745495510608, var=11.605668314364877, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 10.957877663695694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 10.957877663695694""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 10.957877663695694
""",
)

entry(
    index = 62,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R",
    kinetics = ArrheniusBM(A=(8.15704e-32,'m^3/(mol*s)'), n=10.4874, w0=(858.5,'kJ/mol'), E0=(201.846,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07597622770979322, var=3.8793143373666013, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R
    Total Standard Deviation in ln(k): 4.1394162540011505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 4.1394162540011505""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 4.1394162540011505
""",
)

entry(
    index = 63,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCt-R",
    kinetics = ArrheniusBM(A=(1.88854e-35,'m^3/(mol*s)'), n=11.7495, w0=(858.5,'kJ/mol'), E0=(192.275,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCt-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.55901e-25,'m^3/(mol*s)'), n=7.85908, w0=(975,'kJ/mol'), E0=(146.424,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2192330987969802, var=13.57969341746177, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 7.938413106341768"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 7.938413106341768""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 7.938413106341768
""",
)

entry(
    index = 65,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.75808e-23,'m^3/(mol*s)'), n=7.59676, w0=(975,'kJ/mol'), E0=(140.227,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.0823032,'m^3/(mol*s)'), n=1.92336, w0=(711,'kJ/mol'), E0=(212.188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->Cl1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO_Ext-3CO-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.60814e-58,'m^3/(mol*s)'), n=18.2614, w0=(871.5,'kJ/mol'), E0=(175.729,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO_Ext-3CO-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO_Ext-3CO-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO_Ext-3CO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_3COCdCt->CO_Ext-3CO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.99313e-58,'m^3/(mol*s)'), n=18.5023, w0=(755,'kJ/mol'), E0=(258.36,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.48961e-32,'m^3/(mol*s)'), n=10.8436, w0=(755,'kJ/mol'), E0=(313.093,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7626218610223013, var=0.7748478492016803, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 3.6808122480105117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.6808122480105117""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.6808122480105117
""",
)

entry(
    index = 70,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(8.91547e-56,'m^3/(mol*s)'), n=16.8605, w0=(858.5,'kJ/mol'), E0=(201.505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2559231639574366, var=29.373819810902564, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.50820995730164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.50820995730164""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.50820995730164
""",
)

entry(
    index = 71,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(125.267,'m^3/(mol*s)'), n=1.1096, w0=(858.5,'kJ/mol'), E0=(261.872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.242182665399847, var=22.542687620902537, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 15.151934584585028"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 15.151934584585028""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 15.151934584585028
""",
)

entry(
    index = 72,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F_3COCdCt->Ct",
    kinetics = ArrheniusBM(A=(3.60487e+39,'m^3/(mol*s)'), n=-9.93467, w0=(847,'kJ/mol'), E0=(360.535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F_3COCdCt->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F_3COCdCt->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F_3COCdCt->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F_3COCdCt->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F_N-3COCdCt->Ct",
    kinetics = ArrheniusBM(A=(3.14941,'m^3/(mol*s)'), n=1.63113, w0=(858.5,'kJ/mol'), E0=(244.653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F_N-3COCdCt->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F_N-3COCdCt->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F_N-3COCdCt->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_N-5R!H->F_N-3COCdCt->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_5R!H->F",
    kinetics = ArrheniusBM(A=(6.06166,'m^3/(mol*s)'), n=1.35437, w0=(858.5,'kJ/mol'), E0=(211.118,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03509149546506197, var=2.473925735349749, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_5R!H->F
    Total Standard Deviation in ln(k): 3.241360879314917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 3.241360879314917""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 3.241360879314917
""",
)

entry(
    index = 75,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(24.851,'m^3/(mol*s)'), n=1.25249, w0=(858.5,'kJ/mol'), E0=(239.116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.29072e-32,'m^3/(mol*s)'), n=10.7069, w0=(858.5,'kJ/mol'), E0=(205.275,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09076058711937247, var=0.9739595842926226, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
    Total Standard Deviation in ln(k): 2.206502509837374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
Total Standard Deviation in ln(k): 2.206502509837374""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
Total Standard Deviation in ln(k): 2.206502509837374
""",
)

entry(
    index = 77,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2.426e-34,'m^3/(mol*s)'), n=11.2313, w0=(858.5,'kJ/mol'), E0=(184.207,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.09665e-26,'m^3/(mol*s)'), n=8.06194, w0=(975,'kJ/mol'), E0=(147.323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.81675e-24,'m^3/(mol*s)'), n=7.58858, w0=(975,'kJ/mol'), E0=(146.107,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-3COCdCt-R_Ext-5R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.56402e-32,'m^3/(mol*s)'), n=10.7316, w0=(755,'kJ/mol'), E0=(309.077,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_2F1sH->H_N-3COCdCt->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C",
    kinetics = ArrheniusBM(A=(9.8916e-58,'m^3/(mol*s)'), n=17.4051, w0=(858.5,'kJ/mol'), E0=(198.206,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07637184010214733, var=22.640529637986447, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C
    Total Standard Deviation in ln(k): 9.73083263555755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C
Total Standard Deviation in ln(k): 9.73083263555755""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C
Total Standard Deviation in ln(k): 9.73083263555755
""",
)

entry(
    index = 82,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(126609,'m^3/(mol*s)'), n=0.247244, w0=(858.5,'kJ/mol'), E0=(289.294,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.727386091917859, var=96.91881224654463, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
    Total Standard Deviation in ln(k): 31.61394059622384"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
Total Standard Deviation in ln(k): 31.61394059622384""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
Total Standard Deviation in ln(k): 31.61394059622384
""",
)

entry(
    index = 83,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_6R!H->F",
    kinetics = ArrheniusBM(A=(8.19918,'m^3/(mol*s)'), n=1.36893, w0=(858.5,'kJ/mol'), E0=(229.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0484539841974525, var=1.7251977549761428, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_6R!H->F
    Total Standard Deviation in ln(k): 2.754898721807278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 2.754898721807278""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 2.754898721807278
""",
)

entry(
    index = 84,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(4.49727,'m^3/(mol*s)'), n=1.54397, w0=(858.5,'kJ/mol'), E0=(265.753,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(14.8208,'m^3/(mol*s)'), n=1.21604, w0=(858.5,'kJ/mol'), E0=(215.271,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_N-3COCdCt->Ct_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.83024e-32,'m^3/(mol*s)'), n=10.7119, w0=(858.5,'kJ/mol'), E0=(205.573,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(9.10251e-33,'m^3/(mol*s)'), n=10.7019, w0=(858.5,'kJ/mol'), E0=(204.977,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCt-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(4.21028e-60,'m^3/(mol*s)'), n=17.9382, w0=(858.5,'kJ/mol'), E0=(197.688,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.42879e-56,'m^3/(mol*s)'), n=17.219, w0=(858.5,'kJ/mol'), E0=(195.721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(12.1292,'m^3/(mol*s)'), n=1.44664, w0=(858.5,'kJ/mol'), E0=(294.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(295139,'m^3/(mol*s)'), n=-0.0462351, w0=(858.5,'kJ/mol'), E0=(228.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.032098671944279795, var=38.442285366203905, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 12.510376884005026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 12.510376884005026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 12.510376884005026
""",
)

entry(
    index = 92,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4.45749,'m^3/(mol*s)'), n=1.21594, w0=(858.5,'kJ/mol'), E0=(218.95,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_5R!H->F_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(22.8223,'m^3/(mol*s)'), n=1.20947, w0=(858.5,'kJ/mol'), E0=(204.182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->Cl1s_N-2Br1sF1sH->Br1s_N-3COCdCddCtO2d->O2d_1Br1sCl1sF1sH->H_N-2F1sH->H_Ext-3COCdCt-R_Ext-3COCdCt-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

