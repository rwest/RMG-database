#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.33623e+14,'s^-1'), n=-0.233834, w0=(665.882,'kJ/mol'), E0=(276.243,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19657427908502767, var=169.3720167872319, Tref=1000.0, N=34, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 34 training reactions at node Root
    Total Standard Deviation in ln(k): 26.584129888700804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 34 training reactions at node Root
Total Standard Deviation in ln(k): 26.584129888700804""",
    longDesc = 
"""
BM rule fitted to 34 training reactions at node Root
Total Standard Deviation in ln(k): 26.584129888700804
""",
)

entry(
    index = 2,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.50194e+32,'s^-1'), n=-4.88332, w0=(678.808,'kJ/mol'), E0=(347.064,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15321733847087632, var=187.39651970172005, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 27.82835771014872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 27.82835771014872""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 27.82835771014872
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(87145,'s^-1'), n=2.31572, w0=(669.519,'kJ/mol'), E0=(244.011,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19068248330455193, var=187.81408695662492, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 27.953049663000613"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 27.953049663000613""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 27.953049663000613
""",
)

entry(
    index = 4,
    label = "Root_1R!H-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(5.55307e+26,'s^-1'), n=-3.27994, w0=(771.973,'kJ/mol'), E0=(375.475,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03534432864450718, var=90.46819300207822, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 19.156796244363576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.156796244363576""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.156796244363576
""",
)

entry(
    index = 5,
    label = "Root_1R!H-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(3.40265e+41,'s^-1'), n=-7.6107, w0=(670.125,'kJ/mol'), E0=(328.334,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3756868807420218, var=394.2316192042286, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 40.748486686278575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 40.748486686278575""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 40.748486686278575
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(5.80983e-50,'s^-1'), n=18.1064, w0=(664.65,'kJ/mol'), E0=(3.2897,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8995846432443477, var=59.0529284841149, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 20.178393519469225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 20.178393519469225""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 20.178393519469225
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(0.000996159,'s^-1'), n=4.39755, w0=(672.562,'kJ/mol'), E0=(256.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2900542002749794, var=223.3000683837458, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 30.68599309588334"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 30.68599309588334""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 30.68599309588334
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.04969e+22,'s^-1'), n=-1.94535, w0=(798.027,'kJ/mol'), E0=(383.84,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04897568024138421, var=81.08171849206428, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 18.17476920446385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 18.17476920446385""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 18.17476920446385
""",
)

entry(
    index = 9,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.1544e+10,'s^-1'), n=1.34775, w0=(693.81,'kJ/mol'), E0=(271.878,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->N",
    kinetics = ArrheniusBM(A=(4.0435e+11,'s^-1'), n=1.01704, w0=(559.5,'kJ/mol'), E0=(142.636,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N",
    kinetics = ArrheniusBM(A=(1.65946e+44,'s^-1'), n=-8.39883, w0=(707,'kJ/mol'), E0=(370.266,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.44211727175528065, var=494.6823313407436, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
    Total Standard Deviation in ln(k): 45.69907291505201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 45.69907291505201""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 45.69907291505201
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C",
    kinetics = ArrheniusBM(A=(9.74165e-54,'s^-1'), n=19.1931, w0=(676.333,'kJ/mol'), E0=(7.95345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9980233105294725, var=51.237958002572476, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
    Total Standard Deviation in ln(k): 19.370191949729055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 19.370191949729055""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 19.370191949729055
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.81632e+14,'s^-1'), n=-0.222789, w0=(559.5,'kJ/mol'), E0=(144.22,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N",
    kinetics = ArrheniusBM(A=(3.754e+11,'s^-1'), n=0.319319, w0=(707,'kJ/mol'), E0=(164.547,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19876961880455732, var=20.67775575197927, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N
    Total Standard Deviation in ln(k): 9.61551295344837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 9.61551295344837""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 9.61551295344837
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N",
    kinetics = ArrheniusBM(A=(272889,'s^-1'), n=1.9403, w0=(661.083,'kJ/mol'), E0=(329.452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21999143483511654, var=130.52456845394215, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N
    Total Standard Deviation in ln(k): 23.456309183140135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 23.456309183140135""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 23.456309183140135
""",
)

entry(
    index = 16,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.83559e+21,'s^-1'), n=-1.90722, w0=(809.025,'kJ/mol'), E0=(397.639,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21168411380691074, var=201.58053604849252, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 28.994909905639062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.994909905639062""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.994909905639062
""",
)

entry(
    index = 17,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.1761e+10,'s^-1'), n=0.996245, w0=(784.54,'kJ/mol'), E0=(403.704,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.6259e+11,'s^-1'), n=1.19107, w0=(707,'kJ/mol'), E0=(254.322,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.23586e+11,'s^-1'), n=1.27308, w0=(707,'kJ/mol'), E0=(193.538,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.13064e-61,'s^-1'), n=21.4292, w0=(661,'kJ/mol'), E0=(16.9337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6070515015805953, var=806.3758312429231, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 58.45323068754681"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 58.45323068754681""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 58.45323068754681
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing",
    kinetics = ArrheniusBM(A=(8.06264e+13,'s^-1'), n=0.109934, w0=(661,'kJ/mol'), E0=(263.087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40026689548027, var=87.91034394741766, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing
    Total Standard Deviation in ln(k): 19.80219528377921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing
Total Standard Deviation in ln(k): 19.80219528377921""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing
Total Standard Deviation in ln(k): 19.80219528377921
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing",
    kinetics = ArrheniusBM(A=(6.58751e+08,'s^-1'), n=1.38337, w0=(707,'kJ/mol'), E0=(163.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31909178710756547, var=56.51199635684979, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing
    Total Standard Deviation in ln(k): 15.872226113046763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing
Total Standard Deviation in ln(k): 15.872226113046763""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing
Total Standard Deviation in ln(k): 15.872226113046763
""",
)

entry(
    index = 23,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N",
    kinetics = ArrheniusBM(A=(1.48357e+12,'s^-1'), n=0.181296, w0=(707,'kJ/mol'), E0=(188.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19549948898846134, var=18.267748324796955, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
    Total Standard Deviation in ln(k): 9.059600143716354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
Total Standard Deviation in ln(k): 9.059600143716354""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
Total Standard Deviation in ln(k): 9.059600143716354
""",
)

entry(
    index = 24,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(7.47585e+10,'s^-1'), n=0.487145, w0=(707,'kJ/mol'), E0=(139.835,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22804644275645652, var=23.772021230970815, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
    Total Standard Deviation in ln(k): 10.34737957947134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 10.34737957947134""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 10.34737957947134
""",
)

entry(
    index = 25,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C",
    kinetics = ArrheniusBM(A=(39930.9,'s^-1'), n=2.19306, w0=(647.944,'kJ/mol'), E0=(318.567,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3634997342010304, var=271.3861150577344, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C
    Total Standard Deviation in ln(k): 36.45148518840312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C
Total Standard Deviation in ln(k): 36.45148518840312""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C
Total Standard Deviation in ln(k): 36.45148518840312
""",
)

entry(
    index = 26,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C",
    kinetics = ArrheniusBM(A=(3.72753e+06,'s^-1'), n=1.59882, w0=(761.392,'kJ/mol'), E0=(342.647,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23753178363147873, var=428.28346328698507, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C
    Total Standard Deviation in ln(k): 42.084827181918975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C
Total Standard Deviation in ln(k): 42.084827181918975""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C
Total Standard Deviation in ln(k): 42.084827181918975
""",
)

entry(
    index = 27,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N",
    kinetics = ArrheniusBM(A=(1.04679e+11,'s^-1'), n=1.26667, w0=(789.904,'kJ/mol'), E0=(334.127,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N",
    kinetics = ArrheniusBM(A=(1.37586e+09,'s^-1'), n=1.6158, w0=(828.147,'kJ/mol'), E0=(401.86,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing",
    kinetics = ArrheniusBM(A=(3.54394e+12,'s^-1'), n=0.452411, w0=(615,'kJ/mol'), E0=(336.068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing",
    kinetics = ArrheniusBM(A=(3.57015e+11,'s^-1'), n=0.576299, w0=(707,'kJ/mol'), E0=(152.637,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N",
    kinetics = ArrheniusBM(A=(5.66856e+16,'s^-1'), n=-0.814872, w0=(615,'kJ/mol'), E0=(311.721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3842118872536077, var=56.559371281125905, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N
    Total Standard Deviation in ln(k): 16.042160049178467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N
Total Standard Deviation in ln(k): 16.042160049178467""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N
Total Standard Deviation in ln(k): 16.042160049178467
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N",
    kinetics = ArrheniusBM(A=(3.85265e+20,'s^-1'), n=-1.69467, w0=(707,'kJ/mol'), E0=(239.372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5340962056458491, var=72.11369728605713, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N
    Total Standard Deviation in ln(k): 18.36611725691921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N
Total Standard Deviation in ln(k): 18.36611725691921""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N
Total Standard Deviation in ln(k): 18.36611725691921
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N",
    kinetics = ArrheniusBM(A=(2.70206e+10,'s^-1'), n=0.860168, w0=(707,'kJ/mol'), E0=(186.64,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24949252742356914, var=32.25929115847382, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N
    Total Standard Deviation in ln(k): 12.013212246091815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N
Total Standard Deviation in ln(k): 12.013212246091815""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N
Total Standard Deviation in ln(k): 12.013212246091815
""",
)

entry(
    index = 34,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(1.09588e+09,'s^-1'), n=1.44217, w0=(707,'kJ/mol'), E0=(127.072,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_N-5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_N-5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.74216e+12,'s^-1'), n=0.0183475, w0=(707,'kJ/mol'), E0=(176.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(9.74444e+12,'s^-1'), n=-0.195371, w0=(707,'kJ/mol'), E0=(155.613,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br",
    kinetics = ArrheniusBM(A=(6.98406e+11,'s^-1'), n=0.40768, w0=(541,'kJ/mol'), E0=(206.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00537460245496675, var=0.05576325998056779, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br
    Total Standard Deviation in ln(k): 0.48690709300471446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br
Total Standard Deviation in ln(k): 0.48690709300471446""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br
Total Standard Deviation in ln(k): 0.48690709300471446
""",
)

entry(
    index = 38,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(3.75149e+06,'s^-1'), n=1.61173, w0=(678.5,'kJ/mol'), E0=(330.702,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.016597871824269, var=284.6664196380138, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br
    Total Standard Deviation in ln(k): 36.3782771726843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br
Total Standard Deviation in ln(k): 36.3782771726843""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br
Total Standard Deviation in ln(k): 36.3782771726843
""",
)

entry(
    index = 39,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.68572e+06,'s^-1'), n=1.59991, w0=(752.551,'kJ/mol'), E0=(342.5,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22329445997371744, var=433.4635162770166, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 42.299197963877106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 42.299197963877106""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 42.299197963877106
""",
)

entry(
    index = 40,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.01986e+12,'s^-1'), n=0.418833, w0=(615,'kJ/mol'), E0=(328.858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.78669e+12,'s^-1'), n=0.204119, w0=(615,'kJ/mol'), E0=(273.65,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.16767e+14,'s^-1'), n=-0.000952816, w0=(707,'kJ/mol'), E0=(256.163,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.03924e+16,'s^-1'), n=-0.601612, w0=(707,'kJ/mol'), E0=(196.261,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.88231e+11,'s^-1'), n=0.661449, w0=(707,'kJ/mol'), E0=(174.499,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(1.94657e+12,'s^-1'), n=0.28187, w0=(541,'kJ/mol'), E0=(206.892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl",
    kinetics = ArrheniusBM(A=(4.21261e+11,'s^-1'), n=0.487024, w0=(583,'kJ/mol'), E0=(230.521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005445922515398178, var=0.10372712383065, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl
    Total Standard Deviation in ln(k): 0.6593421453783467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 0.6593421453783467""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 0.6593421453783467
""",
)

entry(
    index = 47,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl",
    kinetics = ArrheniusBM(A=(1.6073e+08,'s^-1'), n=1.12526, w0=(716.7,'kJ/mol'), E0=(341.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5284214240487969, var=319.933282846702, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl
    Total Standard Deviation in ln(k): 37.18574467256937"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 37.18574467256937""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 37.18574467256937
""",
)

entry(
    index = 48,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R_Ext-4R!H-R_6R!H->O",
    kinetics = ArrheniusBM(A=(2.25e+06,'s^-1'), n=1.38, w0=(700.5,'kJ/mol'), E0=(263.923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R_Ext-4R!H-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R_Ext-4R!H-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R_Ext-4R!H-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R_Ext-4R!H-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R_Ext-4R!H-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(7.89e+07,'s^-1'), n=1.5, w0=(911.88,'kJ/mol'), E0=(423.493,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R_Ext-4R!H-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R_Ext-4R!H-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R_Ext-4R!H-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-1R!H-R_Ext-4R!H-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(1.046e+12,'s^-1'), n=0.380659, w0=(583,'kJ/mol'), E0=(230.604,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.65298e+08,'s^-1'), n=1.10294, w0=(714,'kJ/mol'), E0=(342.507,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3411833047740136, var=362.9886532111716, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 39.051980625121004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 39.051980625121004""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 39.051980625121004
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.69499e+12,'s^-1'), n=0.570599, w0=(741,'kJ/mol'), E0=(311.809,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_2CO->C",
    kinetics = ArrheniusBM(A=(2.11883e+10,'s^-1'), n=0.811585, w0=(741,'kJ/mol'), E0=(311.115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C",
    kinetics = ArrheniusBM(A=(1.79937e+08,'s^-1'), n=1.08262, w0=(700.5,'kJ/mol'), E0=(343.761,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17300076357814695, var=416.6948741590578, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C
    Total Standard Deviation in ln(k): 41.35754382180308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C
Total Standard Deviation in ln(k): 41.35754382180308""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C
Total Standard Deviation in ln(k): 41.35754382180308
""",
)

entry(
    index = 55,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C_Ext-4CF-R_6R!H->O",
    kinetics = ArrheniusBM(A=(5.4394e+08,'s^-1'), n=0.631892, w0=(700.5,'kJ/mol'), E0=(265.587,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C_Ext-4CF-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C_Ext-4CF-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C_Ext-4CF-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C_Ext-4CF-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C_Ext-4CF-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(8.67544e+08,'s^-1'), n=1.19995, w0=(793.588,'kJ/mol'), E0=(424.478,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C_Ext-4CF-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C_Ext-4CF-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C_Ext-4CF-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-3C-R_N-2CO->C_Ext-4CF-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

