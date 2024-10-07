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
    kinetics = ArrheniusBM(A=(1.31181e-30,'m^3/(mol*s)'), n=10.1147, w0=(309.26,'kJ/mol'), E0=(-72.7812,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7545435670792515, var=65.56210058812117, Tref=1000.0, N=25, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 25 training reactions at node Root
    Total Standard Deviation in ln(k): 18.128263644776084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 18.128263644776084""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 18.128263644776084
""",
)

entry(
    index = 2,
    label = "Root_Ext-3R-R",
    kinetics = ArrheniusBM(A=(2.13031e-28,'m^3/(mol*s)'), n=9.36829, w0=(307.676,'kJ/mol'), E0=(-68.8888,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9308234771750868, var=68.16103320990872, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_Ext-3R-R',), comment="""BM rule fitted to 17 training reactions at node Root_Ext-3R-R
    Total Standard Deviation in ln(k): 18.889784209921558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 18.889784209921558""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 18.889784209921558
""",
)

entry(
    index = 3,
    label = "Root_3R->Cl",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=1.10425e-09, w0=(300,'kJ/mol'), E0=(8.23806,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_3R->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_N-3R->Cl",
    kinetics = ArrheniusBM(A=(1.0705,'m^3/(mol*s)'), n=2.21325, w0=(314.429,'kJ/mol'), E0=(39.023,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.629786161225261, var=13.924135352355789, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->Cl
    Total Standard Deviation in ln(k): 11.575620623161832"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->Cl
Total Standard Deviation in ln(k): 11.575620623161832""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->Cl
Total Standard Deviation in ln(k): 11.575620623161832
""",
)

entry(
    index = 5,
    label = "Root_Ext-3R-R_4R!H->F",
    kinetics = ArrheniusBM(A=(6.04793e-24,'m^3/(mol*s)'), n=7.83976, w0=(309.5,'kJ/mol'), E0=(-75.1849,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.7907371235209584, var=108.59945521068522, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R-R_4R!H->F
    Total Standard Deviation in ln(k): 25.390896725653327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R-R_4R!H->F
Total Standard Deviation in ln(k): 25.390896725653327""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R-R_4R!H->F
Total Standard Deviation in ln(k): 25.390896725653327
""",
)

entry(
    index = 6,
    label = "Root_Ext-3R-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(0.00459984,'m^3/(mol*s)'), n=2.53767, w0=(306.917,'kJ/mol'), E0=(33.2638,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19757455850455835, var=1.8729450793692404, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-4R!H->F
    Total Standard Deviation in ln(k): 3.24001038079144"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.24001038079144""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.24001038079144
""",
)

entry(
    index = 7,
    label = "Root_N-3R->Cl_3BrCHOS->Br",
    kinetics = ArrheniusBM(A=(7.12172e+09,'m^3/(mol*s)'), n=-0.817305, w0=(279,'kJ/mol'), E0=(-9.43534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->Cl_3BrCHOS->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->Cl_3BrCHOS->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->Cl_3BrCHOS->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->Cl_3BrCHOS->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-3R->Cl_N-3BrCHOS->Br",
    kinetics = ArrheniusBM(A=(2.8926,'m^3/(mol*s)'), n=2.09038, w0=(320.333,'kJ/mol'), E0=(40.4417,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4429079222582688, var=12.79121083408989, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->Cl_N-3BrCHOS->Br',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->Cl_N-3BrCHOS->Br
    Total Standard Deviation in ln(k): 10.795292159863413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->Cl_N-3BrCHOS->Br
Total Standard Deviation in ln(k): 10.795292159863413""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->Cl_N-3BrCHOS->Br
Total Standard Deviation in ln(k): 10.795292159863413
""",
)

entry(
    index = 9,
    label = "Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.72165e-12,'m^3/(mol*s)'), n=4.04305, w0=(309.5,'kJ/mol'), E0=(-68.8068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.1789235525044215, var=135.1794075646738, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C
    Total Standard Deviation in ln(k): 28.783071360572173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C
Total Standard Deviation in ln(k): 28.783071360572173""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C
Total Standard Deviation in ln(k): 28.783071360572173
""",
)

entry(
    index = 10,
    label = "Root_Ext-3R-R_4R!H->F_Ext-3R-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.075531,'m^3/(mol*s)'), n=2.28113, w0=(309.5,'kJ/mol'), E0=(32.3349,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22795276976069423, var=8.273831447921705, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-3R-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_N-5R!H->C
    Total Standard Deviation in ln(k): 6.339219464963295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.339219464963295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.339219464963295
""",
)

entry(
    index = 11,
    label = "Root_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.00721,'m^3/(mol*s)'), n=2.333, w0=(309.5,'kJ/mol'), E0=(58.1492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.0137305,'m^3/(mol*s)'), n=2.41011, w0=(306.682,'kJ/mol'), E0=(33.0911,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07612407143410618, var=0.8849841741560049, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 2.0771929182538793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 2.0771929182538793""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 2.0771929182538793
""",
)

entry(
    index = 13,
    label = "Root_N-3R->Cl_N-3BrCHOS->Br_3CH->H",
    kinetics = ArrheniusBM(A=(108625,'m^3/(mol*s)'), n=5.5697e-06, w0=(342,'kJ/mol'), E0=(41.9179,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23268370907548702, var=3.3298902215117967, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->Cl_N-3BrCHOS->Br_3CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->Cl_N-3BrCHOS->Br_3CH->H
    Total Standard Deviation in ln(k): 4.242870357282385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->Cl_N-3BrCHOS->Br_3CH->H
Total Standard Deviation in ln(k): 4.242870357282385""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->Cl_N-3BrCHOS->Br_3CH->H
Total Standard Deviation in ln(k): 4.242870357282385
""",
)

entry(
    index = 14,
    label = "Root_N-3R->Cl_N-3BrCHOS->Br_N-3CH->H",
    kinetics = ArrheniusBM(A=(9.27207,'m^3/(mol*s)'), n=1.95144, w0=(309.5,'kJ/mol'), E0=(41.8695,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4047078942019269, var=12.376966522630028, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->Cl_N-3BrCHOS->Br_N-3CH->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->Cl_N-3BrCHOS->Br_N-3CH->H
    Total Standard Deviation in ln(k): 10.582257890513393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->Cl_N-3BrCHOS->Br_N-3CH->H
Total Standard Deviation in ln(k): 10.582257890513393""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->Cl_N-3BrCHOS->Br_N-3CH->H
Total Standard Deviation in ln(k): 10.582257890513393
""",
)

entry(
    index = 15,
    label = "Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.43058e+16,'m^3/(mol*s)'), n=-5.19408, w0=(726.118,'kJ/mol'), E0=(186.967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(1.03077e-05,'m^3/(mol*s)'), n=2.72017, w0=(309.5,'kJ/mol'), E0=(35.6808,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20893547531912984, var=11.98637947863966, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 7.465627191577474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 7.465627191577474""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 7.465627191577474
""",
)

entry(
    index = 17,
    label = "Root_Ext-3R-R_4R!H->F_Ext-3R-R_N-5R!H->C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(0.0496072,'m^3/(mol*s)'), n=2.48433, w0=(309.5,'kJ/mol'), E0=(31.9309,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-3R-R_N-5R!H->C_Ext-3R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_N-5R!H->C_Ext-3R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_N-5R!H->C_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_N-5R!H->C_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_3R->O",
    kinetics = ArrheniusBM(A=(34.1,'m^3/(mol*s)'), n=4.7991e-09, w0=(315.5,'kJ/mol'), E0=(36.7874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_3R->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_3R->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_3R->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_3R->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O",
    kinetics = ArrheniusBM(A=(0.0270326,'m^3/(mol*s)'), n=2.32845, w0=(305.8,'kJ/mol'), E0=(33.8831,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05869694404230775, var=0.675098909608607, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O
    Total Standard Deviation in ln(k): 1.7946583640131002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O
Total Standard Deviation in ln(k): 1.7946583640131002""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O
Total Standard Deviation in ln(k): 1.7946583640131002
""",
)

entry(
    index = 20,
    label = "Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(6.85508e-05,'m^3/(mol*s)'), n=2.34542, w0=(309.5,'kJ/mol'), E0=(39.82,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(0.00136302,'m^3/(mol*s)'), n=2.25138, w0=(309.5,'kJ/mol'), E0=(38.8513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-3R-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_3CS-inRing",
    kinetics = ArrheniusBM(A=(1.48e+06,'m^3/(mol*s)'), n=4.98146e-08, w0=(309.5,'kJ/mol'), E0=(55.5346,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_3CS-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_3CS-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_3CS-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_3CS-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing",
    kinetics = ArrheniusBM(A=(0.0170184,'m^3/(mol*s)'), n=2.38939, w0=(305.389,'kJ/mol'), E0=(33.5661,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04203530249521301, var=0.7793306182878785, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing
    Total Standard Deviation in ln(k): 1.8753905352939237"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing
Total Standard Deviation in ln(k): 1.8753905352939237""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing
Total Standard Deviation in ln(k): 1.8753905352939237
""",
)

entry(
    index = 24,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C",
    kinetics = ArrheniusBM(A=(0.0186886,'m^3/(mol*s)'), n=2.3775, w0=(309.5,'kJ/mol'), E0=(33.7089,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04299247875111058, var=0.7526859696895724, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C
    Total Standard Deviation in ln(k): 1.8472788633836625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C
Total Standard Deviation in ln(k): 1.8472788633836625""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C
Total Standard Deviation in ln(k): 1.8472788633836625
""",
)

entry(
    index = 25,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_N-3CS->C",
    kinetics = ArrheniusBM(A=(0.0785,'m^3/(mol*s)'), n=2.33, w0=(272.5,'kJ/mol'), E0=(17.1121,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_N-3CS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_N-3CS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_N-3CS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_N-3CS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(86.1,'m^3/(mol*s)'), n=1.36, w0=(309.5,'kJ/mol'), E0=(38.8426,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(0.0189435,'m^3/(mol*s)'), n=2.37558, w0=(309.5,'kJ/mol'), E0=(33.8706,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03691983055621024, var=0.7602753465265254, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C
    Total Standard Deviation in ln(k): 1.840767478774243"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C
Total Standard Deviation in ln(k): 1.840767478774243""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C
Total Standard Deviation in ln(k): 1.840767478774243
""",
)

entry(
    index = 28,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(151000,'m^3/(mol*s)'), n=6.17307e-09, w0=(309.5,'kJ/mol'), E0=(55.453,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_N-Sp-4C-3C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00190559,'m^3/(mol*s)'), n=2.65246, w0=(309.5,'kJ/mol'), E0=(30.2549,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2826513266861106, var=0.0040476207964420885, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R
    Total Standard Deviation in ln(k): 0.8377222922787554"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R
Total Standard Deviation in ln(k): 0.8377222922787554""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R
Total Standard Deviation in ln(k): 0.8377222922787554
""",
)

entry(
    index = 30,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(65100,'m^3/(mol*s)'), n=0.45, w0=(309.5,'kJ/mol'), E0=(48.6277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000781605,'m^3/(mol*s)'), n=2.76695, w0=(309.5,'kJ/mol'), E0=(29.4531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->O_N-3R->O_N-3CS-inRing_3CS->C_Sp-4C-3C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

