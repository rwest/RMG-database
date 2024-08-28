#!/usr/bin/env python
# encoding: utf-8

name = "PFAS_Hydrolysis/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.83705e-06,'m^3/(mol*s)'), n=3.04918, w0=(933.5,'kJ/mol'), E0=(239.151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1257533055884845, var=178.70731757557357, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 27.115553542843735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 27.115553542843735""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 27.115553542843735
""",
)

entry(
    index = 2,
    label = "Root_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.06791e-07,'m^3/(mol*s)'), n=3.44867, w0=(933.5,'kJ/mol'), E0=(344.847,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05469108280596011, var=3.6245072685428457, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 3.9540572358561623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.9540572358561623""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.9540572358561623
""",
)

entry(
    index = 3,
    label = "Root_4R->C",
    kinetics = ArrheniusBM(A=(3.5992e-09,'m^3/(mol*s)'), n=3.74529, w0=(933.5,'kJ/mol'), E0=(147.622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24378405930103103, var=0.7909592402477703, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C
    Total Standard Deviation in ln(k): 2.395451730902549"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.395451730902549""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.395451730902549
""",
)

entry(
    index = 4,
    label = "Root_N-4R->C",
    kinetics = ArrheniusBM(A=(6.05e-08,'m^3/(mol*s)'), n=3.33, w0=(933.5,'kJ/mol'), E0=(165.041,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Ext-1C-R_Ext-1C-R_4R->C",
    kinetics = ArrheniusBM(A=(3.76063e-08,'m^3/(mol*s)'), n=3.56442, w0=(933.5,'kJ/mol'), E0=(334.889,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.044184061457185106, var=10.911797374592682, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1C-R_Ext-1C-R_4R->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1C-R_Ext-1C-R_4R->C
    Total Standard Deviation in ln(k): 6.733258578660325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1C-R_Ext-1C-R_4R->C
Total Standard Deviation in ln(k): 6.733258578660325""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1C-R_Ext-1C-R_4R->C
Total Standard Deviation in ln(k): 6.733258578660325
""",
)

entry(
    index = 6,
    label = "Root_Ext-1C-R_Ext-1C-R_N-4R->C",
    kinetics = ArrheniusBM(A=(6.1125e-06,'m^3/(mol*s)'), n=3.22, w0=(933.5,'kJ/mol'), E0=(364.738,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1C-R_Ext-1C-R_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1C-R_Ext-1C-R_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1C-R_Ext-1C-R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1C-R_Ext-1C-R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_4R->C_Ext-4C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.19211e-09,'m^3/(mol*s)'), n=3.80046, w0=(933.5,'kJ/mol'), E0=(149.13,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2756071386927434, var=1.0138669139709182, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 2.711067214384389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 2.711067214384389""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 2.711067214384389
""",
)

entry(
    index = 8,
    label = "Root_4R->C_Ext-4C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.285e-08,'m^3/(mol*s)'), n=3.6, w0=(933.5,'kJ/mol'), E0=(144.912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-4C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-4C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_Ext-1C-R_Ext-1C-R_4R->C_Ext-4C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(5.64167e-09,'m^3/(mol*s)'), n=3.77, w0=(933.5,'kJ/mol'), E0=(340.612,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1C-R_Ext-1C-R_4R->C_Ext-4C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1C-R_Ext-1C-R_4R->C_Ext-4C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1C-R_Ext-1C-R_4R->C_Ext-4C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1C-R_Ext-1C-R_4R->C_Ext-4C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-1C-R_Ext-1C-R_4R->C_Ext-4C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.48333e-07,'m^3/(mol*s)'), n=3.36, w0=(933.5,'kJ/mol'), E0=(329.155,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1C-R_Ext-1C-R_4R->C_Ext-4C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1C-R_Ext-1C-R_4R->C_Ext-4C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1C-R_Ext-1C-R_4R->C_Ext-4C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1C-R_Ext-1C-R_4R->C_Ext-4C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_4R->C_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.335e-09,'m^3/(mol*s)'), n=3.86, w0=(933.5,'kJ/mol'), E0=(151.407,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_4R->C_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(4.615e-09,'m^3/(mol*s)'), n=3.71, w0=(933.5,'kJ/mol'), E0=(147.122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

