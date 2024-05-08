#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.3968e-05,'m^3/(mol*s)'), n=3.09365, w0=(731.222,'kJ/mol'), E0=(365.006,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1715413459708784, var=59.56955487000839, Tref=1000.0, N=27, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 27 training reactions at node Root
    Total Standard Deviation in ln(k): 15.903817489255095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root
Total Standard Deviation in ln(k): 15.903817489255095""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root
Total Standard Deviation in ln(k): 15.903817489255095
""",
)

entry(
    index = 2,
    label = "Root_1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(0.206225,'m^3/(mol*s)'), n=2.23779, w0=(753.875,'kJ/mol'), E0=(241.921,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.187394804003833, var=322.96180445695825, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 44.03590057956975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 44.03590057956975""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 44.03590057956975
""",
)

entry(
    index = 3,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(2.16084e-05,'m^3/(mol*s)'), n=3.09944, w0=(727.283,'kJ/mol'), E0=(368.373,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2115501205778539, var=49.83359548270137, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 23 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 14.683542115987143"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 14.683542115987143""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 14.683542115987143
""",
)

entry(
    index = 4,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(2890,'m^3/(mol*s)'), n=1.16, w0=(763.5,'kJ/mol'), E0=(342.529,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(3.06799e-05,'m^3/(mol*s)'), n=3.24032, w0=(750.667,'kJ/mol'), E0=(155.325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10391561097617022, var=43.22716720023073, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 13.441700477068382"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.441700477068382""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.441700477068382
""",
)

entry(
    index = 6,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(3.9825e-05,'m^3/(mol*s)'), n=2.90949, w0=(665.5,'kJ/mol'), E0=(407.532,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22470363043172253, var=26.937840800323457, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs',), comment="""BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 10.96949324067994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 10.96949324067994""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 10.96949324067994
""",
)

entry(
    index = 7,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(7.33825e-06,'m^3/(mol*s)'), n=3.30625, w0=(749.088,'kJ/mol'), E0=(342.716,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2057814836103543, var=37.48583533887642, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs',), comment="""BM rule fitted to 17 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 12.791165151464313"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 12.791165151464313""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 12.791165151464313
""",
)

entry(
    index = 8,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s",
    kinetics = ArrheniusBM(A=(5.66811e-11,'m^3/(mol*s)'), n=4.88105, w0=(867,'kJ/mol'), E0=(180.226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00924345,'m^3/(mol*s)'), n=2.53105, w0=(692.5,'kJ/mol'), E0=(141.907,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.059030279559912704, var=9.231478319943692, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 6.2393736235645205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.2393736235645205""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.2393736235645205
""",
)

entry(
    index = 10,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R",
    kinetics = ArrheniusBM(A=(0.000646296,'m^3/(mol*s)'), n=2.49169, w0=(667.5,'kJ/mol'), E0=(367.73,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15712369319124717, var=2.2249267420538024, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R
    Total Standard Deviation in ln(k): 3.3850837447293753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 3.3850837447293753""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 3.3850837447293753
""",
)

entry(
    index = 11,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.000538,'m^3/(mol*s)'), n=3.29, w0=(655.5,'kJ/mol'), E0=(448.701,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.28179e-06,'m^3/(mol*s)'), n=3.34686, w0=(667.5,'kJ/mol'), E0=(430.304,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3000044829219761, var=1.3666563603169115, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 3.0973971792876913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 3.0973971792876913""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 3.0973971792876913
""",
)

entry(
    index = 13,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(3.19017e-06,'m^3/(mol*s)'), n=3.36861, w0=(794.5,'kJ/mol'), E0=(345.116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2919963264658192, var=39.77897724504212, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s
    Total Standard Deviation in ln(k): 13.377638983844236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 13.377638983844236""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 13.377638983844236
""",
)

entry(
    index = 14,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(0.00684114,'m^3/(mol*s)'), n=2.75339, w0=(698,'kJ/mol'), E0=(326.269,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1600848339170222, var=12.044783560006554, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 8 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s
    Total Standard Deviation in ln(k): 7.359775660176242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 7.359775660176242""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 7.359775660176242
""",
)

entry(
    index = 15,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.006108,'m^3/(mol*s)'), n=2.57909, w0=(719.5,'kJ/mol'), E0=(150.108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0152384,'m^3/(mol*s)'), n=2.47236, w0=(665.5,'kJ/mol'), E0=(133.798,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(0.000100447,'m^3/(mol*s)'), n=2.73849, w0=(667.5,'kJ/mol'), E0=(371.259,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(0.0041564,'m^3/(mol*s)'), n=2.24495, w0=(667.5,'kJ/mol'), E0=(364.201,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1COCbCdCsCtNOSSidSis-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.48267e-06,'m^3/(mol*s)'), n=3.33526, w0=(667.5,'kJ/mol'), E0=(427.126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2990925519183369, var=0.07202579058103312, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 1.2895120278596846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 1.2895120278596846""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 1.2895120278596846
""",
)

entry(
    index = 20,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.63848e-07,'m^3/(mol*s)'), n=3.3693, w0=(667.5,'kJ/mol'), E0=(436.665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R",
    kinetics = ArrheniusBM(A=(2.945e-06,'m^3/(mol*s)'), n=3.37453, w0=(794.5,'kJ/mol'), E0=(344.919,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29572559498415885, var=40.335584955097666, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R
    Total Standard Deviation in ln(k): 13.475162208492629"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 13.475162208492629""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 13.475162208492629
""",
)

entry(
    index = 22,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.027508,'m^3/(mol*s)'), n=2.65932, w0=(690.5,'kJ/mol'), E0=(341.01,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10949868278833581, var=3.4508238454519153, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 3.9991970257239307"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 3.9991970257239307""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 3.9991970257239307
""",
)

entry(
    index = 23,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.27e-07,'m^3/(mol*s)'), n=3.7, w0=(750.5,'kJ/mol'), E0=(245.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(2.36999e-07,'m^3/(mol*s)'), n=3.56686, w0=(667.5,'kJ/mol'), E0=(426.1,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(9.27727e-06,'m^3/(mol*s)'), n=3.10363, w0=(667.5,'kJ/mol'), E0=(428.153,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O",
    kinetics = ArrheniusBM(A=(8.70872e-08,'m^3/(mol*s)'), n=3.66137, w0=(794.5,'kJ/mol'), E0=(295.511,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.42628274711784997, var=198.51612653631878, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O
    Total Standard Deviation in ln(k): 29.316927609924708"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O
Total Standard Deviation in ln(k): 29.316927609924708""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O
Total Standard Deviation in ln(k): 29.316927609924708
""",
)

entry(
    index = 27,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(9.91617e-06,'m^3/(mol*s)'), n=3.28323, w0=(794.5,'kJ/mol'), E0=(364.241,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24149625292006716, var=28.680224303278255, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.34291685569893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.34291685569893""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.34291685569893
""",
)

entry(
    index = 28,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H",
    kinetics = ArrheniusBM(A=(0.0241273,'m^3/(mol*s)'), n=2.64607, w0=(720.5,'kJ/mol'), E0=(342.942,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1640557451179403, var=2.084186193263976, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H
    Total Standard Deviation in ln(k): 3.3063784231040487"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H
Total Standard Deviation in ln(k): 3.3063784231040487""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H
Total Standard Deviation in ln(k): 3.3063784231040487
""",
)

entry(
    index = 29,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H",
    kinetics = ArrheniusBM(A=(0.0096373,'m^3/(mol*s)'), n=2.95599, w0=(615.5,'kJ/mol'), E0=(328.231,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18284517425263203, var=8.006055933679962, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H
    Total Standard Deviation in ln(k): 6.131802815400595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H
Total Standard Deviation in ln(k): 6.131802815400595""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H
Total Standard Deviation in ln(k): 6.131802815400595
""",
)

entry(
    index = 30,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.6641e-11,'m^3/(mol*s)'), n=4.80873, w0=(794.5,'kJ/mol'), E0=(332.263,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.000319223,'m^3/(mol*s)'), n=2.55831, w0=(794.5,'kJ/mol'), E0=(258.363,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(2.36028e-06,'m^3/(mol*s)'), n=3.37858, w0=(794.5,'kJ/mol'), E0=(358.342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2564347683255395, var=44.64889667491692, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 14.03991414917353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 14.03991414917353""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 14.03991414917353
""",
)

entry(
    index = 33,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(0.0023437,'m^3/(mol*s)'), n=2.91659, w0=(794.5,'kJ/mol'), E0=(386.506,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11053150447395992, var=0.23751621675645537, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_N-5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 1.254737727978971"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.254737727978971""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.254737727978971
""",
)

entry(
    index = 34,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.0272095,'m^3/(mol*s)'), n=2.58218, w0=(720.5,'kJ/mol'), E0=(339.675,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18781295013985375, var=3.3730633191276174, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R
    Total Standard Deviation in ln(k): 4.15376849830483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 4.15376849830483""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 4.15376849830483
""",
)

entry(
    index = 35,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.00734196,'m^3/(mol*s)'), n=2.97843, w0=(636.5,'kJ/mol'), E0=(335.591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0163189,'m^3/(mol*s)'), n=2.90186, w0=(594.5,'kJ/mol'), E0=(321.146,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(2.23296e-06,'m^3/(mol*s)'), n=3.43153, w0=(794.5,'kJ/mol'), E0=(357.088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(2.56232e-06,'m^3/(mol*s)'), n=3.35301, w0=(794.5,'kJ/mol'), E0=(358.828,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24891436526674468, var=84.66327378824407, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 19.071511264686446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 19.071511264686446""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 19.071511264686446
""",
)

entry(
    index = 39,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.83428,'m^3/(mol*s)'), n=2.03702, w0=(720.5,'kJ/mol'), E0=(343.691,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1874020864537245, var=4.5825242706269895, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 4.76236207753982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 4.76236207753982""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 4.76236207753982
""",
)

entry(
    index = 40,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.81927e-16,'m^3/(mol*s)'), n=6.80628, w0=(720.5,'kJ/mol'), E0=(308.481,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.28726e-06,'m^3/(mol*s)'), n=3.34441, w0=(794.5,'kJ/mol'), E0=(346.458,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2489524811015141, var=236.4437147670073, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 31.45177153518189"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 31.45177153518189""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 31.45177153518189
""",
)

entry(
    index = 42,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(5.43885e-06,'m^3/(mol*s)'), n=3.21456, w0=(794.5,'kJ/mol'), E0=(384.924,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(8.26069,'m^3/(mol*s)'), n=1.78987, w0=(720.5,'kJ/mol'), E0=(338.164,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.229798356330123, var=10.40246183297155, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
    Total Standard Deviation in ln(k): 7.043224313309215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 7.043224313309215""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 7.043224313309215
""",
)

entry(
    index = 44,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(8.43453e-06,'m^3/(mol*s)'), n=3.52638, w0=(794.5,'kJ/mol'), E0=(319.086,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(5.69856e-08,'m^3/(mol*s)'), n=3.54975, w0=(794.5,'kJ/mol'), E0=(370.463,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(88.9,'m^3/(mol*s)'), n=1.51, w0=(720.5,'kJ/mol'), E0=(332.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

