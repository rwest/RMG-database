#!/usr/bin/env python
# encoding: utf-8

name = "CO2_Elimination_From_CarboxylicAcid_or_Ester/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.55253e-14,'s^-1'), n=7.63079, w0=(828.5,'kJ/mol'), E0=(125.641,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.51782021207343, var=6.213491254815403, Tref=1000.0, N=4, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 4 training reactions at node Root
    Total Standard Deviation in ln(k): 6.298233990924361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 6.298233990924361""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 6.298233990924361
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R-R_7R!H->F",
    kinetics = ArrheniusBM(A=(5.85e-12,'s^-1'), n=6.85, w0=(828.5,'kJ/mol'), E0=(150.204,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_Ext-2R-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(2.24851e-15,'s^-1'), n=7.88545, w0=(828.5,'kJ/mol'), E0=(117.493,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5006083882250826, var=2.7689425068383597, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F
    Total Standard Deviation in ln(k): 4.593717204323286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F
Total Standard Deviation in ln(k): 4.593717204323286""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F
Total Standard Deviation in ln(k): 4.593717204323286
""",
)

entry(
    index = 4,
    label = "Root_Ext-2R-R_N-7R!H->F_7BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.54e-21,'s^-1'), n=9.6, w0=(828.5,'kJ/mol'), E0=(112.6,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_7BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_7BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_7BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_7BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.92389e-13,'s^-1'), n=7.20957, w0=(828.5,'kJ/mol'), E0=(118.385,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.46454614542434636, var=0.003948675801457142, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 1.2931758951432089"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.2931758951432089""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.2931758951432089
""",
)

entry(
    index = 6,
    label = "Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C_Ext-7O-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(2.1e-13,'s^-1'), n=7.32, w0=(828.5,'kJ/mol'), E0=(117.643,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C_Ext-7O-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C_Ext-7O-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C_Ext-7O-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C_Ext-7O-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C_Ext-7O-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(1.14661e-12,'s^-1'), n=7.1, w0=(828.5,'kJ/mol'), E0=(119.119,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C_Ext-7O-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C_Ext-7O-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C_Ext-7O-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-7BrCClINOPSSi->C_Ext-7O-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

