#!/usr/bin/env python
# encoding: utf-8

name = "CF_Radical_Formation_1/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.3681e+20,'s^-1'), n=-1.89285, w0=(682.167,'kJ/mol'), E0=(261.48,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3808124970879997, var=273.66351098830955, Tref=1000.0, N=3, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 3 training reactions at node Root
    Total Standard Deviation in ln(k): 34.12070307948766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 34.12070307948766""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 34.12070307948766
""",
)

entry(
    index = 2,
    label = "Root_2R->C",
    kinetics = ArrheniusBM(A=(2.80141e+25,'s^-1'), n=-3.46591, w0=(676.852,'kJ/mol'), E0=(306.197,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5914399659898856, var=604.5532824892405, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_2R->C
    Total Standard Deviation in ln(k): 50.77778506496147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R->C
Total Standard Deviation in ln(k): 50.77778506496147""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R->C
Total Standard Deviation in ln(k): 50.77778506496147
""",
)

entry(
    index = 3,
    label = "Root_N-2R->C",
    kinetics = ArrheniusBM(A=(1.505e+12,'s^-1'), n=0.49, w0=(730.5,'kJ/mol'), E0=(177.436,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_2R->C_Ext-2C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(4.635e+10,'s^-1'), n=0.64, w0=(658,'kJ/mol'), E0=(180.293,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2R->C_Ext-2C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_2R->C_Ext-2C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2R->C_Ext-2C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2R->C_Ext-2C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_2R->C_Ext-2C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(7.2e+09,'s^-1'), n=1.13, w0=(818.751,'kJ/mol'), E0=(348.047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2R->C_Ext-2C-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_2R->C_Ext-2C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2R->C_Ext-2C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2R->C_Ext-2C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

