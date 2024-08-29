#!/usr/bin/env python
# encoding: utf-8

name = "Perfluorinated_Alkyl_Rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(184795,'s^-1'), n=1.70472, w0=(1536.5,'kJ/mol'), E0=(367.366,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012729637810097694, var=62.28539990888931, Tref=1000.0, N=2, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 15.85357372266047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 15.85357372266047""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 15.85357372266047
""",
)

entry(
    index = 2,
    label = "Root_Ext-6C-R_Ext-6C-R_Ext-7R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(302000,'s^-1'), n=1.52, w0=(1536.5,'kJ/mol'), E0=(383.856,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6C-R_Ext-6C-R_Ext-7R!H-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6C-R_Ext-6C-R_Ext-7R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6C-R_Ext-6C-R_Ext-7R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6C-R_Ext-6C-R_Ext-7R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_Ext-6C-R_Ext-6C-R_Ext-7R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.83e+08,'s^-1'), n=0.97, w0=(1536.5,'kJ/mol'), E0=(358.92,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6C-R_Ext-6C-R_Ext-7R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6C-R_Ext-6C-R_Ext-7R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6C-R_Ext-6C-R_Ext-7R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6C-R_Ext-6C-R_Ext-7R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

