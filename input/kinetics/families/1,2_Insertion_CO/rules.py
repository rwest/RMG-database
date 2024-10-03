#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.11691e-09,'m^3/(mol*s)'), n=4.21807, w0=(718.364,'kJ/mol'), E0=(391.996,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16720023076269405, var=66.522448207154, Tref=1000.0, N=33, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 33 training reactions at node Root
    Total Standard Deviation in ln(k): 16.770979960484514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 16.770979960484514""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 16.770979960484514
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
    kinetics = ArrheniusBM(A=(8.38254e-09,'m^3/(mol*s)'), n=4.21151, w0=(743.471,'kJ/mol'), E0=(395.063,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18817413509934436, var=57.52700621975046, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 15.678025212269217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 15.678025212269217""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 15.678025212269217
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
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(7.17943e-19,'m^3/(mol*s)'), n=7.14504, w0=(756.327,'kJ/mol'), E0=(433.368,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6228771097107028, var=113.4009414182921, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 22.913417268881258"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 22.913417268881258""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 22.913417268881258
""",
)

entry(
    index = 7,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(1.13821e-06,'m^3/(mol*s)'), n=3.58385, w0=(736.705,'kJ/mol'), E0=(378.984,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27055772495920943, var=16.305522489818504, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 8.77493300510135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 8.77493300510135""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 8.77493300510135
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
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.94054e-19,'m^3/(mol*s)'), n=7.3154, w0=(788.159,'kJ/mol'), E0=(439.277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5149135479858351, var=87.94057855274406, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 20.093484219116164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 20.093484219116164""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 20.093484219116164
""",
)

entry(
    index = 11,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.27e-07,'m^3/(mol*s)'), n=3.7, w0=(750.5,'kJ/mol'), E0=(245.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Br1s",
    kinetics = ArrheniusBM(A=(0.0163189,'m^3/(mol*s)'), n=2.90186, w0=(621.936,'kJ/mol'), E0=(321.138,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s",
    kinetics = ArrheniusBM(A=(1.15463e-06,'m^3/(mol*s)'), n=3.57985, w0=(743.081,'kJ/mol'), E0=(379.294,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2737591262648627, var=15.744830835906782, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s',), comment="""BM rule fitted to 18 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s
    Total Standard Deviation in ln(k): 8.642576991895817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s
Total Standard Deviation in ln(k): 8.642576991895817""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s
Total Standard Deviation in ln(k): 8.642576991895817
""",
)

entry(
    index = 14,
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
    index = 15,
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
    index = 16,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(4.73499e-18,'m^3/(mol*s)'), n=6.83384, w0=(779.338,'kJ/mol'), E0=(438.574,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8378125093291641, var=105.08123069663891, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R
    Total Standard Deviation in ln(k): 22.65542272920326"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R
Total Standard Deviation in ln(k): 22.65542272920326""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R
Total Standard Deviation in ln(k): 22.65542272920326
""",
)

entry(
    index = 17,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_2Cl1sCsF1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.00734196,'m^3/(mol*s)'), n=2.97843, w0=(647.769,'kJ/mol'), E0=(335.588,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_2Cl1sCsF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_2Cl1sCsF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_2Cl1sCsF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_2Cl1sCsF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.15533e-06,'m^3/(mol*s)'), n=3.57764, w0=(748.687,'kJ/mol'), E0=(379.526,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27661779715428686, var=15.378438325203856, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s',), comment="""BM rule fitted to 17 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s
    Total Standard Deviation in ln(k): 8.556658763608986"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s
Total Standard Deviation in ln(k): 8.556658763608986""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s
Total Standard Deviation in ln(k): 8.556658763608986
""",
)

entry(
    index = 19,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.0160108,'m^3/(mol*s)'), n=2.60692, w0=(720.5,'kJ/mol'), E0=(333.341,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.247059523398854, var=5.183931019487016, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 5.185183046777958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 5.185183046777958""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 5.185183046777958
""",
)

entry(
    index = 20,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.01387e-23,'m^3/(mol*s)'), n=8.17076, w0=(910.678,'kJ/mol'), E0=(451.687,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19401946186240443, var=4.676957229971805, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.822981074071763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.822981074071763""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.822981074071763
""",
)

entry(
    index = 21,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R",
    kinetics = ArrheniusBM(A=(5.36056e-06,'m^3/(mol*s)'), n=3.35568, w0=(752.167,'kJ/mol'), E0=(362.394,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21363487737064854, var=9.180671493387404, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R
    Total Standard Deviation in ln(k): 6.611042739432919"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 6.611042739432919""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 6.611042739432919
""",
)

entry(
    index = 22,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs",
    kinetics = ArrheniusBM(A=(3.91403e-06,'m^3/(mol*s)'), n=3.4626, w0=(788.666,'kJ/mol'), E0=(405.684,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.32636302624161784, var=13.550414985805787, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs
    Total Standard Deviation in ln(k): 8.199615507246111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs
Total Standard Deviation in ln(k): 8.199615507246111""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs
Total Standard Deviation in ln(k): 8.199615507246111
""",
)

entry(
    index = 23,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_N-2CsF1s->Cs",
    kinetics = ArrheniusBM(A=(0.000614234,'m^3/(mol*s)'), n=3.16963, w0=(794.5,'kJ/mol'), E0=(363.506,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_N-2CsF1s->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_N-2CsF1s->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_N-2CsF1s->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_N-2CsF1s->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.26069,'m^3/(mol*s)'), n=1.78987, w0=(720.5,'kJ/mol'), E0=(338.164,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.229798356330123, var=10.40246183297155, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 7.043224313309215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 7.043224313309215""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 7.043224313309215
""",
)

entry(
    index = 25,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.81927e-16,'m^3/(mol*s)'), n=6.80628, w0=(720.5,'kJ/mol'), E0=(308.481,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.95386e-25,'m^3/(mol*s)'), n=8.85153, w0=(910.594,'kJ/mol'), E0=(452.988,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(7.86681e-21,'m^3/(mol*s)'), n=7.49585, w0=(910.762,'kJ/mol'), E0=(450.336,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.99433e-06,'m^3/(mol*s)'), n=3.43052, w0=(740.071,'kJ/mol'), E0=(358.66,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21790401836581527, var=11.289159190893553, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
    Total Standard Deviation in ln(k): 7.2832758885516675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
Total Standard Deviation in ln(k): 7.2832758885516675""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
Total Standard Deviation in ln(k): 7.2832758885516675
""",
)

entry(
    index = 29,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0023437,'m^3/(mol*s)'), n=2.91659, w0=(794.5,'kJ/mol'), E0=(386.506,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11053150447395992, var=0.23751621675645537, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
    Total Standard Deviation in ln(k): 1.254737727978971"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.254737727978971""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.254737727978971
""",
)

entry(
    index = 30,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.000538,'m^3/(mol*s)'), n=3.29, w0=(885.995,'kJ/mol'), E0=(448.684,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(3.29107e-06,'m^3/(mol*s)'), n=3.47243, w0=(772.445,'kJ/mol'), E0=(404.497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.32885467589370915, var=14.072233730243552, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 8.346625926767244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 8.346625926767244""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 8.346625926767244
""",
)

entry(
    index = 32,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(88.9,'m^3/(mol*s)'), n=1.51, w0=(720.5,'kJ/mol'), E0=(332.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R",
    kinetics = ArrheniusBM(A=(0.000646288,'m^3/(mol*s)'), n=2.4917, w0=(716.923,'kJ/mol'), E0=(367.722,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15699964691804363, var=2.2252347933374517, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R
    Total Standard Deviation in ln(k): 3.384979073908383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R
Total Standard Deviation in ln(k): 3.384979073908383""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R
Total Standard Deviation in ln(k): 3.384979073908383
""",
)

entry(
    index = 34,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.99883e-09,'m^3/(mol*s)'), n=4.23832, w0=(752.167,'kJ/mol'), E0=(349.79,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24336671816327302, var=42.80731917162696, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 13.727915007598067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 13.727915007598067""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 13.727915007598067
""",
)

entry(
    index = 35,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.97532e-05,'m^3/(mol*s)'), n=3.22544, w0=(794.5,'kJ/mol'), E0=(362.283,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22783205549101904, var=5.1887513664573435, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 5.138994480895391"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.138994480895391""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.138994480895391
""",
)

entry(
    index = 36,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R",
    kinetics = ArrheniusBM(A=(2.6164e-06,'m^3/(mol*s)'), n=3.49588, w0=(779.839,'kJ/mol'), E0=(405.724,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34271609905446115, var=18.596958023435917, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
    Total Standard Deviation in ln(k): 9.506353455074818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
Total Standard Deviation in ln(k): 9.506353455074818""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
Total Standard Deviation in ln(k): 9.506353455074818
""",
)

entry(
    index = 37,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(0.000100447,'m^3/(mol*s)'), n=2.73849, w0=(723.98,'kJ/mol'), E0=(371.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(0.0041564,'m^3/(mol*s)'), n=2.24495, w0=(709.866,'kJ/mol'), E0=(364.194,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(9.64243e-06,'m^3/(mol*s)'), n=3.35746, w0=(794.5,'kJ/mol'), E0=(344.138,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1886217895610347, var=22.420877291018996, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 9.966482770437088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 9.966482770437088""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 9.966482770437088
""",
)

entry(
    index = 40,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(4.23497e-07,'m^3/(mol*s)'), n=3.48174, w0=(712.908,'kJ/mol'), E0=(383.101,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.23296e-06,'m^3/(mol*s)'), n=3.43153, w0=(794.5,'kJ/mol'), E0=(357.088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_N-6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.000729731,'m^3/(mol*s)'), n=3.01554, w0=(794.5,'kJ/mol'), E0=(367.51,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_N-6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_N-6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.54927e-07,'m^3/(mol*s)'), n=3.84834, w0=(757.106,'kJ/mol'), E0=(395.202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3806611735200859, var=4.918682127323757, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 5.402557032220877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 5.402557032220877""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 5.402557032220877
""",
)

entry(
    index = 44,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.63848e-07,'m^3/(mol*s)'), n=3.3693, w0=(870.772,'kJ/mol'), E0=(436.664,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(6.28645e-08,'m^3/(mol*s)'), n=3.72541, w0=(794.5,'kJ/mol'), E0=(337.378,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(0.00121549,'m^3/(mol*s)'), n=3.01393, w0=(794.5,'kJ/mol'), E0=(350.69,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_N-7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R",
    kinetics = ArrheniusBM(A=(7.42676e-06,'m^3/(mol*s)'), n=3.65749, w0=(784.665,'kJ/mol'), E0=(403.794,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.41957717132397787, var=15.806124086847793, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R
    Total Standard Deviation in ln(k): 9.024422503682247"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R
Total Standard Deviation in ln(k): 9.024422503682247""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R
Total Standard Deviation in ln(k): 9.024422503682247
""",
)

entry(
    index = 48,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(7.9377e-09,'m^3/(mol*s)'), n=4.0356, w0=(723.557,'kJ/mol'), E0=(386.084,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.85608e-06,'m^3/(mol*s)'), n=3.87966, w0=(773.341,'kJ/mol'), E0=(399.503,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(8.7634e-06,'m^3/(mol*s)'), n=3.4963, w0=(795.99,'kJ/mol'), E0=(407.559,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

