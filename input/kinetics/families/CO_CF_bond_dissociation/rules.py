#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6.8373e+11,'s^-1'), n=0.118327, w0=(860.82,'kJ/mol'), E0=(266.191,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6262932215868212, var=133.4405609258091, Tref=1000.0, N=25, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 25 training reactions at node Root
    Total Standard Deviation in ln(k): 24.73159408764215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 24.73159408764215""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 24.73159408764215
""",
)

entry(
    index = 2,
    label = "Root_5R->H",
    kinetics = ArrheniusBM(A=(3.62287e+07,'s^-1'), n=1.50114, w0=(842.214,'kJ/mol'), E0=(352.704,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6636434747035178, var=22.396548094042007, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_5R->H',), comment="""BM rule fitted to 7 training reactions at node Root_5R->H
    Total Standard Deviation in ln(k): 11.154852942634747"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_5R->H
Total Standard Deviation in ln(k): 11.154852942634747""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_5R->H
Total Standard Deviation in ln(k): 11.154852942634747
""",
)

entry(
    index = 3,
    label = "Root_N-5R->H",
    kinetics = ArrheniusBM(A=(1.73785e+13,'s^-1'), n=-0.336882, w0=(868.056,'kJ/mol'), E0=(237.208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6117380079102149, var=120.39018177811357, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-5R->H',), comment="""BM rule fitted to 18 training reactions at node Root_N-5R->H
    Total Standard Deviation in ln(k): 23.53347655836386"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-5R->H
Total Standard Deviation in ln(k): 23.53347655836386""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-5R->H
Total Standard Deviation in ln(k): 23.53347655836386
""",
)

entry(
    index = 4,
    label = "Root_5R->H_4F1sH->H",
    kinetics = ArrheniusBM(A=(5.55165e+06,'s^-1'), n=1.68236, w0=(810.5,'kJ/mol'), E0=(368.428,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6318524864572626, var=1.3979865024010873, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5R->H_4F1sH->H',), comment="""BM rule fitted to 4 training reactions at node Root_5R->H_4F1sH->H
    Total Standard Deviation in ln(k): 3.957897235130205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5R->H_4F1sH->H
Total Standard Deviation in ln(k): 3.957897235130205""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5R->H_4F1sH->H
Total Standard Deviation in ln(k): 3.957897235130205
""",
)

entry(
    index = 5,
    label = "Root_5R->H_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(2.77058e+10,'s^-1'), n=0.779061, w0=(884.5,'kJ/mol'), E0=(324.483,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7540811258035519, var=4.964023801992417, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5R->H_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_5R->H_N-4F1sH->H
    Total Standard Deviation in ln(k): 6.361243854628342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5R->H_N-4F1sH->H
Total Standard Deviation in ln(k): 6.361243854628342""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5R->H_N-4F1sH->H
Total Standard Deviation in ln(k): 6.361243854628342
""",
)

entry(
    index = 6,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.99315e+14,'s^-1'), n=-0.815183, w0=(864.767,'kJ/mol'), E0=(224.015,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5840594507901763, var=120.46181197081468, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 23.470475235174707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 23.470475235174707""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 23.470475235174707
""",
)

entry(
    index = 7,
    label = "Root_N-5R->H_N-5BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.14314e+08,'s^-1'), n=1.03129, w0=(884.5,'kJ/mol'), E0=(311.92,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.832349500019348, var=1.3762494074660754, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->H_N-5BrCClFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 4.443158430747474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.443158430747474""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.443158430747474
""",
)

entry(
    index = 8,
    label = "Root_5R->H_4F1sH->H_Ext-3C-R_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(2.28157e+07,'s^-1'), n=1.55668, w0=(810.5,'kJ/mol'), E0=(373.816,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4038254360614921, var=8.795753473319063, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5R->H_4F1sH->H_Ext-3C-R_Sp-6R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 6.9602070070829445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 6.9602070070829445""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 6.9602070070829445
""",
)

entry(
    index = 9,
    label = "Root_5R->H_4F1sH->H_Ext-3C-R_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(1.1183e+06,'s^-1'), n=1.83156, w0=(810.5,'kJ/mol'), E0=(362.82,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8565140220461873, var=0.2651129965466199, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5R->H_4F1sH->H_Ext-3C-R_N-Sp-6R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 3.1842658260295265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 3.1842658260295265""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 3.1842658260295265
""",
)

entry(
    index = 10,
    label = "Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(5.8714e+09,'s^-1'), n=0.800009, w0=(884.5,'kJ/mol'), E0=(318.904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4906514378330778, var=0.2763425786510259, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 2.286647634910217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C
Total Standard Deviation in ln(k): 2.286647634910217""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C
Total Standard Deviation in ln(k): 2.286647634910217
""",
)

entry(
    index = 11,
    label = "Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.19667e+11,'s^-1'), n=0.77, w0=(884.5,'kJ/mol'), E0=(329.989,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.9357e+19,'s^-1'), n=-2.16371, w0=(869.7,'kJ/mol'), E0=(228.681,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5408134020472531, var=187.43041567337696, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 28.804699011536705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 28.804699011536705""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 28.804699011536705
""",
)

entry(
    index = 13,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.06441e+06,'s^-1'), n=1.81097, w0=(810.5,'kJ/mol'), E0=(176.912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6437687050196552, var=0.345222696442125, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_4F1sH->H
    Total Standard Deviation in ln(k): 2.795404529704455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_4F1sH->H
Total Standard Deviation in ln(k): 2.795404529704455""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_4F1sH->H
Total Standard Deviation in ln(k): 2.795404529704455
""",
)

entry(
    index = 14,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(2.26858e+08,'s^-1'), n=1.05732, w0=(884.5,'kJ/mol'), E0=(247.584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7836409303513345, var=1.888831849632878, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 4.724150285616353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.724150285616353""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.724150285616353
""",
)

entry(
    index = 15,
    label = "Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.40627e+08,'s^-1'), n=1.04533, w0=(884.5,'kJ/mol'), E0=(303.364,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9696754826640495, var=0.16913808042905815, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 3.260845932988073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C
Total Standard Deviation in ln(k): 3.260845932988073""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C
Total Standard Deviation in ln(k): 3.260845932988073
""",
)

entry(
    index = 16,
    label = "Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(5.66667e+08,'s^-1'), n=1.16, w0=(884.5,'kJ/mol'), E0=(327.64,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_5R->H_4F1sH->H_Ext-3C-R_Sp-6R!H-3C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.66e+07,'s^-1'), n=1.5, w0=(810.5,'kJ/mol'), E0=(376.399,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->H_4F1sH->H_Ext-3C-R_Sp-6R!H-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_Sp-6R!H-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_Sp-6R!H-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_Sp-6R!H-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_5R->H_4F1sH->H_Ext-3C-R_N-Sp-6R!H-3C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.895e+06,'s^-1'), n=1.63, w0=(810.5,'kJ/mol'), E0=(362.612,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->H_4F1sH->H_Ext-3C-R_N-Sp-6R!H-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_N-Sp-6R!H-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_N-Sp-6R!H-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->H_4F1sH->H_Ext-3C-R_N-Sp-6R!H-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.9e+09,'s^-1'), n=0.8, w0=(884.5,'kJ/mol'), E0=(318.928,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.49e+09,'s^-1'), n=0.79, w0=(884.5,'kJ/mol'), E0=(314.352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->H_N-4F1sH->H_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.16197e+08,'s^-1'), n=1.10594, w0=(863.357,'kJ/mol'), E0=(261.948,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0857877387652644, var=29.745034904642488, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.149173502694422"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O
Total Standard Deviation in ln(k): 11.149173502694422""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O
Total Standard Deviation in ln(k): 11.149173502694422
""",
)

entry(
    index = 22,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(9.75603e+11,'s^-1'), n=-0.0272617, w0=(884.5,'kJ/mol'), E0=(59.6303,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7708270830500455, var=10.938097420462, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 8.566970607315517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O
Total Standard Deviation in ln(k): 8.566970607315517""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O
Total Standard Deviation in ln(k): 8.566970607315517
""",
)

entry(
    index = 23,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_4F1sH->H_Ext-2C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(560000,'s^-1'), n=1.87, w0=(810.5,'kJ/mol'), E0=(176.482,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_4F1sH->H_Ext-2C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_4F1sH->H_Ext-2C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_4F1sH->H_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_4F1sH->H_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.16437e+08,'s^-1'), n=0.998649, w0=(884.5,'kJ/mol'), E0=(250.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8732690086111938, var=0.519962773234154, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 3.6397265133853915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 3.6397265133853915""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 3.6397265133853915
""",
)

entry(
    index = 25,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(8.1e+07,'s^-1'), n=1.22, w0=(884.5,'kJ/mol'), E0=(240.868,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.77e+08,'s^-1'), n=1.06, w0=(884.5,'kJ/mol'), E0=(305.758,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.65e+08,'s^-1'), n=1.02, w0=(884.5,'kJ/mol'), E0=(301.059,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_N-5BrCClFINOPSSi->C_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.19708e+06,'s^-1'), n=1.8254, w0=(810.5,'kJ/mol'), E0=(306.197,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4016148869920091, var=0.0065606720497902666, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_4F1sH->H
    Total Standard Deviation in ln(k): 1.1714621134977619"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_4F1sH->H
Total Standard Deviation in ln(k): 1.1714621134977619""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_4F1sH->H
Total Standard Deviation in ln(k): 1.1714621134977619
""",
)

entry(
    index = 29,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(1.91691e+08,'s^-1'), n=0.983593, w0=(884.5,'kJ/mol'), E0=(242.794,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2651933318231002, var=28.981020078752778, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H
    Total Standard Deviation in ln(k): 11.458610285014414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H
Total Standard Deviation in ln(k): 11.458610285014414""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H
Total Standard Deviation in ln(k): 11.458610285014414
""",
)

entry(
    index = 30,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.30133e+12,'s^-1'), n=-0.175813, w0=(884.5,'kJ/mol'), E0=(43.7231,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1915726154724149, var=3.830979452375602, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 6.917746560806228"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 6.917746560806228""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 6.917746560806228
""",
)

entry(
    index = 31,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.4e+06,'s^-1'), n=1.62, w0=(884.5,'kJ/mol'), E0=(74.1717,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.63e+08,'s^-1'), n=1.07, w0=(884.5,'kJ/mol'), E0=(251.413,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(7.65e+08,'s^-1'), n=0.9, w0=(884.5,'kJ/mol'), E0=(250.308,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_N-4F1sH->H_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_4F1sH->H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.865e+06,'s^-1'), n=1.71, w0=(810.5,'kJ/mol'), E0=(302.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_4F1sH->H_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_4F1sH->H_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_4F1sH->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_4F1sH->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0",
    kinetics = ArrheniusBM(A=(7.67737e+10,'s^-1'), n=0.312004, w0=(884.5,'kJ/mol'), E0=(228.515,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21091945439183424, var=1.8152522095282693, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0
    Total Standard Deviation in ln(k): 3.2309539270328806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0
Total Standard Deviation in ln(k): 3.2309539270328806""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0
Total Standard Deviation in ln(k): 3.2309539270328806
""",
)

entry(
    index = 36,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0",
    kinetics = ArrheniusBM(A=(1442.69,'s^-1'), n=2.34038, w0=(884.5,'kJ/mol'), E0=(261.174,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.316788840815947, var=0.13412667554010754, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0
    Total Standard Deviation in ln(k): 1.5301521815359753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0
Total Standard Deviation in ln(k): 1.5301521815359753""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0
Total Standard Deviation in ln(k): 1.5301521815359753
""",
)

entry(
    index = 37,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.93633e+08,'s^-1'), n=0.921903, w0=(884.5,'kJ/mol'), E0=(15.6461,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(3.41184e+09,'s^-1'), n=0.704563, w0=(884.5,'kJ/mol'), E0=(7.34871,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_N-6R!H->O_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.58553e+11,'s^-1'), n=0.0485841, w0=(884.5,'kJ/mol'), E0=(223.015,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.45036002431623506, var=1.241589883661321, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.3653670337096813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.3653670337096813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.3653670337096813
""",
)

entry(
    index = 40,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.23333e+10,'s^-1'), n=0.42, w0=(884.5,'kJ/mol'), E0=(243.199,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C",
    kinetics = ArrheniusBM(A=(5066.67,'s^-1'), n=2.17, w0=(884.5,'kJ/mol'), E0=(262.594,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(413.333,'s^-1'), n=2.51, w0=(884.5,'kJ/mol'), E0=(259.761,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_N-3C-u0_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.235e+11,'s^-1'), n=0.12, w0=(884.5,'kJ/mol'), E0=(224.37,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.08e+12,'s^-1'), n=-0.04, w0=(884.5,'kJ/mol'), E0=(221.809,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->H_5BrCClFINOPSSi->C_Ext-3C-R_6R!H->O_N-4F1sH->H_3C-u0_Ext-5C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

