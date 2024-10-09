#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.38756e-92,'s^-1'), n=29.3567, w0=(690.396,'kJ/mol'), E0=(-44.8029,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5715575371559116, var=507.59368197247494, Tref=1000.0, N=48, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 48 training reactions at node Root
    Total Standard Deviation in ln(k): 49.11499718802224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root
Total Standard Deviation in ln(k): 49.11499718802224""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root
Total Standard Deviation in ln(k): 49.11499718802224
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(3.5606e-80,'s^-1'), n=26.4474, w0=(671.075,'kJ/mol'), E0=(54.8819,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7584963999975427, var=273.12135008869967, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 40 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 37.5493532772266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 37.5493532772266""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 37.5493532772266
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(7.19513e-106,'s^-1'), n=31.5517, w0=(1257.63,'kJ/mol'), E0=(-163.452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4567741634895961, var=1382.1011629626928, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 75.67695033236872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 75.67695033236872""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 75.67695033236872
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_1C-inRing",
    kinetics = ArrheniusBM(A=(1.50194e+32,'s^-1'), n=-4.88332, w0=(678.808,'kJ/mol'), E0=(347.064,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15321733847087632, var=187.39651970172005, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_1C-inRing
    Total Standard Deviation in ln(k): 27.82835771014872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_1C-inRing
Total Standard Deviation in ln(k): 27.82835771014872""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_1C-inRing
Total Standard Deviation in ln(k): 27.82835771014872
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(2.37381e-99,'s^-1'), n=31.794, w0=(675.328,'kJ/mol'), E0=(-40.6568,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.046910207710973, var=252.7099733367782, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing',), comment="""BM rule fitted to 32 training reactions at node Root_1R!H->C_N-1C-inRing
    Total Standard Deviation in ln(k): 37.01197169907477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_1R!H->C_N-1C-inRing
Total Standard Deviation in ln(k): 37.01197169907477""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_1R!H->C_N-1C-inRing
Total Standard Deviation in ln(k): 37.01197169907477
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.15428e-74,'s^-1'), n=21.7781, w0=(1514.28,'kJ/mol'), E0=(21.2336,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-12.355937056874975, var=3923.5649833951848, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 156.61839890509017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 156.61839890509017""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 156.61839890509017
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.03e+09,'s^-1'), n=0.6, w0=(787,'kJ/mol'), E0=(200.99,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_1R!H->C_1C-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(5.55307e+26,'s^-1'), n=-3.27994, w0=(771.973,'kJ/mol'), E0=(375.475,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03534432864450718, var=90.46819300207822, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N
    Total Standard Deviation in ln(k): 19.156796244363576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.156796244363576""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.156796244363576
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_1C-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(3.40265e+41,'s^-1'), n=-7.6107, w0=(670.125,'kJ/mol'), E0=(328.334,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3756868807420218, var=394.2316192042286, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 40.748486686278575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 40.748486686278575""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 40.748486686278575
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(5.80983e-50,'s^-1'), n=18.1064, w0=(664.65,'kJ/mol'), E0=(3.2897,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8995846432443477, var=59.0529284841149, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N
    Total Standard Deviation in ln(k): 20.178393519469225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N
Total Standard Deviation in ln(k): 20.178393519469225""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N
Total Standard Deviation in ln(k): 20.178393519469225
""",
)

entry(
    index = 11,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(6.80386e-118,'s^-1'), n=36.9375, w0=(680.182,'kJ/mol'), E0=(-58.3415,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.790005897481048, var=172.41765710955573, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N',), comment="""BM rule fitted to 22 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 33.33382122217645"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 33.33382122217645""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 33.33382122217645
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.26132e+53,'s^-1'), n=-19.9605, w0=(2656.75,'kJ/mol'), E0=(1328.37,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-44.544158689228894, var=1630.221309633121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 192.86317854385823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 192.86317854385823""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 192.86317854385823
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.09485e-70,'s^-1'), n=23.2967, w0=(966.363,'kJ/mol'), E0=(36.9993,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-15.804803949143722, var=1870.7702644047508, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 126.42016982433978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 126.42016982433978""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 126.42016982433978
""",
)

entry(
    index = 14,
    label = "Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.04969e+22,'s^-1'), n=-1.94535, w0=(798.027,'kJ/mol'), E0=(383.84,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04897568024138421, var=81.08171849206428, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 18.17476920446385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 18.17476920446385""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 18.17476920446385
""",
)

entry(
    index = 15,
    label = "Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.1544e+10,'s^-1'), n=1.34775, w0=(693.81,'kJ/mol'), E0=(271.878,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_1R!H->C_1C-inRing_N-2R!H->N_4R!H->N",
    kinetics = ArrheniusBM(A=(4.0435e+11,'s^-1'), n=1.01704, w0=(559.5,'kJ/mol'), E0=(142.636,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_N-2R!H->N_4R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_4R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N",
    kinetics = ArrheniusBM(A=(1.65946e+44,'s^-1'), n=-8.39883, w0=(707,'kJ/mol'), E0=(370.266,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.44211727175528065, var=494.6823313407436, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N
    Total Standard Deviation in ln(k): 45.69907291505201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 45.69907291505201""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 45.69907291505201
""",
)

entry(
    index = 18,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_4R!H->N",
    kinetics = ArrheniusBM(A=(3.81632e+14,'s^-1'), n=-0.222789, w0=(559.5,'kJ/mol'), E0=(144.22,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_4R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_4R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N",
    kinetics = ArrheniusBM(A=(9.74165e-54,'s^-1'), n=19.1931, w0=(676.333,'kJ/mol'), E0=(7.95345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9980233105294725, var=51.237958002572476, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N
    Total Standard Deviation in ln(k): 19.370191949729055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 19.370191949729055""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 19.370191949729055
""",
)

entry(
    index = 20,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N",
    kinetics = ArrheniusBM(A=(3.754e+11,'s^-1'), n=0.319319, w0=(707,'kJ/mol'), E0=(164.547,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19876961880455732, var=20.67775575197927, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N
    Total Standard Deviation in ln(k): 9.61551295344837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 9.61551295344837""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 9.61551295344837
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N",
    kinetics = ArrheniusBM(A=(1.34655e-117,'s^-1'), n=36.8067, w0=(674.222,'kJ/mol'), E0=(-13.8838,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.0200376013094177, var=119.96686794453268, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N',), comment="""BM rule fitted to 18 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N
    Total Standard Deviation in ln(k): 29.54577474934978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 29.54577474934978""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 29.54577474934978
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.79369e+54,'s^-1'), n=-19.3634, w0=(2471.05,'kJ/mol'), E0=(1235.52,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.85085e+52,'s^-1'), n=-20.5577, w0=(2842.45,'kJ/mol'), E0=(1421.22,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.63589e-48,'s^-1'), n=16.7171, w0=(1173.31,'kJ/mol'), E0=(561.156,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.778472819007242, var=137.28418155539063, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 35.495359737919465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 35.495359737919465""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 35.495359737919465
""",
)

entry(
    index = 25,
    label = "Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.83559e+21,'s^-1'), n=-1.90722, w0=(809.025,'kJ/mol'), E0=(397.639,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21168411380691074, var=201.58053604849252, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 28.994909905639062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 28.994909905639062""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 28.994909905639062
""",
)

entry(
    index = 26,
    label = "Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.1761e+10,'s^-1'), n=0.996245, w0=(784.54,'kJ/mol'), E0=(403.704,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.6259e+11,'s^-1'), n=1.19107, w0=(707,'kJ/mol'), E0=(254.322,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.23586e+11,'s^-1'), n=1.27308, w0=(707,'kJ/mol'), E0=(193.538,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.13064e-61,'s^-1'), n=21.4292, w0=(661,'kJ/mol'), E0=(16.9337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6070515015805953, var=806.3758312429231, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R
    Total Standard Deviation in ln(k): 58.45323068754681"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 58.45323068754681""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 58.45323068754681
""",
)

entry(
    index = 30,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing",
    kinetics = ArrheniusBM(A=(8.06264e+13,'s^-1'), n=0.109934, w0=(661,'kJ/mol'), E0=(263.087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40026689548027, var=87.91034394741766, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing
    Total Standard Deviation in ln(k): 19.80219528377921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing
Total Standard Deviation in ln(k): 19.80219528377921""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing
Total Standard Deviation in ln(k): 19.80219528377921
""",
)

entry(
    index = 31,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing",
    kinetics = ArrheniusBM(A=(6.58751e+08,'s^-1'), n=1.38337, w0=(707,'kJ/mol'), E0=(163.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31909178710756547, var=56.51199635684979, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing
    Total Standard Deviation in ln(k): 15.872226113046763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing
Total Standard Deviation in ln(k): 15.872226113046763""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing
Total Standard Deviation in ln(k): 15.872226113046763
""",
)

entry(
    index = 32,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N",
    kinetics = ArrheniusBM(A=(1.48357e+12,'s^-1'), n=0.181296, w0=(707,'kJ/mol'), E0=(188.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19549948898846134, var=18.267748324796955, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
    Total Standard Deviation in ln(k): 9.059600143716354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
Total Standard Deviation in ln(k): 9.059600143716354""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
Total Standard Deviation in ln(k): 9.059600143716354
""",
)

entry(
    index = 33,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(7.47585e+10,'s^-1'), n=0.487145, w0=(707,'kJ/mol'), E0=(139.835,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22804644275645652, var=23.772021230970815, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
    Total Standard Deviation in ln(k): 10.34737957947134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 10.34737957947134""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 10.34737957947134
""",
)

entry(
    index = 34,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C",
    kinetics = ArrheniusBM(A=(3.65134e-119,'s^-1'), n=37.2359, w0=(738.148,'kJ/mol'), E0=(-14.9908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.156142886394913, var=117.352706073496, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C
    Total Standard Deviation in ln(k): 29.64719289028058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C
Total Standard Deviation in ln(k): 29.64719289028058""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C
Total Standard Deviation in ln(k): 29.64719289028058
""",
)

entry(
    index = 35,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C",
    kinetics = ArrheniusBM(A=(282040,'s^-1'), n=2.28544, w0=(621.667,'kJ/mol'), E0=(234.225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15677459581544367, var=45.16091411476698, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C
    Total Standard Deviation in ln(k): 13.866100744480862"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 13.866100744480862""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 13.866100744480862
""",
)

entry(
    index = 36,
    label = "Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(2.11e+09,'s^-1'), n=0.46, w0=(1116.85,'kJ/mol'), E0=(754.225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.075e+09,'s^-1'), n=0.64, w0=(1229.76,'kJ/mol'), E0=(842.538,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_3R!H->N",
    kinetics = ArrheniusBM(A=(1.04679e+11,'s^-1'), n=1.26667, w0=(789.904,'kJ/mol'), E0=(334.127,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_N-3R!H->N",
    kinetics = ArrheniusBM(A=(1.37586e+09,'s^-1'), n=1.6158, w0=(828.147,'kJ/mol'), E0=(401.86,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_N-3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R_2N-inRing",
    kinetics = ArrheniusBM(A=(3.54394e+12,'s^-1'), n=0.452411, w0=(615,'kJ/mol'), E0=(336.068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R_2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R_2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R_N-2N-inRing",
    kinetics = ArrheniusBM(A=(3.57015e+11,'s^-1'), n=0.576299, w0=(707,'kJ/mol'), E0=(152.637,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R_N-2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R_N-2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N",
    kinetics = ArrheniusBM(A=(5.66856e+16,'s^-1'), n=-0.814872, w0=(615,'kJ/mol'), E0=(311.721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3842118872536077, var=56.559371281125905, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N
    Total Standard Deviation in ln(k): 16.042160049178467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N
Total Standard Deviation in ln(k): 16.042160049178467""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N
Total Standard Deviation in ln(k): 16.042160049178467
""",
)

entry(
    index = 43,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N",
    kinetics = ArrheniusBM(A=(3.85265e+20,'s^-1'), n=-1.69467, w0=(707,'kJ/mol'), E0=(239.372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5340962056458491, var=72.11369728605713, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N
    Total Standard Deviation in ln(k): 18.36611725691921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N
Total Standard Deviation in ln(k): 18.36611725691921""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N
Total Standard Deviation in ln(k): 18.36611725691921
""",
)

entry(
    index = 44,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_5R!H->N",
    kinetics = ArrheniusBM(A=(2.70206e+10,'s^-1'), n=0.860168, w0=(707,'kJ/mol'), E0=(186.64,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24949252742356914, var=32.25929115847382, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_5R!H->N
    Total Standard Deviation in ln(k): 12.013212246091815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_5R!H->N
Total Standard Deviation in ln(k): 12.013212246091815""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_5R!H->N
Total Standard Deviation in ln(k): 12.013212246091815
""",
)

entry(
    index = 45,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(1.09588e+09,'s^-1'), n=1.44217, w0=(707,'kJ/mol'), E0=(127.072,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_N-5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_N-5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.74216e+12,'s^-1'), n=0.0183475, w0=(707,'kJ/mol'), E0=(176.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.74444e+12,'s^-1'), n=-0.195371, w0=(707,'kJ/mol'), E0=(155.613,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R",
    kinetics = ArrheniusBM(A=(2.0881e-144,'s^-1'), n=43.5265, w0=(980.516,'kJ/mol'), E0=(-81.2332,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6092974270115137, var=1067.4060415599124, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R
    Total Standard Deviation in ln(k): 69.54052263328794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R
Total Standard Deviation in ln(k): 69.54052263328794""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R
Total Standard Deviation in ln(k): 69.54052263328794
""",
)

entry(
    index = 49,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C",
    kinetics = ArrheniusBM(A=(1.17751e-124,'s^-1'), n=38.983, w0=(726.864,'kJ/mol'), E0=(-36.2329,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.4177094224205504, var=180.94057923863284, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C
    Total Standard Deviation in ln(k): 35.55373411876186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C
Total Standard Deviation in ln(k): 35.55373411876186""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C
Total Standard Deviation in ln(k): 35.55373411876186
""",
)

entry(
    index = 50,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C",
    kinetics = ArrheniusBM(A=(2.33181e+12,'s^-1'), n=0.0958976, w0=(700.5,'kJ/mol'), E0=(304.977,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5611732263872631, var=121.35063546726235, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C
    Total Standard Deviation in ln(k): 23.493997137488186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C
Total Standard Deviation in ln(k): 23.493997137488186""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C
Total Standard Deviation in ln(k): 23.493997137488186
""",
)

entry(
    index = 51,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F",
    kinetics = ArrheniusBM(A=(1.89509e+11,'s^-1'), n=0.691092, w0=(741,'kJ/mol'), E0=(311.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008826311126699286, var=12.921234577307308, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F
    Total Standard Deviation in ln(k): 7.228421189216816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F
Total Standard Deviation in ln(k): 7.228421189216816""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F
Total Standard Deviation in ln(k): 7.228421189216816
""",
)

entry(
    index = 52,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F",
    kinetics = ArrheniusBM(A=(3.51652e+11,'s^-1'), n=0.501279, w0=(562,'kJ/mol'), E0=(218.187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0004855151561837557, var=4.675560224069761, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F
    Total Standard Deviation in ln(k): 4.336067322347818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F
Total Standard Deviation in ln(k): 4.336067322347818""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F
Total Standard Deviation in ln(k): 4.336067322347818
""",
)

entry(
    index = 53,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N_Ext-4BrCClF-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.01986e+12,'s^-1'), n=0.418833, w0=(615,'kJ/mol'), E0=(328.858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N_Ext-4BrCClF-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N_Ext-4BrCClF-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N_Ext-4BrCClF-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N_Ext-4BrCClF-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N_Ext-4BrCClF-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.78669e+12,'s^-1'), n=0.204119, w0=(615,'kJ/mol'), E0=(273.65,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N_Ext-4BrCClF-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N_Ext-4BrCClF-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N_Ext-4BrCClF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N_Ext-4BrCClF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N_Ext-4BrCClF-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.16767e+14,'s^-1'), n=-0.000952816, w0=(707,'kJ/mol'), E0=(256.163,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N_Ext-4BrCClF-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N_Ext-4BrCClF-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N_Ext-4BrCClF-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N_Ext-4BrCClF-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.03924e+16,'s^-1'), n=-0.601612, w0=(707,'kJ/mol'), E0=(196.261,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_5R!H->N_Ext-4BrCClF-R",
    kinetics = ArrheniusBM(A=(1.88231e+11,'s^-1'), n=0.661449, w0=(707,'kJ/mol'), E0=(174.499,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_5R!H->N_Ext-4BrCClF-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_5R!H->N_Ext-4BrCClF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_5R!H->N_Ext-4BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing_Ext-4BrCClF-R_5R!H->N_Ext-4BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.7458e+26,'s^-1'), n=-6.55938, w0=(1167.44,'kJ/mol'), E0=(489.769,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(8.67544e+08,'s^-1'), n=1.19995, w0=(793.588,'kJ/mol'), E0=(424.478,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9.97305e-124,'s^-1'), n=38.6249, w0=(710.728,'kJ/mol'), E0=(-39.1433,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.357064565186675, var=274.40677911565723, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 41.64372925318938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 41.64372925318938""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 41.64372925318938
""",
)

entry(
    index = 61,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.28035e+11,'s^-1'), n=-0.015434, w0=(700.5,'kJ/mol'), E0=(274.551,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6207405736219159, var=351.89209664433304, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 39.16604836119208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 39.16604836119208""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 39.16604836119208
""",
)

entry(
    index = 62,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(1.69499e+12,'s^-1'), n=0.570599, w0=(741,'kJ/mol'), E0=(311.809,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(9.28347e+11,'s^-1'), n=0.384754, w0=(562,'kJ/mol'), E0=(218.281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1154591660188996, var=15.400657637498893, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
    Total Standard Deviation in ln(k): 8.157414917229499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 8.157414917229499""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 8.157414917229499
""",
)

entry(
    index = 64,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Br",
    kinetics = ArrheniusBM(A=(2.5058e+11,'s^-1'), n=0.533491, w0=(541,'kJ/mol'), E0=(206.698,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Br",
    kinetics = ArrheniusBM(A=(1.69656e+11,'s^-1'), n=0.593389, w0=(583,'kJ/mol'), E0=(230.439,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(2.39834e-43,'s^-1'), n=15.6472, w0=(808.892,'kJ/mol'), E0=(282.345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.413224139712793, var=151.6362425968821, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C
    Total Standard Deviation in ln(k): 28.23725619810417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 28.23725619810417""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 28.23725619810417
""",
)

entry(
    index = 67,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(1.575e+06,'s^-1'), n=1.45, w0=(700.5,'kJ/mol'), E0=(212.781,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.36187e+16,'s^-1'), n=-1.17746, w0=(700.5,'kJ/mol'), E0=(343.057,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.93207e+11,'s^-1'), n=-0.056024, w0=(700.5,'kJ/mol'), E0=(216.564,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Br",
    kinetics = ArrheniusBM(A=(1.94657e+12,'s^-1'), n=0.28187, w0=(541,'kJ/mol'), E0=(206.892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Br",
    kinetics = ArrheniusBM(A=(1.046e+12,'s^-1'), n=0.380659, w0=(583,'kJ/mol'), E0=(230.604,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.27634e-17,'s^-1'), n=8.17123, w0=(860.57,'kJ/mol'), E0=(386.289,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3040681658067679, var=151.69969300022254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1C-R
    Total Standard Deviation in ln(k): 27.968159292647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1C-R
Total Standard Deviation in ln(k): 27.968159292647""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1C-R
Total Standard Deviation in ln(k): 27.968159292647
""",
)

entry(
    index = 73,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1C-R_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(7.89e+07,'s^-1'), n=1.5, w0=(911.88,'kJ/mol'), E0=(423.493,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1C-R_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1C-R_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1C-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1C-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

