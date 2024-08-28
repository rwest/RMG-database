#!/usr/bin/env python
# encoding: utf-8

name = "Perfluoroalkene_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.85013e+13,'s^-1'), n=-0.119091, w0=(786,'kJ/mol'), E0=(368.789,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6525674998874904, var=380.112630126333, Tref=1000.0, N=3, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 3 training reactions at node Root
    Total Standard Deviation in ln(k): 40.72488891792468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 40.72488891792468""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 40.72488891792468
""",
)

entry(
    index = 2,
    label = "Root_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.33333e+09,'s^-1'), n=1.49, w0=(1094.12,'kJ/mol'), E0=(518.256,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_Ext-3C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.23e+06,'s^-1'), n=1.56, w0=(786,'kJ/mol'), E0=(289.945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-3C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.23333e+07,'s^-1'), n=1.21, w0=(786,'kJ/mol'), E0=(256.218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

