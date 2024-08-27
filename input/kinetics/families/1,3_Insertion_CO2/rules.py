#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/rules"
shortDesc = ""
longDesc = """
572 - 575 Some of the tortional motions in the alkyl part of the 
transition states are treated as free rotations as they are relatively loose TSs. 

The dictionary defines CO2 in two ways, allowing the R-R' to insert either way
around. However, there are only rates for one of these ways. The other is
presumably matching the top level node.
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(7.95348e-39,'m^3/(mol*s)'), n=13.0658, w0=(838.656,'kJ/mol'), E0=(199.804,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5326144378166825, var=63.374534123131895, Tref=1000.0, N=16, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 16 training reactions at node Root
    Total Standard Deviation in ln(k): 17.297547100471956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root
Total Standard Deviation in ln(k): 17.297547100471956""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root
Total Standard Deviation in ln(k): 17.297547100471956
""",
)

entry(
    index = 2,
    label = "Root_5R->C",
    kinetics = ArrheniusBM(A=(0.000281644,'m^3/(mol*s)'), n=2.93535, w0=(815,'kJ/mol'), E0=(321.814,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-17.045790163455024, var=569.8865692638138, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5R->C',), comment="""BM rule fitted to 2 training reactions at node Root_5R->C
    Total Standard Deviation in ln(k): 90.68624989367476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5R->C
Total Standard Deviation in ln(k): 90.68624989367476""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5R->C
Total Standard Deviation in ln(k): 90.68624989367476
""",
)

entry(
    index = 3,
    label = "Root_N-5R->C",
    kinetics = ArrheniusBM(A=(3.02885e-42,'m^3/(mol*s)'), n=14.0674, w0=(842.036,'kJ/mol'), E0=(187.877,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5404253112424251, var=67.47146341942634, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-5R->C',), comment="""BM rule fitted to 14 training reactions at node Root_N-5R->C
    Total Standard Deviation in ln(k): 17.824949943124036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-5R->C
Total Standard Deviation in ln(k): 17.824949943124036""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-5R->C
Total Standard Deviation in ln(k): 17.824949943124036
""",
)

entry(
    index = 4,
    label = "Root_5R->C_4R->C",
    kinetics = ArrheniusBM(A=(7.3e-05,'m^3/(mol*s)'), n=3.13, w0=(954.373,'kJ/mol'), E0=(459.986,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->C_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_5R->C_N-4R->C",
    kinetics = ArrheniusBM(A=(0.000312353,'m^3/(mol*s)'), n=2.92234, w0=(884.5,'kJ/mol'), E0=(321.212,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->C_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->C_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-5R->C_4R->F",
    kinetics = ArrheniusBM(A=(2.38939e-08,'m^3/(mol*s)'), n=4.04963, w0=(975,'kJ/mol'), E0=(140.031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_4R->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_4R->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_4R->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_4R->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-5R->C_N-4R->F",
    kinetics = ArrheniusBM(A=(1.9172e-46,'m^3/(mol*s)'), n=15.3021, w0=(831.808,'kJ/mol'), E0=(191.134,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5940221314637297, var=45.00698403484252, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F',), comment="""BM rule fitted to 13 training reactions at node Root_N-5R->C_N-4R->F
    Total Standard Deviation in ln(k): 14.941733190889785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-5R->C_N-4R->F
Total Standard Deviation in ln(k): 14.941733190889785""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-5R->C_N-4R->F
Total Standard Deviation in ln(k): 14.941733190889785
""",
)

entry(
    index = 8,
    label = "Root_N-5R->C_N-4R->F_4CH->C",
    kinetics = ArrheniusBM(A=(2.70411e-47,'m^3/(mol*s)'), n=15.5468, w0=(828.5,'kJ/mol'), E0=(189.202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6128718629185259, var=46.06228445448083, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-5R->C_N-4R->F_4CH->C
    Total Standard Deviation in ln(k): 15.14585584608024"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-5R->C_N-4R->F_4CH->C
Total Standard Deviation in ln(k): 15.14585584608024""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-5R->C_N-4R->F_4CH->C
Total Standard Deviation in ln(k): 15.14585584608024
""",
)

entry(
    index = 9,
    label = "Root_N-5R->C_N-4R->F_N-4CH->C",
    kinetics = ArrheniusBM(A=(1510,'m^3/(mol*s)'), n=1.23, w0=(871.5,'kJ/mol'), E0=(301.639,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.31504e-48,'m^3/(mol*s)'), n=15.776, w0=(828.5,'kJ/mol'), E0=(186.98,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6197810035316649, var=47.17088466654267, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R
    Total Standard Deviation in ln(k): 15.325972392886799"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R
Total Standard Deviation in ln(k): 15.325972392886799""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R
Total Standard Deviation in ln(k): 15.325972392886799
""",
)

entry(
    index = 11,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_6R!H-u1",
    kinetics = ArrheniusBM(A=(2.04642e-14,'m^3/(mol*s)'), n=5.39471, w0=(828.5,'kJ/mol'), E0=(114.893,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_6R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_6R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_6R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_6R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1",
    kinetics = ArrheniusBM(A=(7.17175e-52,'m^3/(mol*s)'), n=16.9469, w0=(828.5,'kJ/mol'), E0=(196.296,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6118589858552823, var=14.321016656799332, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1',), comment="""BM rule fitted to 10 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1
    Total Standard Deviation in ln(k): 9.123876971616424"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1
Total Standard Deviation in ln(k): 9.123876971616424""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1
Total Standard Deviation in ln(k): 9.123876971616424
""",
)

entry(
    index = 13,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C",
    kinetics = ArrheniusBM(A=(5.2253e-50,'m^3/(mol*s)'), n=16.4316, w0=(828.5,'kJ/mol'), E0=(197.239,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6164703424571195, var=12.331990924259715, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C
    Total Standard Deviation in ln(k): 8.588935509405324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C
Total Standard Deviation in ln(k): 8.588935509405324""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C
Total Standard Deviation in ln(k): 8.588935509405324
""",
)

entry(
    index = 14,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.68462e-61,'m^3/(mol*s)'), n=19.4743, w0=(828.5,'kJ/mol'), E0=(200.137,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(2.76559e-52,'m^3/(mol*s)'), n=17.1015, w0=(828.5,'kJ/mol'), E0=(191.86,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.62557033274967, var=13.163522401489004, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R
    Total Standard Deviation in ln(k): 8.84527813463752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 8.84527813463752""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 8.84527813463752
""",
)

entry(
    index = 16,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.106,'m^3/(mol*s)'), n=2.13, w0=(828.5,'kJ/mol'), E0=(312.367,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_7R!H-u1",
    kinetics = ArrheniusBM(A=(7.34947e-60,'m^3/(mol*s)'), n=19.0378, w0=(828.5,'kJ/mol'), E0=(194.759,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_7R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_7R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_7R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_7R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1",
    kinetics = ArrheniusBM(A=(2.05904e-50,'m^3/(mol*s)'), n=16.6042, w0=(828.5,'kJ/mol'), E0=(192.882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6219178516867071, var=9.963451074098401, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1
    Total Standard Deviation in ln(k): 7.890540863654595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1
Total Standard Deviation in ln(k): 7.890540863654595""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1
Total Standard Deviation in ln(k): 7.890540863654595
""",
)

entry(
    index = 19,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O",
    kinetics = ArrheniusBM(A=(1.43704e-42,'m^3/(mol*s)'), n=14.2172, w0=(828.5,'kJ/mol'), E0=(204.525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6576773119599859, var=0.2537607371759542, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O
    Total Standard Deviation in ln(k): 2.6623342361360267"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 2.6623342361360267""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 2.6623342361360267
""",
)

entry(
    index = 20,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(1.62295e-58,'m^3/(mol*s)'), n=19.0655, w0=(828.5,'kJ/mol'), E0=(180.576,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5817325355705631, var=38.620520117037685, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 13.92014791378812"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 13.92014791378812""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 13.92014791378812
""",
)

entry(
    index = 21,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C",
    kinetics = ArrheniusBM(A=(6.89256e-41,'m^3/(mol*s)'), n=13.6746, w0=(828.5,'kJ/mol'), E0=(204.405,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6862868745850565, var=0.3236849977908273, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C
    Total Standard Deviation in ln(k): 2.8648992442649273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C
Total Standard Deviation in ln(k): 2.8648992442649273""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C
Total Standard Deviation in ln(k): 2.8648992442649273
""",
)

entry(
    index = 22,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(6.53205e-46,'m^3/(mol*s)'), n=15.297, w0=(828.5,'kJ/mol'), E0=(204.813,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C",
    kinetics = ArrheniusBM(A=(1.21101e-55,'m^3/(mol*s)'), n=18.4099, w0=(828.5,'kJ/mol'), E0=(178.108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5099795531113656, var=8.362790889634976, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C
    Total Standard Deviation in ln(k): 7.078746876854606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C
Total Standard Deviation in ln(k): 7.078746876854606""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C
Total Standard Deviation in ln(k): 7.078746876854606
""",
)

entry(
    index = 24,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_N-7R!H->C",
    kinetics = ArrheniusBM(A=(5.60757e-58,'m^3/(mol*s)'), n=18.5763, w0=(828.5,'kJ/mol'), E0=(201.125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(1.19876e-39,'m^3/(mol*s)'), n=13.3095, w0=(828.5,'kJ/mol'), E0=(205.515,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(3.96304e-42,'m^3/(mol*s)'), n=14.0396, w0=(828.5,'kJ/mol'), E0=(203.295,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C_Ext-7C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(8.09887e-56,'m^3/(mol*s)'), n=18.555, w0=(828.5,'kJ/mol'), E0=(174.239,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C_Ext-7C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C_Ext-7C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C_Ext-7C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.47701e-55,'m^3/(mol*s)'), n=18.2259, w0=(828.5,'kJ/mol'), E0=(182.314,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C_Ext-7C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C_Ext-7C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_4CH->C_Ext-4C-R_N-6R!H-u1_6R!H->C_Ext-6C-R_N-7R!H-u1_Ext-6C-R_Ext-6C-R_N-8R!H->O_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

