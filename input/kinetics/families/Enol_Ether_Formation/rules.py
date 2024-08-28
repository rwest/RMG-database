#!/usr/bin/env python
# encoding: utf-8

name = "Enol_Ether_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.00717e+08,'s^-1'), n=1.22122, w0=(613,'kJ/mol'), E0=(293.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.018156212961141487, var=0.32424906679373755, Tref=1000.0, N=3, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 3 training reactions at node Root
    Total Standard Deviation in ln(k): 1.1871723539439398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 1.1871723539439398""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 1.1871723539439398
""",
)

entry(
    index = 2,
    label = "Root_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.15964e+08,'s^-1'), n=1.22, w0=(613,'kJ/mol'), E0=(296.851,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03201921928892215, var=0.14832878796964, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 0.852543474613249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 0.852543474613249""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 0.852543474613249
""",
)

entry(
    index = 3,
    label = "Root_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.30333e+09,'s^-1'), n=0.87, w0=(613,'kJ/mol'), E0=(290.813,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.05333e+07,'s^-1'), n=1.56, w0=(613,'kJ/mol'), E0=(295.15,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.27667e+09,'s^-1'), n=0.88, w0=(613,'kJ/mol'), E0=(298.551,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

