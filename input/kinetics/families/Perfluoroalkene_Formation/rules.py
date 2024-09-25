#!/usr/bin/env python
# encoding: utf-8

name = "Perfluoroalkene_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(119470,'s^-1'), n=2.21267, w0=(749,'kJ/mol'), E0=(324.935,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5379476748122662, var=165.08868049457297, Tref=1000.0, N=6, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 6 training reactions at node Root
    Total Standard Deviation in ln(k): 27.10983483389311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root
Total Standard Deviation in ln(k): 27.10983483389311""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root
Total Standard Deviation in ln(k): 27.10983483389311
""",
)

entry(
    index = 2,
    label = "Root_5R->O",
    kinetics = ArrheniusBM(A=(7.61656e+07,'s^-1'), n=1.11174, w0=(749,'kJ/mol'), E0=(261.046,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.46150230895535915, var=17.29588781286242, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5R->O',), comment="""BM rule fitted to 4 training reactions at node Root_5R->O
    Total Standard Deviation in ln(k): 9.496910945849935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5R->O
Total Standard Deviation in ln(k): 9.496910945849935""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5R->O
Total Standard Deviation in ln(k): 9.496910945849935
""",
)

entry(
    index = 3,
    label = "Root_N-5R->O",
    kinetics = ArrheniusBM(A=(1.30602e-14,'s^-1'), n=8.24016, w0=(893.697,'kJ/mol'), E0=(418.318,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3498520166101543, var=139.98157935884745, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->O
    Total Standard Deviation in ln(k): 24.59780992553563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->O
Total Standard Deviation in ln(k): 24.59780992553563""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->O
Total Standard Deviation in ln(k): 24.59780992553563
""",
)

entry(
    index = 4,
    label = "Root_5R->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.23941e+11,'s^-1'), n=0.122098, w0=(786,'kJ/mol'), E0=(284.282,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5717287601531534, var=61.314256936671164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5R->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_5R->O_Ext-2C-R
    Total Standard Deviation in ln(k): 17.134265838662177"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5R->O_Ext-2C-R
Total Standard Deviation in ln(k): 17.134265838662177""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5R->O_Ext-2C-R
Total Standard Deviation in ln(k): 17.134265838662177
""",
)

entry(
    index = 5,
    label = "Root_5R->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(206500,'s^-1'), n=1.73, w0=(712,'kJ/mol'), E0=(225.301,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_5R->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-5R->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.33333e+09,'s^-1'), n=1.49, w0=(1094.12,'kJ/mol'), E0=(518.256,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.23e+06,'s^-1'), n=1.56, w0=(786,'kJ/mol'), E0=(289.945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(6.23333e+07,'s^-1'), n=1.21, w0=(786,'kJ/mol'), E0=(256.218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

