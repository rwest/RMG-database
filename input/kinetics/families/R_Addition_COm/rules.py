#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/rules"
shortDesc = ""
longDesc = """
.. [MRHCBSQB31DHR] M.R. Harper (mrharper_at_mit_dot_edu or michael_dot_harper_dot_jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 method.
The zero-point energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the 
temperatures used were from 600 K to 2000 K (in 200 K increments).
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(164.647,'m^3/(mol*s)'), n=1.08425, w0=(309.227,'kJ/mol'), E0=(40.7013,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06704114901360426, var=6.612514018264607, Tref=1000.0, N=22, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 22 training reactions at node Root
    Total Standard Deviation in ln(k): 5.323583058791248"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root
Total Standard Deviation in ln(k): 5.323583058791248""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root
Total Standard Deviation in ln(k): 5.323583058791248
""",
)

entry(
    index = 2,
    label = "Root_3R->O",
    kinetics = ArrheniusBM(A=(34.1,'m^3/(mol*s)'), n=4.7991e-09, w0=(315.5,'kJ/mol'), E0=(36.7874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-3R->O",
    kinetics = ArrheniusBM(A=(208.51,'m^3/(mol*s)'), n=1.0559, w0=(308.929,'kJ/mol'), E0=(40.9623,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06300403601758225, var=6.5507021196904205, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-3R->O',), comment="""BM rule fitted to 21 training reactions at node Root_N-3R->O
    Total Standard Deviation in ln(k): 5.289288606190444"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 5.289288606190444""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 5.289288606190444
""",
)

entry(
    index = 4,
    label = "Root_N-3R->O_3BrCClFHINPSSi->Br",
    kinetics = ArrheniusBM(A=(7.12172e+09,'m^3/(mol*s)'), n=-0.817305, w0=(279,'kJ/mol'), E0=(-9.43534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br",
    kinetics = ArrheniusBM(A=(213.845,'m^3/(mol*s)'), n=1.05253, w0=(310.425,'kJ/mol'), E0=(41.0373,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0637919689937198, var=6.487055154238581, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br',), comment="""BM rule fitted to 20 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br
    Total Standard Deviation in ln(k): 5.266281025154847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br
Total Standard Deviation in ln(k): 5.266281025154847""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br
Total Standard Deviation in ln(k): 5.266281025154847
""",
)

entry(
    index = 6,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_3CClHS->Cl",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=1.10425e-09, w0=(300,'kJ/mol'), E0=(8.23806,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_3CClHS->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_3CClHS->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_3CClHS->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_3CClHS->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl",
    kinetics = ArrheniusBM(A=(205.368,'m^3/(mol*s)'), n=1.05733, w0=(310.974,'kJ/mol'), E0=(41.0244,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06516404005397178, var=6.4563291232410425, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl',), comment="""BM rule fitted to 19 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl
    Total Standard Deviation in ln(k): 5.25762176612803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl
Total Standard Deviation in ln(k): 5.25762176612803""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl
Total Standard Deviation in ln(k): 5.25762176612803
""",
)

entry(
    index = 8,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing",
    kinetics = ArrheniusBM(A=(2.49727e+12,'m^3/(mol*s)'), n=-1.81636, w0=(309.5,'kJ/mol'), E0=(87.9115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.746325767588697, var=19.055466163304082, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing
    Total Standard Deviation in ln(k): 10.626373623579733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing
Total Standard Deviation in ln(k): 10.626373623579733""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing
Total Standard Deviation in ln(k): 10.626373623579733
""",
)

entry(
    index = 9,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing",
    kinetics = ArrheniusBM(A=(441.502,'m^3/(mol*s)'), n=0.961459, w0=(311.147,'kJ/mol'), E0=(41.1466,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.035150432513794336, var=6.611625236704371, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing
    Total Standard Deviation in ln(k): 5.243109170224693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing
Total Standard Deviation in ln(k): 5.243109170224693""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing
Total Standard Deviation in ln(k): 5.243109170224693
""",
)

entry(
    index = 10,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00721,'m^3/(mol*s)'), n=2.333, w0=(309.5,'kJ/mol'), E0=(57.1975,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.48e+06,'m^3/(mol*s)'), n=4.98146e-08, w0=(309.5,'kJ/mol'), E0=(55.5346,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_3CHS->S",
    kinetics = ArrheniusBM(A=(0.0785,'m^3/(mol*s)'), n=2.33, w0=(272.5,'kJ/mol'), E0=(17.1121,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_3CHS->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_3CHS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_3CHS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_3CHS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S",
    kinetics = ArrheniusBM(A=(444.001,'m^3/(mol*s)'), n=0.960508, w0=(313.562,'kJ/mol'), E0=(41.1654,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03551571173339375, var=6.606199583842893, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S',), comment="""BM rule fitted to 16 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S
    Total Standard Deviation in ln(k): 5.241911452440181"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S
Total Standard Deviation in ln(k): 5.241911452440181""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S
Total Standard Deviation in ln(k): 5.241911452440181
""",
)

entry(
    index = 14,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(239.752,'m^3/(mol*s)'), n=1.02586, w0=(309.5,'kJ/mol'), E0=(40.2101,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0580632952607818, var=7.274142535187226, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R
    Total Standard Deviation in ln(k): 5.552782140597428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R
Total Standard Deviation in ln(k): 5.552782140597428""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R
Total Standard Deviation in ln(k): 5.552782140597428
""",
)

entry(
    index = 15,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C",
    kinetics = ArrheniusBM(A=(49.1128,'m^3/(mol*s)'), n=1.44161, w0=(309.5,'kJ/mol'), E0=(44.0884,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09435603370017663, var=0.5552055549964423, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C
    Total Standard Deviation in ln(k): 1.7308460039496685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C
Total Standard Deviation in ln(k): 1.7308460039496685""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C
Total Standard Deviation in ln(k): 1.7308460039496685
""",
)

entry(
    index = 16,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C",
    kinetics = ArrheniusBM(A=(108625,'m^3/(mol*s)'), n=5.5697e-06, w0=(342,'kJ/mol'), E0=(41.9179,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23268370907548702, var=3.3298902215117967, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C
    Total Standard Deviation in ln(k): 4.242870357282385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C
Total Standard Deviation in ln(k): 4.242870357282385""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C
Total Standard Deviation in ln(k): 4.242870357282385
""",
)

entry(
    index = 17,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.568411,'m^3/(mol*s)'), n=1.56435, w0=(309.5,'kJ/mol'), E0=(32.6596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10504263548285178, var=9.703191424302856, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 6.508665181645542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.508665181645542""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.508665181645542
""",
)

entry(
    index = 18,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Sp-4R!H=3CCHH",
    kinetics = ArrheniusBM(A=(0.000138715,'m^3/(mol*s)'), n=2.91249, w0=(309.5,'kJ/mol'), E0=(25.2402,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.200720354537158, var=13.35387226147436, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Sp-4R!H=3CCHH',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Sp-4R!H=3CCHH
    Total Standard Deviation in ln(k): 15.367904396947111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Sp-4R!H=3CCHH
Total Standard Deviation in ln(k): 15.367904396947111""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Sp-4R!H=3CCHH
Total Standard Deviation in ln(k): 15.367904396947111
""",
)

entry(
    index = 19,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH",
    kinetics = ArrheniusBM(A=(7.25515e-10,'m^3/(mol*s)'), n=4.67248, w0=(309.5,'kJ/mol'), E0=(4.37354,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5031815357819036, var=1.724513246969998, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH
    Total Standard Deviation in ln(k): 3.8969078271752604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH
Total Standard Deviation in ln(k): 3.8969078271752604""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH
Total Standard Deviation in ln(k): 3.8969078271752604
""",
)

entry(
    index = 20,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(0.0637525,'m^3/(mol*s)'), n=1.82747, w0=(309.5,'kJ/mol'), E0=(30.3325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16830289871461207, var=10.232890615674123, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R
    Total Standard Deviation in ln(k): 6.835796523288124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R
Total Standard Deviation in ln(k): 6.835796523288124""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R
Total Standard Deviation in ln(k): 6.835796523288124
""",
)

entry(
    index = 21,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Sp-4R!H=3CCHH_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(0.00324606,'m^3/(mol*s)'), n=2.52184, w0=(309.5,'kJ/mol'), E0=(28.7836,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Sp-4R!H=3CCHH_Ext-3CH-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Sp-4R!H=3CCHH_Ext-3CH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Sp-4R!H=3CCHH_Ext-3CH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Sp-4R!H=3CCHH_Ext-3CH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(0.0380097,'m^3/(mol*s)'), n=2.50266, w0=(309.5,'kJ/mol'), E0=(31.2259,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7283280200119541, var=0.7415010221239028, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH_Ext-3CH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH_Ext-3CH-R
    Total Standard Deviation in ln(k): 3.556256368387537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH_Ext-3CH-R
Total Standard Deviation in ln(k): 3.556256368387537""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH_Ext-3CH-R
Total Standard Deviation in ln(k): 3.556256368387537
""",
)

entry(
    index = 23,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_5R!H->O",
    kinetics = ArrheniusBM(A=(0.00354327,'m^3/(mol*s)'), n=2.28162, w0=(309.5,'kJ/mol'), E0=(13.4031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.00267422,'m^3/(mol*s)'), n=2.17481, w0=(309.5,'kJ/mol'), E0=(33.6172,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1847162723253508, var=4.579858691356068, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O
    Total Standard Deviation in ln(k): 4.754365470919057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.754365470919057""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.754365470919057
""",
)

entry(
    index = 25,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH_Ext-3CH-R_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(0.0496072,'m^3/(mol*s)'), n=2.48433, w0=(309.5,'kJ/mol'), E0=(31.9309,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH_Ext-3CH-R_Ext-3CH-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH_Ext-3CH-R_Ext-3CH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH_Ext-3CH-R_Ext-3CH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_N-Sp-4R!H=3CCHH_Ext-3CH-R_Ext-3CH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O_5CF->C",
    kinetics = ArrheniusBM(A=(0.00113676,'m^3/(mol*s)'), n=2.28855, w0=(309.5,'kJ/mol'), E0=(26.7017,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O_5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O_5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O_N-5CF->C",
    kinetics = ArrheniusBM(A=(0.00136302,'m^3/(mol*s)'), n=2.25138, w0=(309.5,'kJ/mol'), E0=(38.8513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O_N-5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O_N-5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Br_N-3CClHS->Cl_N-3CHS-inRing_N-3CHS->S_Ext-3CH-R_Ext-4R!H-R_Ext-3CH-R_N-5R!H->O_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

