#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.03121e+13,'s^-1'), n=-0.336062, w0=(884.5,'kJ/mol'), E0=(251.476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8288977860261169, var=124.73377756908368, Tref=1000.0, N=21, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 21 training reactions at node Root
    Total Standard Deviation in ln(k): 24.472396548401118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 24.472396548401118""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 24.472396548401118
""",
)

entry(
    index = 2,
    label = "Root_3C-u0",
    kinetics = ArrheniusBM(A=(4.15015e+09,'s^-1'), n=0.762925, w0=(884.5,'kJ/mol'), E0=(272.329,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7969850492817171, var=44.28642288961711, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_3C-u0',), comment="""BM rule fitted to 16 training reactions at node Root_3C-u0
    Total Standard Deviation in ln(k): 15.343595005977956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_3C-u0
Total Standard Deviation in ln(k): 15.343595005977956""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_3C-u0
Total Standard Deviation in ln(k): 15.343595005977956
""",
)

entry(
    index = 3,
    label = "Root_N-3C-u0",
    kinetics = ArrheniusBM(A=(5.3516e+28,'s^-1'), n=-4.8882, w0=(884.5,'kJ/mol'), E0=(193.409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0345353243258473, var=362.1486374397543, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3C-u0',), comment="""BM rule fitted to 5 training reactions at node Root_N-3C-u0
    Total Standard Deviation in ln(k): 40.749851060682744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3C-u0
Total Standard Deviation in ln(k): 40.749851060682744""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3C-u0
Total Standard Deviation in ln(k): 40.749851060682744
""",
)

entry(
    index = 4,
    label = "Root_3C-u0_7R->F",
    kinetics = ArrheniusBM(A=(5.88502e+09,'s^-1'), n=0.766005, w0=(884.5,'kJ/mol'), E0=(308.597,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8547971731013316, var=3.073203386560898, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_3C-u0_7R->F',), comment="""BM rule fitted to 10 training reactions at node Root_3C-u0_7R->F
    Total Standard Deviation in ln(k): 5.662143330093777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_3C-u0_7R->F
Total Standard Deviation in ln(k): 5.662143330093777""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_3C-u0_7R->F
Total Standard Deviation in ln(k): 5.662143330093777
""",
)

entry(
    index = 5,
    label = "Root_3C-u0_N-7R->F",
    kinetics = ArrheniusBM(A=(5.70503e+08,'s^-1'), n=0.932276, w0=(884.5,'kJ/mol'), E0=(210.276,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6661045986080345, var=36.17068129408174, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3C-u0_N-7R->F',), comment="""BM rule fitted to 6 training reactions at node Root_3C-u0_N-7R->F
    Total Standard Deviation in ln(k): 13.730520622892136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3C-u0_N-7R->F
Total Standard Deviation in ln(k): 13.730520622892136""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3C-u0_N-7R->F
Total Standard Deviation in ln(k): 13.730520622892136
""",
)

entry(
    index = 6,
    label = "Root_N-3C-u0_7R->O",
    kinetics = ArrheniusBM(A=(1442.74,'s^-1'), n=2.34038, w0=(884.5,'kJ/mol'), E0=(262.374,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3091352839065547, var=0.07250119342877608, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3C-u0_7R->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3C-u0_7R->O
    Total Standard Deviation in ln(k): 1.3165177009397602"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3C-u0_7R->O
Total Standard Deviation in ln(k): 1.3165177009397602""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3C-u0_7R->O
Total Standard Deviation in ln(k): 1.3165177009397602
""",
)

entry(
    index = 7,
    label = "Root_N-3C-u0_N-7R->O",
    kinetics = ArrheniusBM(A=(6.36421e+12,'s^-1'), n=-0.26062, w0=(884.5,'kJ/mol'), E0=(58.3629,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6847730575369689, var=11.02720525019171, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3C-u0_N-7R->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-7R->O
    Total Standard Deviation in ln(k): 8.377706410515446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-7R->O
Total Standard Deviation in ln(k): 8.377706410515446""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-7R->O
Total Standard Deviation in ln(k): 8.377706410515446
""",
)

entry(
    index = 8,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s",
    kinetics = ArrheniusBM(A=(1.14504e+10,'s^-1'), n=0.716566, w0=(884.5,'kJ/mol'), E0=(309.637,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8688986301757061, var=3.0530929553077617, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s',), comment="""BM rule fitted to 9 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s
    Total Standard Deviation in ln(k): 5.68605644804073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s
Total Standard Deviation in ln(k): 5.68605644804073""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s
Total Standard Deviation in ln(k): 5.68605644804073
""",
)

entry(
    index = 9,
    label = "Root_3C-u0_7R->F_N-4CF1sH->F1s",
    kinetics = ArrheniusBM(A=(1.08e+10,'s^-1'), n=0.39, w0=(884.5,'kJ/mol'), E0=(306.297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_7R->F_N-4CF1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_N-4CF1sH->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_N-4CF1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_N-4CF1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_3C-u0_N-7R->F_4CF1sH->C",
    kinetics = ArrheniusBM(A=(3.07704e+09,'s^-1'), n=0.693435, w0=(884.5,'kJ/mol'), E0=(212.342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7646177837232305, var=53.878926070572376, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3C-u0_N-7R->F_4CF1sH->C',), comment="""BM rule fitted to 4 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C
    Total Standard Deviation in ln(k): 16.636359887386302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C
Total Standard Deviation in ln(k): 16.636359887386302""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C
Total Standard Deviation in ln(k): 16.636359887386302
""",
)

entry(
    index = 11,
    label = "Root_3C-u0_N-7R->F_N-4CF1sH->C",
    kinetics = ArrheniusBM(A=(1.96204e+07,'s^-1'), n=1.4099, w0=(884.5,'kJ/mol'), E0=(206.145,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5006224611209922, var=131.82453563872733, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_N-7R->F_N-4CF1sH->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_N-7R->F_N-4CF1sH->C
    Total Standard Deviation in ln(k): 24.275184402751794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_N-7R->F_N-4CF1sH->C
Total Standard Deviation in ln(k): 24.275184402751794""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_N-7R->F_N-4CF1sH->C
Total Standard Deviation in ln(k): 24.275184402751794
""",
)

entry(
    index = 12,
    label = "Root_N-3C-u0_7R->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(5066.67,'s^-1'), n=2.17, w0=(884.5,'kJ/mol'), E0=(263.498,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_7R->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_7R->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_7R->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_7R->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-3C-u0_7R->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(413.333,'s^-1'), n=2.51, w0=(884.5,'kJ/mol'), E0=(261.256,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_7R->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_7R->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_7R->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_7R->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-3C-u0_N-7R->O_4CF1sH->C",
    kinetics = ArrheniusBM(A=(2.26945e+13,'s^-1'), n=-0.460587, w0=(884.5,'kJ/mol'), E0=(42.1611,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.03893457902195, var=3.195481414267717, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3C-u0_N-7R->O_4CF1sH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-7R->O_4CF1sH->C
    Total Standard Deviation in ln(k): 6.194034676464524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-7R->O_4CF1sH->C
Total Standard Deviation in ln(k): 6.194034676464524""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-7R->O_4CF1sH->C
Total Standard Deviation in ln(k): 6.194034676464524
""",
)

entry(
    index = 15,
    label = "Root_N-3C-u0_N-7R->O_N-4CF1sH->C",
    kinetics = ArrheniusBM(A=(3.4e+06,'s^-1'), n=1.62, w0=(884.5,'kJ/mol'), E0=(71.1229,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-7R->O_N-4CF1sH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-7R->O_N-4CF1sH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-7R->O_N-4CF1sH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-7R->O_N-4CF1sH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C",
    kinetics = ArrheniusBM(A=(5.51248e+10,'s^-1'), n=0.545652, w0=(884.5,'kJ/mol'), E0=(308.559,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.877820059112479, var=3.9098523140103643, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C',), comment="""BM rule fitted to 6 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C
    Total Standard Deviation in ln(k): 6.169610168504506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C
Total Standard Deviation in ln(k): 6.169610168504506""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C
Total Standard Deviation in ln(k): 6.169610168504506
""",
)

entry(
    index = 17,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C",
    kinetics = ArrheniusBM(A=(6.07134e+08,'s^-1'), n=1.03275, w0=(884.5,'kJ/mol'), E0=(312.014,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8529437633036756, var=1.3115859418612013, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C
    Total Standard Deviation in ln(k): 4.4389874586961104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C
Total Standard Deviation in ln(k): 4.4389874586961104""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C
Total Standard Deviation in ln(k): 4.4389874586961104
""",
)

entry(
    index = 18,
    label = "Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.66708e+11,'s^-1'), n=0.00201256, w0=(884.5,'kJ/mol'), E0=(177.986,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6972849589862969, var=1.4477353565342361, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.164107089482756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.164107089482756""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.164107089482756
""",
)

entry(
    index = 19,
    label = "Root_3C-u0_N-7R->F_4CF1sH->C_Ext-7CHO-R_Ext-7CHO-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.63e+08,'s^-1'), n=1.07, w0=(884.5,'kJ/mol'), E0=(250.619,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-7R->F_4CF1sH->C_Ext-7CHO-R_Ext-7CHO-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-7CHO-R_Ext-7CHO-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-7CHO-R_Ext-7CHO-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-7CHO-R_Ext-7CHO-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_3C-u0_N-7R->F_4CF1sH->C_Ext-7CHO-R_Ext-7CHO-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(7.65e+08,'s^-1'), n=0.9, w0=(884.5,'kJ/mol'), E0=(249.645,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-7R->F_4CF1sH->C_Ext-7CHO-R_Ext-7CHO-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-7CHO-R_Ext-7CHO-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-7CHO-R_Ext-7CHO-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-7CHO-R_Ext-7CHO-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_3C-u0_N-7R->F_N-4CF1sH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.23333e+10,'s^-1'), n=0.42, w0=(884.5,'kJ/mol'), E0=(182.306,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-7R->F_N-4CF1sH->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_N-4CF1sH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_N-4CF1sH->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_N-4CF1sH->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-3C-u0_N-7R->O_4CF1sH->C_Ext-7CFH-R_Ext-7CFH-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.28224e+10,'s^-1'), n=0.400164, w0=(884.5,'kJ/mol'), E0=(-59.1518,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-7R->O_4CF1sH->C_Ext-7CFH-R_Ext-7CFH-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-7R->O_4CF1sH->C_Ext-7CFH-R_Ext-7CFH-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-7R->O_4CF1sH->C_Ext-7CFH-R_Ext-7CFH-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-7R->O_4CF1sH->C_Ext-7CFH-R_Ext-7CFH-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-3C-u0_N-7R->O_4CF1sH->C_Ext-7CFH-R_Ext-7CFH-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.69734e+11,'s^-1'), n=0.218411, w0=(884.5,'kJ/mol'), E0=(26.956,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-7R->O_4CF1sH->C_Ext-7CFH-R_Ext-7CFH-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-7R->O_4CF1sH->C_Ext-7CFH-R_Ext-7CFH-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-7R->O_4CF1sH->C_Ext-7CFH-R_Ext-7CFH-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-7R->O_4CF1sH->C_Ext-7CFH-R_Ext-7CFH-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_5CF1sH->F1s",
    kinetics = ArrheniusBM(A=(7.21374e+10,'s^-1'), n=0.80051, w0=(884.5,'kJ/mol'), E0=(319.508,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6789974715567533, var=7.1113215765411715, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_5CF1sH->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_5CF1sH->F1s
    Total Standard Deviation in ln(k): 7.052063115073463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_5CF1sH->F1s
Total Standard Deviation in ln(k): 7.052063115073463""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_5CF1sH->F1s
Total Standard Deviation in ln(k): 7.052063115073463
""",
)

entry(
    index = 25,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s",
    kinetics = ArrheniusBM(A=(5.15306e+10,'s^-1'), n=0.409878, w0=(884.5,'kJ/mol'), E0=(303.154,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9757070644935583, var=5.708388716789278, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s',), comment="""BM rule fitted to 4 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s
    Total Standard Deviation in ln(k): 7.241285355168285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s
Total Standard Deviation in ln(k): 7.241285355168285""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s
Total Standard Deviation in ln(k): 7.241285355168285
""",
)

entry(
    index = 26,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_5CF1sH->F1s",
    kinetics = ArrheniusBM(A=(5.66667e+08,'s^-1'), n=1.16, w0=(884.5,'kJ/mol'), E0=(327.64,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_5CF1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_5CF1sH->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_5CF1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_5CF1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s",
    kinetics = ArrheniusBM(A=(3.40038e+08,'s^-1'), n=1.04555, w0=(884.5,'kJ/mol'), E0=(303.522,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0007821082272608, var=0.21194032785904834, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s
    Total Standard Deviation in ln(k): 3.4374473425519185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s
Total Standard Deviation in ln(k): 3.4374473425519185""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s
Total Standard Deviation in ln(k): 3.4374473425519185
""",
)

entry(
    index = 28,
    label = "Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R_Ext-7CHO-R_Ext-7CHO-R_9R!H->C",
    kinetics = ArrheniusBM(A=(2.235e+11,'s^-1'), n=0.12, w0=(884.5,'kJ/mol'), E0=(179.272,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R_Ext-7CHO-R_Ext-7CHO-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R_Ext-7CHO-R_Ext-7CHO-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R_Ext-7CHO-R_Ext-7CHO-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R_Ext-7CHO-R_Ext-7CHO-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R_Ext-7CHO-R_Ext-7CHO-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(1.08e+12,'s^-1'), n=-0.04, w0=(884.5,'kJ/mol'), E0=(176.036,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R_Ext-7CHO-R_Ext-7CHO-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R_Ext-7CHO-R_Ext-7CHO-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R_Ext-7CHO-R_Ext-7CHO-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-7R->F_4CF1sH->C_Ext-3C-R_Ext-7CHO-R_Ext-7CHO-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_5CF1sH->F1s_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.31333e+10,'s^-1'), n=0.98, w0=(884.5,'kJ/mol'), E0=(307.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_5CF1sH->F1s_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_5CF1sH->F1s_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_5CF1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_5CF1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(8.58742e+10,'s^-1'), n=0.356425, w0=(884.5,'kJ/mol'), E0=(304.73,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9602251107818673, var=13.721201921527582, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 9.838593799008404"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 9.838593799008404""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 9.838593799008404
""",
)

entry(
    index = 32,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(3.03063e+10,'s^-1'), n=0.465833, w0=(884.5,'kJ/mol'), E0=(301.555,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9720599539151915, var=25.839816090694164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 12.633007297550606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 12.633007297550606""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 12.633007297550606
""",
)

entry(
    index = 33,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(4.77e+08,'s^-1'), n=1.06, w0=(884.5,'kJ/mol'), E0=(305.835,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.65e+08,'s^-1'), n=1.02, w0=(884.5,'kJ/mol'), E0=(301.302,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_N-Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.715e+11,'s^-1'), n=0.16, w0=(884.5,'kJ/mol'), E0=(288.004,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_9R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.18e+10,'s^-1'), n=0.57, w0=(884.5,'kJ/mol'), E0=(284.49,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_7R->F_4CF1sH->F1s_Ext-3C-R_Sp-8R!H-3C_N-5CF1sH->F1s_Ext-8R!H-R_Ext-8R!H-R_N-9R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

