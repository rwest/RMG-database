#!/usr/bin/env python
# encoding: utf-8

name = "Enol_Ether_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(7.78503e+21,'s^-1'), n=-2.7015, w0=(583.4,'kJ/mol'), E0=(307.898,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3275336518189088, var=18.438402117763637, Tref=1000.0, N=5, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 5 training reactions at node Root
    Total Standard Deviation in ln(k): 9.431273386962342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 9.431273386962342""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 9.431273386962342
""",
)

entry(
    index = 2,
    label = "Root_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.56867e+08,'s^-1'), n=1.10473, w0=(613,'kJ/mol'), E0=(290.182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0012325637500235735, var=0.15935895519543375, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3C-R
    Total Standard Deviation in ln(k): 0.8033829062844328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3C-R
Total Standard Deviation in ln(k): 0.8033829062844328""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3C-R
Total Standard Deviation in ln(k): 0.8033829062844328
""",
)

entry(
    index = 3,
    label = "Root_Ext-5C-R",
    kinetics = ArrheniusBM(A=(80.6667,'s^-1'), n=3.11, w0=(539,'kJ/mol'), E0=(220.383,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-3C-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.15964e+08,'s^-1'), n=1.22, w0=(613,'kJ/mol'), E0=(289.131,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.023445964083352887, var=0.14829930703762614, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 0.8309259002924556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 0.8309259002924556""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 0.8309259002924556
""",
)

entry(
    index = 5,
    label = "Root_Ext-3C-R_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.30333e+09,'s^-1'), n=0.87, w0=(613,'kJ/mol'), E0=(292.323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.05333e+07,'s^-1'), n=1.56, w0=(613,'kJ/mol'), E0=(287.446,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.27667e+09,'s^-1'), n=0.88, w0=(613,'kJ/mol'), E0=(290.815,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

