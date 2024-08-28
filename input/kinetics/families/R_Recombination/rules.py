#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/rules"
shortDesc = ""
longDesc = """
For some reason the definition of Cs_rad::

 Cs_rad
 1 * C 1 

which is not mutually exclusive from its L2 siblings such as::

 Cd_rad
 1 * C 1 {2,D}, {3,S}
 2   C 0 {1,D}
 3   R 0 {1,S}

is apparently not causing a problem
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(22550.3,'m^3/(mol*s)'), n=0.777973, w0=(184.932,'kJ/mol'), E0=(64.2014,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12127497985143244, var=25.567990914774224, Tref=1000.0, N=368, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 368 training reactions at node Root
    Total Standard Deviation in ln(k): 10.441614012036363"""),
    rank = 11,
    shortDesc = """BM rule fitted to 368 training reactions at node Root
Total Standard Deviation in ln(k): 10.441614012036363""",
    longDesc = 
"""
BM rule fitted to 368 training reactions at node Root
Total Standard Deviation in ln(k): 10.441614012036363
""",
)

entry(
    index = 2,
    label = "Root_1R-inRing",
    kinetics = ArrheniusBM(A=(8.48393e+10,'m^3/(mol*s)'), n=-1.02738, w0=(190.107,'kJ/mol'), E0=(92.3465,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0487334454380854, var=1.9549347327596756, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_1R-inRing',), comment="""BM rule fitted to 28 training reactions at node Root_1R-inRing
    Total Standard Deviation in ln(k): 2.925445991148266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_1R-inRing
Total Standard Deviation in ln(k): 2.925445991148266""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_1R-inRing
Total Standard Deviation in ln(k): 2.925445991148266
""",
)

entry(
    index = 3,
    label = "Root_N-1R-inRing",
    kinetics = ArrheniusBM(A=(12369.9,'m^3/(mol*s)'), n=0.846222, w0=(185.755,'kJ/mol'), E0=(64.5344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16112236157949886, var=27.204396092322924, Tref=1000.0, N=340, data_mean=0.0, correlation='Root_N-1R-inRing',), comment="""BM rule fitted to 340 training reactions at node Root_N-1R-inRing
    Total Standard Deviation in ln(k): 10.861093918609614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 340 training reactions at node Root_N-1R-inRing
Total Standard Deviation in ln(k): 10.861093918609614""",
    longDesc = 
"""
BM rule fitted to 340 training reactions at node Root_N-1R-inRing
Total Standard Deviation in ln(k): 10.861093918609614
""",
)

entry(
    index = 4,
    label = "Root_1R-inRing_2R->O",
    kinetics = ArrheniusBM(A=(1.90891e+06,'m^3/(mol*s)'), n=0.0381637, w0=(179,'kJ/mol'), E0=(43.5106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03546201418563302, var=0.4381627496362536, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R-inRing_2R->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R-inRing_2R->O
    Total Standard Deviation in ln(k): 1.4161121284194658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R-inRing_2R->O
Total Standard Deviation in ln(k): 1.4161121284194658""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R-inRing_2R->O
Total Standard Deviation in ln(k): 1.4161121284194658
""",
)

entry(
    index = 5,
    label = "Root_1R-inRing_N-2R->O",
    kinetics = ArrheniusBM(A=(3.35757e+08,'m^3/(mol*s)'), n=-0.23432, w0=(191.958,'kJ/mol'), E0=(88.3754,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012914222317034664, var=2.735353537967276, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O',), comment="""BM rule fitted to 24 training reactions at node Root_1R-inRing_N-2R->O
    Total Standard Deviation in ln(k): 3.3480599439669354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_1R-inRing_N-2R->O
Total Standard Deviation in ln(k): 3.3480599439669354""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_1R-inRing_N-2R->O
Total Standard Deviation in ln(k): 3.3480599439669354
""",
)

entry(
    index = 6,
    label = "Root_N-1R-inRing_1R->F",
    kinetics = ArrheniusBM(A=(4.14373e-06,'m^3/(mol*s)'), n=3.17868, w0=(286.811,'kJ/mol'), E0=(28.6811,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2715026717610398, var=58.975730897059144, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_1R->F
    Total Standard Deviation in ln(k): 16.077662458083473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_1R->F
Total Standard Deviation in ln(k): 16.077662458083473""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_1R->F
Total Standard Deviation in ln(k): 16.077662458083473
""",
)

entry(
    index = 7,
    label = "Root_N-1R-inRing_N-1R->F",
    kinetics = ArrheniusBM(A=(622543,'m^3/(mol*s)'), n=0.37885, w0=(182.692,'kJ/mol'), E0=(85.6293,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.031014374458344752, var=24.688654502024576, Tref=1000.0, N=330, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F',), comment="""BM rule fitted to 330 training reactions at node Root_N-1R-inRing_N-1R->F
    Total Standard Deviation in ln(k): 10.038988876216983"""),
    rank = 11,
    shortDesc = """BM rule fitted to 330 training reactions at node Root_N-1R-inRing_N-1R->F
Total Standard Deviation in ln(k): 10.038988876216983""",
    longDesc = 
"""
BM rule fitted to 330 training reactions at node Root_N-1R-inRing_N-1R->F
Total Standard Deviation in ln(k): 10.038988876216983
""",
)

entry(
    index = 8,
    label = "Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.6229e+06,'m^3/(mol*s)'), n=-0.00476945, w0=(179,'kJ/mol'), E0=(41.2931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.97515e+06,'m^3/(mol*s)'), n=-0.00323035, w0=(179,'kJ/mol'), E0=(42.7163,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->C",
    kinetics = ArrheniusBM(A=(1.26173e+09,'m^3/(mol*s)'), n=-0.614843, w0=(190.901,'kJ/mol'), E0=(21.0947,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.011178639048893173, var=0.26322627303330903, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->C',), comment="""BM rule fitted to 10 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C
    Total Standard Deviation in ln(k): 1.0566280290611583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C
Total Standard Deviation in ln(k): 1.0566280290611583""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C
Total Standard Deviation in ln(k): 1.0566280290611583
""",
)

entry(
    index = 11,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C",
    kinetics = ArrheniusBM(A=(3.59291e+08,'m^3/(mol*s)'), n=-0.14961, w0=(205.5,'kJ/mol'), E0=(99.1137,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.025230312686491178, var=2.9455079525908534, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C',), comment="""BM rule fitted to 14 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C
    Total Standard Deviation in ln(k): 3.5040157535562955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C
Total Standard Deviation in ln(k): 3.5040157535562955""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C
Total Standard Deviation in ln(k): 3.5040157535562955
""",
)

entry(
    index = 12,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.77828e-08,'m^3/(mol*s)'), n=3.67849, w0=(298.619,'kJ/mol'), E0=(29.8619,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31564352566031106, var=60.0537891615979, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 16.32864435381591"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 16.32864435381591""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 16.32864435381591
""",
)

entry(
    index = 13,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_3R!H->O",
    kinetics = ArrheniusBM(A=(1e+06,'m^3/(mol*s)'), n=0, w0=(255.23,'kJ/mol'), E0=(127.615,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_3R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(1.1418e+08,'m^3/(mol*s)'), n=-0.286048, w0=(261.275,'kJ/mol'), E0=(95.4103,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1698219849290636, var=2.775505017416308, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O
    Total Standard Deviation in ln(k): 6.279109182970643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O
Total Standard Deviation in ln(k): 6.279109182970643""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O
Total Standard Deviation in ln(k): 6.279109182970643
""",
)

entry(
    index = 15,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S",
    kinetics = ArrheniusBM(A=(181562,'m^3/(mol*s)'), n=0.790398, w0=(143.909,'kJ/mol'), E0=(19.457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07669228625122698, var=5.298790955838148, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S
    Total Standard Deviation in ln(k): 4.807414478020215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S
Total Standard Deviation in ln(k): 4.807414478020215""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S
Total Standard Deviation in ln(k): 4.807414478020215
""",
)

entry(
    index = 16,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S",
    kinetics = ArrheniusBM(A=(3.62374e+06,'m^3/(mol*s)'), n=0.0920865, w0=(184.265,'kJ/mol'), E0=(111.914,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09082893252753682, var=27.347503405718207, Tref=1000.0, N=319, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S',), comment="""BM rule fitted to 319 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S
    Total Standard Deviation in ln(k): 10.71194350551679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 319 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S
Total Standard Deviation in ln(k): 10.71194350551679""",
    longDesc = 
"""
BM rule fitted to 319 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S
Total Standard Deviation in ln(k): 10.71194350551679
""",
)

entry(
    index = 17,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(1.64652e+10,'m^3/(mol*s)'), n=-0.959714, w0=(173,'kJ/mol'), E0=(33.7245,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09367025166372299, var=0.36713088084725354, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R',), comment="""BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R
    Total Standard Deviation in ln(k): 1.4500479609402603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R
Total Standard Deviation in ln(k): 1.4500479609402603""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R
Total Standard Deviation in ln(k): 1.4500479609402603
""",
)

entry(
    index = 18,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(1.00531e+09,'m^3/(mol*s)'), n=-0.575959, w0=(219.772,'kJ/mol'), E0=(118.697,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005789413300265933, var=0.26041095707090806, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R',), comment="""BM rule fitted to 6 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R
    Total Standard Deviation in ln(k): 1.0375721347697802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 1.0375721347697802""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 1.0375721347697802
""",
)

entry(
    index = 19,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.62382e+10,'m^3/(mol*s)'), n=-0.658072, w0=(205.5,'kJ/mol'), E0=(124.946,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0393643864394397, var=13.285346387383807, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 9.918541045275036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 9.918541045275036""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 9.918541045275036
""",
)

entry(
    index = 20,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(4.42592e+07,'m^3/(mol*s)'), n=0.134893, w0=(205.5,'kJ/mol'), E0=(82.0945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08996108806766272, var=0.25047067524989414, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 1.2293435587709212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.2293435587709212""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.2293435587709212
""",
)

entry(
    index = 21,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.43891e-18,'m^3/(mol*s)'), n=6.43993, w0=(330.899,'kJ/mol'), E0=(33.0899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.498963972089182, var=9.073827303693635, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 7.29250053786487"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 7.29250053786487""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 7.29250053786487
""",
)

entry(
    index = 22,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(4.17854e+07,'m^3/(mol*s)'), n=-0.265153, w0=(255.578,'kJ/mol'), E0=(220.784,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04456806303368258, var=0.5080232584609017, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.540870026345269"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.540870026345269""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.540870026345269
""",
)

entry(
    index = 23,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O_3BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(259.855,'kJ/mol'), E0=(129.927,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O_3BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O_3BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O_3BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O_3BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O_N-3BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1.14662e+08,'m^3/(mol*s)'), n=-0.287508, w0=(262.695,'kJ/mol'), E0=(131.348,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O_N-3BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O_N-3BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O_N-3BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_N-3R!H->O_N-3BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_2R->H",
    kinetics = ArrheniusBM(A=(1.676e+07,'m^3/(mol*s)'), n=0.496549, w0=(181.5,'kJ/mol'), E0=(44.7624,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.5291918295868276, var=20.635194422375754, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_2R->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_2R->H
    Total Standard Deviation in ln(k): 15.461458415551279"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_2R->H
Total Standard Deviation in ln(k): 15.461458415551279""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_2R->H
Total Standard Deviation in ln(k): 15.461458415551279
""",
)

entry(
    index = 26,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H",
    kinetics = ArrheniusBM(A=(74997.8,'m^3/(mol*s)'), n=0.851454, w0=(129.812,'kJ/mol'), E0=(15.7351,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03769384279176273, var=4.863804081318706, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H
    Total Standard Deviation in ln(k): 4.515957669226741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H
Total Standard Deviation in ln(k): 4.515957669226741""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H
Total Standard Deviation in ln(k): 4.515957669226741
""",
)

entry(
    index = 27,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C",
    kinetics = ArrheniusBM(A=(5.93713e+07,'m^3/(mol*s)'), n=-0.267261, w0=(189.115,'kJ/mol'), E0=(148.347,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.095956193862517, var=25.662898186132736, Tref=1000.0, N=296, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C',), comment="""BM rule fitted to 296 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C
    Total Standard Deviation in ln(k): 10.396795416883133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 296 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C
Total Standard Deviation in ln(k): 10.396795416883133""",
    longDesc = 
"""
BM rule fitted to 296 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C
Total Standard Deviation in ln(k): 10.396795416883133
""",
)

entry(
    index = 28,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C",
    kinetics = ArrheniusBM(A=(2.74888e+08,'m^3/(mol*s)'), n=-0.264449, w0=(136.804,'kJ/mol'), E0=(59.8442,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4668744664022471, var=3.6916922491526507, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C
    Total Standard Deviation in ln(k): 5.02490468641507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C
Total Standard Deviation in ln(k): 5.02490468641507""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C
Total Standard Deviation in ln(k): 5.02490468641507
""",
)

entry(
    index = 29,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_2C-inRing",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=-4.2422e-08, w0=(173,'kJ/mol'), E0=(52.9253,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_2C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_2C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_2C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_2C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing",
    kinetics = ArrheniusBM(A=(3.13485e+11,'m^3/(mol*s)'), n=-1.32812, w0=(173,'kJ/mol'), E0=(92.2881,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09531566341903863, var=0.3090043440973829, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing
    Total Standard Deviation in ln(k): 1.3538819174557606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing
Total Standard Deviation in ln(k): 1.3538819174557606""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing
Total Standard Deviation in ln(k): 1.3538819174557606
""",
)

entry(
    index = 31,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.22559e+09,'m^3/(mol*s)'), n=-0.615758, w0=(221.182,'kJ/mol'), E0=(114.724,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4549489928407617, var=0.5964661350051438, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R
    Total Standard Deviation in ln(k): 2.691369280705523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R
Total Standard Deviation in ln(k): 2.691369280705523""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R
Total Standard Deviation in ln(k): 2.691369280705523
""",
)

entry(
    index = 32,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H",
    kinetics = ArrheniusBM(A=(5.89413e+12,'m^3/(mol*s)'), n=-1.86165, w0=(205.5,'kJ/mol'), E0=(146.752,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03654003415492, var=7.683465661669159, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H',), comment="""BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H
    Total Standard Deviation in ln(k): 5.648747328970367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H
Total Standard Deviation in ln(k): 5.648747328970367""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H
Total Standard Deviation in ln(k): 5.648747328970367
""",
)

entry(
    index = 33,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing",
    kinetics = ArrheniusBM(A=(5.13792e+08,'m^3/(mol*s)'), n=-0.00786446, w0=(206.286,'kJ/mol'), E0=(125.653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7799819642937372, var=0.5697251147831431, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing
    Total Standard Deviation in ln(k): 3.472930470837731"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 3.472930470837731""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 3.472930470837731
""",
)

entry(
    index = 34,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.37186e+06,'m^3/(mol*s)'), n=0.39882, w0=(205.5,'kJ/mol'), E0=(58.4221,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_N-5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_N-5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.70417e+07,'m^3/(mol*s)'), n=0.13817, w0=(205.5,'kJ/mol'), E0=(78.8935,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00980750222858381, var=0.006570523121723872, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.18714331168925397"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.18714331168925397""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.18714331168925397
""",
)

entry(
    index = 36,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.15096e+07,'m^3/(mol*s)'), n=0.183576, w0=(205.5,'kJ/mol'), E0=(85.895,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9406904256473184, var=0.36637113566177576, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.5769818489306324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.5769818489306324""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.5769818489306324
""",
)

entry(
    index = 37,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_3R!H->C",
    kinetics = ArrheniusBM(A=(5.35143,'m^3/(mol*s)'), n=0.941405, w0=(332.575,'kJ/mol'), E0=(228.974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_3R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_3R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(3.68346e+22,'m^3/(mol*s)'), n=-5.07831, w0=(330.34,'kJ/mol'), E0=(328.729,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05335834313369799, var=16.51144244689708, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C
    Total Standard Deviation in ln(k): 8.280161684255964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 8.280161684255964""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 8.280161684255964
""",
)

entry(
    index = 39,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.18489e+06,'m^3/(mol*s)'), n=0.0886418, w0=(260.394,'kJ/mol'), E0=(130.197,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(3.96079e+06,'m^3/(mol*s)'), n=-0.0332618, w0=(248.069,'kJ/mol'), E0=(184.484,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_N-6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.42179e+07,'m^3/(mol*s)'), n=-0.16386, w0=(258.273,'kJ/mol'), E0=(129.136,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_N-6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_N-6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_2R->H_Ext-1S-R",
    kinetics = ArrheniusBM(A=(1.10462e+09,'m^3/(mol*s)'), n=0.328649, w0=(181.5,'kJ/mol'), E0=(64.9468,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_2R->H_Ext-1S-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_2R->H_Ext-1S-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_2R->H_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_2R->H_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_2BrCClNOS->S",
    kinetics = ArrheniusBM(A=(7.78803e+06,'m^3/(mol*s)'), n=0.612733, w0=(125.417,'kJ/mol'), E0=(62.7083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.760264977224771, var=24.73094294486889, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_2BrCClNOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_2BrCClNOS->S
    Total Standard Deviation in ln(k): 16.904929801686773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_2BrCClNOS->S
Total Standard Deviation in ln(k): 16.904929801686773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_2BrCClNOS->S
Total Standard Deviation in ln(k): 16.904929801686773
""",
)

entry(
    index = 44,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S",
    kinetics = ArrheniusBM(A=(24544.6,'m^3/(mol*s)'), n=0.916744, w0=(135.417,'kJ/mol'), E0=(10.2993,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.057973742322497024, var=1.6403916016702245, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S
    Total Standard Deviation in ln(k): 2.713282717094137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S
Total Standard Deviation in ln(k): 2.713282717094137""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S
Total Standard Deviation in ln(k): 2.713282717094137
""",
)

entry(
    index = 45,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.067e+07,'m^3/(mol*s)'), n=-0.306513, w0=(190.042,'kJ/mol'), E0=(152.053,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10641393049435416, var=25.733720676747087, Tref=1000.0, N=284, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R',), comment="""BM rule fitted to 284 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 10.437074940793584"""),
    rank = 11,
    shortDesc = """BM rule fitted to 284 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R
Total Standard Deviation in ln(k): 10.437074940793584""",
    longDesc = 
"""
BM rule fitted to 284 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R
Total Standard Deviation in ln(k): 10.437074940793584
""",
)

entry(
    index = 46,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_2R->Br",
    kinetics = ArrheniusBM(A=(19036.1,'m^3/(mol*s)'), n=0.381498, w0=(159.583,'kJ/mol'), E0=(117.198,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_2R->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_2R->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_2R->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_2R->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br",
    kinetics = ArrheniusBM(A=(6.3279e+09,'m^3/(mol*s)'), n=-0.792659, w0=(176.5,'kJ/mol'), E0=(68.9088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40909526798164586, var=8.005243311359537, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br
    Total Standard Deviation in ln(k): 6.699982503634987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br
Total Standard Deviation in ln(k): 6.699982503634987""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br
Total Standard Deviation in ln(k): 6.699982503634987
""",
)

entry(
    index = 48,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_1BrClHNO->Cl",
    kinetics = ArrheniusBM(A=(4.5295e+12,'m^3/(mol*s)'), n=-2.86943, w0=(136,'kJ/mol'), E0=(81.547,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_1BrClHNO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_1BrClHNO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_1BrClHNO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_1BrClHNO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl",
    kinetics = ArrheniusBM(A=(2.84836e+08,'m^3/(mol*s)'), n=-0.267795, w0=(136.841,'kJ/mol'), E0=(60.0291,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4793912102418554, var=3.6328862343473394, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl
    Total Standard Deviation in ln(k): 5.025552003967393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl
Total Standard Deviation in ln(k): 5.025552003967393""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl
Total Standard Deviation in ln(k): 5.025552003967393
""",
)

entry(
    index = 50,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.17885e+10,'m^3/(mol*s)'), n=-0.943326, w0=(173,'kJ/mol'), E0=(74.3779,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_2C-inRing",
    kinetics = ArrheniusBM(A=(1.6752e+09,'m^3/(mol*s)'), n=-0.659797, w0=(245.546,'kJ/mol'), E0=(122.773,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0695928823053067, var=3.0590605129317723, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_2C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_2C-inRing
    Total Standard Deviation in ln(k): 6.193735059864426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_2C-inRing
Total Standard Deviation in ln(k): 6.193735059864426""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_2C-inRing
Total Standard Deviation in ln(k): 6.193735059864426
""",
)

entry(
    index = 52,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=-1.02914e-09, w0=(196.817,'kJ/mol'), E0=(79.5152,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04819879335509886, var=0.00464624736177513, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing
    Total Standard Deviation in ln(k): 0.25775202928677016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing
Total Standard Deviation in ln(k): 0.25775202928677016""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing
Total Standard Deviation in ln(k): 0.25775202928677016
""",
)

entry(
    index = 53,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.0097e+07,'m^3/(mol*s)'), n=0.00242491, w0=(205.5,'kJ/mol'), E0=(59.197,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19666361647152325, var=2.2999937304769236, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.53445682387577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.53445682387577""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.53445682387577
""",
)

entry(
    index = 54,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(9.3466e+06,'m^3/(mol*s)'), n=0.408973, w0=(205.5,'kJ/mol'), E0=(73.8676,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_Sp-3R!H-1R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_Sp-3R!H-1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_N-Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(7.92127e+07,'m^3/(mol*s)'), n=0.261109, w0=(235.072,'kJ/mol'), E0=(117.536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_N-Sp-3R!H-1R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_N-Sp-3R!H-1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(1.19686e+08,'m^3/(mol*s)'), n=-0.0437933, w0=(205.5,'kJ/mol'), E0=(76.7788,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6404779430141558, var=0.06304376223149576, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R
    Total Standard Deviation in ln(k): 2.112600309115223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R
Total Standard Deviation in ln(k): 2.112600309115223""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R
Total Standard Deviation in ln(k): 2.112600309115223
""",
)

entry(
    index = 57,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(2.45117e+07,'m^3/(mol*s)'), n=0.200434, w0=(235.808,'kJ/mol'), E0=(117.904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007347913792462111, var=0.001811147240851766, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R
    Total Standard Deviation in ln(k): 0.10377875956780065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 0.10377875956780065""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 0.10377875956780065
""",
)

entry(
    index = 58,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(3.94526e+07,'m^3/(mol*s)'), n=0.217294, w0=(205.5,'kJ/mol'), E0=(87.1432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-1R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(2.2e+08,'m^3/(mol*s)'), n=0, w0=(236.394,'kJ/mol'), E0=(118.197,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-1R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1489.88,'m^3/(mol*s)'), n=0.313518, w0=(351.664,'kJ/mol'), E0=(243.375,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(4.10194e+12,'m^3/(mol*s)'), n=-2.14427, w0=(319.678,'kJ/mol'), E0=(277.313,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09556643197910461, var=27.83780250498703, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 10.81740794069054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 10.81740794069054""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 10.81740794069054
""",
)

entry(
    index = 62,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_2BrCClNOS->S_Ext-1S-R",
    kinetics = ArrheniusBM(A=(4.35417e+06,'m^3/(mol*s)'), n=0.747681, w0=(126.595,'kJ/mol'), E0=(63.2976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_2BrCClNOS->S_Ext-1S-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_2BrCClNOS->S_Ext-1S-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_2BrCClNOS->S_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_2BrCClNOS->S_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R",
    kinetics = ArrheniusBM(A=(28641.6,'m^3/(mol*s)'), n=0.894523, w0=(136,'kJ/mol'), E0=(50.2285,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05017112092866764, var=1.0341867732989298, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R
    Total Standard Deviation in ln(k): 2.164772908128855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R
Total Standard Deviation in ln(k): 2.164772908128855""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R
Total Standard Deviation in ln(k): 2.164772908128855
""",
)

entry(
    index = 64,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(4.88819e+09,'m^3/(mol*s)'), n=-0.840174, w0=(201.225,'kJ/mol'), E0=(176.888,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20145562779199877, var=26.17391052364994, Tref=1000.0, N=130, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F',), comment="""BM rule fitted to 130 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F
    Total Standard Deviation in ln(k): 10.762483628537119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 130 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F
Total Standard Deviation in ln(k): 10.762483628537119""",
    longDesc = 
"""
BM rule fitted to 130 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F
Total Standard Deviation in ln(k): 10.762483628537119
""",
)

entry(
    index = 65,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(2.76978e+12,'m^3/(mol*s)'), n=-1.47757, w0=(180.89,'kJ/mol'), E0=(88.048,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13719715300084306, var=4.636148093598334, Tref=1000.0, N=154, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F',), comment="""BM rule fitted to 154 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 4.661255170943689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 154 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F
Total Standard Deviation in ln(k): 4.661255170943689""",
    longDesc = 
"""
BM rule fitted to 154 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F
Total Standard Deviation in ln(k): 4.661255170943689
""",
)

entry(
    index = 66,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R",
    kinetics = ArrheniusBM(A=(1.75676e+08,'m^3/(mol*s)'), n=-0.351185, w0=(168.4,'kJ/mol'), E0=(32.1913,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08582907012607634, var=24.18381349251263, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R
    Total Standard Deviation in ln(k): 10.074344814481604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R
Total Standard Deviation in ln(k): 10.074344814481604""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R
Total Standard Deviation in ln(k): 10.074344814481604
""",
)

entry(
    index = 67,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_2CClHNO->Cl",
    kinetics = ArrheniusBM(A=(7.86166e+28,'m^3/(mol*s)'), n=-6.81801, w0=(235.385,'kJ/mol'), E0=(166.744,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_2CClHNO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_2CClHNO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_2CClHNO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_2CClHNO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl",
    kinetics = ArrheniusBM(A=(7.281e+13,'m^3/(mol*s)'), n=-1.89266, w0=(204.293,'kJ/mol'), E0=(197.86,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2589476500403787, var=1.1450060561099549, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl
    Total Standard Deviation in ln(k): 2.795788119318485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl
Total Standard Deviation in ln(k): 2.795788119318485""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl
Total Standard Deviation in ln(k): 2.795788119318485
""",
)

entry(
    index = 69,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R",
    kinetics = ArrheniusBM(A=(1.17844e+07,'m^3/(mol*s)'), n=0.100029, w0=(129.088,'kJ/mol'), E0=(40.346,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28658637376291146, var=1.6915145078591673, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R
    Total Standard Deviation in ln(k): 3.3273893690824425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R
Total Standard Deviation in ln(k): 3.3273893690824425""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R
Total Standard Deviation in ln(k): 3.3273893690824425
""",
)

entry(
    index = 70,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_1BrHNO->N",
    kinetics = ArrheniusBM(A=(3.68973e+08,'m^3/(mol*s)'), n=0.0640189, w0=(140.577,'kJ/mol'), E0=(104.243,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_1BrHNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_1BrHNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_1BrHNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_1BrHNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N",
    kinetics = ArrheniusBM(A=(7.26423e+07,'m^3/(mol*s)'), n=0.018442, w0=(200.9,'kJ/mol'), E0=(80.3987,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.0384071632530025, var=36.310070519902986, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N
    Total Standard Deviation in ln(k): 19.71428902427088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N
Total Standard Deviation in ln(k): 19.71428902427088""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N
Total Standard Deviation in ln(k): 19.71428902427088
""",
)

entry(
    index = 72,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(193.92,'kJ/mol'), E0=(96.96,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(199.715,'kJ/mol'), E0=(99.8574,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_N-Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->C_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.55633e+09,'m^3/(mol*s)'), n=-0.593907, w0=(205.5,'kJ/mol'), E0=(127.259,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Sp-3R!H=1R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(228.026,'kJ/mol'), E0=(114.013,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Sp-3R!H=1R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Sp-3R!H=1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Sp-3R!H=1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Sp-3R!H=1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_N-Sp-3R!H=1R",
    kinetics = ArrheniusBM(A=(1.5763e+09,'m^3/(mol*s)'), n=-0.786601, w0=(205.5,'kJ/mol'), E0=(105.708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_N-Sp-3R!H=1R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_N-Sp-3R!H=1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_N-Sp-3R!H=1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_N-Sp-3R!H=1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R_Ext-1R-R",
    kinetics = ArrheniusBM(A=(2.36997e+07,'m^3/(mol*s)'), n=0.0829452, w0=(205.5,'kJ/mol'), E0=(62.9775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R_Ext-1R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R_Ext-1R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R_Ext-1R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R_Ext-1R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.29183e+07,'m^3/(mol*s)'), n=0.208569, w0=(235.097,'kJ/mol'), E0=(117.548,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->C_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C_Ext-6C-R_Ext-6C-R",
    kinetics = ArrheniusBM(A=(12121.6,'m^3/(mol*s)'), n=0.487299, w0=(311.393,'kJ/mol'), E0=(222.214,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C_Ext-6C-R_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C_Ext-6C-R_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C",
    kinetics = ArrheniusBM(A=(15609.6,'m^3/(mol*s)'), n=0.89762, w0=(140.553,'kJ/mol'), E0=(70.2764,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06086937253965734, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C
    Total Standard Deviation in ln(k): 0.15293812195893802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C
Total Standard Deviation in ln(k): 0.15293812195893802""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C
Total Standard Deviation in ln(k): 0.15293812195893802
""",
)

entry(
    index = 81,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(71187.7,'m^3/(mol*s)'), n=0.889878, w0=(136,'kJ/mol'), E0=(61.2718,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04260018029728362, var=0.01177311932906228, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_N-3R!H->C
    Total Standard Deviation in ln(k): 0.32455741585538117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.32455741585538117""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.32455741585538117
""",
)

entry(
    index = 82,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl",
    kinetics = ArrheniusBM(A=(2.31481e+14,'m^3/(mol*s)'), n=-2.01467, w0=(163.5,'kJ/mol'), E0=(62.3505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22811668133446578, var=43.268526874405175, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl
    Total Standard Deviation in ln(k): 13.760067550139247"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl
Total Standard Deviation in ln(k): 13.760067550139247""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl
Total Standard Deviation in ln(k): 13.760067550139247
""",
)

entry(
    index = 83,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl",
    kinetics = ArrheniusBM(A=(2.32395e+10,'m^3/(mol*s)'), n=-1.03421, w0=(204.286,'kJ/mol'), E0=(178.344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19941518586177953, var=26.059201839571816, Tref=1000.0, N=125, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl',), comment="""BM rule fitted to 125 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl
    Total Standard Deviation in ln(k): 10.73485776656153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 125 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl
Total Standard Deviation in ln(k): 10.73485776656153""",
    longDesc = 
"""
BM rule fitted to 125 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl
Total Standard Deviation in ln(k): 10.73485776656153
""",
)

entry(
    index = 84,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C",
    kinetics = ArrheniusBM(A=(1.04424e+09,'m^3/(mol*s)'), n=-0.565926, w0=(182.679,'kJ/mol'), E0=(97.952,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.040986047295970884, var=2.366020140008974, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C',), comment="""BM rule fitted to 68 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C
    Total Standard Deviation in ln(k): 3.1866380347773133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C
Total Standard Deviation in ln(k): 3.1866380347773133""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C
Total Standard Deviation in ln(k): 3.1866380347773133
""",
)

entry(
    index = 85,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C",
    kinetics = ArrheniusBM(A=(3.5847e+13,'m^3/(mol*s)'), n=-1.77712, w0=(187.128,'kJ/mol'), E0=(89.4682,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.35622440381563203, var=4.959014740194045, Tref=1000.0, N=86, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C',), comment="""BM rule fitted to 86 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C
    Total Standard Deviation in ln(k): 5.359349734700873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 86 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C
Total Standard Deviation in ln(k): 5.359349734700873""",
    longDesc = 
"""
BM rule fitted to 86 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C
Total Standard Deviation in ln(k): 5.359349734700873
""",
)

entry(
    index = 86,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_Ext-2CClHNO-R",
    kinetics = ArrheniusBM(A=(1.46789e+12,'m^3/(mol*s)'), n=-1.37202, w0=(152.5,'kJ/mol'), E0=(64.4424,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_Ext-2CClHNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_Ext-2CClHNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_Ext-2CClHNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_Ext-2CClHNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_3R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-4.23606e-08, w0=(179,'kJ/mol'), E0=(70.8713,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_3R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_3R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(107805,'m^3/(mol*s)'), n=0.470366, w0=(170.167,'kJ/mol'), E0=(44.4056,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4765163178441915, var=0.4144344599263851, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C
    Total Standard Deviation in ln(k): 2.4878571465334844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C
Total Standard Deviation in ln(k): 2.4878571465334844""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C
Total Standard Deviation in ln(k): 2.4878571465334844
""",
)

entry(
    index = 89,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_2CHNO->C",
    kinetics = ArrheniusBM(A=(2.7032e+09,'m^3/(mol*s)'), n=-0.671759, w0=(193.572,'kJ/mol'), E0=(113.674,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.39669066013312737, var=0.35528669677274394, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_2CHNO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_2CHNO->C
    Total Standard Deviation in ln(k): 2.1916512011317053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_2CHNO->C
Total Standard Deviation in ln(k): 2.1916512011317053""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_2CHNO->C
Total Standard Deviation in ln(k): 2.1916512011317053
""",
)

entry(
    index = 90,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C",
    kinetics = ArrheniusBM(A=(9.75816e+07,'m^3/(mol*s)'), n=0.0674833, w0=(211.44,'kJ/mol'), E0=(143.445,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0257753756575725, var=1.5339568686567078, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C
    Total Standard Deviation in ln(k): 5.0602498489449745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C
Total Standard Deviation in ln(k): 5.0602498489449745""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C
Total Standard Deviation in ln(k): 5.0602498489449745
""",
)

entry(
    index = 91,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_3R!H->Cl",
    kinetics = ArrheniusBM(A=(2.54516e+11,'m^3/(mol*s)'), n=-2.9831, w0=(229.5,'kJ/mol'), E0=(94.7569,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.057261895203365755, var=1.2163227514485672e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_3R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_3R!H->Cl
    Total Standard Deviation in ln(k): 0.1508657863229021"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_3R!H->Cl
Total Standard Deviation in ln(k): 0.1508657863229021""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_3R!H->Cl
Total Standard Deviation in ln(k): 0.1508657863229021
""",
)

entry(
    index = 92,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl",
    kinetics = ArrheniusBM(A=(1.16463e+07,'m^3/(mol*s)'), n=0.104596, w0=(115.7,'kJ/mol'), E0=(40.5859,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.37013554855603914, var=1.270948032047048, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl
    Total Standard Deviation in ln(k): 3.190053587380667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 3.190053587380667""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 3.190053587380667
""",
)

entry(
    index = 93,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O",
    kinetics = ArrheniusBM(A=(2.19513e+08,'m^3/(mol*s)'), n=-0.0548873, w0=(177.527,'kJ/mol'), E0=(90.4545,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.629409236135252, var=19.884456255930367, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O
    Total Standard Deviation in ln(k): 15.546068642177413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O
Total Standard Deviation in ln(k): 15.546068642177413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O
Total Standard Deviation in ln(k): 15.546068642177413
""",
)

entry(
    index = 94,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_N-1HO->O",
    kinetics = ArrheniusBM(A=(1.04607e+06,'m^3/(mol*s)'), n=-0.000249502, w0=(224.272,'kJ/mol'), E0=(166.226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12984451529271046, var=52.92098688017469, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_N-1HO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_N-1HO->O
    Total Standard Deviation in ln(k): 14.91005112312643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_N-1HO->O
Total Standard Deviation in ln(k): 14.91005112312643""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_N-1HO->O
Total Standard Deviation in ln(k): 14.91005112312643
""",
)

entry(
    index = 95,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(15609.6,'m^3/(mol*s)'), n=0.89762, w0=(139.905,'kJ/mol'), E0=(69.9523,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06086936834917852, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R
    Total Standard Deviation in ln(k): 0.15293811143009678"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R
Total Standard Deviation in ln(k): 0.15293811143009678""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R
Total Standard Deviation in ln(k): 0.15293811143009678
""",
)

entry(
    index = 96,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_N-3R!H->C_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(71187.7,'m^3/(mol*s)'), n=0.889878, w0=(136,'kJ/mol'), E0=(61.1052,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_N-3R!H->C_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_N-3R!H->C_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_N-3R!H->C_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_N-3R!H->C_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.35017e+16,'m^3/(mol*s)'), n=-2.51834, w0=(163.5,'kJ/mol'), E0=(56.912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28819147482758345, var=62.503342978660875, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 16.57334541001471"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 16.57334541001471""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 16.57334541001471
""",
)

entry(
    index = 98,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br",
    kinetics = ArrheniusBM(A=(2.30066e+09,'m^3/(mol*s)'), n=-0.741101, w0=(142.5,'kJ/mol'), E0=(57.2752,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1554025914675551, var=2.83329482073936, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br
    Total Standard Deviation in ln(k): 3.7649078074360314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br
Total Standard Deviation in ln(k): 3.7649078074360314""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br
Total Standard Deviation in ln(k): 3.7649078074360314
""",
)

entry(
    index = 99,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br",
    kinetics = ArrheniusBM(A=(7.4059e+10,'m^3/(mol*s)'), n=-1.17843, w0=(206.493,'kJ/mol'), E0=(179.409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19473894833037222, var=25.994306931302106, Tref=1000.0, N=122, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br',), comment="""BM rule fitted to 122 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br
    Total Standard Deviation in ln(k): 10.710357911979475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 122 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br
Total Standard Deviation in ln(k): 10.710357911979475""",
    longDesc = 
"""
BM rule fitted to 122 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br
Total Standard Deviation in ln(k): 10.710357911979475
""",
)

entry(
    index = 100,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.02464e+12,'m^3/(mol*s)'), n=-1.37664, w0=(183.676,'kJ/mol'), E0=(144.354,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.37017653417053603, var=7.570272524698937, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R',), comment="""BM rule fitted to 32 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.445945593834469"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.445945593834469""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.445945593834469
""",
)

entry(
    index = 101,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(9.25278e+07,'m^3/(mol*s)'), n=-0.310369, w0=(173,'kJ/mol'), E0=(89.1404,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.036428634722012326, var=0.32519675870050985, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 1.2347499698829045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 1.2347499698829045""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 1.2347499698829045
""",
)

entry(
    index = 102,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.16619e+13,'m^3/(mol*s)'), n=-1.9955, w0=(206.26,'kJ/mol'), E0=(167.941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028885702918985946, var=1.5971532592911533, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 2.606131844226376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 2.606131844226376""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 2.606131844226376
""",
)

entry(
    index = 103,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.91851e+08,'m^3/(mol*s)'), n=-0.461975, w0=(208.478,'kJ/mol'), E0=(48.5151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7700678267015224, var=1.9377332523612902, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 4.725484881014499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.725484881014499""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.725484881014499
""",
)

entry(
    index = 104,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_2BrClHNO->N",
    kinetics = ArrheniusBM(A=(4.23489e+61,'m^3/(mol*s)'), n=-16.8824, w0=(152.5,'kJ/mol'), E0=(1.525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_2BrClHNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_2BrClHNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_2BrClHNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_2BrClHNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N",
    kinetics = ArrheniusBM(A=(4.90328e+11,'m^3/(mol*s)'), n=-1.19347, w0=(187.535,'kJ/mol'), E0=(87.9501,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2701352573889006, var=3.7981635656049226, Tref=1000.0, N=85, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N',), comment="""BM rule fitted to 85 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N
    Total Standard Deviation in ln(k): 4.585735490048852"""),
    rank = 11,
    shortDesc = """BM rule fitted to 85 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N
Total Standard Deviation in ln(k): 4.585735490048852""",
    longDesc = 
"""
BM rule fitted to 85 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N
Total Standard Deviation in ln(k): 4.585735490048852
""",
)

entry(
    index = 106,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C_2CClHNO->O",
    kinetics = ArrheniusBM(A=(20726.2,'m^3/(mol*s)'), n=0.643665, w0=(179,'kJ/mol'), E0=(35.9004,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008646631423688505, var=1.2203977949675984, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C_2CClHNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C_2CClHNO->O
    Total Standard Deviation in ln(k): 2.2363884418263904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C_2CClHNO->O
Total Standard Deviation in ln(k): 2.2363884418263904""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C_2CClHNO->O
Total Standard Deviation in ln(k): 2.2363884418263904
""",
)

entry(
    index = 107,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C_N-2CClHNO->O",
    kinetics = ArrheniusBM(A=(2.4e+06,'m^3/(mol*s)'), n=0.085, w0=(152.5,'kJ/mol'), E0=(86.5718,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C_N-2CClHNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C_N-2CClHNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C_N-2CClHNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_Ext-2CClHNO-R_N-3R!H->C_N-2CClHNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C_2HO->O",
    kinetics = ArrheniusBM(A=(6.03e+07,'m^3/(mol*s)'), n=0, w0=(192.568,'kJ/mol'), E0=(96.2838,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C_2HO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C_2HO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C_2HO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C_2HO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C_N-2HO->O",
    kinetics = ArrheniusBM(A=(1.78165e+08,'m^3/(mol*s)'), n=6.66614e-05, w0=(220.876,'kJ/mol'), E0=(214.315,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0638883361312863, var=3.290806237208001, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C_N-2HO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C_N-2HO->O
    Total Standard Deviation in ln(k): 6.309791871642371"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C_N-2HO->O
Total Standard Deviation in ln(k): 6.309791871642371""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_N-2R->Br_N-2CClHNO->Cl_N-2CHNO->C_N-2HO->O
Total Standard Deviation in ln(k): 6.309791871642371
""",
)

entry(
    index = 110,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1",
    kinetics = ArrheniusBM(A=(4.46987e+32,'m^3/(mol*s)'), n=-8.0692, w0=(143.5,'kJ/mol'), E0=(89.5426,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6387839521119674, var=74.9854106708193, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1
    Total Standard Deviation in ln(k): 18.964811151930718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 18.964811151930718""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 18.964811151930718
""",
)

entry(
    index = 111,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1",
    kinetics = ArrheniusBM(A=(1.01243e+07,'m^3/(mol*s)'), n=0.124158, w0=(108.75,'kJ/mol'), E0=(36.438,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34198205253163055, var=1.1202071149149675, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1
    Total Standard Deviation in ln(k): 2.9810597314821314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 2.9810597314821314""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 2.9810597314821314
""",
)

entry(
    index = 112,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O_2R->H",
    kinetics = ArrheniusBM(A=(1.62e+08,'m^3/(mol*s)'), n=-1.30367e-07, w0=(249.815,'kJ/mol'), E0=(185.838,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O_2R->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O_2R->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O_2R->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O_2R->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O_N-2R->H",
    kinetics = ArrheniusBM(A=(1.57e+07,'m^3/(mol*s)'), n=0, w0=(105.238,'kJ/mol'), E0=(52.6192,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O_N-2R->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O_N-2R->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O_N-2R->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_N-1BrHNO->N_1HO->O_N-2R->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(15609.6,'m^3/(mol*s)'), n=0.89762, w0=(141.183,'kJ/mol'), E0=(70.5914,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_1BrCClHNOS->S_N-2R->H_N-2BrCClNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.85364e+42,'m^3/(mol*s)'), n=-9.9178, w0=(163.5,'kJ/mol'), E0=(1.635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.61723e+07,'m^3/(mol*s)'), n=-0.0518497, w0=(163.5,'kJ/mol'), E0=(81.3805,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05779465118716443, var=8.301056686147676, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.921166071230092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.921166071230092""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.921166071230092
""",
)

entry(
    index = 117,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.86795e+10,'m^3/(mol*s)'), n=-1.11165, w0=(142.5,'kJ/mol'), E0=(49.4539,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23310386285421747, var=3.4352181513961657, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.301332553396669"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.301332553396669""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.301332553396669
""",
)

entry(
    index = 118,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(6.64432e+08,'m^3/(mol*s)'), n=-0.597923, w0=(195.443,'kJ/mol'), E0=(175.279,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20154777904531945, var=26.667673900214883, Tref=1000.0, N=99, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R',), comment="""BM rule fitted to 99 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R
    Total Standard Deviation in ln(k): 10.859004389174855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 99 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R
Total Standard Deviation in ln(k): 10.859004389174855""",
    longDesc = 
"""
BM rule fitted to 99 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R
Total Standard Deviation in ln(k): 10.859004389174855
""",
)

entry(
    index = 119,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H",
    kinetics = ArrheniusBM(A=(23.6765,'m^3/(mol*s)'), n=1.77207, w0=(262.118,'kJ/mol'), E0=(26.2118,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.556934715064611, var=56.02068149549521, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H
    Total Standard Deviation in ln(k): 16.4041670451343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H
Total Standard Deviation in ln(k): 16.4041670451343""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H
Total Standard Deviation in ln(k): 16.4041670451343
""",
)

entry(
    index = 120,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H",
    kinetics = ArrheniusBM(A=(1.22533e+19,'m^3/(mol*s)'), n=-4.65414, w0=(215.742,'kJ/mol'), E0=(52.9505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.260209451359763, var=3.710088856036884, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H
    Total Standard Deviation in ln(k): 7.02779410614205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H
Total Standard Deviation in ln(k): 7.02779410614205""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H
Total Standard Deviation in ln(k): 7.02779410614205
""",
)

entry(
    index = 121,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.30307e+10,'m^3/(mol*s)'), n=-0.531722, w0=(173,'kJ/mol'), E0=(113.838,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10581052341867284, var=3.125481767642796, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 3.8100331693777356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 3.8100331693777356""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 3.8100331693777356
""",
)

entry(
    index = 122,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(4.91043e+13,'m^3/(mol*s)'), n=-2.57482, w0=(235.515,'kJ/mol'), E0=(54.097,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5264069513049662, var=6.3945623856957265, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 6.392098738351453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.392098738351453""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.392098738351453
""",
)

entry(
    index = 123,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(1.67383e+10,'m^3/(mol*s)'), n=-0.731997, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4626984145598659, var=9.685272207522559, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 7.401528940844223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 7.401528940844223""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 7.401528940844223
""",
)

entry(
    index = 124,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(1.12295e+09,'m^3/(mol*s)'), n=-0.683198, w0=(173,'kJ/mol'), E0=(98.1456,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29384857806191805, var=1.0879312592065988, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 2.829330749043721"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 2.829330749043721""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 2.829330749043721
""",
)

entry(
    index = 125,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(1.92413e+07,'m^3/(mol*s)'), n=-0.0744857, w0=(173,'kJ/mol'), E0=(74.8099,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04592196914225198, var=0.2080323178396392, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 1.0297527262070152"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 1.0297527262070152""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 1.0297527262070152
""",
)

entry(
    index = 126,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(9.36855e+08,'m^3/(mol*s)'), n=-0.615689, w0=(181.414,'kJ/mol'), E0=(10.8247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.025608949500472343, var=2.8599650318476133, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C
    Total Standard Deviation in ln(k): 3.4546380156437624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C
Total Standard Deviation in ln(k): 3.4546380156437624""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C
Total Standard Deviation in ln(k): 3.4546380156437624
""",
)

entry(
    index = 127,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(4.09586e+08,'m^3/(mol*s)'), n=-0.20188, w0=(237.318,'kJ/mol'), E0=(118.865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2528358111769738, var=0.628792674726394, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 2.224949575758291"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 2.224949575758291""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 2.224949575758291
""",
)

entry(
    index = 128,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_3BrClO->O",
    kinetics = ArrheniusBM(A=(1.52618e+07,'m^3/(mol*s)'), n=-9.1347e-08, w0=(173,'kJ/mol'), E0=(71.4771,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4041830051568411, var=0.028061083468149926, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_3BrClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_3BrClO->O
    Total Standard Deviation in ln(k): 1.3513572378993426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_3BrClO->O
Total Standard Deviation in ln(k): 1.3513572378993426""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_3BrClO->O
Total Standard Deviation in ln(k): 1.3513572378993426
""",
)

entry(
    index = 129,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O",
    kinetics = ArrheniusBM(A=(2.24266e+26,'m^3/(mol*s)'), n=-6.1236, w0=(238.776,'kJ/mol'), E0=(167.749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06682587955520769, var=0.8908687620794246, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O
    Total Standard Deviation in ln(k): 2.0600903505244297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O
Total Standard Deviation in ln(k): 2.0600903505244297""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O
Total Standard Deviation in ln(k): 2.0600903505244297
""",
)

entry(
    index = 130,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.73156e+14,'m^3/(mol*s)'), n=-2.10707, w0=(187.493,'kJ/mol'), E0=(91.8871,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15605212217138692, var=4.361540972188522, Tref=1000.0, N=74, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C',), comment="""BM rule fitted to 74 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 4.578840168363466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 74 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.578840168363466""",
    longDesc = 
"""
BM rule fitted to 74 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.578840168363466
""",
)

entry(
    index = 131,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.90689e+06,'m^3/(mol*s)'), n=0.418002, w0=(193.811,'kJ/mol'), E0=(126.08,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.067844274798981, var=46.24811338928726, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 26.36667151648348"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 26.36667151648348""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 26.36667151648348
""",
)

entry(
    index = 132,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_2R->N",
    kinetics = ArrheniusBM(A=(1.94697e+33,'m^3/(mol*s)'), n=-8.77465, w0=(100.5,'kJ/mol'), E0=(62.8034,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21180353796563897, var=231.95075518798305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_2R->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_2R->N
    Total Standard Deviation in ln(k): 31.064143760247813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_2R->N
Total Standard Deviation in ln(k): 31.064143760247813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_2R->N
Total Standard Deviation in ln(k): 31.064143760247813
""",
)

entry(
    index = 133,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_N-2R->N",
    kinetics = ArrheniusBM(A=(43950,'m^3/(mol*s)'), n=1, w0=(229.5,'kJ/mol'), E0=(53.7489,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_N-2R->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_N-2R->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_N-2R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_N-2R->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.35656e+10,'m^3/(mol*s)'), n=-0.746808, w0=(88.875,'kJ/mol'), E0=(86.5671,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.971139102085062, var=21.094891276809662, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R
    Total Standard Deviation in ln(k): 16.672756468255248"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R
Total Standard Deviation in ln(k): 16.672756468255248""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R
Total Standard Deviation in ln(k): 16.672756468255248
""",
)

entry(
    index = 135,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi",
    kinetics = ArrheniusBM(A=(6.81143e+06,'m^3/(mol*s)'), n=0.15318, w0=(108.071,'kJ/mol'), E0=(31.0957,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13355378082801436, var=0.6807151410709787, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi
    Total Standard Deviation in ln(k): 1.9895782191971843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi
Total Standard Deviation in ln(k): 1.9895782191971843""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi
Total Standard Deviation in ln(k): 1.9895782191971843
""",
)

entry(
    index = 136,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_N-Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi",
    kinetics = ArrheniusBM(A=(8.84147e+06,'m^3/(mol*s)'), n=0.349925, w0=(228.417,'kJ/mol'), E0=(114.208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_N-Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_N-Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_N-Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_N-Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.49202e+07,'m^3/(mol*s)'), n=-0.181327, w0=(163.5,'kJ/mol'), E0=(79.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_4BrCFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_4BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(3.46638e+07,'m^3/(mol*s)'), n=0.0128888, w0=(164.4,'kJ/mol'), E0=(82.1998,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.044574436569025946, var=15.233807308235251, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 7.936579371609077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 7.936579371609077""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 7.936579371609077
""",
)

entry(
    index = 139,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(4.77213e+06,'m^3/(mol*s)'), n=0.171878, w0=(142.5,'kJ/mol'), E0=(57.719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(7.31171e+13,'m^3/(mol*s)'), n=-2.39518, w0=(142.5,'kJ/mol'), E0=(41.1889,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_2BrCHNO->Br_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0",
    kinetics = ArrheniusBM(A=(1.78484e+08,'m^3/(mol*s)'), n=-0.444435, w0=(191.731,'kJ/mol'), E0=(171.199,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.025678027746315512, var=26.690736117617913, Tref=1000.0, N=95, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0',), comment="""BM rule fitted to 95 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0
    Total Standard Deviation in ln(k): 10.421596092581378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 95 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0
Total Standard Deviation in ln(k): 10.421596092581378""",
    longDesc = 
"""
BM rule fitted to 95 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0
Total Standard Deviation in ln(k): 10.421596092581378
""",
)

entry(
    index = 142,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0",
    kinetics = ArrheniusBM(A=(3.16281e+07,'m^3/(mol*s)'), n=-0.0149709, w0=(283.614,'kJ/mol'), E0=(177.39,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1980379765614555, var=4.355670235940915, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0
    Total Standard Deviation in ln(k): 4.681513584643128"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0
Total Standard Deviation in ln(k): 4.681513584643128""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0
Total Standard Deviation in ln(k): 4.681513584643128
""",
)

entry(
    index = 143,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(22.9439,'m^3/(mol*s)'), n=1.77783, w0=(263.339,'kJ/mol'), E0=(26.3339,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5284786104871207, var=56.863950756479966, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R
    Total Standard Deviation in ln(k): 16.44518000859462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R
Total Standard Deviation in ln(k): 16.44518000859462""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R
Total Standard Deviation in ln(k): 16.44518000859462
""",
)

entry(
    index = 144,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.35279e+19,'m^3/(mol*s)'), n=-4.67047, w0=(210.631,'kJ/mol'), E0=(57.2321,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1952341737846044, var=4.188869186441967, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H_Ext-1C-R
    Total Standard Deviation in ln(k): 7.106137515084264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H_Ext-1C-R
Total Standard Deviation in ln(k): 7.106137515084264""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H_Ext-1C-R
Total Standard Deviation in ln(k): 7.106137515084264
""",
)

entry(
    index = 145,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.81979e+07,'m^3/(mol*s)'), n=-0.126529, w0=(173,'kJ/mol'), E0=(49.1223,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.223e+10,'m^3/(mol*s)'), n=-0.506, w0=(184.66,'kJ/mol'), E0=(136.628,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_Ext-3BrCClINOPSSi-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.09341e+11,'m^3/(mol*s)'), n=-1.72762, w0=(201.852,'kJ/mol'), E0=(32.4355,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20512779005364343, var=0.5767536953848286, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 2.0378785119787235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.0378785119787235""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.0378785119787235
""",
)

entry(
    index = 148,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.22365e+25,'m^3/(mol*s)'), n=-6.39447, w0=(279.856,'kJ/mol'), E0=(130.061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16112100613289282, var=29.317262212952514, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-2C-R
    Total Standard Deviation in ln(k): 11.25954839513142"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 11.25954839513142""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 11.25954839513142
""",
)

entry(
    index = 149,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O",
    kinetics = ArrheniusBM(A=(7.27037e+07,'m^3/(mol*s)'), n=-0.266667, w0=(173,'kJ/mol'), E0=(41.1049,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.036421985976179e-09, var=0.9482355719647005, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O
    Total Standard Deviation in ln(k): 1.9521586725237043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O
Total Standard Deviation in ln(k): 1.9521586725237043""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O
Total Standard Deviation in ln(k): 1.9521586725237043
""",
)

entry(
    index = 150,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O",
    kinetics = ArrheniusBM(A=(3.40267e+10,'m^3/(mol*s)'), n=-0.792692, w0=(173.931,'kJ/mol'), E0=(17.3931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4811781698477286, var=10.001103928474157, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O
    Total Standard Deviation in ln(k): 7.548869235970634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O
Total Standard Deviation in ln(k): 7.548869235970634""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O
Total Standard Deviation in ln(k): 7.548869235970634
""",
)

entry(
    index = 151,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.9609e+09,'m^3/(mol*s)'), n=-0.904668, w0=(173,'kJ/mol'), E0=(22.528,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28018604732531893, var=1.8325624862226306, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.417838453998129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.417838453998129""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.417838453998129
""",
)

entry(
    index = 152,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.51229e+07,'m^3/(mol*s)'), n=-0.0676006, w0=(173,'kJ/mol'), E0=(49.6983,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0039751620550457995, var=0.08330493739625001, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R
    Total Standard Deviation in ln(k): 0.5886064049544166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R
Total Standard Deviation in ln(k): 0.5886064049544166""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R
Total Standard Deviation in ln(k): 0.5886064049544166
""",
)

entry(
    index = 153,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5.38619e+06,'m^3/(mol*s)'), n=0.213797, w0=(186.233,'kJ/mol'), E0=(93.1164,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0030036702694343715, var=0.03535203814212297, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.3844799596401528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.3844799596401528""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.3844799596401528
""",
)

entry(
    index = 154,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(8.06003e+08,'m^3/(mol*s)'), n=-0.684834, w0=(179.164,'kJ/mol'), E0=(81.1464,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6906217089536835, var=1.1467119298361357, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.881993687810519"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.881993687810519""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.881993687810519
""",
)

entry(
    index = 155,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_Sp-3C#1C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(288.568,'kJ/mol'), E0=(144.284,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_Sp-3C#1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_Sp-3C#1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_Sp-3C#1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_Sp-3C#1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C",
    kinetics = ArrheniusBM(A=(5.36756e+09,'m^3/(mol*s)'), n=-0.545538, w0=(220.234,'kJ/mol'), E0=(179.815,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4450592725346621, var=1.0313806549991054, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C
    Total Standard Deviation in ln(k): 3.154186433884112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C
Total Standard Deviation in ln(k): 3.154186433884112""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C
Total Standard Deviation in ln(k): 3.154186433884112
""",
)

entry(
    index = 157,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_3BrClO->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.51e+07,'m^3/(mol*s)'), n=-1.88915e-08, w0=(173,'kJ/mol'), E0=(61.8128,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_3BrClO->O_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_3BrClO->O_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_3BrClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_3BrClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_3BrCl->Cl",
    kinetics = ArrheniusBM(A=(9.26048e+36,'m^3/(mol*s)'), n=-9.23874, w0=(282.184,'kJ/mol'), E0=(193.589,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05438046726055889, var=0.3176744838946306, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_3BrCl->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_3BrCl->Cl
    Total Standard Deviation in ln(k): 1.266555536755236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_3BrCl->Cl
Total Standard Deviation in ln(k): 1.266555536755236""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_3BrCl->Cl
Total Standard Deviation in ln(k): 1.266555536755236
""",
)

entry(
    index = 159,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_N-3BrCl->Cl",
    kinetics = ArrheniusBM(A=(6.23766e+12,'m^3/(mol*s)'), n=-2.0926, w0=(173,'kJ/mol'), E0=(75.9802,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_N-3BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_N-3BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H",
    kinetics = ArrheniusBM(A=(9.31572e+08,'m^3/(mol*s)'), n=-0.253646, w0=(210.136,'kJ/mol'), E0=(54.2831,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04086937261481295, var=3.277701084670652, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H',), comment="""BM rule fitted to 38 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H
    Total Standard Deviation in ln(k): 3.732143919080211"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H
Total Standard Deviation in ln(k): 3.732143919080211""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H
Total Standard Deviation in ln(k): 3.732143919080211
""",
)

entry(
    index = 161,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H",
    kinetics = ArrheniusBM(A=(1.12667e+19,'m^3/(mol*s)'), n=-3.52779, w0=(168.486,'kJ/mol'), E0=(93.6825,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21422490989411397, var=8.989685624753072, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H',), comment="""BM rule fitted to 36 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H
    Total Standard Deviation in ln(k): 6.549011521696398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H
Total Standard Deviation in ln(k): 6.549011521696398""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H
Total Standard Deviation in ln(k): 6.549011521696398
""",
)

entry(
    index = 162,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_3ClNOS->S",
    kinetics = ArrheniusBM(A=(2.12532e+06,'m^3/(mol*s)'), n=0.469939, w0=(205.5,'kJ/mol'), E0=(98.1764,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_3ClNOS->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_3ClNOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_3ClNOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_3ClNOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S",
    kinetics = ArrheniusBM(A=(1.89741e+12,'m^3/(mol*s)'), n=-2.26485, w0=(193.557,'kJ/mol'), E0=(18.7048,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2188263698140419, var=3.2106572858026916, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S
    Total Standard Deviation in ln(k): 4.141960872428238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S
Total Standard Deviation in ln(k): 4.141960872428238""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S
Total Standard Deviation in ln(k): 4.141960872428238
""",
)

entry(
    index = 164,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_2R->N_Ext-2N-R",
    kinetics = ArrheniusBM(A=(1.22646e+19,'m^3/(mol*s)'), n=-4.10331, w0=(100.5,'kJ/mol'), E0=(1.21992,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_2R->N_Ext-2N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_2R->N_Ext-2N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_2R->N_Ext-2N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_3BrBrCCFFIINNOOPPSSSiSi-u1_2R->N_Ext-2N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R",
    kinetics = ArrheniusBM(A=(3.86414e+11,'m^3/(mol*s)'), n=-1.83498, w0=(92,'kJ/mol'), E0=(40.0187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28923775130661766, var=2.0602707343700155, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R
    Total Standard Deviation in ln(k): 3.604253221765591"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R
Total Standard Deviation in ln(k): 3.604253221765591""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R
Total Standard Deviation in ln(k): 3.604253221765591
""",
)

entry(
    index = 166,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_1BrHNO->N",
    kinetics = ArrheniusBM(A=(1.59771e+09,'m^3/(mol*s)'), n=-0.461068, w0=(100.5,'kJ/mol'), E0=(47.4882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_1BrHNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_1BrHNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_1BrHNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_1BrHNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_N-1BrHNO->N",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(77.2673,'kJ/mol'), E0=(38.6336,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_N-1BrHNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_N-1BrHNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_N-1BrHNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_N-1BrHNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_3BrCFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.12593e+08,'m^3/(mol*s)'), n=-0.33733, w0=(71,'kJ/mol'), E0=(19.9199,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_3BrCFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_3BrCFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_3BrCFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_3BrCFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N",
    kinetics = ArrheniusBM(A=(2.59977e+07,'m^3/(mol*s)'), n=-0.00894004, w0=(116.774,'kJ/mol'), E0=(58.3782,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23721352520630443, var=0.10054151839377981, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N
    Total Standard Deviation in ln(k): 1.2316809456740203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N
Total Standard Deviation in ln(k): 1.2316809456740203""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N
Total Standard Deviation in ln(k): 1.2316809456740203
""",
)

entry(
    index = 170,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.80245e+06,'m^3/(mol*s)'), n=0.0257778, w0=(163.5,'kJ/mol'), E0=(74.5352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_2R->Cl_Ext-1C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F",
    kinetics = ArrheniusBM(A=(4.47213,'m^3/(mol*s)'), n=1.66001, w0=(203.846,'kJ/mol'), E0=(20.3846,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1083115121253379, var=36.664005075402095, Tref=1000.0, N=60, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F',), comment="""BM rule fitted to 60 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F
    Total Standard Deviation in ln(k): 12.41097261561785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 60 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F
Total Standard Deviation in ln(k): 12.41097261561785""",
    longDesc = 
"""
BM rule fitted to 60 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F
Total Standard Deviation in ln(k): 12.41097261561785
""",
)

entry(
    index = 172,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F",
    kinetics = ArrheniusBM(A=(9.31387e+10,'m^3/(mol*s)'), n=-1.09749, w0=(176.429,'kJ/mol'), E0=(65.5688,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.101304353484427, var=8.05564812829803, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F',), comment="""BM rule fitted to 35 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F
    Total Standard Deviation in ln(k): 5.944467610658331"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F
Total Standard Deviation in ln(k): 5.944467610658331""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F
Total Standard Deviation in ln(k): 5.944467610658331
""",
)

entry(
    index = 173,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(7.90859e+06,'m^3/(mol*s)'), n=0.0977368, w0=(266.484,'kJ/mol'), E0=(168.038,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19766764971989847, var=5.370421075105351, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 5.142459328854026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 5.142459328854026""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 5.142459328854026
""",
)

entry(
    index = 174,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.75765e+07,'m^3/(mol*s)'), n=0.181385, w0=(335.003,'kJ/mol'), E0=(200.161,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0327685,'m^3/(mol*s)'), n=2.45851, w0=(266.029,'kJ/mol'), E0=(26.6029,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0051654343000989, var=101.89681866047123, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 22.762129852451952"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 22.762129852451952""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 22.762129852451952
""",
)

entry(
    index = 176,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.63468e+17,'m^3/(mol*s)'), n=-2.64305, w0=(249.888,'kJ/mol'), E0=(246.807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-14.37392588651005, var=456.8060464599228, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 78.96263751151896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 78.96263751151896""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 78.96263751151896
""",
)

entry(
    index = 177,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.78e+27,'m^3/(mol*s)'), n=-6.64, w0=(257.506,'kJ/mol'), E0=(186.106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_N-2CHO->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.95004e+08,'m^3/(mol*s)'), n=-0.654592, w0=(176.087,'kJ/mol'), E0=(32.8805,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.384037453733207, var=1.4882035948788261, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 3.410533645608265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R
Total Standard Deviation in ln(k): 3.410533645608265""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R
Total Standard Deviation in ln(k): 3.410533645608265
""",
)

entry(
    index = 179,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.816e+40,'m^3/(mol*s)'), n=-10.56, w0=(276.766,'kJ/mol'), E0=(189.23,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(8.11368e+07,'m^3/(mol*s)'), n=-0.32, w0=(173,'kJ/mol'), E0=(12.3549,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.06745173525263e-08, var=0.5020281551937015, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R
    Total Standard Deviation in ln(k): 1.4204339955560865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R
Total Standard Deviation in ln(k): 1.4204339955560865""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R
Total Standard Deviation in ln(k): 1.4204339955560865
""",
)

entry(
    index = 181,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(5.44763e+10,'m^3/(mol*s)'), n=-0.821521, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4963762373919454, var=9.904855265810328, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R
    Total Standard Deviation in ln(k): 7.556474706615869"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R
Total Standard Deviation in ln(k): 7.556474706615869""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R
Total Standard Deviation in ln(k): 7.556474706615869
""",
)

entry(
    index = 182,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.82036e+08,'m^3/(mol*s)'), n=-0.5, w0=(187.402,'kJ/mol'), E0=(139.216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16920761856358965, var=1.2798808077192283, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 2.693137994621831"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.693137994621831""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.693137994621831
""",
)

entry(
    index = 183,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C",
    kinetics = ArrheniusBM(A=(2.19331e+13,'m^3/(mol*s)'), n=-2.11077, w0=(173,'kJ/mol'), E0=(86.4669,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2293247030427738, var=0.08141112270043357, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C
    Total Standard Deviation in ln(k): 1.1481964519560872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C
Total Standard Deviation in ln(k): 1.1481964519560872""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C
Total Standard Deviation in ln(k): 1.1481964519560872
""",
)

entry(
    index = 184,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-5R!H-2C",
    kinetics = ArrheniusBM(A=(250896,'m^3/(mol*s)'), n=0.298496, w0=(173,'kJ/mol'), E0=(73.0117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6275205214902675, var=0.8643428515802953, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-5R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-5R!H-2C
    Total Standard Deviation in ln(k): 3.4404877499228292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-5R!H-2C
Total Standard Deviation in ln(k): 3.4404877499228292""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-5R!H-2C
Total Standard Deviation in ln(k): 3.4404877499228292
""",
)

entry(
    index = 185,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(3.11826e+08,'m^3/(mol*s)'), n=-0.382134, w0=(173,'kJ/mol'), E0=(75.4719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3103717364191287, var=0.19251948769113075, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 1.659446949581135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.659446949581135""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.659446949581135
""",
)

entry(
    index = 186,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.92981e+07,'m^3/(mol*s)'), n=-0.0980858, w0=(176.039,'kJ/mol'), E0=(70.9125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.027636288480833365, var=0.08748618983592148, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 0.6623997445926043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 0.6623997445926043""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 0.6623997445926043
""",
)

entry(
    index = 187,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(5.749e+06,'m^3/(mol*s)'), n=0.214, w0=(186.262,'kJ/mol'), E0=(93.131,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(8.41487e+08,'m^3/(mol*s)'), n=-0.692606, w0=(181.472,'kJ/mol'), E0=(90.7359,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4612600998246526, var=0.494140255580928, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R_4R!H->C
    Total Standard Deviation in ln(k): 2.568175711693148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 2.568175711693148""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 2.568175711693148
""",
)

entry(
    index = 189,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(174.548,'kJ/mol'), E0=(87.274,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_Sp-3C-1C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(5.93833e+09,'m^3/(mol*s)'), n=-0.634702, w0=(223.806,'kJ/mol'), E0=(168.051,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40624356009784207, var=1.915584577804702, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.795358931097789"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.795358931097789""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.795358931097789
""",
)

entry(
    index = 191,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_3BrCl->Cl_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.568e+40,'m^3/(mol*s)'), n=-10.21, w0=(290.002,'kJ/mol'), E0=(199.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_3BrCl->Cl_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_3BrCl->Cl_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_3BrCl->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_N-3BrCClINOPSSi->C_N-3BrClO->O_3BrCl->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.3734e+10,'m^3/(mol*s)'), n=-0.689502, w0=(205.5,'kJ/mol'), E0=(40.0325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08204118046051638, var=8.080189336525653, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R
    Total Standard Deviation in ln(k): 5.904728165199943"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R
Total Standard Deviation in ln(k): 5.904728165199943""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R
Total Standard Deviation in ln(k): 5.904728165199943
""",
)

entry(
    index = 193,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing",
    kinetics = ArrheniusBM(A=(3.82247e+08,'m^3/(mol*s)'), n=-0.106414, w0=(205.5,'kJ/mol'), E0=(105.177,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06899945697746504, var=0.08357538883509968, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing
    Total Standard Deviation in ln(k): 0.7529225186827172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing
Total Standard Deviation in ln(k): 0.7529225186827172""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing
Total Standard Deviation in ln(k): 0.7529225186827172
""",
)

entry(
    index = 194,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.99782e+09,'m^3/(mol*s)'), n=-0.419678, w0=(236.076,'kJ/mol'), E0=(89.6673,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3670792464105536, var=4.7239695091764995, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing
    Total Standard Deviation in ln(k): 5.279540137660447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing
Total Standard Deviation in ln(k): 5.279540137660447""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing
Total Standard Deviation in ln(k): 5.279540137660447
""",
)

entry(
    index = 195,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_3C-inRing",
    kinetics = ArrheniusBM(A=(252.533,'m^3/(mol*s)'), n=0.999283, w0=(179,'kJ/mol'), E0=(17.329,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing",
    kinetics = ArrheniusBM(A=(3.72444e+17,'m^3/(mol*s)'), n=-3.03351, w0=(168.186,'kJ/mol'), E0=(99.2281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22794868696123646, var=12.35469017309726, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing',), comment="""BM rule fitted to 35 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing
    Total Standard Deviation in ln(k): 7.619226673939448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing
Total Standard Deviation in ln(k): 7.619226673939448""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing
Total Standard Deviation in ln(k): 7.619226673939448
""",
)

entry(
    index = 197,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_2BrClHO->O",
    kinetics = ArrheniusBM(A=(3.5e+06,'m^3/(mol*s)'), n=-4.09333e-09, w0=(179,'kJ/mol'), E0=(33.4569,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_2BrClHO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_2BrClHO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_2BrClHO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_2BrClHO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O",
    kinetics = ArrheniusBM(A=(8.22778e+12,'m^3/(mol*s)'), n=-2.5165, w0=(206.876,'kJ/mol'), E0=(52.1755,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18023883473541716, var=2.2324597514088094, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O
    Total Standard Deviation in ln(k): 3.4482198929409047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O
Total Standard Deviation in ln(k): 3.4482198929409047""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O
Total Standard Deviation in ln(k): 3.4482198929409047
""",
)

entry(
    index = 199,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R_2R->N",
    kinetics = ArrheniusBM(A=(2.63e+08,'m^3/(mol*s)'), n=-1.1, w0=(83.5,'kJ/mol'), E0=(13.7525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R_2R->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R_2R->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R_2R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R_2R->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R_N-2R->N",
    kinetics = ArrheniusBM(A=(122000,'m^3/(mol*s)'), n=0.2, w0=(100.5,'kJ/mol'), E0=(22.1948,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R_N-2R->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R_N-2R->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R_N-2R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Ext-2R-R_Ext-1BrHNO-R_N-2R->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O",
    kinetics = ArrheniusBM(A=(3.66143e+06,'m^3/(mol*s)'), n=0.234906, w0=(98.3861,'kJ/mol'), E0=(34.1712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4711309255437375, var=0.4736670982046028, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O
    Total Standard Deviation in ln(k): 2.5634744283513373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O
Total Standard Deviation in ln(k): 2.5634744283513373""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O
Total Standard Deviation in ln(k): 2.5634744283513373
""",
)

entry(
    index = 202,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O",
    kinetics = ArrheniusBM(A=(3.07678e+07,'m^3/(mol*s)'), n=-0.0296345, w0=(137.833,'kJ/mol'), E0=(41.2683,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0008851932897977679, var=0.010221723311110159, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O
    Total Standard Deviation in ln(k): 0.20490790928570335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O
Total Standard Deviation in ln(k): 0.20490790928570335""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O
Total Standard Deviation in ln(k): 0.20490790928570335
""",
)

entry(
    index = 203,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0989031,'m^3/(mol*s)'), n=2.08284, w0=(205.253,'kJ/mol'), E0=(20.5253,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14739217315285127, var=43.97415235697432, Tref=1000.0, N=39, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C',), comment="""BM rule fitted to 39 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C
    Total Standard Deviation in ln(k): 13.664333726774531"""),
    rank = 11,
    shortDesc = """BM rule fitted to 39 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C
Total Standard Deviation in ln(k): 13.664333726774531""",
    longDesc = 
"""
BM rule fitted to 39 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C
Total Standard Deviation in ln(k): 13.664333726774531
""",
)

entry(
    index = 204,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.02271e+06,'m^3/(mol*s)'), n=0.291041, w0=(201.233,'kJ/mol'), E0=(20.1233,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.017886114723587823, var=6.3086677742006785, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 5.080245405864381"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.080245405864381""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.080245405864381
""",
)

entry(
    index = 205,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(9.03743e+19,'m^3/(mol*s)'), n=-3.55363, w0=(174.5,'kJ/mol'), E0=(56.8722,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2993816014578487, var=10.175480426502773, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O
    Total Standard Deviation in ln(k): 7.147125289464794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 7.147125289464794""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 7.147125289464794
""",
)

entry(
    index = 206,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(2.70914e+09,'m^3/(mol*s)'), n=-0.676508, w0=(178.346,'kJ/mol'), E0=(57.0824,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07113091944065854, var=6.074524179388921, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O',), comment="""BM rule fitted to 31 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 5.119701198837356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 5.119701198837356""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 5.119701198837356
""",
)

entry(
    index = 207,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(3.35407e+06,'m^3/(mol*s)'), n=0.141943, w0=(232.471,'kJ/mol'), E0=(147.287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(678625,'m^3/(mol*s)'), n=0.434559, w0=(283.49,'kJ/mol'), E0=(174.791,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24214158638107328, var=0.1097042748014476, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 1.2723969937279491"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 1.2723969937279491""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 1.2723969937279491
""",
)

entry(
    index = 209,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0223205,'m^3/(mol*s)'), n=2.51767, w0=(264.362,'kJ/mol'), E0=(26.4362,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0823985381463817, var=104.38356097783358, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 23.201626473218425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 23.201626473218425""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 23.201626473218425
""",
)

entry(
    index = 210,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Sp-4C-1C",
    kinetics = ArrheniusBM(A=(1.02279e+36,'m^3/(mol*s)'), n=-10.0662, w0=(270.517,'kJ/mol'), E0=(207.666,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27840156192545956, var=1.620315432518365, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Sp-4C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Sp-4C-1C
    Total Standard Deviation in ln(k): 3.251360995588611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Sp-4C-1C
Total Standard Deviation in ln(k): 3.251360995588611""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Sp-4C-1C
Total Standard Deviation in ln(k): 3.251360995588611
""",
)

entry(
    index = 211,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_N-Sp-4C-1C",
    kinetics = ArrheniusBM(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, w0=(277.051,'kJ/mol'), E0=(200.669,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_N-Sp-4C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_N-Sp-4C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_N-Sp-4C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_N-Sp-4C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.56996e+11,'m^3/(mol*s)'), n=-0.751574, w0=(236.266,'kJ/mol'), E0=(204.859,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2623305746125397, var=25.506588659253637, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 18.321534149630548"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 18.321534149630548""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 18.321534149630548
""",
)

entry(
    index = 213,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(92.2154,'m^3/(mol*s)'), n=1.49683, w0=(173,'kJ/mol'), E0=(67.4291,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05691081219099027, var=2.6324204852565347, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 3.3956216682966667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 3.3956216682966667""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 3.3956216682966667
""",
)

entry(
    index = 214,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(1.4799e+07,'m^3/(mol*s)'), n=1.6104e-07, w0=(173,'kJ/mol'), E0=(38.5842,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.2894336636982114e-09, var=0.32434505653595475, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_5R!H->O
    Total Standard Deviation in ln(k): 1.1417226927701243"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_5R!H->O
Total Standard Deviation in ln(k): 1.1417226927701243""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_5R!H->O
Total Standard Deviation in ln(k): 1.1417226927701243
""",
)

entry(
    index = 215,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(2.52275e+08,'m^3/(mol*s)'), n=-0.533333, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.451479787986673e-11, var=0.3834307427530253, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 1.2413677397151985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.2413677397151985""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.2413677397151985
""",
)

entry(
    index = 216,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.65983e+11,'m^3/(mol*s)'), n=-0.84129, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1366575543344507, var=2.914302666931026, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.7657098538028677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.7657098538028677""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.7657098538028677
""",
)

entry(
    index = 217,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.55114e+09,'m^3/(mol*s)'), n=-1.1, w0=(174.533,'kJ/mol'), E0=(17.4533,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6086135054859668, var=0.2596471514605582, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 2.550704123214994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 2.550704123214994""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 2.550704123214994
""",
)

entry(
    index = 218,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.41902e+08,'m^3/(mol*s)'), n=-0.65, w0=(179.08,'kJ/mol'), E0=(17.908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2939972122180608e-10, var=0.8907254751531062, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_5R!H->C
    Total Standard Deviation in ln(k): 1.8920339555642838"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 1.8920339555642838""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 1.8920339555642838
""",
)

entry(
    index = 219,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-6.17521e-08, w0=(173,'kJ/mol'), E0=(69.7954,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C_5R!H-inRing",
    kinetics = ArrheniusBM(A=(3.144e+13,'m^3/(mol*s)'), n=-2.163, w0=(173,'kJ/mol'), E0=(86.7215,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.80218e+07,'m^3/(mol*s)'), n=-0.134489, w0=(173,'kJ/mol'), E0=(68.6955,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C_N-5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C_N-5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-5R!H-2C_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.81979e+07,'m^3/(mol*s)'), n=-0.126529, w0=(173,'kJ/mol'), E0=(62.7077,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi",
    kinetics = ArrheniusBM(A=(2.17712e+06,'m^3/(mol*s)'), n=0.213828, w0=(183.244,'kJ/mol'), E0=(77.8501,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00017420524692625505, var=0.09909663638708269, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi
    Total Standard Deviation in ln(k): 0.6315206505006369"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 0.6315206505006369""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 0.6315206505006369
""",
)

entry(
    index = 224,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi",
    kinetics = ArrheniusBM(A=(8.05579e+10,'m^3/(mol*s)'), n=-1.31825, w0=(173,'kJ/mol'), E0=(70.1326,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11515356162216171, var=8.862062190662188e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi
    Total Standard Deviation in ln(k): 0.3082028374807834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 0.3082028374807834""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 0.3082028374807834
""",
)

entry(
    index = 225,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=0, w0=(244.3,'kJ/mol'), E0=(122.15,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(203.312,'kJ/mol'), E0=(101.656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_3BrCClINOPSSi->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_3C-inRing",
    kinetics = ArrheniusBM(A=(1.16055e+34,'m^3/(mol*s)'), n=-7.5829, w0=(205.5,'kJ/mol'), E0=(23.3615,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 228,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing",
    kinetics = ArrheniusBM(A=(2.96838e+07,'m^3/(mol*s)'), n=0.205688, w0=(205.5,'kJ/mol'), E0=(98.4363,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014796686746860407, var=0.08507179062171762, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing
    Total Standard Deviation in ln(k): 0.6219000654902375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing
Total Standard Deviation in ln(k): 0.6219000654902375""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing
Total Standard Deviation in ln(k): 0.6219000654902375
""",
)

entry(
    index = 229,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.69017e+08,'m^3/(mol*s)'), n=0.0270733, w0=(205.5,'kJ/mol'), E0=(110.329,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07859689658672972, var=0.29828115478932965, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.2923681473768245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.2923681473768245""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.2923681473768245
""",
)

entry(
    index = 230,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(5.24875e+07,'m^3/(mol*s)'), n=0.108702, w0=(205.5,'kJ/mol'), E0=(86.89,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13966497549833137, var=0.060976250169598185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 0.845953665821445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.845953665821445""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.845953665821445
""",
)

entry(
    index = 231,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.83153e+09,'m^3/(mol*s)'), n=-0.472098, w0=(235.104,'kJ/mol'), E0=(88.9793,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5241266783778138, var=6.191049709717304, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 6.3050469542594705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 6.3050469542594705""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 6.3050469542594705
""",
)

entry(
    index = 232,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Sp-3C#1C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(277.999,'kJ/mol'), E0=(139,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Sp-3C#1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Sp-3C#1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Sp-3C#1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Sp-3C#1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C",
    kinetics = ArrheniusBM(A=(1.30121e+08,'m^3/(mol*s)'), n=-0.0104386, w0=(221.434,'kJ/mol'), E0=(112.941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18513990790935178, var=0.004340108194692165, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C
    Total Standard Deviation in ln(k): 0.597246587591217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C
Total Standard Deviation in ln(k): 0.597246587591217""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C
Total Standard Deviation in ln(k): 0.597246587591217
""",
)

entry(
    index = 234,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(2.74542e+17,'m^3/(mol*s)'), n=-2.98653, w0=(170.231,'kJ/mol'), E0=(93.2203,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15785304224664345, var=13.502872862885626, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C
    Total Standard Deviation in ln(k): 7.763266401362987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C
Total Standard Deviation in ln(k): 7.763266401362987""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C
Total Standard Deviation in ln(k): 7.763266401362987
""",
)

entry(
    index = 235,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(8.35745e+14,'m^3/(mol*s)'), n=-2.42176, w0=(162.278,'kJ/mol'), E0=(90.4341,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5567865169538585, var=1.0472086059819863, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 3.4504708732678733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C
Total Standard Deviation in ln(k): 3.4504708732678733""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C
Total Standard Deviation in ln(k): 3.4504708732678733
""",
)

entry(
    index = 236,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl",
    kinetics = ArrheniusBM(A=(1.22185e+12,'m^3/(mol*s)'), n=-2.24226, w0=(195.206,'kJ/mol'), E0=(26.3188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19761962228075053, var=7.388499069837912, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl
    Total Standard Deviation in ln(k): 5.945761237450544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl
Total Standard Deviation in ln(k): 5.945761237450544""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl
Total Standard Deviation in ln(k): 5.945761237450544
""",
)

entry(
    index = 237,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl",
    kinetics = ArrheniusBM(A=(3.7835e+13,'m^3/(mol*s)'), n=-2.73588, w0=(216.213,'kJ/mol'), E0=(14.2673,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1561775585582476, var=0.3562102304487583, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl
    Total Standard Deviation in ln(k): 1.588898985098241"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl
Total Standard Deviation in ln(k): 1.588898985098241""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl
Total Standard Deviation in ln(k): 1.588898985098241
""",
)

entry(
    index = 238,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O_1BrHNO->O",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(90.1681,'kJ/mol'), E0=(45.084,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O_1BrHNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O_1BrHNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O_1BrHNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O_1BrHNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O_N-1BrHNO->O",
    kinetics = ArrheniusBM(A=(3.65367e+06,'m^3/(mol*s)'), n=0.2352, w0=(102.495,'kJ/mol'), E0=(51.2476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4647064516488904, var=0.481324023566866, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O_N-1BrHNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O_N-1BrHNO->O
    Total Standard Deviation in ln(k): 2.5584396225376094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O_N-1BrHNO->O
Total Standard Deviation in ln(k): 2.5584396225376094""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_2R->O_N-1BrHNO->O
Total Standard Deviation in ln(k): 2.5584396225376094
""",
)

entry(
    index = 240,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_2HN->H",
    kinetics = ArrheniusBM(A=(2.21037e+06,'m^3/(mol*s)'), n=0.349925, w0=(229.5,'kJ/mol'), E0=(88.9685,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_2HN->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_2HN->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_2HN->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_2HN->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H",
    kinetics = ArrheniusBM(A=(4.1567e+08,'m^3/(mol*s)'), n=-0.404886, w0=(113.775,'kJ/mol'), E0=(42.0699,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04995692072360852, var=4.431663431144694, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H
    Total Standard Deviation in ln(k): 4.345791239042951"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H
Total Standard Deviation in ln(k): 4.345791239042951""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H
Total Standard Deviation in ln(k): 4.345791239042951
""",
)

entry(
    index = 242,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(115432,'m^3/(mol*s)'), n=0.737923, w0=(183.345,'kJ/mol'), E0=(18.3345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07812153679625017, var=1.3728208894241956, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C
    Total Standard Deviation in ln(k): 2.5451820285784703"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 2.5451820285784703""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 2.5451820285784703
""",
)

entry(
    index = 243,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(0.00080002,'m^3/(mol*s)'), n=2.54661, w0=(212.807,'kJ/mol'), E0=(21.2807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18241639247444652, var=49.42215796567784, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C',), comment="""BM rule fitted to 29 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
    Total Standard Deviation in ln(k): 14.551799603486971"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 14.551799603486971""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 14.551799603486971
""",
)

entry(
    index = 244,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.71558e+13,'m^3/(mol*s)'), n=-1.79496, w0=(173,'kJ/mol'), E0=(76.6317,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48953136518204227, var=0.7469372747681267, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi
    Total Standard Deviation in ln(k): 2.9625812795817383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 2.9625812795817383""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 2.9625812795817383
""",
)

entry(
    index = 245,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(37275.5,'m^3/(mol*s)'), n=0.706335, w0=(206.282,'kJ/mol'), E0=(20.6282,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.027135978032599328, var=6.641755355493768, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi
    Total Standard Deviation in ln(k): 5.234704558656989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 5.234704558656989""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 5.234704558656989
""",
)

entry(
    index = 246,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.77939e+22,'m^3/(mol*s)'), n=-4.28607, w0=(173,'kJ/mol'), E0=(59.2452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4346790339494022, var=2.6825794312792315, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 4.375630130253821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 4.375630130253821""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 4.375630130253821
""",
)

entry(
    index = 247,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O",
    kinetics = ArrheniusBM(A=(6.97424e+09,'m^3/(mol*s)'), n=-0.755598, w0=(175.609,'kJ/mol'), E0=(17.5609,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05919846361270117, var=3.5246427320828375, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O
    Total Standard Deviation in ln(k): 3.9124358846637137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O
Total Standard Deviation in ln(k): 3.9124358846637137""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O
Total Standard Deviation in ln(k): 3.9124358846637137
""",
)

entry(
    index = 248,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O",
    kinetics = ArrheniusBM(A=(1.91244e+09,'m^3/(mol*s)'), n=-0.647379, w0=(179.298,'kJ/mol'), E0=(52.5379,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07506909174384382, var=7.640310135441183, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O
    Total Standard Deviation in ln(k): 5.729926274713971"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O
Total Standard Deviation in ln(k): 5.729926274713971""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O
Total Standard Deviation in ln(k): 5.729926274713971
""",
)

entry(
    index = 249,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(25637.8,'m^3/(mol*s)'), n=0.759408, w0=(264.35,'kJ/mol'), E0=(164.836,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.3882e+06,'m^3/(mol*s)'), n=0.317264, w0=(302.631,'kJ/mol'), E0=(182.645,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_N-4R!H-u0_Ext-1C-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(246.285,'kJ/mol'), E0=(178.838,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0181796,'m^3/(mol*s)'), n=2.5459, w0=(266.005,'kJ/mol'), E0=(26.6005,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0174011388988842, var=107.26680278783425, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 23.31926292358801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 23.31926292358801""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 23.31926292358801
""",
)

entry(
    index = 253,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.11e+34,'m^3/(mol*s)'), n=-9.59, w0=(271.762,'kJ/mol'), E0=(194.038,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Sp-4C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R_4BrClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=-1.71507e-08, w0=(244.299,'kJ/mol'), E0=(177.487,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R_4BrClFINOPSSi->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R_4BrClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R_4BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R_4BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 255,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R_N-4BrClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(2.03025e+08,'m^3/(mol*s)'), n=0.0776927, w0=(228.234,'kJ/mol'), E0=(169.317,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R_N-4BrClFINOPSSi->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R_N-4BrClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R_N-4BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_N-4R!H->C_Ext-1C-R_N-4BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(25018.3,'m^3/(mol*s)'), n=0.762967, w0=(173,'kJ/mol'), E0=(57.3292,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-2C-R_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_5R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=5.25761e-08, w0=(173,'kJ/mol'), E0=(64.0531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_5R!H->O_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_5R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 258,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.26848e+08,'m^3/(mol*s)'), n=-0.55, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3562201627384158e-15, var=0.18719384195212602, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 0.8673667472247014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 0.8673667472247014""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 0.8673667472247014
""",
)

entry(
    index = 259,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.39195e+11,'m^3/(mol*s)'), n=-0.855542, w0=(173,'kJ/mol'), E0=(80.042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08362621578487493, var=0.7494705113280606, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.9456546683702245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9456546683702245""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9456546683702245
""",
)

entry(
    index = 260,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.20378e+09,'m^3/(mol*s)'), n=-0.813265, w0=(173,'kJ/mol'), E0=(76.4155,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 261,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.14759e+09,'m^3/(mol*s)'), n=-1.3, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12459479191003729, var=4.722672561921672, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.669684542985857"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.669684542985857""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.669684542985857
""",
)

entry(
    index = 262,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.98065e+08,'m^3/(mol*s)'), n=-0.75, w0=(177.753,'kJ/mol'), E0=(88.8765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09619936845727288, var=0.8575717470917584, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.098195278084049"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.098195278084049""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.098195278084049
""",
)

entry(
    index = 263,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.04234e+06,'m^3/(mol*s)'), n=0.213743, w0=(183.281,'kJ/mol'), E0=(79.4146,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0001902170257574481, var=0.06095973871761109, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 0.4954475454031361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.4954475454031361""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.4954475454031361
""",
)

entry(
    index = 264,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_3BrCClINOPSSi-inRing",
    kinetics = ArrheniusBM(A=(5.781e+11,'m^3/(mol*s)'), n=-1.568, w0=(173,'kJ/mol'), E0=(71.0565,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_3BrCClINOPSSi-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_3BrCClINOPSSi-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 265,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_N-3BrCClINOPSSi-inRing",
    kinetics = ArrheniusBM(A=(1.92839e+08,'m^3/(mol*s)'), n=-0.425577, w0=(173,'kJ/mol'), E0=(70.7985,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_N-3BrCClINOPSSi-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_N-3BrCClINOPSSi-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_N-3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_N-3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 266,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.9764e+07,'m^3/(mol*s)'), n=0.206427, w0=(205.5,'kJ/mol'), E0=(98.6789,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012762858847282958, var=0.0681928511809308, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 0.5555792106608185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 0.5555792106608185""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 0.5555792106608185
""",
)

entry(
    index = 267,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(4.79728e+07,'m^3/(mol*s)'), n=0.210679, w0=(205.5,'kJ/mol'), E0=(102.402,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 268,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(6.84478e+06,'m^3/(mol*s)'), n=0.41638, w0=(205.5,'kJ/mol'), E0=(76.6427,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 269,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(3.16837e+06,'m^3/(mol*s)'), n=0.460513, w0=(205.5,'kJ/mol'), E0=(83.6747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(8.58356e+07,'m^3/(mol*s)'), n=0.0405873, w0=(205.5,'kJ/mol'), E0=(94.779,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 271,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(2.11623e+09,'m^3/(mol*s)'), n=-0.373695, w0=(205.5,'kJ/mol'), E0=(114.051,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1561377006943811, var=0.2424883010508162, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 1.3794995025163954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.3794995025163954""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.3794995025163954
""",
)

entry(
    index = 272,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.15008e+19,'m^3/(mol*s)'), n=-5.14141, w0=(283.352,'kJ/mol'), E0=(28.3352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30194898785893354, var=33.391442354799615, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 12.343093378056347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 12.343093378056347""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 12.343093378056347
""",
)

entry(
    index = 273,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(210.252,'kJ/mol'), E0=(105.126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C_Sp-3C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C_Sp-3C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C_Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C_Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 274,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.21e+08,'m^3/(mol*s)'), n=0, w0=(232.616,'kJ/mol'), E0=(116.308,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C_N-Sp-3C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_N-Sp-3C#1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 275,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.53909e+17,'m^3/(mol*s)'), n=-3.01436, w0=(169.5,'kJ/mol'), E0=(92.8645,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1322010867318754, var=14.085044258927631, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 7.8559436970640055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 7.8559436970640055""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 7.8559436970640055
""",
)

entry(
    index = 276,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R",
    kinetics = ArrheniusBM(A=(3.43828e+09,'m^3/(mol*s)'), n=-0.877143, w0=(179,'kJ/mol'), E0=(57.4483,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00018182398773329, var=0.9747614083673242, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R
    Total Standard Deviation in ln(k): 1.9797319062752796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R
Total Standard Deviation in ln(k): 1.9797319062752796""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R
Total Standard Deviation in ln(k): 1.9797319062752796
""",
)

entry(
    index = 277,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.70271e+41,'m^3/(mol*s)'), n=-10.4621, w0=(286.306,'kJ/mol'), E0=(240.126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34272571023162446, var=8.35187014438832, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.654724524958882"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 6.654724524958882""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 6.654724524958882
""",
)

entry(
    index = 278,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_2BrClO->O",
    kinetics = ArrheniusBM(A=(7.7e+07,'m^3/(mol*s)'), n=0, w0=(195.452,'kJ/mol'), E0=(97.726,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_2BrClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_2BrClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_2BrClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_2BrClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O",
    kinetics = ArrheniusBM(A=(1.30795e+08,'m^3/(mol*s)'), n=-0.354336, w0=(200.59,'kJ/mol'), E0=(39.061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6744961738357014, var=5.983113072146612, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O
    Total Standard Deviation in ln(k): 6.598376763156257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O
Total Standard Deviation in ln(k): 6.598376763156257""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O
Total Standard Deviation in ln(k): 6.598376763156257
""",
)

entry(
    index = 280,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_2BrClO->O",
    kinetics = ArrheniusBM(A=(1066.12,'m^3/(mol*s)'), n=0.975002, w0=(179,'kJ/mol'), E0=(56.2372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.6160302404187386, var=16.555154998552645, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_2BrClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_2BrClO->O
    Total Standard Deviation in ln(k): 14.729811696507475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_2BrClO->O
Total Standard Deviation in ln(k): 14.729811696507475""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_2BrClO->O
Total Standard Deviation in ln(k): 14.729811696507475
""",
)

entry(
    index = 281,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O",
    kinetics = ArrheniusBM(A=(1.3326e+15,'m^3/(mol*s)'), n=-2.42843, w0=(172.989,'kJ/mol'), E0=(100.135,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06802077035451923, var=1.127523964505584, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O
    Total Standard Deviation in ln(k): 2.2996330237868694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O
Total Standard Deviation in ln(k): 2.2996330237868694""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O
Total Standard Deviation in ln(k): 2.2996330237868694
""",
)

entry(
    index = 282,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_3ClO->O",
    kinetics = ArrheniusBM(A=(1.50059e+20,'m^3/(mol*s)'), n=-4.57992, w0=(255.701,'kJ/mol'), E0=(178.485,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_3ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_3ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O",
    kinetics = ArrheniusBM(A=(8.17544e+14,'m^3/(mol*s)'), n=-3.04515, w0=(175.041,'kJ/mol'), E0=(36.0171,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11357895682607125, var=3.0907683508548973, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O
    Total Standard Deviation in ln(k): 3.8098150432507616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O
Total Standard Deviation in ln(k): 3.8098150432507616""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O
Total Standard Deviation in ln(k): 3.8098150432507616
""",
)

entry(
    index = 284,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_3ClO->O",
    kinetics = ArrheniusBM(A=(2.31504e+12,'m^3/(mol*s)'), n=-2.20453, w0=(205.5,'kJ/mol'), E0=(73.19,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_3ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_3ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_N-3ClO->O",
    kinetics = ArrheniusBM(A=(7.1883e+15,'m^3/(mol*s)'), n=-3.4347, w0=(233.671,'kJ/mol'), E0=(119.145,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.027178382159491407, var=0.09441460044167417, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_N-3ClO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_N-3ClO->O
    Total Standard Deviation in ln(k): 0.684281516028437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_N-3ClO->O
Total Standard Deviation in ln(k): 0.684281516028437""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_N-3ClO->O
Total Standard Deviation in ln(k): 0.684281516028437
""",
)

entry(
    index = 286,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H_1BrHNO->O",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=-2.58451e-08, w0=(100.5,'kJ/mol'), E0=(38.1729,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H_1BrHNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H_1BrHNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H_1BrHNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H_1BrHNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H_N-1BrHNO->O",
    kinetics = ArrheniusBM(A=(5.02e+08,'m^3/(mol*s)'), n=-0.429, w0=(134.802,'kJ/mol'), E0=(100.322,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H_N-1BrHNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H_N-1BrHNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H_N-1BrHNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->C_N-1BrClHNO->Cl_Ext-1BrHNO-R_N-3R!H->Cl_N-3BrBrCCFFIINNOOPPSSSiSi-u1_Sp-3BrCFINOPSSi-1BrBrCFHINNOOPSSi_N-3BrCFINOPSSi->N_N-2R->O_N-2HN->H_N-1BrHNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(1.66076e+12,'m^3/(mol*s)'), n=-1.11288, w0=(200.425,'kJ/mol'), E0=(195.6,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1565620711466221, var=0.4470975497024635, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O
    Total Standard Deviation in ln(k): 1.7338452340467785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O
Total Standard Deviation in ln(k): 1.7338452340467785""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O
Total Standard Deviation in ln(k): 1.7338452340467785
""",
)

entry(
    index = 289,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(2.52979e+09,'m^3/(mol*s)'), n=-0.80585, w0=(173,'kJ/mol'), E0=(78.8627,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09973385939881636, var=2.469428406434827, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 3.400911495360566"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O
Total Standard Deviation in ln(k): 3.400911495360566""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O
Total Standard Deviation in ln(k): 3.400911495360566
""",
)

entry(
    index = 290,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.4003e-05,'m^3/(mol*s)'), n=3.05268, w0=(221.749,'kJ/mol'), E0=(22.1749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23096908084748602, var=43.21594392569762, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R',), comment="""BM rule fitted to 28 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R
    Total Standard Deviation in ln(k): 13.759219118151918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R
Total Standard Deviation in ln(k): 13.759219118151918""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R
Total Standard Deviation in ln(k): 13.759219118151918
""",
)

entry(
    index = 291,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_Ext-1C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(3.1564e+20,'m^3/(mol*s)'), n=-4.13392, w0=(173,'kJ/mol'), E0=(55.8427,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_Ext-1C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_Ext-1C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_Ext-1C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_Ext-1C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 292,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_Ext-1C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(3.03428e+07,'m^3/(mol*s)'), n=0.110658, w0=(194.841,'kJ/mol'), E0=(144.13,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_Ext-1C-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_Ext-1C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_Ext-1C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_Ext-1C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 293,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(17938.9,'m^3/(mol*s)'), n=0.724393, w0=(203.647,'kJ/mol'), E0=(20.3647,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.045812496628463636, var=5.974901518640497, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 5.015403350353836"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 5.015403350353836""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 5.015403350353836
""",
)

entry(
    index = 294,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(650762,'m^3/(mol*s)'), n=0.635726, w0=(208.198,'kJ/mol'), E0=(20.8198,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10446152198264383, var=1.0578772723645535, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 2.324399532016101"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.324399532016101""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.324399532016101
""",
)

entry(
    index = 295,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(3.0188e+23,'m^3/(mol*s)'), n=-4.63802, w0=(173,'kJ/mol'), E0=(58.1291,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.44975507924449165, var=0.9502532974344873, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 3.08427241466098"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 3.08427241466098""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 3.08427241466098
""",
)

entry(
    index = 296,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.19798e+21,'m^3/(mol*s)'), n=-3.58217, w0=(173,'kJ/mol'), E0=(61.4775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R",
    kinetics = ArrheniusBM(A=(1.39951e+14,'m^3/(mol*s)'), n=-1.98214, w0=(173,'kJ/mol'), E0=(84.173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12162076670474682, var=3.5754321587283755, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R
    Total Standard Deviation in ln(k): 4.096295921207409"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R
Total Standard Deviation in ln(k): 4.096295921207409""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R
Total Standard Deviation in ln(k): 4.096295921207409
""",
)

entry(
    index = 298,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO",
    kinetics = ArrheniusBM(A=(4.16386e+06,'m^3/(mol*s)'), n=0.163343, w0=(180.057,'kJ/mol'), E0=(18.0057,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0015930387371685213, var=1.3613694417207851, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO
    Total Standard Deviation in ln(k): 2.343082140127374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO
Total Standard Deviation in ln(k): 2.343082140127374""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO
Total Standard Deviation in ln(k): 2.343082140127374
""",
)

entry(
    index = 299,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_N-Sp-4O-2CHO",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=0, w0=(179.602,'kJ/mol'), E0=(89.8012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_N-Sp-4O-2CHO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_N-Sp-4O-2CHO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_N-Sp-4O-2CHO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_N-Sp-4O-2CHO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O",
    kinetics = ArrheniusBM(A=(1.94393e+09,'m^3/(mol*s)'), n=-0.649346, w0=(179,'kJ/mol'), E0=(51.6546,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07544611943440914, var=7.6378459515068835, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O
    Total Standard Deviation in ln(k): 5.729979905398212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O
Total Standard Deviation in ln(k): 5.729979905398212""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O
Total Standard Deviation in ln(k): 5.729979905398212
""",
)

entry(
    index = 301,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O",
    kinetics = ArrheniusBM(A=(474.478,'m^3/(mol*s)'), n=1.18309, w0=(202.279,'kJ/mol'), E0=(5.42947,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3276350899348033, var=12.464335599725395, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O
    Total Standard Deviation in ln(k): 7.9008940614600744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O
Total Standard Deviation in ln(k): 7.9008940614600744""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O
Total Standard Deviation in ln(k): 7.9008940614600744
""",
)

entry(
    index = 302,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(244.986,'kJ/mol'), E0=(177.869,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 303,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(0.0147919,'m^3/(mol*s)'), n=2.57428, w0=(268.107,'kJ/mol'), E0=(26.8107,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.952014556784187, var=110.22776226510153, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 23.439591685732978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 23.439591685732978""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 23.439591685732978
""",
)

entry(
    index = 304,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.75e+08,'m^3/(mol*s)'), n=-0.75, w0=(173,'kJ/mol'), E0=(69.7441,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_3CO->O_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.1576e+11,'m^3/(mol*s)'), n=-0.948728, w0=(173,'kJ/mol'), E0=(81.224,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.24e+10,'m^3/(mol*s)'), n=-1.5, w0=(173,'kJ/mol'), E0=(69.3328,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-1C-R_N-3BrCClINOPSSi->Cl_N-3CO->O_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 307,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.91473e+06,'m^3/(mol*s)'), n=0.213499, w0=(183.183,'kJ/mol'), E0=(78.8683,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0002843643556459568, var=0.015202055380165683, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.24789153321199428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.24789153321199428""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.24789153321199428
""",
)

entry(
    index = 308,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(3.406e+06,'m^3/(mol*s)'), n=0.211, w0=(183.012,'kJ/mol'), E0=(136.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.88633e+07,'m^3/(mol*s)'), n=0.213913, w0=(205.94,'kJ/mol'), E0=(102.97,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.197906922440378e-05, var=0.01210657880115639, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.22078677680714184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.22078677680714184""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.22078677680714184
""",
)

entry(
    index = 310,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Sp-3C=1C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(249.899,'kJ/mol'), E0=(124.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Sp-3C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Sp-3C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Sp-3C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Sp-3C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C",
    kinetics = ArrheniusBM(A=(3.01146e+07,'m^3/(mol*s)'), n=0.20296, w0=(205.5,'kJ/mol'), E0=(95.2091,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7080255759885304, var=1.015783988518826, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C
    Total Standard Deviation in ln(k): 3.799453225621823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C
Total Standard Deviation in ln(k): 3.799453225621823""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C
Total Standard Deviation in ln(k): 3.799453225621823
""",
)

entry(
    index = 312,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(2.06819e+09,'m^3/(mol*s)'), n=-0.368028, w0=(205.516,'kJ/mol'), E0=(109.441,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02118791466423305, var=0.059047477739823905, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C
    Total Standard Deviation in ln(k): 0.5403803109828671"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C
Total Standard Deviation in ln(k): 0.5403803109828671""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C
Total Standard Deviation in ln(k): 0.5403803109828671
""",
)

entry(
    index = 313,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(2.83712e+08,'m^3/(mol*s)'), n=-0.251115, w0=(205.5,'kJ/mol'), E0=(121.486,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09753801016004564, var=3.4382379629420625, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 3.962347637832616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 3.962347637832616""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 3.962347637832616
""",
)

entry(
    index = 314,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(4.36443e+19,'m^3/(mol*s)'), n=-5.46416, w0=(282.202,'kJ/mol'), E0=(28.2202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24476884684624783, var=42.99031552256663, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C
    Total Standard Deviation in ln(k): 13.759443681283665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C
Total Standard Deviation in ln(k): 13.759443681283665""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C
Total Standard Deviation in ln(k): 13.759443681283665
""",
)

entry(
    index = 315,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.43521e+26,'m^3/(mol*s)'), n=-6.47299, w0=(285.077,'kJ/mol'), E0=(184.723,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28584039541456774, var=0.30467661605832125, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 1.8247559838418383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.8247559838418383""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.8247559838418383
""",
)

entry(
    index = 316,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_2BrClO->Br",
    kinetics = ArrheniusBM(A=(96.2589,'m^3/(mol*s)'), n=1.014, w0=(190.329,'kJ/mol'), E0=(138.542,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_2BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_2BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_2BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_2BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 317,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br",
    kinetics = ArrheniusBM(A=(3.83865e+17,'m^3/(mol*s)'), n=-3.02378, w0=(171.955,'kJ/mol'), E0=(92.9264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1460652772066544, var=13.924935409351479, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br
    Total Standard Deviation in ln(k): 7.847893613982326"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br
Total Standard Deviation in ln(k): 7.847893613982326""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br
Total Standard Deviation in ln(k): 7.847893613982326
""",
)

entry(
    index = 318,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.64227e+08,'m^3/(mol*s)'), n=-0.443448, w0=(179,'kJ/mol'), E0=(51.3527,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.027679913061982666, var=0.7111546953226252, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.760140379624283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.760140379624283""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.760140379624283
""",
)

entry(
    index = 319,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.05803e+27,'m^3/(mol*s)'), n=-6.59025, w0=(305.648,'kJ/mol'), E0=(203.233,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.81048e+30,'m^3/(mol*s)'), n=-7.09644, w0=(275.049,'kJ/mol'), E0=(190.333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 321,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.21509e+31,'m^3/(mol*s)'), n=-7.40295, w0=(278.221,'kJ/mol'), E0=(189.92,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O_2BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.37532e+19,'m^3/(mol*s)'), n=-3.57257, w0=(227.497,'kJ/mol'), E0=(162.134,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06692652365297133, var=8.00644804217264, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O_2BrCl->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O_2BrCl->Cl
    Total Standard Deviation in ln(k): 5.840688829682172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O_2BrCl->Cl
Total Standard Deviation in ln(k): 5.840688829682172""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O_2BrCl->Cl
Total Standard Deviation in ln(k): 5.840688829682172
""",
)

entry(
    index = 323,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O_N-2BrCl->Cl",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(146.776,'kJ/mol'), E0=(73.3882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O_N-2BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O_N-2BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O_N-2BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_N-2BrClO->O_N-2BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_2BrClO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.004135,'m^3/(mol*s)'), n=2.525, w0=(179,'kJ/mol'), E0=(39.2962,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_2BrClO->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_2BrClO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_2BrClO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_2BrClO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 325,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.84656e+14,'m^3/(mol*s)'), n=-2.20814, w0=(167.469,'kJ/mol'), E0=(83.7345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.170212951015834, var=2.1807980442464765, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 3.3881683350873546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.3881683350873546""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.3881683350873546
""",
)

entry(
    index = 326,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_2BrCl->Cl",
    kinetics = ArrheniusBM(A=(2.99534e+23,'m^3/(mol*s)'), n=-5.08851, w0=(185.065,'kJ/mol'), E0=(92.5323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0732383640302599, var=0.25050177797223916, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_2BrCl->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_2BrCl->Cl
    Total Standard Deviation in ln(k): 1.187388956376302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_2BrCl->Cl
Total Standard Deviation in ln(k): 1.187388956376302""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_2BrCl->Cl
Total Standard Deviation in ln(k): 1.187388956376302
""",
)

entry(
    index = 327,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_N-2BrCl->Cl",
    kinetics = ArrheniusBM(A=(5.19615e+07,'m^3/(mol*s)'), n=0, w0=(169.195,'kJ/mol'), E0=(84.5974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.166553000908251e-16, var=2.4138979216251584, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_N-2BrCl->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_N-2BrCl->Cl
    Total Standard Deviation in ln(k): 3.1147015559000386"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_N-2BrCl->Cl
Total Standard Deviation in ln(k): 3.1147015559000386""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_N-2BrCl->Cl
Total Standard Deviation in ln(k): 3.1147015559000386
""",
)

entry(
    index = 328,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.5271e+11,'m^3/(mol*s)'), n=-2.09678, w0=(163.5,'kJ/mol'), E0=(3.44407,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4336750620298182, var=13.74094532953404, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 8.520944410917108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O_Ext-1C-R
Total Standard Deviation in ln(k): 8.520944410917108""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O_Ext-1C-R
Total Standard Deviation in ln(k): 8.520944410917108
""",
)

entry(
    index = 329,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_N-3ClO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.805e+20,'m^3/(mol*s)'), n=-4.82, w0=(231.271,'kJ/mol'), E0=(167.983,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2988541939225804, var=8.66250553588933e-06, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_N-3ClO->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_N-3ClO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 0.7567902977644224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_N-3ClO->O_Ext-1C-R
Total Standard Deviation in ln(k): 0.7567902977644224""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_N-2ClH->Cl_N-3ClO->O_Ext-1C-R
Total Standard Deviation in ln(k): 0.7567902977644224
""",
)

entry(
    index = 330,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O",
    kinetics = ArrheniusBM(A=(2.32449e+07,'m^3/(mol*s)'), n=0.379878, w0=(218.923,'kJ/mol'), E0=(156.14,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.45593690905702194, var=3.648482725719283, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O
    Total Standard Deviation in ln(k): 4.9748149701790085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O
Total Standard Deviation in ln(k): 4.9748149701790085""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O
Total Standard Deviation in ln(k): 4.9748149701790085
""",
)

entry(
    index = 331,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(1.07841e+07,'m^3/(mol*s)'), n=0.27139, w0=(181.927,'kJ/mol'), E0=(18.1927,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3542542970132615, var=0.1662136676078347, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O
    Total Standard Deviation in ln(k): 1.7074028411742377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O
Total Standard Deviation in ln(k): 1.7074028411742377""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O
Total Standard Deviation in ln(k): 1.7074028411742377
""",
)

entry(
    index = 332,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(3.89042e+08,'m^3/(mol*s)'), n=-0.664637, w0=(173,'kJ/mol'), E0=(77.3233,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04858958239348656, var=1.1512762754120196, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.2731158614709948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C
Total Standard Deviation in ln(k): 2.2731158614709948""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C
Total Standard Deviation in ln(k): 2.2731158614709948
""",
)

entry(
    index = 333,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.64502e+10,'m^3/(mol*s)'), n=-0.947062, w0=(173,'kJ/mol'), E0=(80.4021,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054607041174056355, var=3.8424483316942872, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 4.066918195800661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_N-8R!H->C
Total Standard Deviation in ln(k): 4.066918195800661""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_N-8R!H->C
Total Standard Deviation in ln(k): 4.066918195800661
""",
)

entry(
    index = 334,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F",
    kinetics = ArrheniusBM(A=(1.18177e-07,'m^3/(mol*s)'), n=3.59008, w0=(229.752,'kJ/mol'), E0=(22.9752,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28134279373081655, var=36.53586607220452, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F
    Total Standard Deviation in ln(k): 12.824493682571866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F
Total Standard Deviation in ln(k): 12.824493682571866""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F
Total Standard Deviation in ln(k): 12.824493682571866
""",
)

entry(
    index = 335,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F",
    kinetics = ArrheniusBM(A=(2.67279e+12,'m^3/(mol*s)'), n=-1.42569, w0=(173,'kJ/mol'), E0=(77.5258,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1888117226308176, var=43.864707906901536, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F
    Total Standard Deviation in ln(k): 13.751849345939487"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F
Total Standard Deviation in ln(k): 13.751849345939487""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F
Total Standard Deviation in ln(k): 13.751849345939487
""",
)

entry(
    index = 336,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R",
    kinetics = ArrheniusBM(A=(905756,'m^3/(mol*s)'), n=0.256125, w0=(196.794,'kJ/mol'), E0=(98.3971,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012876425435346738, var=2.3118273367630446, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R
    Total Standard Deviation in ln(k): 3.0804912605875283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R
Total Standard Deviation in ln(k): 3.0804912605875283""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R
Total Standard Deviation in ln(k): 3.0804912605875283
""",
)

entry(
    index = 337,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl",
    kinetics = ArrheniusBM(A=(9.40954e+12,'m^3/(mol*s)'), n=-1.95117, w0=(194.895,'kJ/mol'), E0=(187.248,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33502096410165905, var=1.436706917278947, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl
    Total Standard Deviation in ln(k): 3.2446910020859536"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl
Total Standard Deviation in ln(k): 3.2446910020859536""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl
Total Standard Deviation in ln(k): 3.2446910020859536
""",
)

entry(
    index = 338,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl",
    kinetics = ArrheniusBM(A=(619156,'m^3/(mol*s)'), n=0.645957, w0=(213.187,'kJ/mol'), E0=(21.3187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12721342345559444, var=1.019685025685851, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl
    Total Standard Deviation in ln(k): 2.3440022651030223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl
Total Standard Deviation in ln(k): 2.3440022651030223""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl
Total Standard Deviation in ln(k): 2.3440022651030223
""",
)

entry(
    index = 339,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(4.17591e+23,'m^3/(mol*s)'), n=-4.73474, w0=(173,'kJ/mol'), E0=(57.9426,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 340,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.18232e+23,'m^3/(mol*s)'), n=-4.54131, w0=(173,'kJ/mol'), E0=(58.3156,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_5R!H->O_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 341,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.86408e+14,'m^3/(mol*s)'), n=-2.10498, w0=(173,'kJ/mol'), E0=(82.7062,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13981263032647262, var=4.794595046699841, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 4.740968961100198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 4.740968961100198""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 4.740968961100198
""",
)

entry(
    index = 342,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(7.88861e+13,'m^3/(mol*s)'), n=-1.73645, w0=(174.213,'kJ/mol'), E0=(87.1066,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 343,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(2.09174e+06,'m^3/(mol*s)'), n=0.247771, w0=(177.095,'kJ/mol'), E0=(17.7095,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01955127560727745, var=2.562356453815091, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 3.25817586282907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.25817586282907""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.25817586282907
""",
)

entry(
    index = 344,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(4.46756e+07,'m^3/(mol*s)'), n=-0.128224, w0=(188.945,'kJ/mol'), E0=(140.592,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_N-5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.98596e+09,'m^3/(mol*s)'), n=-0.728229, w0=(179,'kJ/mol'), E0=(34.9879,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10603592260189464, var=5.988368566843518, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C
    Total Standard Deviation in ln(k): 5.172237861149569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C
Total Standard Deviation in ln(k): 5.172237861149569""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C
Total Standard Deviation in ln(k): 5.172237861149569
""",
)

entry(
    index = 346,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.73439e+09,'m^3/(mol*s)'), n=-0.228634, w0=(205.59,'kJ/mol'), E0=(73.7662,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04933182918570927, var=16.419145602683322, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C
    Total Standard Deviation in ln(k): 8.247245094332513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C
Total Standard Deviation in ln(k): 8.247245094332513""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C
Total Standard Deviation in ln(k): 8.247245094332513
""",
)

entry(
    index = 347,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-4CCl-R",
    kinetics = ArrheniusBM(A=(0.0678417,'m^3/(mol*s)'), n=2.13578, w0=(241.47,'kJ/mol'), E0=(179.656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-4CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-4CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-4CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-4CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4808.73,'m^3/(mol*s)'), n=0.885933, w0=(177.951,'kJ/mol'), E0=(88.9756,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028989899202882224, var=28.040324790211425, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-2C-R
    Total Standard Deviation in ln(k): 10.688535824411682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-2C-R
Total Standard Deviation in ln(k): 10.688535824411682""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-2C-R
Total Standard Deviation in ln(k): 10.688535824411682
""",
)

entry(
    index = 349,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F",
    kinetics = ArrheniusBM(A=(0.014057,'m^3/(mol*s)'), n=2.58073, w0=(271.03,'kJ/mol'), E0=(27.103,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8580547263388923, var=114.27822676489258, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F
    Total Standard Deviation in ln(k): 23.586733794279073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F
Total Standard Deviation in ln(k): 23.586733794279073""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F
Total Standard Deviation in ln(k): 23.586733794279073
""",
)

entry(
    index = 350,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->F",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(241.803,'kJ/mol'), E0=(120.902,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.83408e+06,'m^3/(mol*s)'), n=0.21354, w0=(183.599,'kJ/mol'), E0=(18.3599,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00013833946776604204, var=0.009545124806212434, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.19620850882650892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.19620850882650892""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.19620850882650892
""",
)

entry(
    index = 352,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(1.92552e+06,'m^3/(mol*s)'), n=0.212513, w0=(182.445,'kJ/mol'), E0=(91.2227,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 353,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.85197e+07,'m^3/(mol*s)'), n=0.213787, w0=(205.932,'kJ/mol'), E0=(102.966,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00012681105802580086, var=0.012046587691161825, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.22035222491166043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.22035222491166043""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.22035222491166043
""",
)

entry(
    index = 354,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.89626e+07,'m^3/(mol*s)'), n=0.120172, w0=(205.5,'kJ/mol'), E0=(29.6951,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0028590242889813336, var=4.845846638591843, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.420263699272195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.420263699272195""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.420263699272195
""",
)

entry(
    index = 355,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(227.003,'kJ/mol'), E0=(164.454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(73.3774,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005718031450769882, var=3.1264413462487737e-19, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 0.014366914313828543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Sp-4R!H-1C
Total Standard Deviation in ln(k): 0.014366914313828543""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Sp-4R!H-1C
Total Standard Deviation in ln(k): 0.014366914313828543
""",
)

entry(
    index = 357,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(6.117e+08,'m^3/(mol*s)'), n=-0.152, w0=(221.392,'kJ/mol'), E0=(163.779,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 358,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_Sp-4C=3C",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(80.9193,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_Sp-4C=3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_Sp-4C=3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C",
    kinetics = ArrheniusBM(A=(2.33349e+09,'m^3/(mol*s)'), n=-0.385433, w0=(210.716,'kJ/mol'), E0=(96.0261,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07348196797957501, var=0.05109986366496323, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C
    Total Standard Deviation in ln(k): 0.6378040168110805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 0.6378040168110805""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 0.6378040168110805
""",
)

entry(
    index = 360,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(231.764,'kJ/mol'), E0=(115.882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-1C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.237e+44,'m^3/(mol*s)'), n=-12.5348, w0=(281.452,'kJ/mol'), E0=(271.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27924283284942597, var=85.96327841141091, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 19.288793860718414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 19.288793860718414""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 19.288793860718414
""",
)

entry(
    index = 362,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, w0=(288.192,'kJ/mol'), E0=(208.98,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-1C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 363,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C",
    kinetics = ArrheniusBM(A=(10282.8,'m^3/(mol*s)'), n=0.629746, w0=(179,'kJ/mol'), E0=(38.3788,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0969772487821997, var=1.2726115569720906, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C
    Total Standard Deviation in ln(k): 2.5052047998808504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C
Total Standard Deviation in ln(k): 2.5052047998808504""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C
Total Standard Deviation in ln(k): 2.5052047998808504
""",
)

entry(
    index = 364,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.87495e+17,'m^3/(mol*s)'), n=-2.92111, w0=(169.312,'kJ/mol'), E0=(71.8978,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24938109458749066, var=14.972183373046281, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C
    Total Standard Deviation in ln(k): 8.383688665978172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C
Total Standard Deviation in ln(k): 8.383688665978172""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C
Total Standard Deviation in ln(k): 8.383688665978172
""",
)

entry(
    index = 365,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.51621e+07,'m^3/(mol*s)'), n=-0.174915, w0=(179,'kJ/mol'), E0=(44.4978,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03956688772608961, var=0.3363780132360048, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 1.2621226370738217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 1.2621226370738217""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 1.2621226370738217
""",
)

entry(
    index = 366,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.505e+06,'m^3/(mol*s)'), n=-1.00399e-08, w0=(179,'kJ/mol'), E0=(33.3298,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 367,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.92813e+14,'m^3/(mol*s)'), n=-2.36382, w0=(195.754,'kJ/mol'), E0=(181.056,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02036797597342975, var=0.262503875604926, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.078304483158511"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.078304483158511""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.078304483158511
""",
)

entry(
    index = 368,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_2BrCl->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.27064e+20,'m^3/(mol*s)'), n=-4.11807, w0=(163.5,'kJ/mol'), E0=(80.933,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_2BrCl->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_2BrCl->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_2BrCl->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_2BrCl->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 369,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.98116e+19,'m^3/(mol*s)'), n=-4.24465, w0=(180.757,'kJ/mol'), E0=(129.557,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_N-3BrCClINOPSSi->C_N-3ClNOS->S_N-2BrClHO->O_2ClH->Cl_N-3ClO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 370,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C",
    kinetics = ArrheniusBM(A=(1.59893e+08,'m^3/(mol*s)'), n=-0.00251802, w0=(218.841,'kJ/mol'), E0=(156.09,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4558687086139027, var=0.9394751407096138, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C
    Total Standard Deviation in ln(k): 3.0885188277291884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C
Total Standard Deviation in ln(k): 3.0885188277291884""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C
Total Standard Deviation in ln(k): 3.0885188277291884
""",
)

entry(
    index = 371,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(490958,'m^3/(mol*s)'), n=1.14475, w0=(219.088,'kJ/mol'), E0=(156.238,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(2.4737e+07,'m^3/(mol*s)'), n=0.118041, w0=(174.143,'kJ/mol'), E0=(87.0716,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15028921279112692, var=0.1261429949268402, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C
    Total Standard Deviation in ln(k): 1.0896251289400354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C
Total Standard Deviation in ln(k): 1.0896251289400354""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C
Total Standard Deviation in ln(k): 1.0896251289400354
""",
)

entry(
    index = 373,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(7.64581e+08,'m^3/(mol*s)'), n=-0.158759, w0=(197.495,'kJ/mol'), E0=(145.431,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 374,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C_Ext-8C-R_9R!H->O",
    kinetics = ArrheniusBM(A=(2.0472e+13,'m^3/(mol*s)'), n=-2.1772, w0=(173,'kJ/mol'), E0=(65.6017,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C_Ext-8C-R_9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C_Ext-8C-R_9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C_Ext-8C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C_Ext-8C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 375,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C_Ext-8C-R_N-9R!H->O",
    kinetics = ArrheniusBM(A=(180089,'m^3/(mol*s)'), n=0.450629, w0=(178.09,'kJ/mol'), E0=(131.736,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C_Ext-8C-R_N-9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C_Ext-8C-R_N-9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C_Ext-8C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_8R!H->C_Ext-8C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 376,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_N-8R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.84859e+06,'m^3/(mol*s)'), n=0.192007, w0=(188.226,'kJ/mol'), E0=(139.223,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_N-8R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_N-8R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_N-8R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_N-7R!H->O_Ext-2CHO-R_Ext-1C-R_N-8R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 377,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C",
    kinetics = ArrheniusBM(A=(1.01458e-10,'m^3/(mol*s)'), n=4.44836, w0=(235.401,'kJ/mol'), E0=(23.5401,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3316343075788476, var=74.51605833204273, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C
    Total Standard Deviation in ln(k): 18.138663358003893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C
Total Standard Deviation in ln(k): 18.138663358003893""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C
Total Standard Deviation in ln(k): 18.138663358003893
""",
)

entry(
    index = 378,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C",
    kinetics = ArrheniusBM(A=(6.27042e-06,'m^3/(mol*s)'), n=3.1073, w0=(226.575,'kJ/mol'), E0=(22.6575,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2530538098771226, var=24.578595151342025, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C
    Total Standard Deviation in ln(k): 10.574649434048109"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C
Total Standard Deviation in ln(k): 10.574649434048109""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C
Total Standard Deviation in ln(k): 10.574649434048109
""",
)

entry(
    index = 379,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C",
    kinetics = ArrheniusBM(A=(3.25591e+15,'m^3/(mol*s)'), n=-2.31291, w0=(173,'kJ/mol'), E0=(70.9824,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4071372401053639, var=134.88237776205023, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C
    Total Standard Deviation in ln(k): 24.30572510564982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C
Total Standard Deviation in ln(k): 24.30572510564982""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C
Total Standard Deviation in ln(k): 24.30572510564982
""",
)

entry(
    index = 380,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.80115e+06,'m^3/(mol*s)'), n=0.348747, w0=(181.225,'kJ/mol'), E0=(90.6127,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 381,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.39084e+11,'m^3/(mol*s)'), n=-1.45358, w0=(173,'kJ/mol'), E0=(85.9904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20548865407396646, var=0.36625241772088707, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.7295446012653048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.7295446012653048""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.7295446012653048
""",
)

entry(
    index = 382,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4437.65,'m^3/(mol*s)'), n=0.940006, w0=(206.719,'kJ/mol'), E0=(20.6719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1852708419698569, var=1.6024211481782153, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 3.0032341000829152"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 3.0032341000829152""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 3.0032341000829152
""",
)

entry(
    index = 383,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.9799e+06,'m^3/(mol*s)'), n=3.44366e-08, w0=(179.627,'kJ/mol'), E0=(17.9627,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06227071931309014, var=0.9044945335503305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.0630607354981096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.0630607354981096""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.0630607354981096
""",
)

entry(
    index = 384,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(542068,'m^3/(mol*s)'), n=0.666984, w0=(213.751,'kJ/mol'), E0=(21.3751,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.32435980182103324, var=0.48881859155191304, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 2.216596187566236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.216596187566236""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.216596187566236
""",
)

entry(
    index = 385,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(1.80345e+13,'m^3/(mol*s)'), n=-2.05221, w0=(173,'kJ/mol'), E0=(84.3599,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-2CHO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-2CHO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 386,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(4.46947e+13,'m^3/(mol*s)'), n=-2.00999, w0=(173,'kJ/mol'), E0=(82.3019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 387,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(7.77453e+14,'m^3/(mol*s)'), n=-2.19997, w0=(173,'kJ/mol'), E0=(83.1106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Ext-4O-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 388,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(395232,'m^3/(mol*s)'), n=0.425994, w0=(178.51,'kJ/mol'), E0=(17.851,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19849966568688132, var=3.831074176402041, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 4.42263690532311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 4.42263690532311""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 4.42263690532311
""",
)

entry(
    index = 389,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(5.85897e+07,'m^3/(mol*s)'), n=-0.108673, w0=(174.264,'kJ/mol'), E0=(87.132,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 390,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.2746e+10,'m^3/(mol*s)'), n=-1.07028, w0=(179,'kJ/mol'), E0=(50.2226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.106295565462015, var=4.73371602245711, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.628797370191297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.628797370191297""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.628797370191297
""",
)

entry(
    index = 391,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.92632e+06,'m^3/(mol*s)'), n=-0.178517, w0=(222.247,'kJ/mol'), E0=(204.153,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8629513207983656, var=3.447500474738627, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 5.89050040953728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 5.89050040953728""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 5.89050040953728
""",
)

entry(
    index = 392,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(9.13566e+07,'m^3/(mol*s)'), n=-0.359201, w0=(205.899,'kJ/mol'), E0=(20.5899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.44467105253388656, var=8.451974125813205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 6.94548572201523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 6.94548572201523""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 6.94548572201523
""",
)

entry(
    index = 393,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.08601e+12,'m^3/(mol*s)'), n=-0.861305, w0=(179,'kJ/mol'), E0=(89.332,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 394,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_Sp-5BrCClFINPSSi-1C",
    kinetics = ArrheniusBM(A=(1.32152e+08,'m^3/(mol*s)'), n=-0.0163218, w0=(203.748,'kJ/mol'), E0=(101.874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_Sp-5BrCClFINPSSi-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_Sp-5BrCClFINPSSi-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 395,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_N-Sp-5BrCClFINPSSi-1C",
    kinetics = ArrheniusBM(A=(1.8084e+07,'m^3/(mol*s)'), n=0.148656, w0=(234.358,'kJ/mol'), E0=(174.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_N-Sp-5BrCClFINPSSi-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_N-Sp-5BrCClFINPSSi-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_N-Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_N-6R!H->C_N-Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 396,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.4e+07,'m^3/(mol*s)'), n=0, w0=(180.051,'kJ/mol'), E0=(90.0254,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_N-2CHO->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 397,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C",
    kinetics = ArrheniusBM(A=(0.0109324,'m^3/(mol*s)'), n=2.61719, w0=(266.699,'kJ/mol'), E0=(26.6699,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6788194376928866, var=110.38937233971409, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C
    Total Standard Deviation in ln(k): 22.768595568863272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C
Total Standard Deviation in ln(k): 22.768595568863272""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C
Total Standard Deviation in ln(k): 22.768595568863272
""",
)

entry(
    index = 398,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-1C",
    kinetics = ArrheniusBM(A=(1.32819e+27,'m^3/(mol*s)'), n=-6.74987, w0=(286.189,'kJ/mol'), E0=(195.206,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24358966990940747, var=0.15523956227103788, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-1C
    Total Standard Deviation in ln(k): 1.4019090296500178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-1C
Total Standard Deviation in ln(k): 1.4019090296500178""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-1C
Total Standard Deviation in ln(k): 1.4019090296500178
""",
)

entry(
    index = 399,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(2.03116e+06,'m^3/(mol*s)'), n=0.193234, w0=(183.528,'kJ/mol'), E0=(145.665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0693853095667973, var=0.007005448011209662, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.342128376623813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.342128376623813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.342128376623813
""",
)

entry(
    index = 400,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.942e+06,'m^3/(mol*s)'), n=0.212, w0=(183.721,'kJ/mol'), E0=(136.78,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 401,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.83155e+07,'m^3/(mol*s)'), n=0.213711, w0=(205.927,'kJ/mol'), E0=(102.964,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00015371010021244128, var=0.013218501330287211, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.23087408926051417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.23087408926051417""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.23087408926051417
""",
)

entry(
    index = 402,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.888,'kJ/mol'), E0=(102.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 403,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-4R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(66.5142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-4R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-4R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-4R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Ext-4R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 404,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Sp-4R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(76.502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Sp-4R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Sp-4R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=1C_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 405,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(3.22741e+07,'m^3/(mol*s)'), n=0.213, w0=(211.537,'kJ/mol'), E0=(157.489,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0022644853453986234, var=7.490440640059255e-07, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_Sp-4C-3C
    Total Standard Deviation in ln(k): 0.0074247063908091816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_Sp-4C-3C
Total Standard Deviation in ln(k): 0.0074247063908091816""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_Sp-4C-3C
Total Standard Deviation in ln(k): 0.0074247063908091816
""",
)

entry(
    index = 406,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(1.13248e+10,'m^3/(mol*s)'), n=-0.605871, w0=(209.896,'kJ/mol'), E0=(99.2182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22335532936049374, var=0.0003995897404736133, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_N-Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 0.6012684296069748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 0.6012684296069748""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 0.6012684296069748
""",
)

entry(
    index = 407,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.27e+36,'m^3/(mol*s)'), n=-9.86, w0=(283.487,'kJ/mol'), E0=(202.591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-1C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 408,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.8422e+07,'m^3/(mol*s)'), n=-0.361029, w0=(179,'kJ/mol'), E0=(36.0057,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 409,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(2.94057e+10,'m^3/(mol*s)'), n=-1.39317, w0=(179,'kJ/mol'), E0=(54.5323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_Sp-4C-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_Sp-4C-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 410,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(1.53331,'m^3/(mol*s)'), n=1.7252, w0=(179,'kJ/mol'), E0=(16.4458,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_N-Sp-4C-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_4R!H->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 411,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O",
    kinetics = ArrheniusBM(A=(2.10912e+17,'m^3/(mol*s)'), n=-2.93464, w0=(179,'kJ/mol'), E0=(86.6595,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2620731312264369, var=15.202718368514994, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O
    Total Standard Deviation in ln(k): 8.475070276486878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O
Total Standard Deviation in ln(k): 8.475070276486878""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O
Total Standard Deviation in ln(k): 8.475070276486878
""",
)

entry(
    index = 412,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O",
    kinetics = ArrheniusBM(A=(1.83003e+11,'m^3/(mol*s)'), n=-1.33077, w0=(163.5,'kJ/mol'), E0=(63.0408,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1610385167342049, var=8.19164528031402, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O
    Total Standard Deviation in ln(k): 6.1423817647706445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O
Total Standard Deviation in ln(k): 6.1423817647706445""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O
Total Standard Deviation in ln(k): 6.1423817647706445
""",
)

entry(
    index = 413,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.99472e+07,'m^3/(mol*s)'), n=-0.113947, w0=(179,'kJ/mol'), E0=(42.2581,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.26963456790657, var=2.084894315327429, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.08470628175997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.08470628175997""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.08470628175997
""",
)

entry(
    index = 414,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_4R!H->C",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=5.63977e-09, w0=(179,'kJ/mol'), E0=(72.2214,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 415,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.77e+06,'m^3/(mol*s)'), n=3.80153e-09, w0=(179,'kJ/mol'), E0=(33.8046,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 416,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.64994e+14,'m^3/(mol*s)'), n=-2.23152, w0=(190.619,'kJ/mol'), E0=(141.55,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_N-Sp-3C-1C_N-2BrClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 417,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(4.00279e+08,'m^3/(mol*s)'), n=-0.187532, w0=(218.548,'kJ/mol'), E0=(155.918,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 418,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(6.39094e+07,'m^3/(mol*s)'), n=0.182418, w0=(219.134,'kJ/mol'), E0=(156.265,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 419,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(1.50858e+07,'m^3/(mol*s)'), n=0.160637, w0=(173,'kJ/mol'), E0=(84.8795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 420,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(4.35356e+07,'m^3/(mol*s)'), n=0.0666425, w0=(178.527,'kJ/mol'), E0=(132.899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_Ext-5C-R_7R!H->O_Ext-2CHO-R_N-8R!H->O_Ext-1C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 421,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C",
    kinetics = ArrheniusBM(A=(15240.5,'m^3/(mol*s)'), n=0.916465, w0=(191.632,'kJ/mol'), E0=(19.1632,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3830098276244702, var=60.59608216822393, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C
    Total Standard Deviation in ln(k): 16.56789282002521"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C
Total Standard Deviation in ln(k): 16.56789282002521""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C
Total Standard Deviation in ln(k): 16.56789282002521
""",
)

entry(
    index = 422,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C",
    kinetics = ArrheniusBM(A=(8.27807e-18,'m^3/(mol*s)'), n=6.2143, w0=(257.285,'kJ/mol'), E0=(25.7285,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09599981394349306, var=26.08730386956245, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C
    Total Standard Deviation in ln(k): 10.480536692775221"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C
Total Standard Deviation in ln(k): 10.480536692775221""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C
Total Standard Deviation in ln(k): 10.480536692775221
""",
)

entry(
    index = 423,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R",
    kinetics = ArrheniusBM(A=(2.85707e+07,'m^3/(mol*s)'), n=-0.367495, w0=(210.315,'kJ/mol'), E0=(154.009,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17889909264193077, var=0.026965679080669387, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R
    Total Standard Deviation in ln(k): 0.7786973632082254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R
Total Standard Deviation in ln(k): 0.7786973632082254""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R
Total Standard Deviation in ln(k): 0.7786973632082254
""",
)

entry(
    index = 424,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O",
    kinetics = ArrheniusBM(A=(7.62534e+16,'m^3/(mol*s)'), n=-3.67306, w0=(264.486,'kJ/mol'), E0=(246.062,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2948696335233801, var=25.82959804162103, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O
    Total Standard Deviation in ln(k): 10.92950899623285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O
Total Standard Deviation in ln(k): 10.92950899623285""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O
Total Standard Deviation in ln(k): 10.92950899623285
""",
)

entry(
    index = 425,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O",
    kinetics = ArrheniusBM(A=(1.39432e-06,'m^3/(mol*s)'), n=3.32408, w0=(225.496,'kJ/mol'), E0=(22.5496,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2506109598840494, var=20.675883729377702, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O
    Total Standard Deviation in ln(k): 9.745354915630337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O
Total Standard Deviation in ln(k): 9.745354915630337""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O
Total Standard Deviation in ln(k): 9.745354915630337
""",
)

entry(
    index = 426,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C_Ext-6C-R_9R!H->O",
    kinetics = ArrheniusBM(A=(5.1502e+26,'m^3/(mol*s)'), n=-5.42051, w0=(173,'kJ/mol'), E0=(50.8068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C_Ext-6C-R_9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C_Ext-6C-R_9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C_Ext-6C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C_Ext-6C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 427,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C_Ext-6C-R_N-9R!H->O",
    kinetics = ArrheniusBM(A=(127888,'m^3/(mol*s)'), n=0.567397, w0=(182.316,'kJ/mol'), E0=(135.252,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C_Ext-6C-R_N-9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C_Ext-6C-R_N-9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C_Ext-6C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_N-8R!H->F_6R!H->C_Ext-6C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 428,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H_7R!H->C",
    kinetics = ArrheniusBM(A=(9.33668e+12,'m^3/(mol*s)'), n=-1.82998, w0=(173,'kJ/mol'), E0=(81.1553,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 429,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.11258e+10,'m^3/(mol*s)'), n=-1.07717, w0=(181.651,'kJ/mol'), E0=(90.8255,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 430,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C",
    kinetics = ArrheniusBM(A=(5674.88,'m^3/(mol*s)'), n=0.853744, w0=(206.598,'kJ/mol'), E0=(20.6598,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08684863568513206, var=1.9089271316367382, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C
    Total Standard Deviation in ln(k): 2.9880334043207313"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C
Total Standard Deviation in ln(k): 2.9880334043207313""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C
Total Standard Deviation in ln(k): 2.9880334043207313
""",
)

entry(
    index = 431,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-7R!H->C",
    kinetics = ArrheniusBM(A=(85564.3,'m^3/(mol*s)'), n=0.794442, w0=(207.207,'kJ/mol'), E0=(153.211,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 432,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(180.281,'kJ/mol'), E0=(90.1406,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 433,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(1.4e+06,'m^3/(mol*s)'), n=0, w0=(178.973,'kJ/mol'), E0=(89.4864,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_5BrClF->Cl_Ext-2CHO-R_Ext-1C-R_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 434,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_5BrF->Br",
    kinetics = ArrheniusBM(A=(1.53438e+14,'m^3/(mol*s)'), n=-2.29604, w0=(200.993,'kJ/mol'), E0=(159.17,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5694360602228291, var=1.2705019286776806, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_5BrF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_5BrF->Br
    Total Standard Deviation in ln(k): 3.6904119650984097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_5BrF->Br
Total Standard Deviation in ln(k): 3.6904119650984097""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_5BrF->Br
Total Standard Deviation in ln(k): 3.6904119650984097
""",
)

entry(
    index = 435,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br",
    kinetics = ArrheniusBM(A=(2.33726e+10,'m^3/(mol*s)'), n=-0.658161, w0=(220.13,'kJ/mol'), E0=(173.939,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1480640741027007, var=0.693935862777533, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br
    Total Standard Deviation in ln(k): 2.042020996236215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br
Total Standard Deviation in ln(k): 2.042020996236215""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br
Total Standard Deviation in ln(k): 2.042020996236215
""",
)

entry(
    index = 436,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(944394,'m^3/(mol*s)'), n=0.330618, w0=(190.498,'kJ/mol'), E0=(139.784,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 437,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.86619e+08,'m^3/(mol*s)'), n=-0.406579, w0=(173,'kJ/mol'), E0=(83.2609,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_4BrCClO->O_Sp-4O-2CHO_5BrCClFINPSSi->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 438,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R",
    kinetics = ArrheniusBM(A=(4.76232e+11,'m^3/(mol*s)'), n=-1.24708, w0=(184.833,'kJ/mol'), E0=(92.4164,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09853072911736716, var=3.1996143488703765, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R
    Total Standard Deviation in ln(k): 3.8335276715152014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R
Total Standard Deviation in ln(k): 3.8335276715152014""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R
Total Standard Deviation in ln(k): 3.8335276715152014
""",
)

entry(
    index = 439,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl",
    kinetics = ArrheniusBM(A=(466.341,'m^3/(mol*s)'), n=1.23555, w0=(216.915,'kJ/mol'), E0=(21.6915,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0757845480147395, var=8.09478517859929, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl
    Total Standard Deviation in ln(k): 5.894152556824535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl
Total Standard Deviation in ln(k): 5.894152556824535""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl
Total Standard Deviation in ln(k): 5.894152556824535
""",
)

entry(
    index = 440,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl",
    kinetics = ArrheniusBM(A=(1.96737e+15,'m^3/(mol*s)'), n=-2.57864, w0=(179,'kJ/mol'), E0=(33.3448,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3240154772776741, var=2.677393178435664, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl
    Total Standard Deviation in ln(k): 4.094405475879569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl
Total Standard Deviation in ln(k): 4.094405475879569""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl
Total Standard Deviation in ln(k): 4.094405475879569
""",
)

entry(
    index = 441,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C_Sp-5BrCClFINPSSi-1C",
    kinetics = ArrheniusBM(A=(11871.3,'m^3/(mol*s)'), n=0.590055, w0=(231.206,'kJ/mol'), E0=(167.918,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C_Sp-5BrCClFINPSSi-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C_Sp-5BrCClFINPSSi-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C_Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C_Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 442,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C_N-Sp-5BrCClFINPSSi-1C",
    kinetics = ArrheniusBM(A=(4.97296e+07,'m^3/(mol*s)'), n=-0.541139, w0=(213.289,'kJ/mol'), E0=(106.644,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C_N-Sp-5BrCClFINPSSi-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C_N-Sp-5BrCClFINPSSi-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C_N-Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_7R!H->C_N-Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 443,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C_Sp-5BrCClFINPSSi-1C",
    kinetics = ArrheniusBM(A=(102604,'m^3/(mol*s)'), n=0.53964, w0=(216.146,'kJ/mol'), E0=(159.588,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C_Sp-5BrCClFINPSSi-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C_Sp-5BrCClFINPSSi-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C_Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C_Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 444,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-Sp-5BrCClFINPSSi-1C",
    kinetics = ArrheniusBM(A=(1.16067e+13,'m^3/(mol*s)'), n=-1.87531, w0=(195.651,'kJ/mol'), E0=(97.8256,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-Sp-5BrCClFINPSSi-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-Sp-5BrCClFINPSSi-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-Sp-5BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 445,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00798848,'m^3/(mol*s)'), n=2.66498, w0=(262.643,'kJ/mol'), E0=(26.2643,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8067024458227392, var=114.5831300492851, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R
    Total Standard Deviation in ln(k): 23.486278471433867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 23.486278471433867""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 23.486278471433867
""",
)

entry(
    index = 446,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.74e+37,'m^3/(mol*s)'), n=-10.5, w0=(277.811,'kJ/mol'), E0=(197.941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 447,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-1C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, w0=(288.403,'kJ/mol'), E0=(209.138,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-1C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-1C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 448,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.76821e+06,'m^3/(mol*s)'), n=0.213187, w0=(184.052,'kJ/mol'), E0=(92.026,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_2R->C_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrCCClClIINNOOPPSSSiSi=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 449,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(2.79114e+07,'m^3/(mol*s)'), n=0.21356, w0=(205.917,'kJ/mol'), E0=(102.959,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00020750917090565628, var=0.01529032030782134, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 0.2484149607337448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.2484149607337448""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.2484149607337448
""",
)

entry(
    index = 450,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.888,'kJ/mol'), E0=(102.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 451,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(3.203e+07,'m^3/(mol*s)'), n=0.214, w0=(211.524,'kJ/mol'), E0=(157.481,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 452,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.17785e+10,'m^3/(mol*s)'), n=-0.611491, w0=(227.553,'kJ/mol'), E0=(113.776,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-1C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 453,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(7.60814e+16,'m^3/(mol*s)'), n=-2.95283, w0=(179,'kJ/mol'), E0=(85.453,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2690148597813428, var=22.57377784013769, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 10.200787956756473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C
Total Standard Deviation in ln(k): 10.200787956756473""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C
Total Standard Deviation in ln(k): 10.200787956756473
""",
)

entry(
    index = 454,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.62085e+18,'m^3/(mol*s)'), n=-2.89824, w0=(179,'kJ/mol'), E0=(89.0725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 455,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.93132e+10,'m^3/(mol*s)'), n=-1.22628, w0=(163.5,'kJ/mol'), E0=(62.6353,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13970672260332354, var=10.687591908660787, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 6.904878304511481"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R
Total Standard Deviation in ln(k): 6.904878304511481""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R
Total Standard Deviation in ln(k): 6.904878304511481
""",
)

entry(
    index = 456,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(9.04e+06,'m^3/(mol*s)'), n=4.07933e-08, w0=(179,'kJ/mol'), E0=(72.4227,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 457,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(7.05e+06,'m^3/(mol*s)'), n=-2.21223e-08, w0=(179,'kJ/mol'), E0=(34.9352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-2BrClO-R_Ext-1C-R_5R!H->C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 458,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O",
    kinetics = ArrheniusBM(A=(1147.6,'m^3/(mol*s)'), n=1.03136, w0=(209.28,'kJ/mol'), E0=(144.783,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3069027305808829, var=0.004309508678434536, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O
    Total Standard Deviation in ln(k): 0.9027169276986535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O
Total Standard Deviation in ln(k): 0.9027169276986535""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O
Total Standard Deviation in ln(k): 0.9027169276986535
""",
)

entry(
    index = 459,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_N-10R!H->O",
    kinetics = ArrheniusBM(A=(1.11241e+16,'m^3/(mol*s)'), n=-2.06869, w0=(173,'kJ/mol'), E0=(78.1686,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_N-10R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_N-10R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_N-10R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_N-10R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 460,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_9R!H->C",
    kinetics = ArrheniusBM(A=(2842.4,'m^3/(mol*s)'), n=0.906541, w0=(202.697,'kJ/mol'), E0=(148.927,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 461,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C",
    kinetics = ArrheniusBM(A=(5.27538e+06,'m^3/(mol*s)'), n=-0.721173, w0=(268.203,'kJ/mol'), E0=(208.711,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2504168525905014, var=6.810548417232182, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C
    Total Standard Deviation in ln(k): 5.860950706297799"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C
Total Standard Deviation in ln(k): 5.860950706297799""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C
Total Standard Deviation in ln(k): 5.860950706297799
""",
)

entry(
    index = 462,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_11R!H->O",
    kinetics = ArrheniusBM(A=(1.34728e+10,'m^3/(mol*s)'), n=-1.22262, w0=(212.562,'kJ/mol'), E0=(155.378,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_11R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_11R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_11R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_11R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 463,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O",
    kinetics = ArrheniusBM(A=(3.67062e+06,'m^3/(mol*s)'), n=-0.0824516, w0=(209.567,'kJ/mol'), E0=(153.552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17862246590330175, var=0.031795519483423164, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O
    Total Standard Deviation in ln(k): 0.8062704549835842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O
Total Standard Deviation in ln(k): 0.8062704549835842""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O
Total Standard Deviation in ln(k): 0.8062704549835842
""",
)

entry(
    index = 464,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(0.141937,'m^3/(mol*s)'), n=1.2083, w0=(262.929,'kJ/mol'), E0=(179.659,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 465,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(1454.87,'m^3/(mol*s)'), n=0.456325, w0=(266.042,'kJ/mol'), E0=(183.959,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_6FO->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 466,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(5.70312e-06,'m^3/(mol*s)'), n=3.14132, w0=(222.072,'kJ/mol'), E0=(22.2072,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23020034114791077, var=23.644254026267625, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R
    Total Standard Deviation in ln(k): 10.326488821962863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R
Total Standard Deviation in ln(k): 10.326488821962863""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R
Total Standard Deviation in ln(k): 10.326488821962863
""",
)

entry(
    index = 467,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_8R!H->O",
    kinetics = ArrheniusBM(A=(5.66199e+07,'m^3/(mol*s)'), n=-0.275895, w0=(200.733,'kJ/mol'), E0=(149.45,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 468,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(251454,'m^3/(mol*s)'), n=0.37662, w0=(208.552,'kJ/mol'), E0=(177.691,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04970361234802027, var=0.37018495110705996, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 1.3446209288432394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O
Total Standard Deviation in ln(k): 1.3446209288432394""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O
Total Standard Deviation in ln(k): 1.3446209288432394
""",
)

entry(
    index = 469,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_5BrF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(177.664,'kJ/mol'), E0=(88.8321,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_5BrF->Br_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_5BrF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_5BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_5BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 470,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.15533e+10,'m^3/(mol*s)'), n=-0.646668, w0=(218.691,'kJ/mol'), E0=(178.521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13420903103072734, var=0.7252761720312222, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 2.0445041149453993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 2.0445041149453993""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 2.0445041149453993
""",
)

entry(
    index = 471,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(9.43501e+11,'m^3/(mol*s)'), n=-1.40833, w0=(181.114,'kJ/mol'), E0=(90.5571,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10381212786224284, var=2.628111704333431, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 3.5108011060058555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.5108011060058555""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.5108011060058555
""",
)

entry(
    index = 472,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.09117e+10,'m^3/(mol*s)'), n=-0.602081, w0=(199.707,'kJ/mol'), E0=(99.8536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_N-5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 473,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(145.711,'m^3/(mol*s)'), n=1.27167, w0=(212.995,'kJ/mol'), E0=(21.2995,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27723656647652595, var=5.907159738150128, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 5.569012571583307"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 5.569012571583307""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 5.569012571583307
""",
)

entry(
    index = 474,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1.10694e+07,'m^3/(mol*s)'), n=0.199192, w0=(224.755,'kJ/mol'), E0=(165.22,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_N-5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 475,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(2.58082e+18,'m^3/(mol*s)'), n=-3.56752, w0=(179,'kJ/mol'), E0=(23.6321,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4394731314435992, var=4.22004215687176, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 5.222479233219144"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 5.222479233219144""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 5.222479233219144
""",
)

entry(
    index = 476,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(5.80475e+06,'m^3/(mol*s)'), n=0.152054, w0=(179,'kJ/mol'), E0=(60.7945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_N-5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 477,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(71244.8,'m^3/(mol*s)'), n=0.431732, w0=(274.726,'kJ/mol'), E0=(193.206,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 478,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.81647e+08,'m^3/(mol*s)'), n=-0.118713, w0=(259.623,'kJ/mol'), E0=(115.325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.122498747592709, var=37.640244347607286, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 22.6574166809352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 22.6574166809352""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 22.6574166809352
""",
)

entry(
    index = 479,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.888,'kJ/mol'), E0=(102.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00036890525002828464, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.0009268976131363935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.0009268976131363935""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.0009268976131363935
""",
)

entry(
    index = 480,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.888,'kJ/mol'), E0=(102.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 481,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.59527e+14,'m^3/(mol*s)'), n=-2.30738, w0=(179,'kJ/mol'), E0=(89.1164,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 482,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.62847e+19,'m^3/(mol*s)'), n=-3.59829, w0=(179,'kJ/mol'), E0=(81.7896,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_2ClO->O_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_Ext-3C-R_Ext-3C-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 483,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(228516,'m^3/(mol*s)'), n=0.317874, w0=(163.5,'kJ/mol'), E0=(69.7597,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.044992570828351876, var=20.619355822430787, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 9.21625612615887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 9.21625612615887""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 9.21625612615887
""",
)

entry(
    index = 484,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.13552e+14,'m^3/(mol*s)'), n=-2.31938, w0=(163.5,'kJ/mol'), E0=(68.0308,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 485,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(389.12,'m^3/(mol*s)'), n=1.13144, w0=(199.282,'kJ/mol'), E0=(145.656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 486,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(74400,'m^3/(mol*s)'), n=0.546769, w0=(219.277,'kJ/mol'), E0=(158.87,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_Sp-9R!H=6C_Ext-6C-R_10R!H->O_Ext-5C-R_Ext-2CHO-R_Ext-5C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 487,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_9FO->O",
    kinetics = ArrheniusBM(A=(0.413045,'m^3/(mol*s)'), n=1.07287, w0=(280.484,'kJ/mol'), E0=(189.996,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_9FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_9FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_9FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_9FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 488,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O",
    kinetics = ArrheniusBM(A=(3303.27,'m^3/(mol*s)'), n=0.257119, w0=(265.133,'kJ/mol'), E0=(193.497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31674609539196097, var=5.247559262067128, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O
    Total Standard Deviation in ln(k): 5.3882017095743295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O
Total Standard Deviation in ln(k): 5.3882017095743295""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O
Total Standard Deviation in ln(k): 5.3882017095743295
""",
)

entry(
    index = 489,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_12R!H->O",
    kinetics = ArrheniusBM(A=(7.45304e+06,'m^3/(mol*s)'), n=-0.171776, w0=(208.838,'kJ/mol'), E0=(153.108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_12R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_12R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_12R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_12R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 490,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O",
    kinetics = ArrheniusBM(A=(2.57599e+06,'m^3/(mol*s)'), n=-0.0377895, w0=(209.931,'kJ/mol'), E0=(153.775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17875719170705073, var=0.0034916745760332738, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O
    Total Standard Deviation in ln(k): 0.5675992567431025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O
Total Standard Deviation in ln(k): 0.5675992567431025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O
Total Standard Deviation in ln(k): 0.5675992567431025
""",
)

entry(
    index = 491,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.17235e-05,'m^3/(mol*s)'), n=2.9178, w0=(218.365,'kJ/mol'), E0=(21.8365,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20503142084277695, var=27.630067224921845, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.0529060013427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.0529060013427""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.0529060013427
""",
)

entry(
    index = 492,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(81866.3,'m^3/(mol*s)'), n=0.493654, w0=(214.364,'kJ/mol'), E0=(157.359,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-2CHO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-2CHO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 493,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_8BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(9705.04,'m^3/(mol*s)'), n=0.74494, w0=(200.086,'kJ/mol'), E0=(100.043,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_8BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_8BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 494,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(57189.5,'m^3/(mol*s)'), n=0.620146, w0=(211.207,'kJ/mol'), E0=(155.468,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_5BrClFINOPSSi->O_Ext-5O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 495,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br_Ext-1C-R_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(6.69632e+07,'m^3/(mol*s)'), n=0.134221, w0=(214.162,'kJ/mol'), E0=(157.923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br_Ext-1C-R_Ext-2CHO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br_Ext-1C-R_Ext-2CHO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br_Ext-1C-R_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_N-5R!H->C_N-Sp-5BrBrCClClFFHIINNOOOPPSSSiSi=2BrBrCCClClFFHHIINNOOOOPPSSSiSi_N-5BrClFINOPSSi->O_N-5BrClF->Cl_Ext-1C-R_N-5BrF->Br_Ext-1C-R_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 496,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(2.02037e+09,'m^3/(mol*s)'), n=-0.642574, w0=(194.428,'kJ/mol'), E0=(143.798,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 497,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(2.40874e+13,'m^3/(mol*s)'), n=-1.81179, w0=(179,'kJ/mol'), E0=(88.3381,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15245970705913015, var=2.6378983259427686, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 3.639076731073165"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C
Total Standard Deviation in ln(k): 3.639076731073165""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C
Total Standard Deviation in ln(k): 3.639076731073165
""",
)

entry(
    index = 498,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(9919.91,'m^3/(mol*s)'), n=0.675528, w0=(215.613,'kJ/mol'), E0=(158.279,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 499,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(218671,'m^3/(mol*s)'), n=0.432585, w0=(210.378,'kJ/mol'), E0=(155.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 500,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(9.88258e+13,'m^3/(mol*s)'), n=-2.32699, w0=(179,'kJ/mol'), E0=(33.2299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 501,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(4.17062e+20,'m^3/(mol*s)'), n=-4.18779, w0=(179,'kJ/mol'), E0=(18.8332,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.495397315687663, var=1.122844667497313, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 3.3690216706562577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.3690216706562577""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.3690216706562577
""",
)

entry(
    index = 502,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.03719e+06,'m^3/(mol*s)'), n=0.399582, w0=(235.273,'kJ/mol'), E0=(105.031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09836819034416346, var=0.17362480922090667, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 1.0824954920411491"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.0824954920411491""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.0824954920411491
""",
)

entry(
    index = 503,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.77e+40,'m^3/(mol*s)'), n=-10.8, w0=(292.431,'kJ/mol'), E0=(207.155,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_2CHO->H_Ext-1C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-1C_Ext-4C-R_N-6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 504,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.888,'kJ/mol'), E0=(102.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_2BrClHO->H_Ext-1C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 505,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R_4ClF->F",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=2.48906e-08, w0=(163.5,'kJ/mol'), E0=(60.9633,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R_4ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R_4ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R_4ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R_4ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 506,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R_N-4ClF->F",
    kinetics = ArrheniusBM(A=(5221.95,'m^3/(mol*s)'), n=0.635748, w0=(163.5,'kJ/mol'), E0=(65.7136,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R_N-4ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R_N-4ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R_N-4ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_N-3R!H->F_N-2R->C_N-2BrClHNO->N_3BrCClINOPSSi->C_N-2BrClHO->H_N-3C-inRing_Sp-3C-1C_Ext-3C-R_N-2BrClO->Br_N-4R!H->C_N-2ClO->O_Ext-1C-R_Ext-3C-R_Ext-3C-R_N-4ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 507,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R",
    kinetics = ArrheniusBM(A=(454.689,'m^3/(mol*s)'), n=0.521173, w0=(260.812,'kJ/mol'), E0=(188.169,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3335291326576467, var=8.31272747188984, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R
    Total Standard Deviation in ln(k): 6.618025171078424"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 6.618025171078424""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 6.618025171078424
""",
)

entry(
    index = 508,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O_Sp-10R!H-9R!H",
    kinetics = ArrheniusBM(A=(3.77114e+06,'m^3/(mol*s)'), n=-0.0927661, w0=(210.3,'kJ/mol'), E0=(154,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O_Sp-10R!H-9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O_Sp-10R!H-9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O_Sp-10R!H-9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O_Sp-10R!H-9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 509,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O_N-Sp-10R!H-9R!H",
    kinetics = ArrheniusBM(A=(1.75959e+06,'m^3/(mol*s)'), n=0.0171875, w0=(209.562,'kJ/mol'), E0=(153.549,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O_N-Sp-10R!H-9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O_N-Sp-10R!H-9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O_N-Sp-10R!H-9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_Ext-6FO-R_Ext-9R!H-R_Ext-10R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_Ext-11R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-11R!H->O_Ext-10R!H-R_Ext-9R!H-R_N-12R!H->O_N-Sp-10R!H-9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 510,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(0.26112,'m^3/(mol*s)'), n=1.53297, w0=(252.295,'kJ/mol'), E0=(168.54,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40353767925238276, var=4.835991693695226, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_10R!H->C
    Total Standard Deviation in ln(k): 5.42250428799803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_10R!H->C
Total Standard Deviation in ln(k): 5.42250428799803""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_10R!H->C
Total Standard Deviation in ln(k): 5.42250428799803
""",
)

entry(
    index = 511,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(0.614931,'m^3/(mol*s)'), n=1.77706, w0=(207.055,'kJ/mol'), E0=(20.7055,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10934169546972876, var=17.280616598060572, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 8.608403781785686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C
Total Standard Deviation in ln(k): 8.608403781785686""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C
Total Standard Deviation in ln(k): 8.608403781785686
""",
)

entry(
    index = 512,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(1.6581e+13,'m^3/(mol*s)'), n=-1.93086, w0=(179,'kJ/mol'), E0=(89.0175,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 513,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(2.90322e+13,'m^3/(mol*s)'), n=-1.75226, w0=(179,'kJ/mol'), E0=(87.9984,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1479316071613329, var=0.6554010845754273, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 1.9946577360101834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C
Total Standard Deviation in ln(k): 1.9946577360101834""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C
Total Standard Deviation in ln(k): 1.9946577360101834
""",
)

entry(
    index = 514,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C_8BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(7.22101e+23,'m^3/(mol*s)'), n=-5.20574, w0=(179,'kJ/mol'), E0=(7.92692,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C_8BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C_8BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C_8BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C_8BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 515,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C_N-8BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.40881e+17,'m^3/(mol*s)'), n=-3.16983, w0=(179,'kJ/mol'), E0=(29.7395,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C_N-8BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C_N-8BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C_N-8BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_N-Sp-6C-4CCl_5BrCClFINPSSi->C_Ext-6C-R_Ext-6C-R_N-8R!H->C_N-8BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 516,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6521.98,'m^3/(mol*s)'), n=0.172545, w0=(261.563,'kJ/mol'), E0=(194.435,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3619677054606306, var=28.222832719182275, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.559654991611724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.559654991611724""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.559654991611724
""",
)

entry(
    index = 517,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_10R!H->C_Ext-10C-R_Ext-10C-R_Ext-10C-R_Ext-10C-R_Ext-10C-R",
    kinetics = ArrheniusBM(A=(11.0219,'m^3/(mol*s)'), n=1.16221, w0=(251.912,'kJ/mol'), E0=(174.173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_10R!H->C_Ext-10C-R_Ext-10C-R_Ext-10C-R_Ext-10C-R_Ext-10C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_10R!H->C_Ext-10C-R_Ext-10C-R_Ext-10C-R_Ext-10C-R_Ext-10C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_10R!H->C_Ext-10C-R_Ext-10C-R_Ext-10C-R_Ext-10C-R_Ext-10C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_10R!H->C_Ext-10C-R_Ext-10C-R_Ext-10C-R_Ext-10C-R_Ext-10C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 518,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(430555,'m^3/(mol*s)'), n=0.116778, w0=(184.13,'kJ/mol'), E0=(92.065,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05190402737284642, var=4.416177335835677, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R
    Total Standard Deviation in ln(k): 4.34330331259442"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R
Total Standard Deviation in ln(k): 4.34330331259442""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R
Total Standard Deviation in ln(k): 4.34330331259442
""",
)

entry(
    index = 519,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_10BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(781.022,'m^3/(mol*s)'), n=0.566143, w0=(251.875,'kJ/mol'), E0=(176.17,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_10BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_10BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_10BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_10BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 520,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_N-10BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(130719,'m^3/(mol*s)'), n=0.51445, w0=(253.936,'kJ/mol'), E0=(177.708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_N-10BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_N-10BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_N-10BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_N-10BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 521,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C_7R!H->C",
    kinetics = ArrheniusBM(A=(4.33204e+11,'m^3/(mol*s)'), n=-1.10729, w0=(179.281,'kJ/mol'), E0=(89.6405,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 522,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.94567e+15,'m^3/(mol*s)'), n=-2.39724, w0=(179,'kJ/mol'), E0=(86.3563,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_N-4R!H->F_Ext-1C-R_N-5R!H->O_N-4BrCClO->O_2CHO->O_Ext-4CCl-R_6R!H->C_Ext-1C-R_Ext-6C-R_Ext-6C-R_Ext-4CCl-R_5BrCClFINPSSi->C_Ext-6C-R_N-10R!H->C_Ext-6C-R_Ext-6C-R_N-11R!H->C_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 523,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R_12R!H->O",
    kinetics = ArrheniusBM(A=(0.306352,'m^3/(mol*s)'), n=1.17601, w0=(259.989,'kJ/mol'), E0=(179.386,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R_12R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R_12R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R_12R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R_12R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 524,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R_N-12R!H->O",
    kinetics = ArrheniusBM(A=(44.3716,'m^3/(mol*s)'), n=1.03011, w0=(263.137,'kJ/mol'), E0=(181.579,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R_N-12R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R_N-12R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R_N-12R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_6R!H->C_Ext-6C-R_N-Sp-9R!H=6C_N-9R!H->C_N-9FO->O_Ext-6C-R_Ext-6C-R_Ext-1C-R_N-12R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 525,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H",
    kinetics = ArrheniusBM(A=(9.02904e+08,'m^3/(mol*s)'), n=-0.852379, w0=(173,'kJ/mol'), E0=(83.1199,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17933136377442935, var=1.211517974709165, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H
    Total Standard Deviation in ln(k): 2.657172711750473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 2.657172711750473""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 2.657172711750473
""",
)

entry(
    index = 526,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H",
    kinetics = ArrheniusBM(A=(205.313,'m^3/(mol*s)'), n=1.08594, w0=(202.02,'kJ/mol'), E0=(20.202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.37306867286337364, var=13.899235371578058, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
    Total Standard Deviation in ln(k): 8.41134729853254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 8.41134729853254""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 8.41134729853254
""",
)

entry(
    index = 527,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H_12R!H->C",
    kinetics = ArrheniusBM(A=(1.54144e+10,'m^3/(mol*s)'), n=-1.20194, w0=(173,'kJ/mol'), E0=(79.0327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H_12R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H_12R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H_12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H_12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 528,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H_N-12R!H->C",
    kinetics = ArrheniusBM(A=(5.2888e+07,'m^3/(mol*s)'), n=-0.502822, w0=(174.414,'kJ/mol'), E0=(87.2072,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H_N-12R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H_N-12R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H_N-12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_Sp-12R!H=11R!H_N-12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 529,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-12R!H-R_13R!H->O",
    kinetics = ArrheniusBM(A=(1.66595e+07,'m^3/(mol*s)'), n=-0.290889, w0=(194.83,'kJ/mol'), E0=(144.485,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-12R!H-R_13R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-12R!H-R_13R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-12R!H-R_13R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-12R!H-R_13R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 530,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-12R!H-R_N-13R!H->O",
    kinetics = ArrheniusBM(A=(926.405,'m^3/(mol*s)'), n=0.868703, w0=(209.21,'kJ/mol'), E0=(152.798,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-12R!H-R_N-13R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-12R!H-R_N-13R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-12R!H-R_N-13R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->C_Ext-1C-R_3R!H->F_N-2R->Cl_N-2BrCHNO->Br_Ext-2CHO-R_4R!H-u0_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_Ext-5C-R_Ext-2CHO-R_Ext-1C-R_8R!H->F_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-1C-R_N-10R!H->C_Ext-10BrClFINOPSSi-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-12R!H-R_N-13R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

