#!/usr/bin/env python
# encoding: utf-8

name = "Lactone_to_Perfluoroalkene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.56085e+08,'s^-1'), n=1.58793, w0=(1185.5,'kJ/mol'), E0=(164.129,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3511842813249994, var=16.904190018267, Tref=1000.0, N=2, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 9.124781781493285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 9.124781781493285""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 9.124781781493285
""",
)

entry(
    index = 2,
    label = "Root_Ext-4C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(6.35e+11,'s^-1'), n=0.64, w0=(1185.5,'kJ/mol'), E0=(186.308,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_Ext-4C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(4.63333e+11,'s^-1'), n=0.63, w0=(1185.5,'kJ/mol'), E0=(158.868,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

