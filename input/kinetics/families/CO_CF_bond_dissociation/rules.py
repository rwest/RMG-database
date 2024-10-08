#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.04539e+08,'s^-1'), n=1.2553, w0=(854.9,'kJ/mol'), E0=(286.523,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5246753893448245, var=59.43597879835523, Tref=1000.0, N=20, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 20 training reactions at node Root
    Total Standard Deviation in ln(k): 16.773731456015845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 16.773731456015845""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 16.773731456015845
""",
)

entry(
    index = 2,
    label = "Root_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.05314e+08,'s^-1'), n=1.19522, w0=(854.9,'kJ/mol'), E0=(310.705,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4512855056408595, var=46.223912573205524, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-3C-R',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-3C-R
    Total Standard Deviation in ln(k): 14.76371010081067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-3C-R
Total Standard Deviation in ln(k): 14.76371010081067""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-3C-R
Total Standard Deviation in ln(k): 14.76371010081067
""",
)

entry(
    index = 3,
    label = "Root_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.06441e+06,'s^-1'), n=1.81097, w0=(810.5,'kJ/mol'), E0=(176.912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6437687050196552, var=0.345222696442125, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_4F1sH->H
    Total Standard Deviation in ln(k): 2.795404529704455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4F1sH->H
Total Standard Deviation in ln(k): 2.795404529704455""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4F1sH->H
Total Standard Deviation in ln(k): 2.795404529704455
""",
)

entry(
    index = 4,
    label = "Root_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(2.26858e+08,'s^-1'), n=1.05732, w0=(884.5,'kJ/mol'), E0=(247.584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7836409303513345, var=1.888831849632878, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4F1sH->H
    Total Standard Deviation in ln(k): 4.724150285616353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4F1sH->H
Total Standard Deviation in ln(k): 4.724150285616353""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4F1sH->H
Total Standard Deviation in ln(k): 4.724150285616353
""",
)

entry(
    index = 5,
    label = "Root_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.45367e+08,'s^-1'), n=1.28906, w0=(854.9,'kJ/mol'), E0=(339.607,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7242705449561803, var=18.4022880674646, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 10.419665348328916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 10.419665348328916""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 10.419665348328916
""",
)

entry(
    index = 6,
    label = "Root_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(9.14806e+09,'s^-1'), n=0.631149, w0=(854.9,'kJ/mol'), E0=(262.094,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008875281869050539, var=42.47251991956975, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 13.08734752662318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 13.08734752662318""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 13.08734752662318
""",
)

entry(
    index = 7,
    label = "Root_4F1sH->H_Ext-2C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(560000,'s^-1'), n=1.87, w0=(810.5,'kJ/mol'), E0=(176.482,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4F1sH->H_Ext-2C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4F1sH->H_Ext-2C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4F1sH->H_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4F1sH->H_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.16437e+08,'s^-1'), n=0.998649, w0=(884.5,'kJ/mol'), E0=(250.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8732690086111938, var=0.519962773234154, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
    Total Standard Deviation in ln(k): 3.6397265133853915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
Total Standard Deviation in ln(k): 3.6397265133853915""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
Total Standard Deviation in ln(k): 3.6397265133853915
""",
)

entry(
    index = 9,
    label = "Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(8.1e+07,'s^-1'), n=1.22, w0=(884.5,'kJ/mol'), E0=(240.868,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-3C-R_6R!H->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(5.55165e+06,'s^-1'), n=1.68236, w0=(810.5,'kJ/mol'), E0=(368.428,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6318524864572626, var=1.3979865024010873, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_4F1sH->H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H
    Total Standard Deviation in ln(k): 3.957897235130205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 3.957897235130205""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 3.957897235130205
""",
)

entry(
    index = 11,
    label = "Root_Ext-3C-R_6R!H->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(2.51795e+09,'s^-1'), n=0.944574, w0=(884.5,'kJ/mol'), E0=(316.836,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8010474478141885, var=1.1492917466015615, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-4F1sH->H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 4.161858778139572"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.161858778139572""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.161858778139572
""",
)

entry(
    index = 12,
    label = "Root_Ext-3C-R_N-6R!H->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.19708e+06,'s^-1'), n=1.8254, w0=(810.5,'kJ/mol'), E0=(306.197,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4016148869920091, var=0.0065606720497902666, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_4F1sH->H
    Total Standard Deviation in ln(k): 1.1714621134977619"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 1.1714621134977619""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 1.1714621134977619
""",
)

entry(
    index = 13,
    label = "Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(7.67737e+10,'s^-1'), n=0.312004, w0=(884.5,'kJ/mol'), E0=(228.515,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21091945439183424, var=1.8152522095282693, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 3.2309539270328806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 3.2309539270328806""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 3.2309539270328806
""",
)

entry(
    index = 14,
    label = "Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.63e+08,'s^-1'), n=1.07, w0=(884.5,'kJ/mol'), E0=(251.413,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(7.65e+08,'s^-1'), n=0.9, w0=(884.5,'kJ/mol'), E0=(250.308,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C",
    kinetics = ArrheniusBM(A=(2.28157e+07,'s^-1'), n=1.55668, w0=(810.5,'kJ/mol'), E0=(373.816,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4038254360614921, var=8.795753473319063, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
    Total Standard Deviation in ln(k): 6.9602070070829445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
Total Standard Deviation in ln(k): 6.9602070070829445""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
Total Standard Deviation in ln(k): 6.9602070070829445
""",
)

entry(
    index = 17,
    label = "Root_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C",
    kinetics = ArrheniusBM(A=(1.1183e+06,'s^-1'), n=1.83156, w0=(810.5,'kJ/mol'), E0=(362.82,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8565140220461873, var=0.2651129965466199, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
    Total Standard Deviation in ln(k): 3.1842658260295265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
Total Standard Deviation in ln(k): 3.1842658260295265""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
Total Standard Deviation in ln(k): 3.1842658260295265
""",
)

entry(
    index = 18,
    label = "Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.77058e+10,'s^-1'), n=0.779061, w0=(884.5,'kJ/mol'), E0=(324.483,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7540811764220603, var=4.9640235537909, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
    Total Standard Deviation in ln(k): 6.3612438701461835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.3612438701461835""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.3612438701461835
""",
)

entry(
    index = 19,
    label = "Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.40627e+08,'s^-1'), n=1.04533, w0=(884.5,'kJ/mol'), E0=(303.364,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9696754826640495, var=0.16913808042905815, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.260845932988073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.260845932988073""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.260845932988073
""",
)

entry(
    index = 20,
    label = "Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(5.66667e+08,'s^-1'), n=1.16, w0=(884.5,'kJ/mol'), E0=(327.64,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.865e+06,'s^-1'), n=1.71, w0=(810.5,'kJ/mol'), E0=(302.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
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
    index = 22,
    label = "Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.58553e+11,'s^-1'), n=0.0485841, w0=(884.5,'kJ/mol'), E0=(223.015,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.45036002431623506, var=1.241589883661321, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
    Total Standard Deviation in ln(k): 3.3653670337096813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 3.3653670337096813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 3.3653670337096813
""",
)

entry(
    index = 23,
    label = "Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.23333e+10,'s^-1'), n=0.42, w0=(884.5,'kJ/mol'), E0=(243.199,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
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
    index = 24,
    label = "Root_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.66e+07,'s^-1'), n=1.5, w0=(810.5,'kJ/mol'), E0=(376.399,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.895e+06,'s^-1'), n=1.63, w0=(810.5,'kJ/mol'), E0=(362.612,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(5.8714e+09,'s^-1'), n=0.800009, w0=(884.5,'kJ/mol'), E0=(318.904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4906713825197526, var=0.2763126357432311, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.286640650774833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 2.286640650774833""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 2.286640650774833
""",
)

entry(
    index = 27,
    label = "Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.19667e+11,'s^-1'), n=0.77, w0=(884.5,'kJ/mol'), E0=(329.989,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(4.77e+08,'s^-1'), n=1.06, w0=(884.5,'kJ/mol'), E0=(305.758,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2.65e+08,'s^-1'), n=1.02, w0=(884.5,'kJ/mol'), E0=(301.059,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.235e+11,'s^-1'), n=0.12, w0=(884.5,'kJ/mol'), E0=(224.37,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
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
    index = 31,
    label = "Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.08e+12,'s^-1'), n=-0.04, w0=(884.5,'kJ/mol'), E0=(221.809,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
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
    index = 32,
    label = "Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(5.9e+09,'s^-1'), n=0.8, w0=(884.5,'kJ/mol'), E0=(318.928,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.49e+09,'s^-1'), n=0.79, w0=(884.5,'kJ/mol'), E0=(314.352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

