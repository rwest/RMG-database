#!/usr/bin/env python
# encoding: utf-8

name = "CF_Radical_Formation_2/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.62955e+36,'s^-1'), n=-5.7772, w0=(438.609,'kJ/mol'), E0=(156.333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7577310426154498, var=40.928858257182036, Tref=1000.0, N=2, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 14.729272991125892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 14.729272991125892""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 14.729272991125892
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.66e+20,'s^-1'), n=-1.26, w0=(435.451,'kJ/mol'), E0=(120.868,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_Ext-2R-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(2.54e+21,'s^-1'), n=-1.47, w0=(441.768,'kJ/mol'), E0=(73.7104,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

