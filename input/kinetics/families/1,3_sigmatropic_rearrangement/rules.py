#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.56124e-80,'s^-1'), n=26.4474, w0=(671.075,'kJ/mol'), E0=(54.882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7584954515246072, var=273.1213865641827, Tref=1000.0, N=40, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 40 training reactions at node Root
    Total Standard Deviation in ln(k): 37.549353106460295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root
Total Standard Deviation in ln(k): 37.549353106460295""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root
Total Standard Deviation in ln(k): 37.549353106460295
""",
)

entry(
    index = 2,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.50189e+32,'s^-1'), n=-4.88331, w0=(678.808,'kJ/mol'), E0=(347.064,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1532175688965556, var=187.3965209762362, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 27.828358382431336"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 27.828358382431336""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 27.828358382431336
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(2.37381e-99,'s^-1'), n=31.794, w0=(675.328,'kJ/mol'), E0=(-40.6568,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.04690964858334, var=252.71001065638325, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 32 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 37.011972647398885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 37.011972647398885""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 37.011972647398885
""",
)

entry(
    index = 4,
    label = "Root_1R!H-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(5.55262e+26,'s^-1'), n=-3.27993, w0=(771.973,'kJ/mol'), E0=(375.475,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.035344346008596754, var=90.46819787132577, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 19.15679680113787"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.15679680113787""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.15679680113787
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
    kinetics = ArrheniusBM(A=(5.80983e-50,'s^-1'), n=18.1064, w0=(664.65,'kJ/mol'), E0=(3.28872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8995846896262647, var=59.052929501906824, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 20.178393768766103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 20.178393768766103""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 20.178393768766103
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(6.80387e-118,'s^-1'), n=36.9375, w0=(680.182,'kJ/mol'), E0=(-58.3415,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.790005887371075, var=172.4176548949186, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 33.333821027715345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 33.333821027715345""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 33.333821027715345
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.04965e+22,'s^-1'), n=-1.94535, w0=(798.027,'kJ/mol'), E0=(383.84,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0489760338000236, var=81.08172362490973, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 18.17477066418039"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 18.17477066418039""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 18.17477066418039
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
    kinetics = ArrheniusBM(A=(1.65946e+44,'s^-1'), n=-8.39883, w0=(707,'kJ/mol'), E0=(370.266,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4421174995674848, var=494.682326699365, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
    Total Standard Deviation in ln(k): 45.69907327826899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 45.69907327826899""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 45.69907327826899
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C",
    kinetics = ArrheniusBM(A=(9.74163e-54,'s^-1'), n=19.1931, w0=(676.333,'kJ/mol'), E0=(7.95422,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9980233056402905, var=51.237957574276315, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
    Total Standard Deviation in ln(k): 19.37019187746899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 19.37019187746899""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 19.37019187746899
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
    kinetics = ArrheniusBM(A=(3.75382e+11,'s^-1'), n=0.319325, w0=(707,'kJ/mol'), E0=(164.547,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19877155331695595, var=20.6777406685249, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N
    Total Standard Deviation in ln(k): 9.615514489150675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 9.615514489150675""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 9.615514489150675
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N",
    kinetics = ArrheniusBM(A=(1.34655e-117,'s^-1'), n=36.8067, w0=(674.222,'kJ/mol'), E0=(-13.8838,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.0200378217624, var=119.9668724307735, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N
    Total Standard Deviation in ln(k): 29.5457757138139"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 29.5457757138139""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 29.5457757138139
""",
)

entry(
    index = 16,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.83548e+21,'s^-1'), n=-1.90721, w0=(809.025,'kJ/mol'), E0=(397.639,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2116841138069057, var=201.5805360484876, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 28.994909905638696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.994909905638696""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.994909905638696
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
    kinetics = ArrheniusBM(A=(1.13064e-61,'s^-1'), n=21.4292, w0=(661,'kJ/mol'), E0=(16.9342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6070515015805993, var=806.3758312429169, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 58.45323068754661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 58.45323068754661""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 58.45323068754661
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing",
    kinetics = ArrheniusBM(A=(8.05577e+13,'s^-1'), n=0.110042, w0=(661,'kJ/mol'), E0=(263.086,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40026725127477175, var=87.91033456613418, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing
    Total Standard Deviation in ln(k): 19.802195174808354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing
Total Standard Deviation in ln(k): 19.802195174808354""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing
Total Standard Deviation in ln(k): 19.802195174808354
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing",
    kinetics = ArrheniusBM(A=(6.58705e+08,'s^-1'), n=1.38338, w0=(707,'kJ/mol'), E0=(163.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3190919895165524, var=56.511995741732655, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing
    Total Standard Deviation in ln(k): 15.872226539593054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing
Total Standard Deviation in ln(k): 15.872226539593054""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing
Total Standard Deviation in ln(k): 15.872226539593054
""",
)

entry(
    index = 23,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N",
    kinetics = ArrheniusBM(A=(1.48345e+12,'s^-1'), n=0.181306, w0=(707,'kJ/mol'), E0=(188.929,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1954994889884606, var=18.267748324796194, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
    Total Standard Deviation in ln(k): 9.059600143716175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
Total Standard Deviation in ln(k): 9.059600143716175""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
Total Standard Deviation in ln(k): 9.059600143716175
""",
)

entry(
    index = 24,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(7.47639e+10,'s^-1'), n=0.487135, w0=(707,'kJ/mol'), E0=(139.835,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22804644275646435, var=23.772021230970495, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
    Total Standard Deviation in ln(k): 10.347379579471294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 10.347379579471294""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 10.347379579471294
""",
)

entry(
    index = 25,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C",
    kinetics = ArrheniusBM(A=(3.65139e-119,'s^-1'), n=37.2359, w0=(738.148,'kJ/mol'), E0=(-14.9908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.156142753318919, var=117.35270322926614, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C
    Total Standard Deviation in ln(k): 29.647192292743483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C
Total Standard Deviation in ln(k): 29.647192292743483""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C
Total Standard Deviation in ln(k): 29.647192292743483
""",
)

entry(
    index = 26,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C",
    kinetics = ArrheniusBM(A=(282038,'s^-1'), n=2.28544, w0=(621.667,'kJ/mol'), E0=(234.225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1567746340542229, var=45.16091447499031, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C
    Total Standard Deviation in ln(k): 13.866100894288273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 13.866100894288273""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 13.866100894288273
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
    kinetics = ArrheniusBM(A=(5.66863e+16,'s^-1'), n=-0.814873, w0=(615,'kJ/mol'), E0=(311.721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3842118872535991, var=56.559371281126076, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N
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
    kinetics = ArrheniusBM(A=(3.85272e+20,'s^-1'), n=-1.69467, w0=(707,'kJ/mol'), E0=(239.372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5340962056458471, var=72.1136972860565, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N
    Total Standard Deviation in ln(k): 18.366117256919132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N
Total Standard Deviation in ln(k): 18.366117256919132""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N
Total Standard Deviation in ln(k): 18.366117256919132
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
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R",
    kinetics = ArrheniusBM(A=(2.0881e-144,'s^-1'), n=43.5265, w0=(980.516,'kJ/mol'), E0=(-81.2332,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.609297427011501, var=1067.4060415599013, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R
    Total Standard Deviation in ln(k): 69.54052263328758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R
Total Standard Deviation in ln(k): 69.54052263328758""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R
Total Standard Deviation in ln(k): 69.54052263328758
""",
)

entry(
    index = 38,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C",
    kinetics = ArrheniusBM(A=(1.1775e-124,'s^-1'), n=38.983, w0=(726.864,'kJ/mol'), E0=(-36.2329,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.4177098787380644, var=180.9405715928609, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C
    Total Standard Deviation in ln(k): 35.553734695543504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C
Total Standard Deviation in ln(k): 35.553734695543504""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C
Total Standard Deviation in ln(k): 35.553734695543504
""",
)

entry(
    index = 39,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C",
    kinetics = ArrheniusBM(A=(2.33466e+12,'s^-1'), n=0.095744, w0=(700.5,'kJ/mol'), E0=(304.978,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5611924834386482, var=121.35095318286946, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C
    Total Standard Deviation in ln(k): 23.49407443178242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C
Total Standard Deviation in ln(k): 23.49407443178242""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C
Total Standard Deviation in ln(k): 23.49407443178242
""",
)

entry(
    index = 40,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F",
    kinetics = ArrheniusBM(A=(1.89518e+11,'s^-1'), n=0.691086, w0=(741,'kJ/mol'), E0=(311.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008826311126719081, var=12.92123457730788, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F
    Total Standard Deviation in ln(k): 7.228421189217026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F
Total Standard Deviation in ln(k): 7.228421189217026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F
Total Standard Deviation in ln(k): 7.228421189217026
""",
)

entry(
    index = 41,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F",
    kinetics = ArrheniusBM(A=(3.51667e+11,'s^-1'), n=0.501273, w0=(562,'kJ/mol'), E0=(218.187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00048550687470625005, var=4.6755600104741335, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F
    Total Standard Deviation in ln(k): 4.336067202524735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F
Total Standard Deviation in ln(k): 4.336067202524735""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F
Total Standard Deviation in ln(k): 4.336067202524735
""",
)

entry(
    index = 42,
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
    index = 43,
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
    index = 44,
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
    index = 45,
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
    index = 46,
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
    index = 47,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.7458e+26,'s^-1'), n=-6.55938, w0=(1167.44,'kJ/mol'), E0=(489.769,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(8.67544e+08,'s^-1'), n=1.19995, w0=(793.588,'kJ/mol'), E0=(424.478,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9.97305e-124,'s^-1'), n=38.6249, w0=(710.728,'kJ/mol'), E0=(-39.1433,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.357064565186675, var=274.40677911565723, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 41.64372925318938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 41.64372925318938""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 41.64372925318938
""",
)

entry(
    index = 50,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.21122e+11,'s^-1'), n=-0.0143805, w0=(700.5,'kJ/mol'), E0=(274.543,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6207405736219249, var=351.89209664433315, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 39.16604836119211"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 39.16604836119211""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 39.16604836119211
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(1.69499e+12,'s^-1'), n=0.570599, w0=(741,'kJ/mol'), E0=(311.809,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(9.28368e+11,'s^-1'), n=0.384751, w0=(562,'kJ/mol'), E0=(218.281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11545916601888881, var=15.400657637499883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
    Total Standard Deviation in ln(k): 8.157414917229724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 8.157414917229724""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 8.157414917229724
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.69656e+11,'s^-1'), n=0.593389, w0=(583,'kJ/mol'), E0=(230.439,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Cl",
    kinetics = ArrheniusBM(A=(2.5058e+11,'s^-1'), n=0.533491, w0=(541,'kJ/mol'), E0=(206.698,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(2.39834e-43,'s^-1'), n=15.6472, w0=(808.892,'kJ/mol'), E0=(282.345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.413224139712793, var=151.6362425968821, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C
    Total Standard Deviation in ln(k): 28.23725619810417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 28.23725619810417""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 28.23725619810417
""",
)

entry(
    index = 56,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(1.575e+06,'s^-1'), n=1.45, w0=(700.5,'kJ/mol'), E0=(212.781,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.36187e+16,'s^-1'), n=-1.17746, w0=(700.5,'kJ/mol'), E0=(343.057,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.93207e+11,'s^-1'), n=-0.056024, w0=(700.5,'kJ/mol'), E0=(216.564,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.046e+12,'s^-1'), n=0.380659, w0=(583,'kJ/mol'), E0=(230.604,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.94657e+12,'s^-1'), n=0.28187, w0=(541,'kJ/mol'), E0=(206.892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4.27634e-17,'s^-1'), n=8.17123, w0=(860.57,'kJ/mol'), E0=(386.289,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3040681658067679, var=151.69969300022254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 27.968159292647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R
Total Standard Deviation in ln(k): 27.968159292647""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R
Total Standard Deviation in ln(k): 27.968159292647
""",
)

entry(
    index = 62,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(7.89e+07,'s^-1'), n=1.5, w0=(911.88,'kJ/mol'), E0=(423.493,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

