#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.36656e+09,'s^-1'), n=0.930978, w0=(853.342,'kJ/mol'), E0=(303.286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5624120644880793, var=74.05591801404864, Tref=1000.0, N=19, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 19 training reactions at node Root
    Total Standard Deviation in ln(k): 18.664993345872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 18.664993345872""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 18.664993345872
""",
)

entry(
    index = 2,
    label = "Root_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.44785e+09,'s^-1'), n=0.942525, w0=(849.967,'kJ/mol'), E0=(318.32,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5106527275315708, var=73.13982350353754, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-3C-R',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-3C-R
    Total Standard Deviation in ln(k): 18.427907064568625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-3C-R
Total Standard Deviation in ln(k): 18.427907064568625""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-3C-R
Total Standard Deviation in ln(k): 18.427907064568625
""",
)

entry(
    index = 3,
    label = "Root_Ext-2C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(251383,'s^-1'), n=1.88683, w0=(884.5,'kJ/mol'), E0=(271.416,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7842002618501013, var=22.237214085779982, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2C-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.423951447853803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.423951447853803""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.423951447853803
""",
)

entry(
    index = 4,
    label = "Root_4F1sH->H",
    kinetics = ArrheniusBM(A=(2.055e+06,'s^-1'), n=1.75, w0=(810.5,'kJ/mol'), E0=(174.216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_4F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(8.1e+07,'s^-1'), n=1.22, w0=(884.5,'kJ/mol'), E0=(242.019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(6.32461e+07,'s^-1'), n=1.37309, w0=(847.5,'kJ/mol'), E0=(352.586,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6994265698771439, var=10.630002913137663, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 8.293528336201252"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 8.293528336201252""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 8.293528336201252
""",
)

entry(
    index = 7,
    label = "Root_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.28717e+13,'s^-1'), n=-0.270885, w0=(854.9,'kJ/mol'), E0=(252.778,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16681317949109725, var=88.57140087745086, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 19.286167551674108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 19.286167551674108""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 19.286167551674108
""",
)

entry(
    index = 8,
    label = "Root_Ext-2C-R_Ext-6R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.63e+08,'s^-1'), n=1.07, w0=(884.5,'kJ/mol'), E0=(292.221,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2C-R_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_Ext-2C-R_Ext-6R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(7.65e+08,'s^-1'), n=0.9, w0=(884.5,'kJ/mol'), E0=(266.625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2C-R_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-3C-R_6R!H->C_5R->F",
    kinetics = ArrheniusBM(A=(4.36029e+08,'s^-1'), n=1.12849, w0=(872.167,'kJ/mol'), E0=(343.982,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7405930364877842, var=15.31367641387294, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_5R->F',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F
    Total Standard Deviation in ln(k): 9.705854705493929"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F
Total Standard Deviation in ln(k): 9.705854705493929""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F
Total Standard Deviation in ln(k): 9.705854705493929
""",
)

entry(
    index = 11,
    label = "Root_Ext-3C-R_6R!H->C_N-5R->F",
    kinetics = ArrheniusBM(A=(4.89763e+06,'s^-1'), n=1.69796, w0=(810.5,'kJ/mol'), E0=(365.862,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6398210854230618, var=0.6582589359839236, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-5R->F',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F
    Total Standard Deviation in ln(k): 3.234095548766332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F
Total Standard Deviation in ln(k): 3.234095548766332""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F
Total Standard Deviation in ln(k): 3.234095548766332
""",
)

entry(
    index = 12,
    label = "Root_Ext-3C-R_N-6R!H->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.17974e+06,'s^-1'), n=1.82722, w0=(810.5,'kJ/mol'), E0=(305.334,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.38258627866487727, var=0.43476898594326086, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_4F1sH->H
    Total Standard Deviation in ln(k): 2.2831345123099007"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 2.2831345123099007""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 2.2831345123099007
""",
)

entry(
    index = 13,
    label = "Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(1.22938e+13,'s^-1'), n=-0.319608, w0=(884.5,'kJ/mol'), E0=(205.856,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4110827322317373, var=41.260975195384965, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 13.910228117798662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 13.910228117798662""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 13.910228117798662
""",
)

entry(
    index = 14,
    label = "Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C",
    kinetics = ArrheniusBM(A=(6.83027e+08,'s^-1'), n=1.1272, w0=(859.833,'kJ/mol'), E0=(347.78,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7218512893711543, var=43.23892642969072, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C
    Total Standard Deviation in ln(k): 14.996095344132213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C
Total Standard Deviation in ln(k): 14.996095344132213""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C
Total Standard Deviation in ln(k): 14.996095344132213
""",
)

entry(
    index = 15,
    label = "Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C",
    kinetics = ArrheniusBM(A=(2.88764e+08,'s^-1'), n=1.12522, w0=(884.5,'kJ/mol'), E0=(340.23,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7649399048178857, var=16.088952746328534, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C
    Total Standard Deviation in ln(k): 9.963159809857888"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C
Total Standard Deviation in ln(k): 9.963159809857888""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C
Total Standard Deviation in ln(k): 9.963159809857888
""",
)

entry(
    index = 16,
    label = "Root_Ext-3C-R_6R!H->C_N-5R->F_Sp-6C-3C",
    kinetics = ArrheniusBM(A=(2.14248e+07,'s^-1'), n=1.56451, w0=(810.5,'kJ/mol'), E0=(370.881,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41319966740315883, var=4.015192475202903, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-5R->F_Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_Sp-6C-3C
    Total Standard Deviation in ln(k): 5.0552672796472455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_Sp-6C-3C
Total Standard Deviation in ln(k): 5.0552672796472455""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_Sp-6C-3C
Total Standard Deviation in ln(k): 5.0552672796472455
""",
)

entry(
    index = 17,
    label = "Root_Ext-3C-R_6R!H->C_N-5R->F_N-Sp-6C-3C",
    kinetics = ArrheniusBM(A=(990937,'s^-1'), n=1.8466, w0=(810.5,'kJ/mol'), E0=(360.695,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8652399642158801, var=0.06410572113553809, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-5R->F_N-Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_N-Sp-6C-3C
    Total Standard Deviation in ln(k): 2.6815507913477874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_N-Sp-6C-3C
Total Standard Deviation in ln(k): 2.6815507913477874""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_N-Sp-6C-3C
Total Standard Deviation in ln(k): 2.6815507913477874
""",
)

entry(
    index = 18,
    label = "Root_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.865e+06,'s^-1'), n=1.71, w0=(810.5,'kJ/mol'), E0=(299.882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.18516e+15,'s^-1'), n=-0.929113, w0=(884.5,'kJ/mol'), E0=(189.521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6857481764696116, var=41.55423850638724, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
    Total Standard Deviation in ln(k): 14.646024323805825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 14.646024323805825""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 14.646024323805825
""",
)

entry(
    index = 20,
    label = "Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.23333e+10,'s^-1'), n=0.42, w0=(884.5,'kJ/mol'), E0=(242.647,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.66e+09,'s^-1'), n=0.79, w0=(810.5,'kJ/mol'), E0=(345.457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.9e+09,'s^-1'), n=0.8, w0=(884.5,'kJ/mol'), E0=(376.812,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-6C-R_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.19667e+11,'s^-1'), n=0.77, w0=(884.5,'kJ/mol'), E0=(329.989,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-6C-R_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-6C-R_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_Sp-6C-3C_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.02874e+08,'s^-1'), n=1.10981, w0=(884.5,'kJ/mol'), E0=(346.507,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8768143485714226, var=17.642562571658452, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 10.623550010539699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 10.623550010539699""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 10.623550010539699
""",
)

entry(
    index = 25,
    label = "Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(5.66667e+08,'s^-1'), n=1.16, w0=(884.5,'kJ/mol'), E0=(327.64,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_Ext-3C-R_6R!H->C_N-5R->F_Sp-6C-3C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.66e+07,'s^-1'), n=1.5, w0=(810.5,'kJ/mol'), E0=(370.664,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-5R->F_Sp-6C-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_Sp-6C-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_Ext-3C-R_6R!H->C_N-5R->F_N-Sp-6C-3C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.895e+06,'s^-1'), n=1.63, w0=(810.5,'kJ/mol'), E0=(358.307,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-5R->F_N-Sp-6C-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_N-Sp-6C-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_N-Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-5R->F_N-Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.235e+11,'s^-1'), n=0.12, w0=(884.5,'kJ/mol'), E0=(198.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.08e+12,'s^-1'), n=-0.04, w0=(884.5,'kJ/mol'), E0=(163.594,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(4.77e+08,'s^-1'), n=1.06, w0=(884.5,'kJ/mol'), E0=(363.277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2.65e+08,'s^-1'), n=1.02, w0=(884.5,'kJ/mol'), E0=(330.964,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_5R->F_N-Sp-6C-3C_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

