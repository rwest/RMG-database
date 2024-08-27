#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.42685e+37,'m^3/(mol*s)'), n=-9.42854, w0=(520.969,'kJ/mol'), E0=(178.548,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6199586509164206, var=37.55252308124885, Tref=1000.0, N=32, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 32 training reactions at node Root
    Total Standard Deviation in ln(k): 13.842724356563979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root
Total Standard Deviation in ln(k): 13.842724356563979""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root
Total Standard Deviation in ln(k): 13.842724356563979
""",
)

entry(
    index = 2,
    label = "Root_Ext-3R-R",
    kinetics = ArrheniusBM(A=(2.01929e+35,'m^3/(mol*s)'), n=-8.95413, w0=(547.875,'kJ/mol'), E0=(171.479,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5372346571694742, var=41.23051640764871, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-3R-R',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-3R-R
    Total Standard Deviation in ln(k): 14.222438853395845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 14.222438853395845""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 14.222438853395845
""",
)

entry(
    index = 3,
    label = "Root_Ext-1R-R",
    kinetics = ArrheniusBM(A=(2.5716e+09,'m^3/(mol*s)'), n=-0.704858, w0=(474.2,'kJ/mol'), E0=(77.0583,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05709145435391631, var=0.588758194753732, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1R-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1R-R
    Total Standard Deviation in ln(k): 1.6816907228365745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1R-R
Total Standard Deviation in ln(k): 1.6816907228365745""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1R-R
Total Standard Deviation in ln(k): 1.6816907228365745
""",
)

entry(
    index = 4,
    label = "Root_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.33384e+09,'m^3/(mol*s)'), n=-0.775738, w0=(480,'kJ/mol'), E0=(85.2146,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.031816340360544135, var=0.1433731633323153, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R-R
    Total Standard Deviation in ln(k): 0.8390264513067325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264513067325""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264513067325
""",
)

entry(
    index = 5,
    label = "Root_Sp-2R=1R",
    kinetics = ArrheniusBM(A=(5.61734e+06,'m^3/(mol*s)'), n=-0.137363, w0=(480,'kJ/mol'), E0=(154.984,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8057614146062959, var=0.435875967625411, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Sp-2R=1R',), comment="""BM rule fitted to 2 training reactions at node Root_Sp-2R=1R
    Total Standard Deviation in ln(k): 3.348070374782754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Sp-2R=1R
Total Standard Deviation in ln(k): 3.348070374782754""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Sp-2R=1R
Total Standard Deviation in ln(k): 3.348070374782754
""",
)

entry(
    index = 6,
    label = "Root_N-Sp-2R=1R",
    kinetics = ArrheniusBM(A=(1.52735e+09,'m^3/(mol*s)'), n=-0.643653, w0=(462.5,'kJ/mol'), E0=(86.0387,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-Sp-2R=1R',), comment="""BM rule fitted to 1 training reactions at node Root_N-Sp-2R=1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-Sp-2R=1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-Sp-2R=1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-3R-R_Ext-3R-R",
    kinetics = ArrheniusBM(A=(5.27964e+37,'m^3/(mol*s)'), n=-9.75924, w0=(534.615,'kJ/mol'), E0=(134.492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8749690260990493, var=53.52997230308089, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-3R-R_Ext-3R-R
    Total Standard Deviation in ln(k): 16.865894437390434"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 16.865894437390434""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 16.865894437390434
""",
)

entry(
    index = 8,
    label = "Root_Ext-3R-R_Ext-2R-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00349941,'m^3/(mol*s)'), n=1.94847, w0=(572.5,'kJ/mol'), E0=(120.456,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8113149811132726, var=3.775882180285107, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C
    Total Standard Deviation in ln(k): 5.934006742908749"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 5.934006742908749""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 5.934006742908749
""",
)

entry(
    index = 9,
    label = "Root_Ext-3R-R_Ext-2R-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000391103,'m^3/(mol*s)'), n=2.46641, w0=(572.5,'kJ/mol'), E0=(92.6683,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-1R-R_Ext-1R-R",
    kinetics = ArrheniusBM(A=(3.18e+07,'m^3/(mol*s)'), n=3.3438e-08, w0=(486,'kJ/mol'), E0=(121.323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R-R_Ext-1R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Ext-1R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Ext-1R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Ext-1R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_Ext-1R-R_Sp-2R=1R",
    kinetics = ArrheniusBM(A=(9.41381e+08,'m^3/(mol*s)'), n=-0.607357, w0=(480,'kJ/mol'), E0=(102.035,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7965843144686672, var=0.26948413780238106, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R-R_Sp-2R=1R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R-R_Sp-2R=1R
    Total Standard Deviation in ln(k): 3.042163426256012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R-R_Sp-2R=1R
Total Standard Deviation in ln(k): 3.042163426256012""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R-R_Sp-2R=1R
Total Standard Deviation in ln(k): 3.042163426256012
""",
)

entry(
    index = 12,
    label = "Root_Ext-1R-R_N-Sp-2R=1R",
    kinetics = ArrheniusBM(A=(4.65189e+09,'m^3/(mol*s)'), n=-0.763953, w0=(462.5,'kJ/mol'), E0=(91.1263,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13986271634666708, var=0.8118301244467586, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R-R_N-Sp-2R=1R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R
    Total Standard Deviation in ln(k): 2.1577125657189096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R
Total Standard Deviation in ln(k): 2.1577125657189096""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R
Total Standard Deviation in ln(k): 2.1577125657189096
""",
)

entry(
    index = 13,
    label = "Root_Ext-2R-R_3R->C",
    kinetics = ArrheniusBM(A=(4.13595e+09,'m^3/(mol*s)'), n=-0.801251, w0=(474,'kJ/mol'), E0=(97.3297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1826800169439447, var=0.005086439742254407, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R-R_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R-R_3R->C
    Total Standard Deviation in ln(k): 0.6019712803554198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.6019712803554198""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.6019712803554198
""",
)

entry(
    index = 14,
    label = "Root_Ext-2R-R_N-3R->C",
    kinetics = ArrheniusBM(A=(3.86082e+06,'m^3/(mol*s)'), n=0.0243326, w0=(486,'kJ/mol'), E0=(92.826,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0038925227441374026, var=1.6818078495915973, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R-R_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-3R->C
    Total Standard Deviation in ln(k): 2.609611561551256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.609611561551256""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.609611561551256
""",
)

entry(
    index = 15,
    label = "Root_Sp-2R=1R_3R->C",
    kinetics = ArrheniusBM(A=(1.98e+06,'m^3/(mol*s)'), n=-1.90181e-08, w0=(474,'kJ/mol'), E0=(153.806,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-2R=1R_3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_Sp-2R=1R_N-3R->C",
    kinetics = ArrheniusBM(A=(700000,'m^3/(mol*s)'), n=1.22665e-08, w0=(486,'kJ/mol'), E0=(119.69,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-2R=1R_N-3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_N-3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_Ext-3R-R_Ext-3R-R_4R!H->O",
    kinetics = ArrheniusBM(A=(2.88501e+60,'m^3/(mol*s)'), n=-17.547, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.015778190190873, var=0.3465917491057476, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_4R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O
    Total Standard Deviation in ln(k): 6.244997826389541"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O
Total Standard Deviation in ln(k): 6.244997826389541""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O
Total Standard Deviation in ln(k): 6.244997826389541
""",
)

entry(
    index = 18,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.36573e-08,'m^3/(mol*s)'), n=4.17511, w0=(523.25,'kJ/mol'), E0=(80.1794,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.820231716132256, var=131.96785987152205, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O
    Total Standard Deviation in ln(k): 25.090731959613485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O
Total Standard Deviation in ln(k): 25.090731959613485""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O
Total Standard Deviation in ln(k): 25.090731959613485
""",
)

entry(
    index = 19,
    label = "Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(3.47014e-13,'m^3/(mol*s)'), n=4.61831, w0=(572.5,'kJ/mol'), E0=(97.661,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3987292700038914, var=0.11286114398256664, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 4.187882144989432"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 4.187882144989432""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 4.187882144989432
""",
)

entry(
    index = 20,
    label = "Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(4.41807e-05,'m^3/(mol*s)'), n=2.68884, w0=(572.5,'kJ/mol'), E0=(112.649,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5851058560977576, var=0.2723401435687425, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 2.5163106507603277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.5163106507603277""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.5163106507603277
""",
)

entry(
    index = 21,
    label = "Root_Ext-1R-R_Sp-2R=1R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.54e+07,'m^3/(mol*s)'), n=2.17787e-08, w0=(486,'kJ/mol'), E0=(120.733,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R-R_Sp-2R=1R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Sp-2R=1R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Sp-2R=1R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Sp-2R=1R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_Ext-1R-R_N-Sp-2R=1R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.29568e+09,'m^3/(mol*s)'), n=-0.811807, w0=(462.5,'kJ/mol'), E0=(82.5344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R-R_N-Sp-2R=1R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_Ext-2R-R_3R->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.40609e+09,'m^3/(mol*s)'), n=-0.732703, w0=(474,'kJ/mol'), E0=(102.438,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_3R->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_3R->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_3R->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_3R->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_Ext-2R-R_N-3R->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(7.2835e+06,'m^3/(mol*s)'), n=-2.41431e-09, w0=(486,'kJ/mol'), E0=(122.28,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-3R->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-3R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.6969e+60,'m^3/(mol*s)'), n=-17.5558, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.0005054922280743, var=0.3020400317791764, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 6.1281613969323505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C
Total Standard Deviation in ln(k): 6.1281613969323505""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C
Total Standard Deviation in ln(k): 6.1281613969323505
""",
)

entry(
    index = 26,
    label = "Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.75698e+60,'m^3/(mol*s)'), n=-17.5293, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F",
    kinetics = ArrheniusBM(A=(2.36444e-10,'m^3/(mol*s)'), n=4.68248, w0=(535.562,'kJ/mol'), E0=(75.4568,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4781942356855848, var=143.0192771191006, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F
    Total Standard Deviation in ln(k): 25.176253626589002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F
Total Standard Deviation in ln(k): 25.176253626589002""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F
Total Standard Deviation in ln(k): 25.176253626589002
""",
)

entry(
    index = 28,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F",
    kinetics = ArrheniusBM(A=(0.531385,'m^3/(mol*s)'), n=1.91075, w0=(474,'kJ/mol'), E0=(98.7387,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0577200283147992, var=2.936408170988897, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F
    Total Standard Deviation in ln(k): 3.5803294046746075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F
Total Standard Deviation in ln(k): 3.5803294046746075""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F
Total Standard Deviation in ln(k): 3.5803294046746075
""",
)

entry(
    index = 29,
    label = "Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.17638e-13,'m^3/(mol*s)'), n=4.6762, w0=(572.5,'kJ/mol'), E0=(98.4219,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4436042264366704, var=0.03493136058926443, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C
    Total Standard Deviation in ln(k): 4.001829945921897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C
Total Standard Deviation in ln(k): 4.001829945921897""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C
Total Standard Deviation in ln(k): 4.001829945921897
""",
)

entry(
    index = 30,
    label = "Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2.46363e-12,'m^3/(mol*s)'), n=4.37475, w0=(572.5,'kJ/mol'), E0=(97.2898,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.15733e-05,'m^3/(mol*s)'), n=2.67724, w0=(572.5,'kJ/mol'), E0=(113.187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5885194367825252, var=0.9375920901136175, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.4198637773902503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.4198637773902503""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.4198637773902503
""",
)

entry(
    index = 32,
    label = "Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.12796e-05,'m^3/(mol*s)'), n=2.71651, w0=(572.5,'kJ/mol'), E0=(111.534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(3.61854e+60,'m^3/(mol*s)'), n=-17.5812, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(3.77695e+60,'m^3/(mol*s)'), n=-17.5303, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C",
    kinetics = ArrheniusBM(A=(2.41542e-05,'m^3/(mol*s)'), n=3.34676, w0=(572.5,'kJ/mol'), E0=(93.4291,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.547101108649816, var=279.6621939467631, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C
    Total Standard Deviation in ln(k): 34.90001828677636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C
Total Standard Deviation in ln(k): 34.90001828677636""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C
Total Standard Deviation in ln(k): 34.90001828677636
""",
)

entry(
    index = 36,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.87814e-22,'m^3/(mol*s)'), n=7.85739, w0=(513.4,'kJ/mol'), E0=(34.3453,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4223647178513226, var=2.5552928410344187, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C
    Total Standard Deviation in ln(k): 6.778406525531339"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C
Total Standard Deviation in ln(k): 6.778406525531339""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C
Total Standard Deviation in ln(k): 6.778406525531339
""",
)

entry(
    index = 37,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F_4BrCCl->Br",
    kinetics = ArrheniusBM(A=(0.000161154,'m^3/(mol*s)'), n=2.94391, w0=(474,'kJ/mol'), E0=(70.9316,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F_4BrCCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F_4BrCCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F_4BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F_4BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F_N-4BrCCl->Br",
    kinetics = ArrheniusBM(A=(8.68219e-05,'m^3/(mol*s)'), n=2.97056, w0=(474,'kJ/mol'), E0=(87.4167,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F_N-4BrCCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F_N-4BrCCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F_N-4BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4BrCClF->F_N-4BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.88038e-13,'m^3/(mol*s)'), n=4.68918, w0=(572.5,'kJ/mol'), E0=(98.506,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.51897e-13,'m^3/(mol*s)'), n=4.66321, w0=(572.5,'kJ/mol'), E0=(98.3378,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(7.30815e-05,'m^3/(mol*s)'), n=2.59582, w0=(572.5,'kJ/mol'), E0=(114.247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(5.1903e-05,'m^3/(mol*s)'), n=2.71449, w0=(572.5,'kJ/mol'), E0=(112.538,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-2R-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(282.198,'m^3/(mol*s)'), n=1.44131, w0=(572.5,'kJ/mol'), E0=(127.62,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03121091162125639, var=890.7517446171922, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 59.91066873842166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 59.91066873842166""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 59.91066873842166
""",
)

entry(
    index = 44,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.7648e-05,'m^3/(mol*s)'), n=3.05252, w0=(572.5,'kJ/mol'), E0=(64.5877,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C",
    kinetics = ArrheniusBM(A=(3.57904e-20,'m^3/(mol*s)'), n=7.10843, w0=(498.625,'kJ/mol'), E0=(38.3505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30886754501971014, var=3.774842986878959, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C
    Total Standard Deviation in ln(k): 4.671039901132235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C
Total Standard Deviation in ln(k): 4.671039901132235""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C
Total Standard Deviation in ln(k): 4.671039901132235
""",
)

entry(
    index = 46,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_N-1R->C",
    kinetics = ArrheniusBM(A=(0.00477623,'m^3/(mol*s)'), n=2.38781, w0=(572.5,'kJ/mol'), E0=(83.097,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_N-1R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_N-1R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_N-1R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_N-1R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(774488,'m^3/(mol*s)'), n=0.652409, w0=(572.5,'kJ/mol'), E0=(22.0859,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.74781e-06,'m^3/(mol*s)'), n=3.54047, w0=(572.5,'kJ/mol'), E0=(185.914,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.10298e-06,'m^3/(mol*s)'), n=3.07477, w0=(474,'kJ/mol'), E0=(78.6589,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.01799e-05,'m^3/(mol*s)'), n=2.87159, w0=(474,'kJ/mol'), E0=(101.042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_2R->C",
    kinetics = ArrheniusBM(A=(2.07011e-05,'m^3/(mol*s)'), n=2.98446, w0=(474,'kJ/mol'), E0=(119.563,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_N-2R->C",
    kinetics = ArrheniusBM(A=(4.81575e-05,'m^3/(mol*s)'), n=2.76922, w0=(572.5,'kJ/mol'), E0=(109.078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-3R-R_N-4R!H->O_4BrCClF->F_N-5R!H->C_1R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

