#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(9.84707e+18,'s^-1'), n=-2.04061, w0=(678.632,'kJ/mol'), E0=(316.62,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4652204762008785, var=341.42078923859253, Tref=1000.0, N=38, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 38 training reactions at node Root
    Total Standard Deviation in ln(k): 38.211539032671936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root
Total Standard Deviation in ln(k): 38.211539032671936""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root
Total Standard Deviation in ln(k): 38.211539032671936
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(4.56541e+19,'s^-1'), n=-1.77876, w0=(665.882,'kJ/mol'), E0=(292.812,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3683048509086131, var=200.38779612616264, Tref=1000.0, N=34, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 34 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 29.304097363974996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 34 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 29.304097363974996""",
    longDesc = 
"""
BM rule fitted to 34 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 29.304097363974996
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(1.29042,'s^-1'), n=1.76653, w0=(787,'kJ/mol'), E0=(359.07,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04893414630375096, var=329.4795823127261, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 36.512044111477984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 36.512044111477984""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 36.512044111477984
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_1C-inRing",
    kinetics = ArrheniusBM(A=(6.08012e+32,'s^-1'), n=-5.05731, w0=(654.062,'kJ/mol'), E0=(348.699,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17329717635728206, var=186.8556005005184, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_1C-inRing
    Total Standard Deviation in ln(k): 27.839173331537225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_1C-inRing
Total Standard Deviation in ln(k): 27.839173331537225""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_1C-inRing
Total Standard Deviation in ln(k): 27.839173331537225
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(2.36797e+13,'s^-1'), n=-0.13948, w0=(669.519,'kJ/mol'), E0=(269.591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.47034739213328014, var=231.95290246948989, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing',), comment="""BM rule fitted to 26 training reactions at node Root_1R!H->C_N-1C-inRing
    Total Standard Deviation in ln(k): 31.71389275841201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R!H->C_N-1C-inRing
Total Standard Deviation in ln(k): 31.71389275841201""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R!H->C_N-1C-inRing
Total Standard Deviation in ln(k): 31.71389275841201
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.82311e-05,'s^-1'), n=1.74066, w0=(787,'kJ/mol'), E0=(358.994,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.061794505990388895, var=85.65765743318448, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 18.709370823988497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 18.709370823988497""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 18.709370823988497
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(302000,'s^-1'), n=1.52, w0=(787,'kJ/mol'), E0=(376.55,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-1R!H->C_Ext-4R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.83e+08,'s^-1'), n=0.97, w0=(787,'kJ/mol'), E0=(351.33,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_1C-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(3.43791e+29,'s^-1'), n=-4.07982, w0=(638,'kJ/mol'), E0=(383.138,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1172795413368034, var=88.81510253100076, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N
    Total Standard Deviation in ln(k): 19.187649401207306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.187649401207306""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.187649401207306
""",
)

entry(
    index = 10,
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
    index = 11,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(5.80983e-50,'s^-1'), n=18.1064, w0=(664.65,'kJ/mol'), E0=(3.28872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8995846896262647, var=59.052929501906824, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N
    Total Standard Deviation in ln(k): 20.178393768766103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N
Total Standard Deviation in ln(k): 20.178393768766103""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N
Total Standard Deviation in ln(k): 20.178393768766103
""",
)

entry(
    index = 12,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(2.07946e+06,'s^-1'), n=1.66073, w0=(672.562,'kJ/mol'), E0=(286.872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6368565555651908, var=293.3910602607359, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N',), comment="""BM rule fitted to 16 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 35.93857154310894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 35.93857154310894""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 35.93857154310894
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.29939e-05,'s^-1'), n=1.42851, w0=(787,'kJ/mol'), E0=(376.858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(0.177613,'s^-1'), n=0.777229, w0=(787,'kJ/mol'), E0=(352.283,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-4R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.02096e+24,'s^-1'), n=-2.59989, w0=(645.667,'kJ/mol'), E0=(390.108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0076656667349708305, var=79.12297201978993, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 17.85159838872314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 17.85159838872314""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 17.85159838872314
""",
)

entry(
    index = 16,
    label = "Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.1544e+10,'s^-1'), n=1.34775, w0=(615,'kJ/mol'), E0=(272.121,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
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
    index = 17,
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
    index = 18,
    label = "Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N",
    kinetics = ArrheniusBM(A=(1.65946e+44,'s^-1'), n=-8.39883, w0=(707,'kJ/mol'), E0=(370.266,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4421174995674848, var=494.682326699365, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N
    Total Standard Deviation in ln(k): 45.69907327826899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 45.69907327826899""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 45.69907327826899
""",
)

entry(
    index = 19,
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
    index = 20,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N",
    kinetics = ArrheniusBM(A=(9.74163e-54,'s^-1'), n=19.1931, w0=(676.333,'kJ/mol'), E0=(7.95422,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9980233056402905, var=51.237957574276315, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N
    Total Standard Deviation in ln(k): 19.37019187746899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 19.37019187746899""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 19.37019187746899
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N",
    kinetics = ArrheniusBM(A=(3.75382e+11,'s^-1'), n=0.319325, w0=(707,'kJ/mol'), E0=(164.547,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19877155331695595, var=20.6777406685249, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N
    Total Standard Deviation in ln(k): 9.615514489150675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 9.615514489150675""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 9.615514489150675
""",
)

entry(
    index = 22,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N",
    kinetics = ArrheniusBM(A=(4.94988e+10,'s^-1'), n=0.340003, w0=(661.083,'kJ/mol'), E0=(352.729,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4314900674047088, var=206.60948173226433, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N',), comment="""BM rule fitted to 12 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N
    Total Standard Deviation in ln(k): 29.900040936279034"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 29.900040936279034""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 29.900040936279034
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.03865e+24,'s^-1'), n=-2.55198, w0=(661,'kJ/mol'), E0=(403.659,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21956710944033583, var=198.92006906735634, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 28.82626446149128"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 28.82626446149128""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 28.82626446149128
""",
)

entry(
    index = 24,
    label = "Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.1761e+10,'s^-1'), n=0.996245, w0=(707,'kJ/mol'), E0=(403.723,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_N-2R!H->N_N-4R!H->N_Ext-1C-R
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
    index = 25,
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
    index = 26,
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
    index = 27,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.13064e-61,'s^-1'), n=21.4292, w0=(661,'kJ/mol'), E0=(16.9342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6070515015805993, var=806.3758312429169, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R
    Total Standard Deviation in ln(k): 58.45323068754661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 58.45323068754661""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 58.45323068754661
""",
)

entry(
    index = 28,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing",
    kinetics = ArrheniusBM(A=(8.05577e+13,'s^-1'), n=0.110042, w0=(661,'kJ/mol'), E0=(263.086,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40026725127477175, var=87.91033456613418, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing
    Total Standard Deviation in ln(k): 19.802195174808354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing
Total Standard Deviation in ln(k): 19.802195174808354""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing
Total Standard Deviation in ln(k): 19.802195174808354
""",
)

entry(
    index = 29,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing",
    kinetics = ArrheniusBM(A=(6.58705e+08,'s^-1'), n=1.38338, w0=(707,'kJ/mol'), E0=(163.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3190919895165524, var=56.511995741732655, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing
    Total Standard Deviation in ln(k): 15.872226539593054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing
Total Standard Deviation in ln(k): 15.872226539593054""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_N-2N-inRing
Total Standard Deviation in ln(k): 15.872226539593054
""",
)

entry(
    index = 30,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N",
    kinetics = ArrheniusBM(A=(1.48345e+12,'s^-1'), n=0.181306, w0=(707,'kJ/mol'), E0=(188.929,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1954994889884606, var=18.267748324796194, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
    Total Standard Deviation in ln(k): 9.059600143716175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
Total Standard Deviation in ln(k): 9.059600143716175""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
Total Standard Deviation in ln(k): 9.059600143716175
""",
)

entry(
    index = 31,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(7.47639e+10,'s^-1'), n=0.487135, w0=(707,'kJ/mol'), E0=(139.835,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22804644275646435, var=23.772021230970495, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
    Total Standard Deviation in ln(k): 10.347379579471294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 10.347379579471294""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 10.347379579471294
""",
)

entry(
    index = 32,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C",
    kinetics = ArrheniusBM(A=(7.37051e+11,'s^-1'), n=-0.0374656, w0=(700.5,'kJ/mol'), E0=(365.493,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10455994812947482, var=209.41373052492023, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C
    Total Standard Deviation in ln(k): 29.273504158238623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C
Total Standard Deviation in ln(k): 29.273504158238623""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C
Total Standard Deviation in ln(k): 29.273504158238623
""",
)

entry(
    index = 33,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C",
    kinetics = ArrheniusBM(A=(282038,'s^-1'), n=2.28544, w0=(621.667,'kJ/mol'), E0=(234.225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1567746340542229, var=45.16091447499031, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C
    Total Standard Deviation in ln(k): 13.866100894288273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 13.866100894288273""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 13.866100894288273
""",
)

entry(
    index = 34,
    label = "Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_3R!H->N",
    kinetics = ArrheniusBM(A=(1.04679e+11,'s^-1'), n=1.26667, w0=(615,'kJ/mol'), E0=(334.785,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_3R!H->N
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
    index = 35,
    label = "Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_N-3R!H->N",
    kinetics = ArrheniusBM(A=(1.37586e+09,'s^-1'), n=1.6158, w0=(707,'kJ/mol'), E0=(401.885,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_1C-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1C-R_N-3R!H->N
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
    index = 36,
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
    index = 37,
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
    index = 38,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N",
    kinetics = ArrheniusBM(A=(5.66863e+16,'s^-1'), n=-0.814873, w0=(615,'kJ/mol'), E0=(311.721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3842118872535991, var=56.559371281126076, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_3R!H->N
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
    index = 39,
    label = "Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N",
    kinetics = ArrheniusBM(A=(3.85272e+20,'s^-1'), n=-1.69467, w0=(707,'kJ/mol'), E0=(239.372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5340962056458471, var=72.1136972860565, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N
    Total Standard Deviation in ln(k): 18.366117256919132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N
Total Standard Deviation in ln(k): 18.366117256919132""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_2R!H->N_N-4R!H->N_2N-inRing_N-3R!H->N
Total Standard Deviation in ln(k): 18.366117256919132
""",
)

entry(
    index = 40,
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
    index = 41,
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
    index = 42,
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
    index = 43,
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
    index = 44,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C",
    kinetics = ArrheniusBM(A=(1.51424e+11,'s^-1'), n=0.278341, w0=(700.5,'kJ/mol'), E0=(364.078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1286543011064775, var=580.6133980789741, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C
    Total Standard Deviation in ln(k): 48.62918961607295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C
Total Standard Deviation in ln(k): 48.62918961607295""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C
Total Standard Deviation in ln(k): 48.62918961607295
""",
)

entry(
    index = 45,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C",
    kinetics = ArrheniusBM(A=(3.57264e+12,'s^-1'), n=-0.352751, w0=(700.5,'kJ/mol'), E0=(366.903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20395697867400203, var=810.2309833797854, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C
    Total Standard Deviation in ln(k): 57.576349832061325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C
Total Standard Deviation in ln(k): 57.576349832061325""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C
Total Standard Deviation in ln(k): 57.576349832061325
""",
)

entry(
    index = 46,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F",
    kinetics = ArrheniusBM(A=(1.89518e+11,'s^-1'), n=0.691086, w0=(741,'kJ/mol'), E0=(311.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008826311126719081, var=12.92123457730788, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F
    Total Standard Deviation in ln(k): 7.228421189217026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F
Total Standard Deviation in ln(k): 7.228421189217026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F
Total Standard Deviation in ln(k): 7.228421189217026
""",
)

entry(
    index = 47,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F",
    kinetics = ArrheniusBM(A=(3.51667e+11,'s^-1'), n=0.501273, w0=(562,'kJ/mol'), E0=(218.187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00048550687470625005, var=4.6755600104741335, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F
    Total Standard Deviation in ln(k): 4.336067202524735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F
Total Standard Deviation in ln(k): 4.336067202524735""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F
Total Standard Deviation in ln(k): 4.336067202524735
""",
)

entry(
    index = 48,
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
    index = 49,
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
    index = 50,
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
    index = 51,
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
    index = 52,
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
    index = 53,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.60128e+11,'s^-1'), n=0.27107, w0=(700.5,'kJ/mol'), E0=(364.024,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11674461868401445, var=587.7914788661078, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 48.89694993426942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 48.89694993426942""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 48.89694993426942
""",
)

entry(
    index = 54,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.75543e+12,'s^-1'), n=-0.360282, w0=(700.5,'kJ/mol'), E0=(366.87,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20335335385667708, var=820.477861948962, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 57.934539045362406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 57.934539045362406""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 57.934539045362406
""",
)

entry(
    index = 55,
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
    index = 56,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(9.28368e+11,'s^-1'), n=0.384751, w0=(562,'kJ/mol'), E0=(218.281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11545916601888881, var=15.400657637499883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
    Total Standard Deviation in ln(k): 8.157414917229724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 8.157414917229724""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 8.157414917229724
""",
)

entry(
    index = 57,
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
    index = 58,
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
    index = 59,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R_Ext-4C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(2.25e+06,'s^-1'), n=1.38, w0=(700.5,'kJ/mol'), E0=(263.923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R_Ext-4C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R_Ext-4C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R_Ext-4C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R_Ext-4C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R_Ext-4C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(7.89e+07,'s^-1'), n=1.5, w0=(700.5,'kJ/mol'), E0=(443.198,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R_Ext-4C-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R_Ext-4C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R_Ext-4C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-1C-R_Ext-4C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R_Ext-4C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(5.4394e+08,'s^-1'), n=0.631892, w0=(700.5,'kJ/mol'), E0=(265.587,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R_Ext-4C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R_Ext-4C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R_Ext-4C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R_Ext-4C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R_Ext-4C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(6.466e+06,'s^-1'), n=1.39897, w0=(700.5,'kJ/mol'), E0=(443.656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R_Ext-4C-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R_Ext-4C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R_Ext-4C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-1C-R_Ext-4C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
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
    index = 64,
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

