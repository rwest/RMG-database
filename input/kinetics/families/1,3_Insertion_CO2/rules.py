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
    kinetics = ArrheniusBM(A=(3.40949e-46,'m^3/(mol*s)'), n=15.1422, w0=(835.975,'kJ/mol'), E0=(179.934,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.44440657317388366, var=68.31937884553562, Tref=1000.0, N=20, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 20 training reactions at node Root
    Total Standard Deviation in ln(k): 17.686844973029643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 17.686844973029643""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 17.686844973029643
""",
)

entry(
    index = 2,
    label = "Root_5R->C",
    kinetics = ArrheniusBM(A=(7.3e-05,'m^3/(mol*s)'), n=3.13, w0=(897.745,'kJ/mol'), E0=(398.189,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-5R->C",
    kinetics = ArrheniusBM(A=(3.81132e-46,'m^3/(mol*s)'), n=15.1284, w0=(840.737,'kJ/mol'), E0=(180.019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.44271310384946383, var=68.27836744813347, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-5R->C',), comment="""BM rule fitted to 19 training reactions at node Root_N-5R->C
    Total Standard Deviation in ln(k): 17.677615807182292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-5R->C
Total Standard Deviation in ln(k): 17.677615807182292""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-5R->C
Total Standard Deviation in ln(k): 17.677615807182292
""",
)

entry(
    index = 4,
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
    index = 5,
    label = "Root_N-5R->C_N-4R->F",
    kinetics = ArrheniusBM(A=(6.73917e-48,'m^3/(mol*s)'), n=15.6476, w0=(833.278,'kJ/mol'), E0=(184.815,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4406272870122825, var=53.837482423974635, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F',), comment="""BM rule fitted to 18 training reactions at node Root_N-5R->C_N-4R->F
    Total Standard Deviation in ln(k): 15.816652858049535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-5R->C_N-4R->F
Total Standard Deviation in ln(k): 15.816652858049535""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-5R->C_N-4R->F
Total Standard Deviation in ln(k): 15.816652858049535
""",
)

entry(
    index = 6,
    label = "Root_N-5R->C_N-4R->F_4CH->H",
    kinetics = ArrheniusBM(A=(7.16328e-49,'m^3/(mol*s)'), n=15.982, w0=(871.5,'kJ/mol'), E0=(171.386,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7706566526278554, var=1.0078835581168786, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->H
    Total Standard Deviation in ln(k): 3.948945034630588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 3.948945034630588""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 3.948945034630588
""",
)

entry(
    index = 7,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H",
    kinetics = ArrheniusBM(A=(1.82681e-47,'m^3/(mol*s)'), n=15.5187, w0=(828.5,'kJ/mol'), E0=(186.849,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.492979607700487, var=59.44560530419492, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H',), comment="""BM rule fitted to 16 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H
    Total Standard Deviation in ln(k): 16.695345378604706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 16.695345378604706""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 16.695345378604706
""",
)

entry(
    index = 8,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.12912e-48,'m^3/(mol*s)'), n=15.6675, w0=(828.5,'kJ/mol'), E0=(183.865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.529636565414701, var=66.12065232468231, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R
    Total Standard Deviation in ln(k): 17.632169537472638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 17.632169537472638""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 17.632169537472638
""",
)

entry(
    index = 9,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1",
    kinetics = ArrheniusBM(A=(5.31987e-14,'m^3/(mol*s)'), n=5.1973, w0=(828.5,'kJ/mol'), E0=(106.434,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5658078427683028, var=2.8035422043702223, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1
    Total Standard Deviation in ln(k): 4.778312364859505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1
Total Standard Deviation in ln(k): 4.778312364859505""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1
Total Standard Deviation in ln(k): 4.778312364859505
""",
)

entry(
    index = 10,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1",
    kinetics = ArrheniusBM(A=(2.32218e-49,'m^3/(mol*s)'), n=16.193, w0=(828.5,'kJ/mol'), E0=(212.013,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.37540720633536695, var=10.345955005634364, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1',), comment="""BM rule fitted to 12 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1
    Total Standard Deviation in ln(k): 7.391490352545394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1
Total Standard Deviation in ln(k): 7.391490352545394""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1
Total Standard Deviation in ln(k): 7.391490352545394
""",
)

entry(
    index = 11,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.04642e-14,'m^3/(mol*s)'), n=5.39471, w0=(828.5,'kJ/mol'), E0=(114.893,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F",
    kinetics = ArrheniusBM(A=(7.27053e-52,'m^3/(mol*s)'), n=17.0222, w0=(828.5,'kJ/mol'), E0=(209.734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.38132359425798007, var=13.856630163390701, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F
    Total Standard Deviation in ln(k): 8.420624538124851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F
Total Standard Deviation in ln(k): 8.420624538124851""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F
Total Standard Deviation in ln(k): 8.420624538124851
""",
)

entry(
    index = 13,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F",
    kinetics = ArrheniusBM(A=(4.70674e-43,'m^3/(mol*s)'), n=14.0009, w0=(828.5,'kJ/mol'), E0=(214.048,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.25149915223623975, var=2.876854816985189, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F
    Total Standard Deviation in ln(k): 4.03219744804729"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F
Total Standard Deviation in ln(k): 4.03219744804729""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F
Total Standard Deviation in ln(k): 4.03219744804729
""",
)

entry(
    index = 14,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(2.99715e-35,'m^3/(mol*s)'), n=12.2861, w0=(828.5,'kJ/mol'), E0=(258.309,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05106874703806558, var=5.043469209434383, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O
    Total Standard Deviation in ln(k): 4.630481222103784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O
Total Standard Deviation in ln(k): 4.630481222103784""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O
Total Standard Deviation in ln(k): 4.630481222103784
""",
)

entry(
    index = 15,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(1.90556e-60,'m^3/(mol*s)'), n=19.4663, w0=(828.5,'kJ/mol'), E0=(184.505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.59384195871193, var=26.695322728241386, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 11.850033514233662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.850033514233662""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.850033514233662
""",
)

entry(
    index = 16,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_6CO->O",
    kinetics = ArrheniusBM(A=(1.32726e-49,'m^3/(mol*s)'), n=15.8694, w0=(828.5,'kJ/mol'), E0=(198.63,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4433212133734884, var=2.3876224331846623, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_6CO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_6CO->O
    Total Standard Deviation in ln(k): 4.211575669379599"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_6CO->O
Total Standard Deviation in ln(k): 4.211575669379599""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_6CO->O
Total Standard Deviation in ln(k): 4.211575669379599
""",
)

entry(
    index = 17,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_N-6CO->O",
    kinetics = ArrheniusBM(A=(0.0364844,'m^3/(mol*s)'), n=2.33619, w0=(828.5,'kJ/mol'), E0=(310.299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4322094692883043, var=4.958994637547457, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_N-6CO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_N-6CO->O
    Total Standard Deviation in ln(k): 5.550257935999257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_N-6CO->O
Total Standard Deviation in ln(k): 5.550257935999257""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_N-6CO->O
Total Standard Deviation in ln(k): 5.550257935999257
""",
)

entry(
    index = 18,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(4.58884e-33,'m^3/(mol*s)'), n=11.6902, w0=(828.5,'kJ/mol'), E0=(258.951,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.022482401776918383, var=0.32349495566431863, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 1.1967139376776934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C
Total Standard Deviation in ln(k): 1.1967139376776934""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C
Total Standard Deviation in ln(k): 1.1967139376776934
""",
)

entry(
    index = 19,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(4.42654e-39,'m^3/(mol*s)'), n=13.3234, w0=(828.5,'kJ/mol'), E0=(258.376,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1.58356e-59,'m^3/(mol*s)'), n=19.2519, w0=(828.5,'kJ/mol'), E0=(182.445,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5974853391217698, var=31.300883504909947, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 12.717149377007305"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C
Total Standard Deviation in ln(k): 12.717149377007305""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C
Total Standard Deviation in ln(k): 12.717149377007305
""",
)

entry(
    index = 21,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_N-7BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.68462e-61,'m^3/(mol*s)'), n=19.4743, w0=(828.5,'kJ/mol'), E0=(200.137,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_N-7BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_N-7BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_N-7BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_N-7BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_6CO->O_Ext-6O-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.53097e-49,'m^3/(mol*s)'), n=15.9077, w0=(828.5,'kJ/mol'), E0=(201.977,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_6CO->O_Ext-6O-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_6CO->O_Ext-6O-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_6CO->O_Ext-6O-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_6CO->O_Ext-6O-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_N-6CO->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.106,'m^3/(mol*s)'), n=2.13, w0=(828.5,'kJ/mol'), E0=(313.844,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_N-6CO->O_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_N-6CO->O_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_N-6CO->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->F_N-6CO->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(7.97967e-32,'m^3/(mol*s)'), n=11.3252, w0=(828.5,'kJ/mol'), E0=(260.079,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(2.63889e-34,'m^3/(mol*s)'), n=12.0552, w0=(828.5,'kJ/mol'), E0=(257.823,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H-u1",
    kinetics = ArrheniusBM(A=(7.34947e-60,'m^3/(mol*s)'), n=19.0378, w0=(828.5,'kJ/mol'), E0=(194.759,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1",
    kinetics = ArrheniusBM(A=(1.62293e-58,'m^3/(mol*s)'), n=19.0656, w0=(828.5,'kJ/mol'), E0=(180.576,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5817325394409504, var=38.620518502250846, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1
    Total Standard Deviation in ln(k): 13.920147663057445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1
Total Standard Deviation in ln(k): 13.920147663057445""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1
Total Standard Deviation in ln(k): 13.920147663057445
""",
)

entry(
    index = 28,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C",
    kinetics = ArrheniusBM(A=(1.211e-55,'m^3/(mol*s)'), n=18.4099, w0=(828.5,'kJ/mol'), E0=(178.108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.509979553111372, var=8.36279088963492, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C
    Total Standard Deviation in ln(k): 7.078746876854603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C
Total Standard Deviation in ln(k): 7.078746876854603""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C
Total Standard Deviation in ln(k): 7.078746876854603
""",
)

entry(
    index = 29,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_N-8R!H->C",
    kinetics = ArrheniusBM(A=(5.60757e-58,'m^3/(mol*s)'), n=18.5763, w0=(828.5,'kJ/mol'), E0=(201.125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(8.09887e-56,'m^3/(mol*s)'), n=18.555, w0=(828.5,'kJ/mol'), E0=(174.239,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.47701e-55,'m^3/(mol*s)'), n=18.2259, w0=(828.5,'kJ/mol'), E0=(182.314,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->F_Ext-4C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

