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
    kinetics = ArrheniusBM(A=(11570.6,'m^3/(mol*s)'), n=0.862872, w0=(185.666,'kJ/mol'), E0=(64.2014,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13587632220685839, var=25.450266108008382, Tref=1000.0, N=367, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 367 training reactions at node Root
    Total Standard Deviation in ln(k): 10.454936787852407"""),
    rank = 11,
    shortDesc = """BM rule fitted to 367 training reactions at node Root
Total Standard Deviation in ln(k): 10.454936787852407""",
    longDesc = 
"""
BM rule fitted to 367 training reactions at node Root
Total Standard Deviation in ln(k): 10.454936787852407
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
    kinetics = ArrheniusBM(A=(4516.31,'m^3/(mol*s)'), n=0.975818, w0=(186.552,'kJ/mol'), E0=(64.2014,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1932883380085024, var=27.021577758882025, Tref=1000.0, N=339, data_mean=0.0, correlation='Root_N-1R-inRing',), comment="""BM rule fitted to 339 training reactions at node Root_N-1R-inRing
    Total Standard Deviation in ln(k): 10.906719761627613"""),
    rank = 11,
    shortDesc = """BM rule fitted to 339 training reactions at node Root_N-1R-inRing
Total Standard Deviation in ln(k): 10.906719761627613""",
    longDesc = 
"""
BM rule fitted to 339 training reactions at node Root_N-1R-inRing
Total Standard Deviation in ln(k): 10.906719761627613
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
    kinetics = ArrheniusBM(A=(4.30894e-06,'m^3/(mol*s)'), n=3.17382, w0=(286.753,'kJ/mol'), E0=(28.6753,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2710427519793817, var=58.976011454380036, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_1R->F
    Total Standard Deviation in ln(k): 16.07654350015888"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_1R->F
Total Standard Deviation in ln(k): 16.07654350015888""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_1R->F
Total Standard Deviation in ln(k): 16.07654350015888
""",
)

entry(
    index = 7,
    label = "Root_N-1R-inRing_N-1R->F",
    kinetics = ArrheniusBM(A=(261270,'m^3/(mol*s)'), n=0.487143, w0=(183.506,'kJ/mol'), E0=(83.6619,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.042328919925859174, var=24.558422293812885, Tref=1000.0, N=329, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F',), comment="""BM rule fitted to 329 training reactions at node Root_N-1R-inRing_N-1R->F
    Total Standard Deviation in ln(k): 10.04111042951122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 329 training reactions at node Root_N-1R-inRing_N-1R->F
Total Standard Deviation in ln(k): 10.04111042951122""",
    longDesc = 
"""
BM rule fitted to 329 training reactions at node Root_N-1R-inRing_N-1R->F
Total Standard Deviation in ln(k): 10.04111042951122
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
    kinetics = ArrheniusBM(A=(4.99689e-08,'m^3/(mol*s)'), n=3.67292, w0=(298.547,'kJ/mol'), E0=(29.8547,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31511608080255393, var=60.07220321085591, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 16.32970073729223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 16.32970073729223""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 16.32970073729223
""",
)

entry(
    index = 13,
    label = "Root_N-1R-inRing_1R->F_Ext-2R-R_3R!H->O",
    kinetics = ArrheniusBM(A=(1e+06,'m^3/(mol*s)'), n=0, w0=(255.147,'kJ/mol'), E0=(127.573,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_3R!H->O
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
    kinetics = ArrheniusBM(A=(1.4535e+06,'m^3/(mol*s)'), n=0.209241, w0=(185.112,'kJ/mol'), E0=(112.692,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10708404361247054, var=27.025896163065845, Tref=1000.0, N=318, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S',), comment="""BM rule fitted to 318 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S
    Total Standard Deviation in ln(k): 10.690958736052846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 318 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S
Total Standard Deviation in ln(k): 10.690958736052846""",
    longDesc = 
"""
BM rule fitted to 318 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S
Total Standard Deviation in ln(k): 10.690958736052846
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
    kinetics = ArrheniusBM(A=(1.81507e+07,'m^3/(mol*s)'), n=-0.161397, w0=(255.411,'kJ/mol'), E0=(184.9,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12452648457167755, var=0.31159648014166264, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.431940327231575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.431940327231575""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.431940327231575
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
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H",
    kinetics = ArrheniusBM(A=(3.89084e+07,'m^3/(mol*s)'), n=0.0810725, w0=(222.969,'kJ/mol'), E0=(123.83,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.022995843097168775, var=11.340058010489283, Tref=1000.0, N=73, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H',), comment="""BM rule fitted to 73 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H
    Total Standard Deviation in ln(k): 6.808724397394796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 73 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H
Total Standard Deviation in ln(k): 6.808724397394796""",
    longDesc = 
"""
BM rule fitted to 73 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H
Total Standard Deviation in ln(k): 6.808724397394796
""",
)

entry(
    index = 28,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H",
    kinetics = ArrheniusBM(A=(105944,'m^3/(mol*s)'), n=0.502433, w0=(173.832,'kJ/mol'), E0=(95.3464,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09622012186754023, var=29.295900316718264, Tref=1000.0, N=245, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H',), comment="""BM rule fitted to 245 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H
    Total Standard Deviation in ln(k): 11.092525503071547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 245 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H
Total Standard Deviation in ln(k): 11.092525503071547""",
    longDesc = 
"""
BM rule fitted to 245 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H
Total Standard Deviation in ln(k): 11.092525503071547
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
    kinetics = ArrheniusBM(A=(1.54647e+06,'m^3/(mol*s)'), n=0.239176, w0=(263.092,'kJ/mol'), E0=(195.753,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R
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
    kinetics = ArrheniusBM(A=(1.32281e+07,'m^3/(mol*s)'), n=-0.183314, w0=(244.868,'kJ/mol'), E0=(122.434,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFINOPSSi->O
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
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O",
    kinetics = ArrheniusBM(A=(4.56485e+06,'m^3/(mol*s)'), n=0.253537, w0=(229.5,'kJ/mol'), E0=(49.9103,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1650947137607139, var=11.787849500432575, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O
    Total Standard Deviation in ln(k): 7.297755543834503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O
Total Standard Deviation in ln(k): 7.297755543834503""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O
Total Standard Deviation in ln(k): 7.297755543834503
""",
)

entry(
    index = 46,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O",
    kinetics = ArrheniusBM(A=(6.05105e+07,'m^3/(mol*s)'), n=0.030732, w0=(225.931,'kJ/mol'), E0=(126.625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.015778016742302173, var=12.070446481443636, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O',), comment="""BM rule fitted to 68 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O
    Total Standard Deviation in ln(k): 7.0046037425880785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O
Total Standard Deviation in ln(k): 7.0046037425880785""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O
Total Standard Deviation in ln(k): 7.0046037425880785
""",
)

entry(
    index = 47,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl",
    kinetics = ArrheniusBM(A=(6.03114e+15,'m^3/(mol*s)'), n=-2.81213, w0=(176.324,'kJ/mol'), E0=(144.783,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11793370181987883, var=14.630046873831288, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl
    Total Standard Deviation in ln(k): 7.964276001318288"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl
Total Standard Deviation in ln(k): 7.964276001318288""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl
Total Standard Deviation in ln(k): 7.964276001318288
""",
)

entry(
    index = 48,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl",
    kinetics = ArrheniusBM(A=(98071.5,'m^3/(mol*s)'), n=0.51235, w0=(173.536,'kJ/mol'), E0=(94.9437,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09580609364717538, var=29.34050073234449, Tref=1000.0, N=219, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl',), comment="""BM rule fitted to 219 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl
    Total Standard Deviation in ln(k): 11.099741755692055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 219 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl
Total Standard Deviation in ln(k): 11.099741755692055""",
    longDesc = 
"""
BM rule fitted to 219 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl
Total Standard Deviation in ln(k): 11.099741755692055
""",
)

entry(
    index = 49,
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
    index = 50,
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
    index = 51,
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
    index = 52,
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
    index = 53,
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
    index = 54,
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
    index = 55,
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
    index = 56,
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
    index = 57,
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
    index = 58,
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
    index = 59,
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
    index = 60,
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
    index = 61,
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
    index = 62,
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
    index = 63,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R",
    kinetics = ArrheniusBM(A=(2.68803e+06,'m^3/(mol*s)'), n=0.285593, w0=(229.5,'kJ/mol'), E0=(48.1781,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.96528014847047, var=124.27323569509383, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R
    Total Standard Deviation in ln(k): 39.8490707808857"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R
Total Standard Deviation in ln(k): 39.8490707808857""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R
Total Standard Deviation in ln(k): 39.8490707808857
""",
)

entry(
    index = 64,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_2BrCClHN->N",
    kinetics = ArrheniusBM(A=(8.84147e+06,'m^3/(mol*s)'), n=0.349925, w0=(228.417,'kJ/mol'), E0=(114.208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_2BrCClHN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_2BrCClHN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_2BrCClHN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_2BrCClHN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N",
    kinetics = ArrheniusBM(A=(4.92126e+07,'m^3/(mol*s)'), n=0.0531038, w0=(225.894,'kJ/mol'), E0=(124.531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010005274163140043, var=12.893395438752735, Tref=1000.0, N=67, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N',), comment="""BM rule fitted to 67 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N
    Total Standard Deviation in ln(k): 7.223616200628999"""),
    rank = 11,
    shortDesc = """BM rule fitted to 67 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N
Total Standard Deviation in ln(k): 7.223616200628999""",
    longDesc = 
"""
BM rule fitted to 67 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N
Total Standard Deviation in ln(k): 7.223616200628999
""",
)

entry(
    index = 66,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C",
    kinetics = ArrheniusBM(A=(1.45987e+14,'m^3/(mol*s)'), n=-2.311, w0=(178.263,'kJ/mol'), E0=(111.919,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012321235339187128, var=14.360536543847568, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C
    Total Standard Deviation in ln(k): 7.627961310683196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C
Total Standard Deviation in ln(k): 7.627961310683196""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C
Total Standard Deviation in ln(k): 7.627961310683196
""",
)

entry(
    index = 67,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_N-2R->C",
    kinetics = ArrheniusBM(A=(4.5295e+12,'m^3/(mol*s)'), n=-2.86943, w0=(136,'kJ/mol'), E0=(81.547,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(98363.6,'m^3/(mol*s)'), n=0.50891, w0=(173.8,'kJ/mol'), E0=(96.0463,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10025643018614325, var=29.482544959914087, Tref=1000.0, N=213, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R',), comment="""BM rule fitted to 213 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.137177304063359"""),
    rank = 11,
    shortDesc = """BM rule fitted to 213 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.137177304063359""",
    longDesc = 
"""
BM rule fitted to 213 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.137177304063359
""",
)

entry(
    index = 69,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_1BrCNO->Br",
    kinetics = ArrheniusBM(A=(19036.1,'m^3/(mol*s)'), n=0.381498, w0=(159.583,'kJ/mol'), E0=(117.198,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_1BrCNO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_1BrCNO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_1BrCNO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_1BrCNO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br",
    kinetics = ArrheniusBM(A=(2.90976e+08,'m^3/(mol*s)'), n=-0.172071, w0=(165.106,'kJ/mol'), E0=(34.1618,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08896113814782933, var=12.581122456428956, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br
    Total Standard Deviation in ln(k): 7.3342913102270915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br
Total Standard Deviation in ln(k): 7.3342913102270915""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br
Total Standard Deviation in ln(k): 7.3342913102270915
""",
)

entry(
    index = 71,
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
    index = 72,
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
    index = 73,
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
    index = 74,
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
    index = 75,
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
    index = 76,
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
    index = 77,
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
    index = 78,
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
    index = 79,
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
    index = 80,
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
    index = 81,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_3R!H->Cl",
    kinetics = ArrheniusBM(A=(2.54516e+11,'m^3/(mol*s)'), n=-2.9831, w0=(229.5,'kJ/mol'), E0=(94.7569,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.057261895203365755, var=1.2163227514485672e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_3R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_3R!H->Cl
    Total Standard Deviation in ln(k): 0.1508657863229021"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_3R!H->Cl
Total Standard Deviation in ln(k): 0.1508657863229021""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_3R!H->Cl
Total Standard Deviation in ln(k): 0.1508657863229021
""",
)

entry(
    index = 82,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl",
    kinetics = ArrheniusBM(A=(2.07243e+06,'m^3/(mol*s)'), n=0.359788, w0=(229.5,'kJ/mol'), E0=(47.4759,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.550956046954883, var=4.837543463095088, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl
    Total Standard Deviation in ln(k): 5.793609452682424"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 5.793609452682424""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 5.793609452682424
""",
)

entry(
    index = 83,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C",
    kinetics = ArrheniusBM(A=(5.29867e+07,'m^3/(mol*s)'), n=0.0444226, w0=(225.944,'kJ/mol'), E0=(124.994,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008185503511035728, var=12.830806814227481, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C',), comment="""BM rule fitted to 65 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C
    Total Standard Deviation in ln(k): 7.201550813210921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C
Total Standard Deviation in ln(k): 7.201550813210921""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C
Total Standard Deviation in ln(k): 7.201550813210921
""",
)

entry(
    index = 84,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_N-2CH->C",
    kinetics = ArrheniusBM(A=(1.04607e+06,'m^3/(mol*s)'), n=-0.000249502, w0=(224.272,'kJ/mol'), E0=(166.226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12984451529271046, var=52.92098688017469, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_N-2CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_N-2CH->C
    Total Standard Deviation in ln(k): 14.91005112312643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_N-2CH->C
Total Standard Deviation in ln(k): 14.91005112312643""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_N-2CH->C
Total Standard Deviation in ln(k): 14.91005112312643
""",
)

entry(
    index = 85,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.31426e+13,'m^3/(mol*s)'), n=-2.21307, w0=(175.883,'kJ/mol'), E0=(111.621,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002661728649161995, var=15.061239037267145, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 7.786826471685096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.786826471685096""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.786826471685096
""",
)

entry(
    index = 86,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F",
    kinetics = ArrheniusBM(A=(3.60025e+08,'m^3/(mol*s)'), n=-0.519886, w0=(196.561,'kJ/mol'), E0=(177.457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2261469224321064, var=25.659592296153072, Tref=1000.0, N=105, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F',), comment="""BM rule fitted to 105 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F
    Total Standard Deviation in ln(k): 10.72325365145777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 105 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F
Total Standard Deviation in ln(k): 10.72325365145777""",
    longDesc = 
"""
BM rule fitted to 105 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F
Total Standard Deviation in ln(k): 10.72325365145777
""",
)

entry(
    index = 87,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(2.30248e+14,'m^3/(mol*s)'), n=-2.1297, w0=(163.278,'kJ/mol'), E0=(78.7533,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17247991477774707, var=5.164563719156964, Tref=1000.0, N=108, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F',), comment="""BM rule fitted to 108 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F
    Total Standard Deviation in ln(k): 4.989262701691132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 108 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F
Total Standard Deviation in ln(k): 4.989262701691132""",
    longDesc = 
"""
BM rule fitted to 108 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F
Total Standard Deviation in ln(k): 4.989262701691132
""",
)

entry(
    index = 88,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_1CNO->N",
    kinetics = ArrheniusBM(A=(3.68973e+08,'m^3/(mol*s)'), n=0.0640189, w0=(140.577,'kJ/mol'), E0=(104.243,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_1CNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_1CNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_1CNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_1CNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N",
    kinetics = ArrheniusBM(A=(9.04458e+08,'m^3/(mol*s)'), n=-0.533339, w0=(171.238,'kJ/mol'), E0=(56.2233,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1682018686138175, var=2.558156498921208, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N
    Total Standard Deviation in ln(k): 3.629038760148768"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N
Total Standard Deviation in ln(k): 3.629038760148768""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N
Total Standard Deviation in ln(k): 3.629038760148768
""",
)

entry(
    index = 90,
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
    index = 91,
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
    index = 92,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.21037e+06,'m^3/(mol*s)'), n=0.349925, w0=(229.5,'kJ/mol'), E0=(88.9685,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(43950,'m^3/(mol*s)'), n=1, w0=(229.5,'kJ/mol'), E0=(53.7489,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_2R->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.73373e+07,'m^3/(mol*s)'), n=0.0575725, w0=(226.105,'kJ/mol'), E0=(124.078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.034510703820975944, var=13.128776942229242, Tref=1000.0, N=63, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R',), comment="""BM rule fitted to 63 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R
    Total Standard Deviation in ln(k): 7.350598059987332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 63 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.350598059987332""",
    longDesc = 
"""
BM rule fitted to 63 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.350598059987332
""",
)

entry(
    index = 95,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(2.31481e+14,'m^3/(mol*s)'), n=-2.01467, w0=(163.5,'kJ/mol'), E0=(62.3505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22811668133446578, var=43.268526874405175, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F
    Total Standard Deviation in ln(k): 13.760067550139247"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 13.760067550139247""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 13.760067550139247
""",
)

entry(
    index = 96,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(3.3468e+17,'m^3/(mol*s)'), n=-3.35178, w0=(189.352,'kJ/mol'), E0=(153.518,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03449458752673338, var=8.063390191650992, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 5.77933744055943"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 5.77933744055943""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 5.77933744055943
""",
)

entry(
    index = 97,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br",
    kinetics = ArrheniusBM(A=(2.30066e+09,'m^3/(mol*s)'), n=-0.741101, w0=(142.5,'kJ/mol'), E0=(57.2752,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1554025914675551, var=2.83329482073936, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br
    Total Standard Deviation in ln(k): 3.7649078074360314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br
Total Standard Deviation in ln(k): 3.7649078074360314""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br
Total Standard Deviation in ln(k): 3.7649078074360314
""",
)

entry(
    index = 98,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br",
    kinetics = ArrheniusBM(A=(1.09277e+09,'m^3/(mol*s)'), n=-0.658043, w0=(198.973,'kJ/mol'), E0=(178.377,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2345437296493129, var=25.488273755995642, Tref=1000.0, N=102, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br',), comment="""BM rule fitted to 102 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br
    Total Standard Deviation in ln(k): 10.71039385276096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 102 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br
Total Standard Deviation in ln(k): 10.71039385276096""",
    longDesc = 
"""
BM rule fitted to 102 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br
Total Standard Deviation in ln(k): 10.71039385276096
""",
)

entry(
    index = 99,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1",
    kinetics = ArrheniusBM(A=(159024,'m^3/(mol*s)'), n=0.223939, w0=(169.188,'kJ/mol'), E0=(39.6573,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05246719227074816, var=1.491213011991714, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1
    Total Standard Deviation in ln(k): 2.5799140261702136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 2.5799140261702136""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 2.5799140261702136
""",
)

entry(
    index = 100,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1",
    kinetics = ArrheniusBM(A=(2.38717e+13,'m^3/(mol*s)'), n=-1.81869, w0=(167.087,'kJ/mol'), E0=(71.6862,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41320290029425705, var=6.343135999488398, Tref=1000.0, N=92, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1',), comment="""BM rule fitted to 92 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1
    Total Standard Deviation in ln(k): 6.087240445834672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 92 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 6.087240445834672""",
    longDesc = 
"""
BM rule fitted to 92 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 6.087240445834672
""",
)

entry(
    index = 101,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C",
    kinetics = ArrheniusBM(A=(2.69413e+10,'m^3/(mol*s)'), n=-0.955947, w0=(193.237,'kJ/mol'), E0=(176.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2503474364045006, var=0.3102955591136714, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C
    Total Standard Deviation in ln(k): 1.7457348812464617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C
Total Standard Deviation in ln(k): 1.7457348812464617""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C
Total Standard Deviation in ln(k): 1.7457348812464617
""",
)

entry(
    index = 102,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_N-1CO->C",
    kinetics = ArrheniusBM(A=(1.57e+07,'m^3/(mol*s)'), n=0, w0=(105.238,'kJ/mol'), E0=(52.6192,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_N-1CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_N-1CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_N-1CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_N-1CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
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
    index = 104,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(13.7192,'m^3/(mol*s)'), n=1.83997, w0=(262.213,'kJ/mol'), E0=(26.2213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5828520926569597, var=54.43852886730035, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F
    Total Standard Deviation in ln(k): 16.255883074783807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 16.255883074783807""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 16.255883074783807
""",
)

entry(
    index = 105,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(3.66447e+07,'m^3/(mol*s)'), n=0.127054, w0=(210.513,'kJ/mol'), E0=(46.3735,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3143763131348698, var=3.0469761485822606, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F',), comment="""BM rule fitted to 44 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 4.289273548532721"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 4.289273548532721""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 4.289273548532721
""",
)

entry(
    index = 106,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.35017e+16,'m^3/(mol*s)'), n=-2.51834, w0=(163.5,'kJ/mol'), E0=(56.912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28819147482758345, var=62.503342978660875, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
    Total Standard Deviation in ln(k): 16.57334541001471"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 16.57334541001471""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 16.57334541001471
""",
)

entry(
    index = 107,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.07854e+16,'m^3/(mol*s)'), n=-2.88641, w0=(187.79,'kJ/mol'), E0=(149.865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05003502043357999, var=6.721464579042101, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 5.323149694355823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.323149694355823""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.323149694355823
""",
)

entry(
    index = 108,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.22185e+12,'m^3/(mol*s)'), n=-2.24226, w0=(195.206,'kJ/mol'), E0=(26.3188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19761962228075053, var=7.388499069837912, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 5.945761237450544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.945761237450544""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.945761237450544
""",
)

entry(
    index = 109,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(1.86795e+10,'m^3/(mol*s)'), n=-1.11165, w0=(142.5,'kJ/mol'), E0=(49.4539,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23310386285421747, var=3.4352181513961657, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 4.301332553396669"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 4.301332553396669""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 4.301332553396669
""",
)

entry(
    index = 110,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R",
    kinetics = ArrheniusBM(A=(7.9421e+08,'m^3/(mol*s)'), n=-0.616006, w0=(198.288,'kJ/mol'), E0=(178.476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23494831356871726, var=25.530282917903676, Tref=1000.0, N=98, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R',), comment="""BM rule fitted to 98 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R
    Total Standard Deviation in ln(k): 10.719747628709701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 98 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R
Total Standard Deviation in ln(k): 10.719747628709701""",
    longDesc = 
"""
BM rule fitted to 98 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R
Total Standard Deviation in ln(k): 10.719747628709701
""",
)

entry(
    index = 111,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(1.35279e+19,'m^3/(mol*s)'), n=-4.67047, w0=(210.631,'kJ/mol'), E0=(57.2321,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1952341737846044, var=4.188869186441967, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-1BrCNO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 7.106137515084264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 7.106137515084264""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 7.106137515084264
""",
)

entry(
    index = 112,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C",
    kinetics = ArrheniusBM(A=(38446.7,'m^3/(mol*s)'), n=0.41102, w0=(179,'kJ/mol'), E0=(38.3788,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06957462302137951, var=1.08692714674787, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C
    Total Standard Deviation in ln(k): 2.264863168219771"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C
Total Standard Deviation in ln(k): 2.264863168219771""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C
Total Standard Deviation in ln(k): 2.264863168219771
""",
)

entry(
    index = 113,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R->C",
    kinetics = ArrheniusBM(A=(1.94697e+33,'m^3/(mol*s)'), n=-8.77465, w0=(100.5,'kJ/mol'), E0=(62.8034,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21180353796563897, var=231.95075518798305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R->C
    Total Standard Deviation in ln(k): 31.064143760247813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R->C
Total Standard Deviation in ln(k): 31.064143760247813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R->C
Total Standard Deviation in ln(k): 31.064143760247813
""",
)

entry(
    index = 114,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(2.02039e+53,'m^3/(mol*s)'), n=-14.2627, w0=(162.75,'kJ/mol'), E0=(58.3512,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.26468335989915, var=86.70983787619582, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 29.383000452596846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 29.383000452596846""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 29.383000452596846
""",
)

entry(
    index = 115,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(5.25361e+10,'m^3/(mol*s)'), n=-1.0148, w0=(168.207,'kJ/mol'), E0=(59.3878,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22079645057453268, var=4.9770722911873415, Tref=1000.0, N=90, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 90 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 5.027199192794701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 90 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 5.027199192794701""",
    longDesc = 
"""
BM rule fitted to 90 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 5.027199192794701
""",
)

entry(
    index = 116,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C_2R->C",
    kinetics = ArrheniusBM(A=(2.7032e+09,'m^3/(mol*s)'), n=-0.671759, w0=(193.572,'kJ/mol'), E0=(113.674,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.39669066013312737, var=0.35528669677274394, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C_2R->C
    Total Standard Deviation in ln(k): 2.1916512011317053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C_2R->C
Total Standard Deviation in ln(k): 2.1916512011317053""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C_2R->C
Total Standard Deviation in ln(k): 2.1916512011317053
""",
)

entry(
    index = 117,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C_N-2R->C",
    kinetics = ArrheniusBM(A=(6.03e+07,'m^3/(mol*s)'), n=0, w0=(192.568,'kJ/mol'), E0=(96.2838,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_N-1BrCNO->Br_N-1CNO->N_1CO->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(13.2827,'m^3/(mol*s)'), n=1.84584, w0=(263.439,'kJ/mol'), E0=(26.3439,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.55647656559843, var=55.215317134780825, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R
    Total Standard Deviation in ln(k): 16.294769240730798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 16.294769240730798""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 16.294769240730798
""",
)

entry(
    index = 119,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.31572e+08,'m^3/(mol*s)'), n=-0.253646, w0=(210.136,'kJ/mol'), E0=(54.2831,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04086937261481295, var=3.277701084670652, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C',), comment="""BM rule fitted to 38 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 3.732143919080211"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.732143919080211""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.732143919080211
""",
)

entry(
    index = 120,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.3625e+06,'m^3/(mol*s)'), n=0.449623, w0=(212.903,'kJ/mol'), E0=(60.3128,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.364906397141763, var=57.89639008952726, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 28.733628848353284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 28.733628848353284""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 28.733628848353284
""",
)

entry(
    index = 121,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.85364e+42,'m^3/(mol*s)'), n=-9.9178, w0=(163.5,'kJ/mol'), E0=(1.635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.61723e+07,'m^3/(mol*s)'), n=-0.0518497, w0=(163.5,'kJ/mol'), E0=(81.3805,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05779465118716443, var=8.301056686147676, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.921166071230092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.921166071230092""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.921166071230092
""",
)

entry(
    index = 123,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(3.89852e+12,'m^3/(mol*s)'), n=-1.81556, w0=(194.432,'kJ/mol'), E0=(113.083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09396640097414535, var=9.577524564538674, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 6.440265589232887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C
Total Standard Deviation in ln(k): 6.440265589232887""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C
Total Standard Deviation in ln(k): 6.440265589232887
""",
)

entry(
    index = 124,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(8.92064e+17,'m^3/(mol*s)'), n=-3.36029, w0=(174.507,'kJ/mol'), E0=(87.2536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09522907969373746, var=1.6837903094575888, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 2.8406322447316557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 2.8406322447316557""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 2.8406322447316557
""",
)

entry(
    index = 125,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O",
    kinetics = ArrheniusBM(A=(1.50059e+20,'m^3/(mol*s)'), n=-4.57992, w0=(255.701,'kJ/mol'), E0=(178.485,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O",
    kinetics = ArrheniusBM(A=(8.17544e+14,'m^3/(mol*s)'), n=-3.04515, w0=(175.041,'kJ/mol'), E0=(36.0171,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11357895682607125, var=3.0907683508548973, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O
    Total Standard Deviation in ln(k): 3.8098150432507616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O
Total Standard Deviation in ln(k): 3.8098150432507616""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O
Total Standard Deviation in ln(k): 3.8098150432507616
""",
)

entry(
    index = 127,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(4.77213e+06,'m^3/(mol*s)'), n=0.171878, w0=(142.5,'kJ/mol'), E0=(57.719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(7.31171e+13,'m^3/(mol*s)'), n=-2.39518, w0=(142.5,'kJ/mol'), E0=(41.1889,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO",
    kinetics = ArrheniusBM(A=(3.41245e+13,'m^3/(mol*s)'), n=-1.79379, w0=(173,'kJ/mol'), E0=(81.9963,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19085975968067553, var=8.111949674239309, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO
    Total Standard Deviation in ln(k): 6.189330266724332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO
Total Standard Deviation in ln(k): 6.189330266724332""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO
Total Standard Deviation in ln(k): 6.189330266724332
""",
)

entry(
    index = 130,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO",
    kinetics = ArrheniusBM(A=(2.88156e+07,'m^3/(mol*s)'), n=-0.238559, w0=(206.537,'kJ/mol'), E0=(167.367,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27679852011886713, var=26.782001967307544, Tref=1000.0, N=79, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO',), comment="""BM rule fitted to 79 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO
    Total Standard Deviation in ln(k): 11.070244401322116"""),
    rank = 11,
    shortDesc = """BM rule fitted to 79 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO
Total Standard Deviation in ln(k): 11.070244401322116""",
    longDesc = 
"""
BM rule fitted to 79 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO
Total Standard Deviation in ln(k): 11.070244401322116
""",
)

entry(
    index = 131,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(1.78e+27,'m^3/(mol*s)'), n=-6.64, w0=(257.506,'kJ/mol'), E0=(186.106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-1BrCNO-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(55773.7,'m^3/(mol*s)'), n=0.360175, w0=(179,'kJ/mol'), E0=(38.6047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0936963307734658, var=1.1229497233700851, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.359822088628596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.359822088628596""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.359822088628596
""",
)

entry(
    index = 133,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R->C_Ext-2BrNO-R",
    kinetics = ArrheniusBM(A=(1.22646e+19,'m^3/(mol*s)'), n=-4.10331, w0=(100.5,'kJ/mol'), E0=(1.21992,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R->C_Ext-2BrNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R->C_Ext-2BrNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R->C_Ext-2BrNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R->C_Ext-2BrNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_2R->C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(288.568,'kJ/mol'), E0=(144.284,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-2R->C",
    kinetics = ArrheniusBM(A=(4.23489e+61,'m^3/(mol*s)'), n=-16.8824, w0=(152.5,'kJ/mol'), E0=(1.525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(3.17315e+15,'m^3/(mol*s)'), n=-2.3528, w0=(171.162,'kJ/mol'), E0=(92.7629,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3101506763838944, var=5.396455472680003, Tref=1000.0, N=43, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R',), comment="""BM rule fitted to 43 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 5.436327213290188"""),
    rank = 11,
    shortDesc = """BM rule fitted to 43 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 5.436327213290188""",
    longDesc = 
"""
BM rule fitted to 43 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 5.436327213290188
""",
)

entry(
    index = 137,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(2.93563e+07,'m^3/(mol*s)'), n=-0.167731, w0=(168.565,'kJ/mol'), E0=(13.9349,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5070661790814139, var=3.935437945716467, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 5.251016695961847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 5.251016695961847""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 5.251016695961847
""",
)

entry(
    index = 138,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.56853e+08,'m^3/(mol*s)'), n=-0.178921, w0=(176.532,'kJ/mol'), E0=(29.0249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.3152476880539137, var=13.109708745353018, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
    Total Standard Deviation in ln(k): 15.588378868004453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 15.588378868004453""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 15.588378868004453
""",
)

entry(
    index = 139,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(9.17506e+07,'m^3/(mol*s)'), n=-0.313212, w0=(166.945,'kJ/mol'), E0=(17.8179,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12134947294625562, var=2.9619720381228607, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
    Total Standard Deviation in ln(k): 3.7551235615363048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 3.7551235615363048""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 3.7551235615363048
""",
)

entry(
    index = 140,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0145217,'m^3/(mol*s)'), n=2.55977, w0=(266.149,'kJ/mol'), E0=(26.6149,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9619089586709022, var=97.06003959973536, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
    Total Standard Deviation in ln(k): 22.167316972828687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 22.167316972828687""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 22.167316972828687
""",
)

entry(
    index = 141,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.63468e+17,'m^3/(mol*s)'), n=-2.64305, w0=(249.888,'kJ/mol'), E0=(246.807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-14.37392588651005, var=456.8060464599228, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 78.96263751151896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 78.96263751151896""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 78.96263751151896
""",
)

entry(
    index = 142,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.3734e+10,'m^3/(mol*s)'), n=-0.689502, w0=(205.5,'kJ/mol'), E0=(40.0325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08204118046051638, var=8.080189336525653, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R
    Total Standard Deviation in ln(k): 5.904728165199943"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.904728165199943""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.904728165199943
""",
)

entry(
    index = 143,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing",
    kinetics = ArrheniusBM(A=(3.82247e+08,'m^3/(mol*s)'), n=-0.106414, w0=(205.5,'kJ/mol'), E0=(105.177,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06899945697746504, var=0.08357538883509968, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing
    Total Standard Deviation in ln(k): 0.7529225186827172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing
Total Standard Deviation in ln(k): 0.7529225186827172""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing
Total Standard Deviation in ln(k): 0.7529225186827172
""",
)

entry(
    index = 144,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.99782e+09,'m^3/(mol*s)'), n=-0.419678, w0=(236.076,'kJ/mol'), E0=(89.6673,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3670792464105536, var=4.7239695091764995, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing
    Total Standard Deviation in ln(k): 5.279540137660447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing
Total Standard Deviation in ln(k): 5.279540137660447""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing
Total Standard Deviation in ln(k): 5.279540137660447
""",
)

entry(
    index = 145,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S",
    kinetics = ArrheniusBM(A=(2.12532e+06,'m^3/(mol*s)'), n=0.469939, w0=(205.5,'kJ/mol'), E0=(98.1764,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S",
    kinetics = ArrheniusBM(A=(3.7835e+13,'m^3/(mol*s)'), n=-2.73588, w0=(216.213,'kJ/mol'), E0=(14.2673,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1561775585582476, var=0.3562102304487583, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S
    Total Standard Deviation in ln(k): 1.588898985098241"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S
Total Standard Deviation in ln(k): 1.588898985098241""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S
Total Standard Deviation in ln(k): 1.588898985098241
""",
)

entry(
    index = 147,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.49202e+07,'m^3/(mol*s)'), n=-0.181327, w0=(163.5,'kJ/mol'), E0=(79.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(3.46638e+07,'m^3/(mol*s)'), n=0.0128888, w0=(164.4,'kJ/mol'), E0=(82.1998,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.044574436569025946, var=15.233807308235251, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 7.936579371609077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 7.936579371609077""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 7.936579371609077
""",
)

entry(
    index = 149,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.46811e+08,'m^3/(mol*s)'), n=-0.724216, w0=(194.286,'kJ/mol'), E0=(50.8279,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23066504348443467, var=11.98108346179385, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 7.518690608734419"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 7.518690608734419""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 7.518690608734419
""",
)

entry(
    index = 150,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.65838e+13,'m^3/(mol*s)'), n=-1.74873, w0=(163.5,'kJ/mol'), E0=(64.663,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.84656e+14,'m^3/(mol*s)'), n=-2.20814, w0=(167.469,'kJ/mol'), E0=(83.7345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.170212951015834, var=2.1807980442464765, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.3881683350873546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 3.3881683350873546""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 3.3881683350873546
""",
)

entry(
    index = 152,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.27064e+20,'m^3/(mol*s)'), n=-4.11807, w0=(163.5,'kJ/mol'), E0=(80.933,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.5271e+11,'m^3/(mol*s)'), n=-2.09678, w0=(163.5,'kJ/mol'), E0=(3.44407,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4336750620298182, var=13.74094532953404, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R
    Total Standard Deviation in ln(k): 8.520944410917108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 8.520944410917108""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 8.520944410917108
""",
)

entry(
    index = 154,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F",
    kinetics = ArrheniusBM(A=(2.65988e+11,'m^3/(mol*s)'), n=-1.21933, w0=(173,'kJ/mol'), E0=(86.2621,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13467706597594112, var=5.518653241152231, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F
    Total Standard Deviation in ln(k): 5.047870939800661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F
Total Standard Deviation in ln(k): 5.047870939800661""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F
Total Standard Deviation in ln(k): 5.047870939800661
""",
)

entry(
    index = 155,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(4.77939e+22,'m^3/(mol*s)'), n=-4.28607, w0=(173,'kJ/mol'), E0=(59.2452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4346790339494022, var=2.6825794312792315, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F
    Total Standard Deviation in ln(k): 4.375630130253821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F
Total Standard Deviation in ln(k): 4.375630130253821""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F
Total Standard Deviation in ln(k): 4.375630130253821
""",
)

entry(
    index = 156,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0",
    kinetics = ArrheniusBM(A=(6.84357e+06,'m^3/(mol*s)'), n=-0.0743611, w0=(202.39,'kJ/mol'), E0=(163.467,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3053051025986389, var=29.820619727244623, Tref=1000.0, N=75, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0',), comment="""BM rule fitted to 75 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0
    Total Standard Deviation in ln(k): 11.714607520863886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 75 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0
Total Standard Deviation in ln(k): 11.714607520863886""",
    longDesc = 
"""
BM rule fitted to 75 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0
Total Standard Deviation in ln(k): 11.714607520863886
""",
)

entry(
    index = 157,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0",
    kinetics = ArrheniusBM(A=(4.39065e+07,'m^3/(mol*s)'), n=-0.0557863, w0=(284.288,'kJ/mol'), E0=(178.066,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19484492133751088, var=4.452409885155089, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0
    Total Standard Deviation in ln(k): 4.719698327314135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0
Total Standard Deviation in ln(k): 4.719698327314135""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0
Total Standard Deviation in ln(k): 4.719698327314135
""",
)

entry(
    index = 158,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(15.484,'m^3/(mol*s)'), n=1.37634, w0=(179,'kJ/mol'), E0=(19.0946,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2990574302014041, var=1.2602889366749643, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.0019681215280176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.0019681215280176""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.0019681215280176
""",
)

entry(
    index = 159,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(1.1209e+07,'m^3/(mol*s)'), n=-0.210333, w0=(179,'kJ/mol'), E0=(38.6327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02070667515948491, var=1.334768008766858, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 2.3681405673035982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 2.3681405673035982""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 2.3681405673035982
""",
)

entry(
    index = 160,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(3.24037e+06,'m^3/(mol*s)'), n=-2.57538e-08, w0=(179,'kJ/mol'), E0=(31.982,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14927640611932624, var=0.18413599331399638, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 1.2353196204820034"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 1.2353196204820034""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 1.2353196204820034
""",
)

entry(
    index = 161,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(8.50709e+16,'m^3/(mol*s)'), n=-2.79834, w0=(171.214,'kJ/mol'), E0=(109.776,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2685675528913629, var=13.308760338828654, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 7.988301702773636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 7.988301702773636""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 7.988301702773636
""",
)

entry(
    index = 162,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.25729e+10,'m^3/(mol*s)'), n=-0.704886, w0=(173.5,'kJ/mol'), E0=(17.35,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4718505953191916, var=9.741313512024735, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 7.442548422233415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 7.442548422233415""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 7.442548422233415
""",
)

entry(
    index = 163,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(7.76315e+08,'m^3/(mol*s)'), n=-0.424868, w0=(172.083,'kJ/mol'), E0=(64.4424,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06688668682923737, var=2.158763962935862, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 3.113560679056282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.113560679056282""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.113560679056282
""",
)

entry(
    index = 164,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.12295e+09,'m^3/(mol*s)'), n=-0.683198, w0=(173,'kJ/mol'), E0=(98.1456,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29384857806191805, var=1.0879312592065988, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
    Total Standard Deviation in ln(k): 2.829330749043721"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 2.829330749043721""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 2.829330749043721
""",
)

entry(
    index = 165,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.72782e+07,'m^3/(mol*s)'), n=-0.0666517, w0=(167,'kJ/mol'), E0=(20.3359,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.632094285086532, var=3.1511054587421934, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
    Total Standard Deviation in ln(k): 5.1468526695555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 5.1468526695555""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 5.1468526695555
""",
)

entry(
    index = 166,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.8131e+08,'m^3/(mol*s)'), n=-0.210958, w0=(158.601,'kJ/mol'), E0=(31.5529,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.433199627630243, var=9.274818303110234, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 12.218904657778754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 12.218904657778754""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 12.218904657778754
""",
)

entry(
    index = 167,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(9.05545e+07,'m^3/(mol*s)'), n=-0.0323395, w0=(198.945,'kJ/mol'), E0=(88.8226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004313597059143952, var=0.3491079490871801, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 1.1953430743596014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 1.1953430743596014""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 1.1953430743596014
""",
)

entry(
    index = 168,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.82948e+08,'m^3/(mol*s)'), n=-0.539585, w0=(155.056,'kJ/mol'), E0=(37.6491,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0019554749999578817, var=1.2105546837246874, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 2.2106272327704253"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 2.2106272327704253""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 2.2106272327704253
""",
)

entry(
    index = 169,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(248379,'m^3/(mol*s)'), n=0.353484, w0=(190.723,'kJ/mol'), E0=(1.06988,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5163871332466136, var=2.082883264083792, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 4.190728377883937"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.190728377883937""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.190728377883937
""",
)

entry(
    index = 170,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00983174,'m^3/(mol*s)'), n=2.61969, w0=(264.512,'kJ/mol'), E0=(26.4512,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0372067902789341, var=99.41890257264637, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 22.59506580072398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 22.59506580072398""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 22.59506580072398
""",
)

entry(
    index = 171,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C",
    kinetics = ArrheniusBM(A=(1.02279e+36,'m^3/(mol*s)'), n=-10.0662, w0=(270.517,'kJ/mol'), E0=(207.666,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27840156192545956, var=1.620315432518365, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
    Total Standard Deviation in ln(k): 3.251360995588611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
Total Standard Deviation in ln(k): 3.251360995588611""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
Total Standard Deviation in ln(k): 3.251360995588611
""",
)

entry(
    index = 172,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C",
    kinetics = ArrheniusBM(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, w0=(277.051,'kJ/mol'), E0=(200.669,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.56996e+11,'m^3/(mol*s)'), n=-0.751574, w0=(236.266,'kJ/mol'), E0=(204.859,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2623305746125397, var=25.506588659253637, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 18.321534149630548"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 18.321534149630548""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 18.321534149630548
""",
)

entry(
    index = 174,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing",
    kinetics = ArrheniusBM(A=(1.16055e+34,'m^3/(mol*s)'), n=-7.5829, w0=(205.5,'kJ/mol'), E0=(23.3615,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing",
    kinetics = ArrheniusBM(A=(2.96838e+07,'m^3/(mol*s)'), n=0.205688, w0=(205.5,'kJ/mol'), E0=(98.4363,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014796686746860407, var=0.08507179062171762, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing
    Total Standard Deviation in ln(k): 0.6219000654902375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing
Total Standard Deviation in ln(k): 0.6219000654902375""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing
Total Standard Deviation in ln(k): 0.6219000654902375
""",
)

entry(
    index = 176,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.69017e+08,'m^3/(mol*s)'), n=0.0270733, w0=(205.5,'kJ/mol'), E0=(110.329,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07859689658672972, var=0.29828115478932965, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.2923681473768245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.2923681473768245""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.2923681473768245
""",
)

entry(
    index = 177,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(5.24875e+07,'m^3/(mol*s)'), n=0.108702, w0=(205.5,'kJ/mol'), E0=(86.89,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13966497549833137, var=0.060976250169598185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 0.845953665821445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.845953665821445""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.845953665821445
""",
)

entry(
    index = 178,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.83153e+09,'m^3/(mol*s)'), n=-0.472098, w0=(235.104,'kJ/mol'), E0=(88.9793,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5241266783778138, var=6.191049709717304, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 6.3050469542594705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 6.3050469542594705""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 6.3050469542594705
""",
)

entry(
    index = 179,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(277.999,'kJ/mol'), E0=(139,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C",
    kinetics = ArrheniusBM(A=(1.30121e+08,'m^3/(mol*s)'), n=-0.0104386, w0=(221.434,'kJ/mol'), E0=(112.941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18513990790935178, var=0.004340108194692165, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C
    Total Standard Deviation in ln(k): 0.597246587591217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C
Total Standard Deviation in ln(k): 0.597246587591217""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C
Total Standard Deviation in ln(k): 0.597246587591217
""",
)

entry(
    index = 181,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O",
    kinetics = ArrheniusBM(A=(2.31504e+12,'m^3/(mol*s)'), n=-2.20453, w0=(205.5,'kJ/mol'), E0=(73.19,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O",
    kinetics = ArrheniusBM(A=(7.1883e+15,'m^3/(mol*s)'), n=-3.4347, w0=(233.671,'kJ/mol'), E0=(119.145,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.027178382159491407, var=0.09441460044167417, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O
    Total Standard Deviation in ln(k): 0.684281516028437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O
Total Standard Deviation in ln(k): 0.684281516028437""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O
Total Standard Deviation in ln(k): 0.684281516028437
""",
)

entry(
    index = 183,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.80245e+06,'m^3/(mol*s)'), n=0.0257778, w0=(163.5,'kJ/mol'), E0=(74.5352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.93132e+10,'m^3/(mol*s)'), n=-1.22628, w0=(163.5,'kJ/mol'), E0=(62.6353,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13970672260332354, var=10.687591908660787, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 6.904878304511481"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.904878304511481""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.904878304511481
""",
)

entry(
    index = 185,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.05803e+27,'m^3/(mol*s)'), n=-6.59025, w0=(305.648,'kJ/mol'), E0=(203.233,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.81048e+30,'m^3/(mol*s)'), n=-7.09644, w0=(275.049,'kJ/mol'), E0=(190.333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.21509e+31,'m^3/(mol*s)'), n=-7.40295, w0=(278.221,'kJ/mol'), E0=(189.92,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.92813e+14,'m^3/(mol*s)'), n=-2.36382, w0=(195.754,'kJ/mol'), E0=(181.056,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02036797597342975, var=0.262503875604926, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.078304483158511"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.078304483158511""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.078304483158511
""",
)

entry(
    index = 189,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.98116e+19,'m^3/(mol*s)'), n=-4.24465, w0=(180.757,'kJ/mol'), E0=(129.557,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.0678417,'m^3/(mol*s)'), n=2.13578, w0=(241.47,'kJ/mol'), E0=(179.656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.00364e+10,'m^3/(mol*s)'), n=-0.803737, w0=(173,'kJ/mol'), E0=(81.087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12066052206970235, var=11.0936184222264, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C
    Total Standard Deviation in ln(k): 6.980355095826335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C
Total Standard Deviation in ln(k): 6.980355095826335""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C
Total Standard Deviation in ln(k): 6.980355095826335
""",
)

entry(
    index = 192,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.23995e+13,'m^3/(mol*s)'), n=-1.70626, w0=(173,'kJ/mol'), E0=(86.4812,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15116517577253982, var=1.609099523598039, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C
    Total Standard Deviation in ln(k): 2.922824192686967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C
Total Standard Deviation in ln(k): 2.922824192686967""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C
Total Standard Deviation in ln(k): 2.922824192686967
""",
)

entry(
    index = 193,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.0188e+23,'m^3/(mol*s)'), n=-4.63802, w0=(173,'kJ/mol'), E0=(58.1291,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.44975507924449165, var=0.9502532974344873, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 3.08427241466098"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C
Total Standard Deviation in ln(k): 3.08427241466098""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C
Total Standard Deviation in ln(k): 3.08427241466098
""",
)

entry(
    index = 194,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.19798e+21,'m^3/(mol*s)'), n=-3.58217, w0=(173,'kJ/mol'), E0=(61.4775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.47271e+09,'m^3/(mol*s)'), n=-0.857685, w0=(205.101,'kJ/mol'), E0=(196.214,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10779385123220254, var=25.11653886214632, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C',), comment="""BM rule fitted to 50 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C
    Total Standard Deviation in ln(k): 10.31784999999885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C
Total Standard Deviation in ln(k): 10.31784999999885""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C
Total Standard Deviation in ln(k): 10.31784999999885
""",
)

entry(
    index = 196,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(345965,'m^3/(mol*s)'), n=0.4765, w0=(196.968,'kJ/mol'), E0=(53.8629,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013172196224102475, var=6.255114427020542, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 5.046983858810302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.046983858810302""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.046983858810302
""",
)

entry(
    index = 197,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.65957e+07,'m^3/(mol*s)'), n=0.0055096, w0=(267.384,'kJ/mol'), E0=(169.322,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19036742801987694, var=5.683117720401056, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C
    Total Standard Deviation in ln(k): 5.257456311295365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C
Total Standard Deviation in ln(k): 5.257456311295365""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C
Total Standard Deviation in ln(k): 5.257456311295365
""",
)

entry(
    index = 198,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.75765e+07,'m^3/(mol*s)'), n=0.181385, w0=(335.003,'kJ/mol'), E0=(200.161,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.8422e+07,'m^3/(mol*s)'), n=-0.361029, w0=(179,'kJ/mol'), E0=(36.0057,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(134.737,'m^3/(mol*s)'), n=1.08957, w0=(179,'kJ/mol'), E0=(21.0749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08154989249933986, var=0.01844558039860729, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 0.4771713342289256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.4771713342289256""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.4771713342289256
""",
)

entry(
    index = 201,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(0.004135,'m^3/(mol*s)'), n=2.525, w0=(179,'kJ/mol'), E0=(39.2962,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_N-Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.45339e+06,'m^3/(mol*s)'), n=0.0013093, w0=(179,'kJ/mol'), E0=(38.6327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17507731919087033, var=1.2895074817300112, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.7163994079038525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R
Total Standard Deviation in ln(k): 2.7163994079038525""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R
Total Standard Deviation in ln(k): 2.7163994079038525
""",
)

entry(
    index = 203,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=3.5776e-09, w0=(179,'kJ/mol'), E0=(41.0041,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.5e+06,'m^3/(mol*s)'), n=-4.09333e-09, w0=(179,'kJ/mol'), E0=(33.4569,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_2R->Br",
    kinetics = ArrheniusBM(A=(96.2589,'m^3/(mol*s)'), n=1.014, w0=(190.329,'kJ/mol'), E0=(138.542,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_2R->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_2R->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_2R->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_2R->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br",
    kinetics = ArrheniusBM(A=(9.05686e+16,'m^3/(mol*s)'), n=-2.80537, w0=(176,'kJ/mol'), E0=(99.7859,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2695292716514378, var=13.160625223754336, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br
    Total Standard Deviation in ln(k): 7.949902143617397"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br
Total Standard Deviation in ln(k): 7.949902143617397""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br
Total Standard Deviation in ln(k): 7.949902143617397
""",
)

entry(
    index = 207,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C",
    kinetics = ArrheniusBM(A=(1.98716e+10,'m^3/(mol*s)'), n=-0.751277, w0=(174.117,'kJ/mol'), E0=(17.4117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4561043219388564, var=10.083282976185304, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C
    Total Standard Deviation in ln(k): 7.511863713916891"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C
Total Standard Deviation in ln(k): 7.511863713916891""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C
Total Standard Deviation in ln(k): 7.511863713916891
""",
)

entry(
    index = 208,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.03086e+08,'m^3/(mol*s)'), n=-0.239243, w0=(173,'kJ/mol'), E0=(79.9598,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0181660970758139, var=1.258566655483633, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C
    Total Standard Deviation in ln(k): 2.294672691076115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C
Total Standard Deviation in ln(k): 2.294672691076115""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C
Total Standard Deviation in ln(k): 2.294672691076115
""",
)

entry(
    index = 209,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.59017e+11,'m^3/(mol*s)'), n=-1.79892, w0=(166.808,'kJ/mol'), E0=(33.0389,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09726643598756933, var=5.844533146189304, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R
    Total Standard Deviation in ln(k): 5.0909291567280786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R
Total Standard Deviation in ln(k): 5.0909291567280786""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R
Total Standard Deviation in ln(k): 5.0909291567280786
""",
)

entry(
    index = 210,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N",
    kinetics = ArrheniusBM(A=(7.15577e+10,'m^3/(mol*s)'), n=-0.994857, w0=(117.833,'kJ/mol'), E0=(97.3023,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.35745103770888675, var=2.1080866960413878, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N
    Total Standard Deviation in ln(k): 3.8088435010131296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N
Total Standard Deviation in ln(k): 3.8088435010131296""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N
Total Standard Deviation in ln(k): 3.8088435010131296
""",
)

entry(
    index = 211,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_N-1BrCNO->N",
    kinetics = ArrheniusBM(A=(1.31593e+39,'m^3/(mol*s)'), n=-9.94233, w0=(280.314,'kJ/mol'), E0=(198.469,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04340880157647542, var=0.5179282162607376, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_N-1BrCNO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_N-1BrCNO->N
    Total Standard Deviation in ln(k): 1.5518196403286282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_N-1BrCNO->N
Total Standard Deviation in ln(k): 1.5518196403286282""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_N-1BrCNO->N
Total Standard Deviation in ln(k): 1.5518196403286282
""",
)

entry(
    index = 212,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.9609e+09,'m^3/(mol*s)'), n=-0.904668, w0=(173,'kJ/mol'), E0=(22.528,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28018604732531893, var=1.8325624862226306, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R
    Total Standard Deviation in ln(k): 3.417838453998129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R
Total Standard Deviation in ln(k): 3.417838453998129""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R
Total Standard Deviation in ln(k): 3.417838453998129
""",
)

entry(
    index = 213,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.51229e+07,'m^3/(mol*s)'), n=-0.0676006, w0=(173,'kJ/mol'), E0=(49.6983,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0039751620550457995, var=0.08330493739625001, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R
    Total Standard Deviation in ln(k): 0.5886064049544166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R
Total Standard Deviation in ln(k): 0.5886064049544166""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R
Total Standard Deviation in ln(k): 0.5886064049544166
""",
)

entry(
    index = 214,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5.38619e+06,'m^3/(mol*s)'), n=0.213797, w0=(186.233,'kJ/mol'), E0=(93.1164,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0030036702694343715, var=0.03535203814212297, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.3844799596401528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.3844799596401528""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.3844799596401528
""",
)

entry(
    index = 215,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_1BrCNO->O",
    kinetics = ArrheniusBM(A=(1.12593e+08,'m^3/(mol*s)'), n=-0.33733, w0=(71,'kJ/mol'), E0=(19.9199,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_1BrCNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_1BrCNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_1BrCNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_1BrCNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-1BrCNO->O",
    kinetics = ArrheniusBM(A=(1.69593e+08,'m^3/(mol*s)'), n=-0.383265, w0=(173,'kJ/mol'), E0=(78.646,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-1BrCNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-1BrCNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-1BrCNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-1BrCNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_1BrCNO->N",
    kinetics = ArrheniusBM(A=(1.59771e+09,'m^3/(mol*s)'), n=-0.461068, w0=(100.5,'kJ/mol'), E0=(47.4882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_1BrCNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_1BrCNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_1BrCNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_1BrCNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N",
    kinetics = ArrheniusBM(A=(1.55383e+07,'m^3/(mol*s)'), n=-8.56412e-08, w0=(175.98,'kJ/mol'), E0=(73.5719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09421308698785932, var=0.0029672623616758056, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N
    Total Standard Deviation in ln(k): 0.3459193980198214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N
Total Standard Deviation in ln(k): 0.3459193980198214""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N
Total Standard Deviation in ln(k): 0.3459193980198214
""",
)

entry(
    index = 219,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_2R->C",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=-2.10458e-08, w0=(228.695,'kJ/mol'), E0=(90.4389,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49137027504925385, var=0.1362842420729928, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_2R->C
    Total Standard Deviation in ln(k): 1.9746806289573515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_2R->C
Total Standard Deviation in ln(k): 1.9746806289573515""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_2R->C
Total Standard Deviation in ln(k): 1.9746806289573515
""",
)

entry(
    index = 220,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_N-2R->C",
    kinetics = ArrheniusBM(A=(5.19615e+07,'m^3/(mol*s)'), n=0, w0=(169.195,'kJ/mol'), E0=(84.5974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.166553000908251e-16, var=2.4138979216251584, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_N-2R->C
    Total Standard Deviation in ln(k): 3.1147015559000386"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_N-2R->C
Total Standard Deviation in ln(k): 3.1147015559000386""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_N-2R->C
Total Standard Deviation in ln(k): 3.1147015559000386
""",
)

entry(
    index = 221,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(8.76581e+08,'m^3/(mol*s)'), n=-0.698494, w0=(146.737,'kJ/mol'), E0=(60.3211,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.482637545787142, var=2.720817009133938, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R
    Total Standard Deviation in ln(k): 4.519447460521909"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R
Total Standard Deviation in ln(k): 4.519447460521909""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R
Total Standard Deviation in ln(k): 4.519447460521909
""",
)

entry(
    index = 222,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O",
    kinetics = ArrheniusBM(A=(1.55564e+07,'m^3/(mol*s)'), n=-2.97334e-08, w0=(131.868,'kJ/mol'), E0=(36.1716,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8029778178760756, var=3.408684723999562, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O
    Total Standard Deviation in ln(k): 5.718799132852841"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O
Total Standard Deviation in ln(k): 5.718799132852841""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O
Total Standard Deviation in ln(k): 5.718799132852841
""",
)

entry(
    index = 223,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O",
    kinetics = ArrheniusBM(A=(6.64337e+08,'m^3/(mol*s)'), n=-0.47264, w0=(169.322,'kJ/mol'), E0=(62.5727,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.021138361016725272, var=0.36234128019192474, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O
    Total Standard Deviation in ln(k): 1.2598575395220302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O
Total Standard Deviation in ln(k): 1.2598575395220302""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O
Total Standard Deviation in ln(k): 1.2598575395220302
""",
)

entry(
    index = 224,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_1BrCNO->O",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=-2.58451e-08, w0=(100.5,'kJ/mol'), E0=(38.1729,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_1BrCNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_1BrCNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_1BrCNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_1BrCNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O",
    kinetics = ArrheniusBM(A=(235987,'m^3/(mol*s)'), n=0.357407, w0=(215.216,'kJ/mol'), E0=(61.9964,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.1268914495869713, var=3.9860954744655572, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O
    Total Standard Deviation in ln(k): 11.859006545539177"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O
Total Standard Deviation in ln(k): 11.859006545539177""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O
Total Standard Deviation in ln(k): 11.859006545539177
""",
)

entry(
    index = 226,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(246.285,'kJ/mol'), E0=(178.838,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00799142,'m^3/(mol*s)'), n=2.64817, w0=(266.169,'kJ/mol'), E0=(26.6169,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9738719679812482, var=102.1355601055678, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 22.707196068112502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 22.707196068112502""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 22.707196068112502
""",
)

entry(
    index = 228,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.11e+34,'m^3/(mol*s)'), n=-9.59, w0=(271.762,'kJ/mol'), E0=(194.038,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R_4BrClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=-1.71507e-08, w0=(244.299,'kJ/mol'), E0=(177.487,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R_4BrClFINOPSSi->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R_4BrClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R_4BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R_4BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 230,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R_N-4BrClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(2.03025e+08,'m^3/(mol*s)'), n=0.0776927, w0=(228.234,'kJ/mol'), E0=(169.317,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R_N-4BrClFINOPSSi->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R_N-4BrClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R_N-4BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R_N-4BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.9764e+07,'m^3/(mol*s)'), n=0.206427, w0=(205.5,'kJ/mol'), E0=(98.6789,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012762858847282958, var=0.0681928511809308, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 0.5555792106608185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 0.5555792106608185""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 0.5555792106608185
""",
)

entry(
    index = 232,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(4.79728e+07,'m^3/(mol*s)'), n=0.210679, w0=(205.5,'kJ/mol'), E0=(102.402,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(6.84478e+06,'m^3/(mol*s)'), n=0.41638, w0=(205.5,'kJ/mol'), E0=(76.6427,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(3.16837e+06,'m^3/(mol*s)'), n=0.460513, w0=(205.5,'kJ/mol'), E0=(83.6747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(8.58356e+07,'m^3/(mol*s)'), n=0.0405873, w0=(205.5,'kJ/mol'), E0=(94.779,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(2.11623e+09,'m^3/(mol*s)'), n=-0.373695, w0=(205.5,'kJ/mol'), E0=(114.051,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1561377006943811, var=0.2424883010508162, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 1.3794995025163954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.3794995025163954""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.3794995025163954
""",
)

entry(
    index = 237,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.15008e+19,'m^3/(mol*s)'), n=-5.14141, w0=(283.352,'kJ/mol'), E0=(28.3352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30194898785893354, var=33.391442354799615, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 12.343093378056347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 12.343093378056347""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 12.343093378056347
""",
)

entry(
    index = 238,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(210.252,'kJ/mol'), E0=(105.126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1.21e+08,'m^3/(mol*s)'), n=0, w0=(232.616,'kJ/mol'), E0=(116.308,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.805e+20,'m^3/(mol*s)'), n=-4.82, w0=(231.271,'kJ/mol'), E0=(167.983,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2988541939225804, var=8.66250553588933e-06, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R
    Total Standard Deviation in ln(k): 0.7567902977644224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 0.7567902977644224""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 0.7567902977644224
""",
)

entry(
    index = 241,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(228516,'m^3/(mol*s)'), n=0.317874, w0=(163.5,'kJ/mol'), E0=(69.7597,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.044992570828351876, var=20.619355822430787, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 9.21625612615887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 9.21625612615887""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 9.21625612615887
""",
)

entry(
    index = 242,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.13552e+14,'m^3/(mol*s)'), n=-2.31938, w0=(163.5,'kJ/mol'), E0=(68.0308,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.64994e+14,'m^3/(mol*s)'), n=-2.23152, w0=(190.619,'kJ/mol'), E0=(141.55,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.58726e+10,'m^3/(mol*s)'), n=-0.943457, w0=(173,'kJ/mol'), E0=(80.1186,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14028198769790737, var=28.707507064998268, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.093714951218875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.093714951218875""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.093714951218875
""",
)

entry(
    index = 245,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.83652e+09,'m^3/(mol*s)'), n=-0.617443, w0=(173,'kJ/mol'), E0=(82.3782,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08557209167498957, var=0.5734036438923596, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 1.733059231565796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 1.733059231565796""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 1.733059231565796
""",
)

entry(
    index = 246,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R",
    kinetics = ArrheniusBM(A=(1.26045e+13,'m^3/(mol*s)'), n=-1.70836, w0=(173,'kJ/mol'), E0=(83.711,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15157522682845567, var=1.606734123716368, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R
    Total Standard Deviation in ln(k): 2.9219846517070405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R
Total Standard Deviation in ln(k): 2.9219846517070405""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R
Total Standard Deviation in ln(k): 2.9219846517070405
""",
)

entry(
    index = 247,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(4.17591e+23,'m^3/(mol*s)'), n=-4.73474, w0=(173,'kJ/mol'), E0=(57.9426,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2.18232e+23,'m^3/(mol*s)'), n=-4.54131, w0=(173,'kJ/mol'), E0=(58.3156,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-5BrCClINOPSSi-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 249,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(7.90354e+06,'m^3/(mol*s)'), n=0.225871, w0=(174.9,'kJ/mol'), E0=(47.6296,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002031595674892465, var=5.172999770401151, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C
    Total Standard Deviation in ln(k): 4.564719987014195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 4.564719987014195""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 4.564719987014195
""",
)

entry(
    index = 250,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(0.00553513,'m^3/(mol*s)'), n=2.35071, w0=(215.712,'kJ/mol'), E0=(21.5712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16704735180391003, var=36.18955756890593, Tref=1000.0, N=37, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C',), comment="""BM rule fitted to 37 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
    Total Standard Deviation in ln(k): 12.479753577209701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 37 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 12.479753577209701""",
    longDesc = 
"""
BM rule fitted to 37 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 12.479753577209701
""",
)

entry(
    index = 251,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C",
    kinetics = ArrheniusBM(A=(37198.1,'m^3/(mol*s)'), n=0.706518, w0=(203.584,'kJ/mol'), E0=(20.3584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02716745371710935, var=6.636842042540434, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C
    Total Standard Deviation in ln(k): 5.232872292834666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C
Total Standard Deviation in ln(k): 5.232872292834666""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C
Total Standard Deviation in ln(k): 5.232872292834666
""",
)

entry(
    index = 252,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C",
    kinetics = ArrheniusBM(A=(9.17992e+09,'m^3/(mol*s)'), n=-0.67163, w0=(179,'kJ/mol'), E0=(84.6839,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08559986784151823, var=8.053682610385948, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C
    Total Standard Deviation in ln(k): 5.904314910987091"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C
Total Standard Deviation in ln(k): 5.904314910987091""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C
Total Standard Deviation in ln(k): 5.904314910987091
""",
)

entry(
    index = 253,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(3.35407e+06,'m^3/(mol*s)'), n=0.141943, w0=(232.471,'kJ/mol'), E0=(147.287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(1.06887e+06,'m^3/(mol*s)'), n=0.378031, w0=(284.84,'kJ/mol'), E0=(175.907,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2412710752011891, var=0.26878950365725035, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 1.6455618947186426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 1.6455618947186426""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 1.6455618947186426
""",
)

entry(
    index = 255,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(2.94057e+10,'m^3/(mol*s)'), n=-1.39317, w0=(179,'kJ/mol'), E0=(54.5323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(124.902,'m^3/(mol*s)'), n=1.09941, w0=(179,'kJ/mol'), E0=(16.8874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01560833182403432, var=0.016020860987762845, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 0.2929633293189987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 0.2929633293189987""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 0.2929633293189987
""",
)

entry(
    index = 257,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.18769e+06,'m^3/(mol*s)'), n=0.000841933, w0=(179,'kJ/mol'), E0=(38.6327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.091996424045003e-09, var=0.7836333610822446, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C
    Total Standard Deviation in ln(k): 1.7746530058716035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746530058716035""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746530058716035
""",
)

entry(
    index = 258,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.505e+06,'m^3/(mol*s)'), n=-1.00399e-08, w0=(179,'kJ/mol'), E0=(33.3298,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.81979e+07,'m^3/(mol*s)'), n=-0.126529, w0=(173,'kJ/mol'), E0=(49.1223,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_2CNO->C",
    kinetics = ArrheniusBM(A=(1.52887e+10,'m^3/(mol*s)'), n=-0.421056, w0=(173.605,'kJ/mol'), E0=(86.8027,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0651195782842307, var=2.9701892693694725, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_2CNO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_2CNO->C
    Total Standard Deviation in ln(k): 3.6186249868947136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_2CNO->C
Total Standard Deviation in ln(k): 3.6186249868947136""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_2CNO->C
Total Standard Deviation in ln(k): 3.6186249868947136
""",
)

entry(
    index = 261,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C",
    kinetics = ArrheniusBM(A=(2.10912e+17,'m^3/(mol*s)'), n=-2.93464, w0=(179,'kJ/mol'), E0=(86.6595,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2620731312264369, var=15.202718368514994, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C
    Total Standard Deviation in ln(k): 8.475070276486878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C
Total Standard Deviation in ln(k): 8.475070276486878""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C
Total Standard Deviation in ln(k): 8.475070276486878
""",
)

entry(
    index = 262,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.91432e+10,'m^3/(mol*s)'), n=-0.773997, w0=(173.75,'kJ/mol'), E0=(17.375,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4897490556440522, var=10.28481979224806, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R
    Total Standard Deviation in ln(k): 7.659701529571641"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 7.659701529571641""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 7.659701529571641
""",
)

entry(
    index = 263,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(2.82036e+08,'m^3/(mol*s)'), n=-0.5, w0=(187.402,'kJ/mol'), E0=(139.216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16920761856358965, var=1.2798808077192283, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-1BrCNO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 2.693137994621831"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 2.693137994621831""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 2.693137994621831
""",
)

entry(
    index = 264,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.08827e+07,'m^3/(mol*s)'), n=-0.166667, w0=(173,'kJ/mol'), E0=(38.9085,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4713655005703093e-09, var=0.21450406484183354, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R
    Total Standard Deviation in ln(k): 0.9284847058581546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.9284847058581546""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.9284847058581546
""",
)

entry(
    index = 265,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(2.95004e+08,'m^3/(mol*s)'), n=-0.654592, w0=(176.087,'kJ/mol'), E0=(32.8805,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.384037453733207, var=1.4882035948788261, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 3.410533645608265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 3.410533645608265""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 3.410533645608265
""",
)

entry(
    index = 266,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_2R->O",
    kinetics = ArrheniusBM(A=(122000,'m^3/(mol*s)'), n=0.2, w0=(100.5,'kJ/mol'), E0=(22.1948,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_2R->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_2R->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_2R->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_2R->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O",
    kinetics = ArrheniusBM(A=(1.15556e+14,'m^3/(mol*s)'), n=-3.06271, w0=(196.55,'kJ/mol'), E0=(3.68968,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.6759218653692782, var=45.774116392447, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O
    Total Standard Deviation in ln(k): 22.79933475526203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O
Total Standard Deviation in ln(k): 22.79933475526203""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O
Total Standard Deviation in ln(k): 22.79933475526203
""",
)

entry(
    index = 268,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N_2R->C",
    kinetics = ArrheniusBM(A=(1.46789e+12,'m^3/(mol*s)'), n=-1.37202, w0=(152.5,'kJ/mol'), E0=(64.4424,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 269,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N_N-2R->C",
    kinetics = ArrheniusBM(A=(3.65367e+06,'m^3/(mol*s)'), n=0.2352, w0=(102.495,'kJ/mol'), E0=(51.2476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4647064516488904, var=0.481324023566866, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N_N-2R->C
    Total Standard Deviation in ln(k): 2.5584396225376094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N_N-2R->C
Total Standard Deviation in ln(k): 2.5584396225376094""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_1BrCNO->N_N-2R->C
Total Standard Deviation in ln(k): 2.5584396225376094
""",
)

entry(
    index = 270,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_N-1BrCNO->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.54e+40,'m^3/(mol*s)'), n=-10.66, w0=(279.146,'kJ/mol'), E0=(193.241,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_N-1BrCNO->N_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_N-1BrCNO->N_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_N-1BrCNO->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_N-1BrCNO->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 271,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R",
    kinetics = ArrheniusBM(A=(2.19331e+13,'m^3/(mol*s)'), n=-2.11077, w0=(173,'kJ/mol'), E0=(86.4669,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2293247030427738, var=0.08141112270043357, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R
    Total Standard Deviation in ln(k): 1.1481964519560872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R
Total Standard Deviation in ln(k): 1.1481964519560872""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R
Total Standard Deviation in ln(k): 1.1481964519560872
""",
)

entry(
    index = 272,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-5R!H-2R",
    kinetics = ArrheniusBM(A=(250896,'m^3/(mol*s)'), n=0.298496, w0=(173,'kJ/mol'), E0=(73.0117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6275205214902675, var=0.8643428515802953, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-5R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-5R!H-2R
    Total Standard Deviation in ln(k): 3.4404877499228292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-5R!H-2R
Total Standard Deviation in ln(k): 3.4404877499228292""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-5R!H-2R
Total Standard Deviation in ln(k): 3.4404877499228292
""",
)

entry(
    index = 273,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(3.11826e+08,'m^3/(mol*s)'), n=-0.382134, w0=(173,'kJ/mol'), E0=(75.4719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3103717364191287, var=0.19251948769113075, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 1.659446949581135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.659446949581135""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.659446949581135
""",
)

entry(
    index = 274,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.92981e+07,'m^3/(mol*s)'), n=-0.0980858, w0=(176.039,'kJ/mol'), E0=(70.9125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.027636288480833365, var=0.08748618983592148, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 0.6623997445926043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 0.6623997445926043""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 0.6623997445926043
""",
)

entry(
    index = 275,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(5.749e+06,'m^3/(mol*s)'), n=0.214, w0=(186.262,'kJ/mol'), E0=(93.131,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 276,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.54071e+07,'m^3/(mol*s)'), n=-1.01288e-07, w0=(175.459,'kJ/mol'), E0=(73.2978,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11648449034931463, var=0.0017941964049210067, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R
    Total Standard Deviation in ln(k): 0.3775910783202989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R
Total Standard Deviation in ln(k): 0.3775910783202989""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R
Total Standard Deviation in ln(k): 0.3775910783202989
""",
)

entry(
    index = 277,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=0, w0=(244.3,'kJ/mol'), E0=(122.15,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_2R->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->O_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R_1BrCNO->O",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(77.2673,'kJ/mol'), E0=(38.6336,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R_1BrCNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R_1BrCNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R_1BrCNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R_1BrCNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R_N-1BrCNO->O",
    kinetics = ArrheniusBM(A=(8.41487e+08,'m^3/(mol*s)'), n=-0.692606, w0=(181.472,'kJ/mol'), E0=(90.7359,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4612600998246526, var=0.494140255580928, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R_N-1BrCNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R_N-1BrCNO->O
    Total Standard Deviation in ln(k): 2.568175711693148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R_N-1BrCNO->O
Total Standard Deviation in ln(k): 2.568175711693148""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_Ext-2R-R_N-1BrCNO->O
Total Standard Deviation in ln(k): 2.568175711693148
""",
)

entry(
    index = 280,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O_2R->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-4.23606e-08, w0=(179,'kJ/mol'), E0=(70.8713,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O_N-2R->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(90.1681,'kJ/mol'), E0=(45.084,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_1BrCNO->O_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_2R->O",
    kinetics = ArrheniusBM(A=(7.7e+07,'m^3/(mol*s)'), n=0, w0=(195.452,'kJ/mol'), E0=(97.726,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_2R->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_2R->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_2R->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_2R->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O",
    kinetics = ArrheniusBM(A=(6.72511e+08,'m^3/(mol*s)'), n=-0.475322, w0=(162.79,'kJ/mol'), E0=(60.68,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2089728236937523, var=0.09796623905562106, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O
    Total Standard Deviation in ln(k): 1.1525305833338693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O
Total Standard Deviation in ln(k): 1.1525305833338693""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O
Total Standard Deviation in ln(k): 1.1525305833338693
""",
)

entry(
    index = 284,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_3BrClNO->Cl",
    kinetics = ArrheniusBM(A=(9.26048e+36,'m^3/(mol*s)'), n=-9.23874, w0=(282.184,'kJ/mol'), E0=(193.589,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05438046726055889, var=0.3176744838946306, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_3BrClNO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_3BrClNO->Cl
    Total Standard Deviation in ln(k): 1.266555536755236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_3BrClNO->Cl
Total Standard Deviation in ln(k): 1.266555536755236""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_3BrClNO->Cl
Total Standard Deviation in ln(k): 1.266555536755236
""",
)

entry(
    index = 285,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl",
    kinetics = ArrheniusBM(A=(771171,'m^3/(mol*s)'), n=0.222414, w0=(162.75,'kJ/mol'), E0=(70.8508,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3128541875116064, var=0.31348157568524126, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl
    Total Standard Deviation in ln(k): 1.908505448434297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl
Total Standard Deviation in ln(k): 1.908505448434297""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl
Total Standard Deviation in ln(k): 1.908505448434297
""",
)

entry(
    index = 286,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(244.986,'kJ/mol'), E0=(177.869,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(0.00648885,'m^3/(mol*s)'), n=2.67681, w0=(268.287,'kJ/mol'), E0=(26.8287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.910170935699233, var=104.92502267981115, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 22.821947613963577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 22.821947613963577""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 22.821947613963577
""",
)

entry(
    index = 288,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.88633e+07,'m^3/(mol*s)'), n=0.213913, w0=(205.94,'kJ/mol'), E0=(102.97,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.197906922440378e-05, var=0.01210657880115639, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.22078677680714184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.22078677680714184""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.22078677680714184
""",
)

entry(
    index = 289,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(249.899,'kJ/mol'), E0=(124.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 290,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C",
    kinetics = ArrheniusBM(A=(3.01146e+07,'m^3/(mol*s)'), n=0.20296, w0=(205.5,'kJ/mol'), E0=(95.2091,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7080255759885304, var=1.015783988518826, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
    Total Standard Deviation in ln(k): 3.799453225621823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
Total Standard Deviation in ln(k): 3.799453225621823""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
Total Standard Deviation in ln(k): 3.799453225621823
""",
)

entry(
    index = 291,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(2.06819e+09,'m^3/(mol*s)'), n=-0.368028, w0=(205.516,'kJ/mol'), E0=(109.441,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02118791466423305, var=0.059047477739823905, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 0.5403803109828671"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 0.5403803109828671""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 0.5403803109828671
""",
)

entry(
    index = 292,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(2.83712e+08,'m^3/(mol*s)'), n=-0.251115, w0=(205.5,'kJ/mol'), E0=(121.486,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09753801016004564, var=3.4382379629420625, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 3.962347637832616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 3.962347637832616""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 3.962347637832616
""",
)

entry(
    index = 293,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(4.36443e+19,'m^3/(mol*s)'), n=-5.46416, w0=(282.202,'kJ/mol'), E0=(28.2202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24476884684624783, var=42.99031552256663, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 13.759443681283665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 13.759443681283665""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 13.759443681283665
""",
)

entry(
    index = 294,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1.43521e+26,'m^3/(mol*s)'), n=-6.47299, w0=(285.077,'kJ/mol'), E0=(184.723,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28584039541456774, var=0.30467661605832125, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 1.8247559838418383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 1.8247559838418383""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 1.8247559838418383
""",
)

entry(
    index = 295,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=2.48906e-08, w0=(163.5,'kJ/mol'), E0=(60.9633,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(5221.95,'m^3/(mol*s)'), n=0.635748, w0=(163.5,'kJ/mol'), E0=(65.7136,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_1BrCClNO->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->O",
    kinetics = ArrheniusBM(A=(5.1502e+26,'m^3/(mol*s)'), n=-5.42051, w0=(173,'kJ/mol'), E0=(50.8068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(147596,'m^3/(mol*s)'), n=0.548893, w0=(179.779,'kJ/mol'), E0=(17.9779,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10339424017993883, var=1.022515808255404, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 2.2869630856887997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O
Total Standard Deviation in ln(k): 2.2869630856887997""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O
Total Standard Deviation in ln(k): 2.2869630856887997
""",
)

entry(
    index = 299,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_7BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.6953e+15,'m^3/(mol*s)'), n=-2.51089, w0=(173,'kJ/mol'), E0=(66.6914,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_7BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_7BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_7BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_7BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.91149e+06,'m^3/(mol*s)'), n=0.329282, w0=(180.443,'kJ/mol'), E0=(90.2216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.055135484650235184, var=0.26853316002029687, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 1.1773887995113892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.1773887995113892""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.1773887995113892
""",
)

entry(
    index = 301,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.39951e+14,'m^3/(mol*s)'), n=-1.98214, w0=(173,'kJ/mol'), E0=(84.173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12162076670474682, var=3.5754321587283755, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 4.096295921207409"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 4.096295921207409""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 4.096295921207409
""",
)

entry(
    index = 302,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F",
    kinetics = ArrheniusBM(A=(4.6512e+13,'m^3/(mol*s)'), n=-1.91907, w0=(173,'kJ/mol'), E0=(75.8314,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3612013651820064, var=0.4661739213318802, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F
    Total Standard Deviation in ln(k): 2.276312690352171"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F
Total Standard Deviation in ln(k): 2.276312690352171""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F
Total Standard Deviation in ln(k): 2.276312690352171
""",
)

entry(
    index = 303,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(7.10829e+08,'m^3/(mol*s)'), n=-0.471946, w0=(181.795,'kJ/mol'), E0=(84.2261,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41243082597075226, var=0.4569163782271885, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F
    Total Standard Deviation in ln(k): 2.391370859444379"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F
Total Standard Deviation in ln(k): 2.391370859444379""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F
Total Standard Deviation in ln(k): 2.391370859444379
""",
)

entry(
    index = 304,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C",
    kinetics = ArrheniusBM(A=(5893.55,'m^3/(mol*s)'), n=1.1454, w0=(189.496,'kJ/mol'), E0=(18.9496,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18910978518367083, var=1.2858425593102474, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C
    Total Standard Deviation in ln(k): 2.748419516862346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C
Total Standard Deviation in ln(k): 2.748419516862346""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C
Total Standard Deviation in ln(k): 2.748419516862346
""",
)

entry(
    index = 305,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C",
    kinetics = ArrheniusBM(A=(3.07041e+14,'m^3/(mol*s)'), n=-2.00141, w0=(179,'kJ/mol'), E0=(74.2967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01087985792032603, var=13.866917811989968, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C
    Total Standard Deviation in ln(k): 7.492631087778456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C
Total Standard Deviation in ln(k): 7.492631087778456""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C
Total Standard Deviation in ln(k): 7.492631087778456
""",
)

entry(
    index = 306,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C",
    kinetics = ArrheniusBM(A=(5.27207e-08,'m^3/(mol*s)'), n=3.69052, w0=(231.047,'kJ/mol'), E0=(23.1047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2908598815374362, var=36.61717946481545, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C
    Total Standard Deviation in ln(k): 12.86188279920684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C
Total Standard Deviation in ln(k): 12.86188279920684""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C
Total Standard Deviation in ln(k): 12.86188279920684
""",
)

entry(
    index = 307,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C",
    kinetics = ArrheniusBM(A=(1.59901e+08,'m^3/(mol*s)'), n=-0.440564, w0=(183.764,'kJ/mol'), E0=(39.2347,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09089543975345071, var=6.090887146368586, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C
    Total Standard Deviation in ln(k): 5.1760110900783864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C
Total Standard Deviation in ln(k): 5.1760110900783864""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C
Total Standard Deviation in ln(k): 5.1760110900783864
""",
)

entry(
    index = 308,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O",
    kinetics = ArrheniusBM(A=(17938.9,'m^3/(mol*s)'), n=0.724393, w0=(203.647,'kJ/mol'), E0=(20.3647,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04581249517922337, var=5.974901561308173, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O
    Total Standard Deviation in ln(k): 5.0154033642094085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O
Total Standard Deviation in ln(k): 5.0154033642094085""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O
Total Standard Deviation in ln(k): 5.0154033642094085
""",
)

entry(
    index = 309,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O",
    kinetics = ArrheniusBM(A=(635104,'m^3/(mol*s)'), n=0.636967, w0=(203.545,'kJ/mol'), E0=(20.3545,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11780428666598358, var=1.1769495740941598, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O
    Total Standard Deviation in ln(k): 2.470873764345127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O
Total Standard Deviation in ln(k): 2.470873764345127""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O
Total Standard Deviation in ln(k): 2.470873764345127
""",
)

entry(
    index = 310,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_7R!H->O",
    kinetics = ArrheniusBM(A=(3.09117e+10,'m^3/(mol*s)'), n=-0.602081, w0=(199.707,'kJ/mol'), E0=(99.8536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(1.36506e+07,'m^3/(mol*s)'), n=0.0650004, w0=(179,'kJ/mol'), E0=(47.8702,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04399457921902887, var=1.3101394396400807, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O
    Total Standard Deviation in ln(k): 2.4051854301723923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 2.4051854301723923""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 2.4051854301723923
""",
)

entry(
    index = 312,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(25637.8,'m^3/(mol*s)'), n=0.759408, w0=(264.35,'kJ/mol'), E0=(164.836,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 313,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.3882e+06,'m^3/(mol*s)'), n=0.317264, w0=(305.329,'kJ/mol'), E0=(183.781,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_N-4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H_4R!H-inRing",
    kinetics = ArrheniusBM(A=(252.533,'m^3/(mol*s)'), n=0.999283, w0=(179,'kJ/mol'), E0=(17.329,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H_4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(1.53331,'m^3/(mol*s)'), n=1.7252, w0=(179,'kJ/mol'), E0=(16.4458,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-5R!H-4R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.05e+06,'m^3/(mol*s)'), n=-2.21223e-08, w0=(179,'kJ/mol'), E0=(34.9352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R->C_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 317,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_2CNO->C_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(2.223e+10,'m^3/(mol*s)'), n=-0.506, w0=(184.66,'kJ/mol'), E0=(136.628,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_2CNO->C_Ext-1BrCNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_2CNO->C_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_2CNO->C_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_2CNO->C_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 318,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(7.60814e+16,'m^3/(mol*s)'), n=-2.95283, w0=(179,'kJ/mol'), E0=(85.453,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2690148597813428, var=22.57377784013769, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 10.200787956756473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 10.200787956756473""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 10.200787956756473
""",
)

entry(
    index = 319,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.62085e+18,'m^3/(mol*s)'), n=-2.89824, w0=(179,'kJ/mol'), E0=(89.0725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.65983e+11,'m^3/(mol*s)'), n=-0.84129, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1366575543344507, var=2.914302666931026, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.7657098538028677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.7657098538028677""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.7657098538028677
""",
)

entry(
    index = 321,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(9.69024e+08,'m^3/(mol*s)'), n=-0.88, w0=(173.478,'kJ/mol'), E0=(17.3478,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0232391628674864e-09, var=1.738290842687064, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 2.64312809473536"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.64312809473536""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.64312809473536
""",
)

entry(
    index = 322,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.52099e+07,'m^3/(mol*s)'), n=-0.433333, w0=(178.663,'kJ/mol'), E0=(17.8663,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0511027735631669e-10, var=0.6211068618095666, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C
    Total Standard Deviation in ln(k): 1.5799383944085854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 1.5799383944085854""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 1.5799383944085854
""",
)

entry(
    index = 323,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-6.17521e-08, w0=(173,'kJ/mol'), E0=(69.7954,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_5R!H->C",
    kinetics = ArrheniusBM(A=(6.14427e+07,'m^3/(mol*s)'), n=-0.25, w0=(173,'kJ/mol'), E0=(50.0532,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2058359733662052, var=0.33606202739258995, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_5R!H->C
    Total Standard Deviation in ln(k): 1.679337919603527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 1.679337919603527""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 1.679337919603527
""",
)

entry(
    index = 325,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=-7.64439e-08, w0=(173,'kJ/mol'), E0=(62.6333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 326,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(92.2154,'m^3/(mol*s)'), n=1.49683, w0=(173,'kJ/mol'), E0=(67.4291,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05691081219099027, var=2.6324204852565347, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R_Ext-2R-R
    Total Standard Deviation in ln(k): 3.3956216682966667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R_Ext-2R-R
Total Standard Deviation in ln(k): 3.3956216682966667""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R_Ext-2R-R
Total Standard Deviation in ln(k): 3.3956216682966667
""",
)

entry(
    index = 327,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(9.19256e+13,'m^3/(mol*s)'), n=-2.8571, w0=(153.351,'kJ/mol'), E0=(23.726,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.574241856874702, var=54.84448622125524, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R
    Total Standard Deviation in ln(k): 31.364674869542405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R
Total Standard Deviation in ln(k): 31.364674869542405""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R
Total Standard Deviation in ln(k): 31.364674869542405
""",
)

entry(
    index = 328,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R_5R!H-inRing",
    kinetics = ArrheniusBM(A=(3.144e+13,'m^3/(mol*s)'), n=-2.163, w0=(173,'kJ/mol'), E0=(86.7215,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.80218e+07,'m^3/(mol*s)'), n=-0.134489, w0=(173,'kJ/mol'), E0=(68.6955,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R_N-5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R_N-5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-5R!H-2R_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 330,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.81979e+07,'m^3/(mol*s)'), n=-0.126529, w0=(173,'kJ/mol'), E0=(62.7077,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 331,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi",
    kinetics = ArrheniusBM(A=(2.17712e+06,'m^3/(mol*s)'), n=0.213828, w0=(183.244,'kJ/mol'), E0=(77.8501,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00017420524692625505, var=0.09909663638708269, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi
    Total Standard Deviation in ln(k): 0.6315206505006369"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 0.6315206505006369""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 0.6315206505006369
""",
)

entry(
    index = 332,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi",
    kinetics = ArrheniusBM(A=(8.05579e+10,'m^3/(mol*s)'), n=-1.31825, w0=(173,'kJ/mol'), E0=(70.1326,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11515356162216171, var=8.862062190662188e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi
    Total Standard Deviation in ln(k): 0.3082028374807834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 0.3082028374807834""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 0.3082028374807834
""",
)

entry(
    index = 333,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=-3.88679e-10, w0=(188.93,'kJ/mol'), E0=(74.4653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2604710848375015, var=0.1356903720728491, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C
    Total Standard Deviation in ln(k): 1.3929176648213697"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C
Total Standard Deviation in ln(k): 1.3929176648213697""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C
Total Standard Deviation in ln(k): 1.3929176648213697
""",
)

entry(
    index = 334,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.51e+07,'m^3/(mol*s)'), n=-1.88915e-08, w0=(173,'kJ/mol'), E0=(61.8128,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_2BrCN->Br",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(146.776,'kJ/mol'), E0=(73.3882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_2BrCN->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_2BrCN->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_2BrCN->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_2BrCN->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br",
    kinetics = ArrheniusBM(A=(6.86139e+08,'m^3/(mol*s)'), n=-0.478035, w0=(168.127,'kJ/mol'), E0=(61.8989,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.0872398857971617, var=19.19831206844187, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br
    Total Standard Deviation in ln(k): 16.540806988440963"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br
Total Standard Deviation in ln(k): 16.540806988440963""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br
Total Standard Deviation in ln(k): 16.540806988440963
""",
)

entry(
    index = 337,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_3BrClNO->Cl_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.568e+40,'m^3/(mol*s)'), n=-10.21, w0=(290.002,'kJ/mol'), E0=(199.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_3BrClNO->Cl_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_3BrClNO->Cl_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_3BrClNO->Cl_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_3BrClNO->Cl_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 338,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl_1CN->N",
    kinetics = ArrheniusBM(A=(2.4e+06,'m^3/(mol*s)'), n=0.085, w0=(152.5,'kJ/mol'), E0=(86.5718,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl_1CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl_1CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl_1CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl_1CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl_N-1CN->N",
    kinetics = ArrheniusBM(A=(6.23766e+12,'m^3/(mol*s)'), n=-2.0926, w0=(173,'kJ/mol'), E0=(75.9802,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl_N-1CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl_N-1CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_N-3BrCClINOPSSi->C_N-1BrCNO->O_N-3BrClNO->Cl_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 340,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F",
    kinetics = ArrheniusBM(A=(0.00615375,'m^3/(mol*s)'), n=2.68352, w0=(271.23,'kJ/mol'), E0=(27.123,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8188661071269553, var=108.7494905670324, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F
    Total Standard Deviation in ln(k): 22.963436113011664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F
Total Standard Deviation in ln(k): 22.963436113011664""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F
Total Standard Deviation in ln(k): 22.963436113011664
""",
)

entry(
    index = 341,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->F",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(241.803,'kJ/mol'), E0=(120.902,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.85197e+07,'m^3/(mol*s)'), n=0.213787, w0=(205.932,'kJ/mol'), E0=(102.966,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00012681105802580086, var=0.012046587691161825, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.22035222491166043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.22035222491166043""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.22035222491166043
""",
)

entry(
    index = 343,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.89626e+07,'m^3/(mol*s)'), n=0.120172, w0=(205.5,'kJ/mol'), E0=(29.6951,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0028590242889813336, var=4.845846638591843, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.420263699272195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.420263699272195""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.420263699272195
""",
)

entry(
    index = 344,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(227.003,'kJ/mol'), E0=(164.454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(73.3774,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005718031450769882, var=3.1264413462487737e-19, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 0.014366914313828543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.014366914313828543""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.014366914313828543
""",
)

entry(
    index = 346,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(6.117e+08,'m^3/(mol*s)'), n=-0.152, w0=(221.392,'kJ/mol'), E0=(163.779,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 347,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(80.9193,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C",
    kinetics = ArrheniusBM(A=(2.33349e+09,'m^3/(mol*s)'), n=-0.385433, w0=(210.716,'kJ/mol'), E0=(96.0261,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07348196797957501, var=0.05109986366496323, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
    Total Standard Deviation in ln(k): 0.6378040168110805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 0.6378040168110805""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 0.6378040168110805
""",
)

entry(
    index = 349,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(231.764,'kJ/mol'), E0=(115.882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.237e+44,'m^3/(mol*s)'), n=-12.5348, w0=(281.452,'kJ/mol'), E0=(271.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27924283284942597, var=85.96327841141091, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 19.288793860718414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 19.288793860718414""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 19.288793860718414
""",
)

entry(
    index = 351,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, w0=(288.192,'kJ/mol'), E0=(208.98,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_8BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(944394,'m^3/(mol*s)'), n=0.330618, w0=(190.498,'kJ/mol'), E0=(139.784,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_8BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_8BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 353,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(2.42892e+06,'m^3/(mol*s)'), n=0.194056, w0=(174.419,'kJ/mol'), E0=(87.2094,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07839085003139896, var=2.6147475003312475, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 3.43865481866175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.43865481866175""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.43865481866175
""",
)

entry(
    index = 354,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O_Ext-6C-R_Ext-6C-R_8R!H->O",
    kinetics = ArrheniusBM(A=(1.0902e+07,'m^3/(mol*s)'), n=0.100572, w0=(176.963,'kJ/mol'), E0=(88.4813,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O_Ext-6C-R_Ext-6C-R_8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O_Ext-6C-R_Ext-6C-R_8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O_Ext-6C-R_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O_Ext-6C-R_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O_Ext-6C-R_Ext-6C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(858971,'m^3/(mol*s)'), n=0.440882, w0=(183.924,'kJ/mol'), E0=(136.686,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O_Ext-6C-R_Ext-6C-R_N-8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O_Ext-6C-R_Ext-6C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O_Ext-6C-R_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_N-7R!H->C_N-7BrClFINOPSSi->O_Ext-6C-R_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.86408e+14,'m^3/(mol*s)'), n=-2.10498, w0=(173,'kJ/mol'), E0=(82.7062,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13981263032647262, var=4.794595046699841, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 4.740968961100198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 4.740968961100198""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 4.740968961100198
""",
)

entry(
    index = 357,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(7.88861e+13,'m^3/(mol*s)'), n=-1.73645, w0=(174.213,'kJ/mol'), E0=(87.1066,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 358,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F_6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(3.1564e+20,'m^3/(mol*s)'), n=-4.13392, w0=(173,'kJ/mol'), E0=(55.8427,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F_6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F_6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F_N-6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(3.03428e+07,'m^3/(mol*s)'), n=0.110658, w0=(191.64,'kJ/mol'), E0=(142.286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F_N-6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F_N-6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_7R!H->F_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 360,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F_7CO->C",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=0, w0=(179.602,'kJ/mol'), E0=(89.8012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F_7CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F_7CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F_7CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F_7CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F_N-7CO->C",
    kinetics = ArrheniusBM(A=(7.21342e+08,'m^3/(mol*s)'), n=-0.474354, w0=(183.988,'kJ/mol'), E0=(91.9938,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F_N-7CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F_N-7CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F_N-7CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_N-7R!H->F_N-7CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(1.16294e+12,'m^3/(mol*s)'), n=-1.06854, w0=(200.875,'kJ/mol'), E0=(193.37,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16761850549994273, var=0.4556967537372337, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O
    Total Standard Deviation in ln(k): 1.7744547504220922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O
Total Standard Deviation in ln(k): 1.7744547504220922""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O
Total Standard Deviation in ln(k): 1.7744547504220922
""",
)

entry(
    index = 363,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(1.65041e+07,'m^3/(mol*s)'), n=-0.167753, w0=(173,'kJ/mol'), E0=(83.3696,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03997300183383883, var=1.6277151145050939, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 2.6581145604311485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O
Total Standard Deviation in ln(k): 2.6581145604311485""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O
Total Standard Deviation in ln(k): 2.6581145604311485
""",
)

entry(
    index = 364,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.60793e+14,'m^3/(mol*s)'), n=-2.17033, w0=(179,'kJ/mol'), E0=(23.3028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20999520178972347, var=4.196725837201839, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 4.634508739995885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 4.634508739995885""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 4.634508739995885
""",
)

entry(
    index = 365,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.08601e+12,'m^3/(mol*s)'), n=-0.861305, w0=(179,'kJ/mol'), E0=(89.332,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.73697e-16,'m^3/(mol*s)'), n=5.85161, w0=(245.074,'kJ/mol'), E0=(24.5074,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004400634535392325, var=39.21592013403046, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C
    Total Standard Deviation in ln(k): 12.565232329967813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C
Total Standard Deviation in ln(k): 12.565232329967813""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C
Total Standard Deviation in ln(k): 12.565232329967813
""",
)

entry(
    index = 367,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.99536e-06,'m^3/(mol*s)'), n=3.27888, w0=(228.376,'kJ/mol'), E0=(22.8376,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.26155304198030443, var=35.89909795677069, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C
    Total Standard Deviation in ln(k): 12.66871026112829"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C
Total Standard Deviation in ln(k): 12.66871026112829""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C
Total Standard Deviation in ln(k): 12.66871026112829
""",
)

entry(
    index = 368,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.09805e+08,'m^3/(mol*s)'), n=-0.546218, w0=(179,'kJ/mol'), E0=(22.5276,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10434157665590768, var=5.865487906561262, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 5.117386417757587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 5.117386417757587""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 5.117386417757587
""",
)

entry(
    index = 369,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(4.1117e+07,'m^3/(mol*s)'), n=0.0877021, w0=(219.053,'kJ/mol'), E0=(34.7989,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7332066953924401, var=5.29450990501938, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 6.455083607753889"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 6.455083607753889""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 6.455083607753889
""",
)

entry(
    index = 370,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R",
    kinetics = ArrheniusBM(A=(905757,'m^3/(mol*s)'), n=0.256125, w0=(196.794,'kJ/mol'), E0=(98.3971,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012876422862551803, var=2.311827330184622, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R
    Total Standard Deviation in ln(k): 3.080491249786402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R
Total Standard Deviation in ln(k): 3.080491249786402""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R
Total Standard Deviation in ln(k): 3.080491249786402
""",
)

entry(
    index = 371,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl",
    kinetics = ArrheniusBM(A=(4.80846e+06,'m^3/(mol*s)'), n=-0.0785728, w0=(188.117,'kJ/mol'), E0=(24.3308,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08511435749672956, var=4.231710609030121, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl
    Total Standard Deviation in ln(k): 4.337820157814012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl
Total Standard Deviation in ln(k): 4.337820157814012""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl
Total Standard Deviation in ln(k): 4.337820157814012
""",
)

entry(
    index = 372,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl",
    kinetics = ArrheniusBM(A=(619156,'m^3/(mol*s)'), n=0.645957, w0=(213.187,'kJ/mol'), E0=(21.3187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12721342345559444, var=1.019685025685851, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl
    Total Standard Deviation in ln(k): 2.3440022651030223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl
Total Standard Deviation in ln(k): 2.3440022651030223""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl
Total Standard Deviation in ln(k): 2.3440022651030223
""",
)

entry(
    index = 373,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(143715,'m^3/(mol*s)'), n=0.677718, w0=(179,'kJ/mol'), E0=(60.4543,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.250541801165013, var=21.469093355072577, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 17.45608091919987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 17.45608091919987""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 17.45608091919987
""",
)

entry(
    index = 374,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.59527e+14,'m^3/(mol*s)'), n=-2.30738, w0=(179,'kJ/mol'), E0=(89.1164,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 375,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(3.62847e+19,'m^3/(mol*s)'), n=-3.59829, w0=(179,'kJ/mol'), E0=(81.7896,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_Ext-3BrCClINOPSSi-R_N-2R->Br_N-2CNO->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 376,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.39195e+11,'m^3/(mol*s)'), n=-0.855542, w0=(173,'kJ/mol'), E0=(80.042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08362621578487493, var=0.7494705113280606, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.9456546683702245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9456546683702245""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9456546683702245
""",
)

entry(
    index = 377,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(1.20378e+09,'m^3/(mol*s)'), n=-0.813265, w0=(173,'kJ/mol'), E0=(76.4155,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-1BrCNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 378,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(7.14759e+09,'m^3/(mol*s)'), n=-1.3, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12459479191003729, var=4.722672561921672, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 4.669684542985857"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 4.669684542985857""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 4.669684542985857
""",
)

entry(
    index = 379,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_5R!H->O",
    kinetics = ArrheniusBM(A=(2.26848e+08,'m^3/(mol*s)'), n=-0.55, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3562201627384158e-15, var=0.18719384195212602, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_5R!H->O
    Total Standard Deviation in ln(k): 0.8673667472247014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_5R!H->O
Total Standard Deviation in ln(k): 0.8673667472247014""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_5R!H->O
Total Standard Deviation in ln(k): 0.8673667472247014
""",
)

entry(
    index = 380,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(3.25e+08,'m^3/(mol*s)'), n=-0.7, w0=(178.862,'kJ/mol'), E0=(89.4309,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 381,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_2R->C",
    kinetics = ArrheniusBM(A=(3.41902e+08,'m^3/(mol*s)'), n=-0.65, w0=(179.08,'kJ/mol'), E0=(17.908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2939972122180608e-10, var=0.8907254751531062, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_2R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_2R->C
    Total Standard Deviation in ln(k): 1.8920339555642838"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_2R->C
Total Standard Deviation in ln(k): 1.8920339555642838""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_2R->C
Total Standard Deviation in ln(k): 1.8920339555642838
""",
)

entry(
    index = 382,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_N-2R->C",
    kinetics = ArrheniusBM(A=(7.38323e+06,'m^3/(mol*s)'), n=1.0769e-06, w0=(179,'kJ/mol'), E0=(89.0628,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.046794498132223e-09, var=0.3279077147472298, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_N-2R->C
    Total Standard Deviation in ln(k): 1.147976007474636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_N-2R->C
Total Standard Deviation in ln(k): 1.147976007474636""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_N-2R->C
Total Standard Deviation in ln(k): 1.147976007474636
""",
)

entry(
    index = 383,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_5R!H->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=5.25761e-08, w0=(173,'kJ/mol'), E0=(64.0531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_5R!H->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_5R!H->C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_5R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_N-4R!H->C_Ext-2R-R_5R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 384,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(25018.3,'m^3/(mol*s)'), n=0.762967, w0=(173,'kJ/mol'), E0=(57.3292,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_Ext-1BrCNO-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 385,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R_1BrCNO->N",
    kinetics = ArrheniusBM(A=(2.63e+08,'m^3/(mol*s)'), n=-1.1, w0=(83.5,'kJ/mol'), E0=(13.7525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R_1BrCNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R_1BrCNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R_1BrCNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R_1BrCNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 386,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R_N-1BrCNO->N",
    kinetics = ArrheniusBM(A=(1.816e+40,'m^3/(mol*s)'), n=-10.56, w0=(276.766,'kJ/mol'), E0=(189.23,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R_N-1BrCNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R_N-1BrCNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R_N-1BrCNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_N-3BrCClINOPSSi->C_Ext-2R-R_N-2R->O_Ext-2CN-R_N-1BrCNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 387,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.04234e+06,'m^3/(mol*s)'), n=0.213743, w0=(183.281,'kJ/mol'), E0=(79.4146,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0001902170257574481, var=0.06095973871761109, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 0.4954475454031361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.4954475454031361""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.4954475454031361
""",
)

entry(
    index = 388,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_3BrCClINOPSSi-inRing",
    kinetics = ArrheniusBM(A=(5.781e+11,'m^3/(mol*s)'), n=-1.568, w0=(173,'kJ/mol'), E0=(71.0565,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_3BrCClINOPSSi-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_3BrCClINOPSSi-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 389,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_N-3BrCClINOPSSi-inRing",
    kinetics = ArrheniusBM(A=(1.92839e+08,'m^3/(mol*s)'), n=-0.425577, w0=(173,'kJ/mol'), E0=(70.7985,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_N-3BrCClINOPSSi-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_N-3BrCClINOPSSi-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_N-3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_N-Sp-4R!H-3BrCClINOPSSi_N-3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 390,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C_Sp-4C-2R",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(174.548,'kJ/mol'), E0=(87.274,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C_Sp-4C-2R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C_Sp-4C-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C_Sp-4C-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C_Sp-4C-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 391,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C_N-Sp-4C-2R",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(203.312,'kJ/mol'), E0=(101.656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C_N-Sp-4C-2R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C_N-Sp-4C-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C_N-Sp-4C-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->O_N-1BrCNO->N_Ext-2R-R_4R!H->C_N-Sp-4C-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 392,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br_1CN->N",
    kinetics = ArrheniusBM(A=(5.02e+08,'m^3/(mol*s)'), n=-0.429, w0=(134.802,'kJ/mol'), E0=(100.322,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br_1CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br_1CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br_1CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br_1CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 393,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br_N-1CN->N",
    kinetics = ArrheniusBM(A=(1.18079e+09,'m^3/(mol*s)'), n=-0.555622, w0=(184.79,'kJ/mol'), E0=(183.741,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28856613360358296, var=0.17097679400151225, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br_N-1CN->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br_N-1CN->N
    Total Standard Deviation in ln(k): 1.5539852651745698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br_N-1CN->N
Total Standard Deviation in ln(k): 1.5539852651745698""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_3BrCClINOPSSi->C_N-1BrCNO->O_N-2R->O_N-2BrCN->Br_N-1CN->N
Total Standard Deviation in ln(k): 1.5539852651745698
""",
)

entry(
    index = 394,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C",
    kinetics = ArrheniusBM(A=(0.00476602,'m^3/(mol*s)'), n=2.7205, w0=(266.956,'kJ/mol'), E0=(26.6956,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.653197590215836, var=105.3137152547587, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C
    Total Standard Deviation in ln(k): 22.214286681669435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C
Total Standard Deviation in ln(k): 22.214286681669435""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C
Total Standard Deviation in ln(k): 22.214286681669435
""",
)

entry(
    index = 395,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-2C",
    kinetics = ArrheniusBM(A=(1.32819e+27,'m^3/(mol*s)'), n=-6.74987, w0=(286.189,'kJ/mol'), E0=(195.206,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24358966990940747, var=0.15523956227103788, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-2C
    Total Standard Deviation in ln(k): 1.4019090296500178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-2C
Total Standard Deviation in ln(k): 1.4019090296500178""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-2C
Total Standard Deviation in ln(k): 1.4019090296500178
""",
)

entry(
    index = 396,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.83155e+07,'m^3/(mol*s)'), n=0.213711, w0=(205.927,'kJ/mol'), E0=(102.964,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00015371010021244128, var=0.013218501330287211, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.23087408926051417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.23087408926051417""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.23087408926051417
""",
)

entry(
    index = 397,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.888,'kJ/mol'), E0=(102.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 398,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(66.5142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 399,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(76.502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 400,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(3.22741e+07,'m^3/(mol*s)'), n=0.213, w0=(211.537,'kJ/mol'), E0=(157.489,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0022644853453986234, var=7.490440640059255e-07, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
    Total Standard Deviation in ln(k): 0.0074247063908091816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
Total Standard Deviation in ln(k): 0.0074247063908091816""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
Total Standard Deviation in ln(k): 0.0074247063908091816
""",
)

entry(
    index = 401,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(1.13248e+10,'m^3/(mol*s)'), n=-0.605871, w0=(209.896,'kJ/mol'), E0=(99.2182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22335532936049374, var=0.0003995897404736133, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 0.6012684296069748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 0.6012684296069748""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 0.6012684296069748
""",
)

entry(
    index = 402,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.27e+36,'m^3/(mol*s)'), n=-9.86, w0=(283.487,'kJ/mol'), E0=(202.591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 403,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C_Ext-7C-R_Ext-7C-R_Ext-7C-R_9R!H->O",
    kinetics = ArrheniusBM(A=(2.86619e+08,'m^3/(mol*s)'), n=-0.406579, w0=(173,'kJ/mol'), E0=(83.2609,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C_Ext-7C-R_Ext-7C-R_Ext-7C-R_9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C_Ext-7C-R_Ext-7C-R_Ext-7C-R_9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C_Ext-7C-R_Ext-7C-R_Ext-7C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C_Ext-7C-R_Ext-7C-R_Ext-7C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 404,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C_Ext-7C-R_Ext-7C-R_Ext-7C-R_N-9R!H->O",
    kinetics = ArrheniusBM(A=(127888,'m^3/(mol*s)'), n=0.567397, w0=(182.316,'kJ/mol'), E0=(135.252,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C_Ext-7C-R_Ext-7C-R_Ext-7C-R_N-9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C_Ext-7C-R_Ext-7C-R_Ext-7C-R_N-9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C_Ext-7C-R_Ext-7C-R_Ext-7C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->O_N-8BrCClFINPSSi->C_Ext-7C-R_Ext-7C-R_Ext-7C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 405,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(4.46947e+13,'m^3/(mol*s)'), n=-2.00999, w0=(173,'kJ/mol'), E0=(82.3019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 406,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(7.77453e+14,'m^3/(mol*s)'), n=-2.19997, w0=(173,'kJ/mol'), E0=(83.1106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_Sp-4R!H=2CCNNOO_Ext-1BrCNO-R_5R!H->F_Ext-1BrCNO-R_N-6R!H->C_Ext-2CNO-R_Ext-7R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 407,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O",
    kinetics = ArrheniusBM(A=(2.32449e+07,'m^3/(mol*s)'), n=0.379878, w0=(218.923,'kJ/mol'), E0=(156.14,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.45593690905702194, var=3.648482725719283, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O
    Total Standard Deviation in ln(k): 4.9748149701790085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O
Total Standard Deviation in ln(k): 4.9748149701790085""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O
Total Standard Deviation in ln(k): 4.9748149701790085
""",
)

entry(
    index = 408,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(6.15664e+06,'m^3/(mol*s)'), n=0.341139, w0=(182.827,'kJ/mol'), E0=(18.2827,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.422584387282178, var=0.15605293685004343, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 1.8537110633390925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O
Total Standard Deviation in ln(k): 1.8537110633390925""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O
Total Standard Deviation in ln(k): 1.8537110633390925
""",
)

entry(
    index = 409,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C",
    kinetics = ArrheniusBM(A=(1.67818e+08,'m^3/(mol*s)'), n=-0.560015, w0=(173,'kJ/mol'), E0=(77.9979,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07603867106996752, var=1.7959980871282002, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C
    Total Standard Deviation in ln(k): 2.877694707861636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C
Total Standard Deviation in ln(k): 2.877694707861636""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C
Total Standard Deviation in ln(k): 2.877694707861636
""",
)

entry(
    index = 410,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.84859e+06,'m^3/(mol*s)'), n=0.192007, w0=(188.226,'kJ/mol'), E0=(139.223,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 411,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.02037e+09,'m^3/(mol*s)'), n=-0.642574, w0=(194.428,'kJ/mol'), E0=(143.798,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 412,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(5.593e+17,'m^3/(mol*s)'), n=-3.15652, w0=(179,'kJ/mol'), E0=(48.7837,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4409274206007407, var=0.24221013878782702, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 2.0944851871467067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 2.0944851871467067""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 2.0944851871467067
""",
)

entry(
    index = 413,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_6R!H->C",
    kinetics = ArrheniusBM(A=(389.12,'m^3/(mol*s)'), n=1.13144, w0=(201.981,'kJ/mol'), E0=(147.172,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 414,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(277625,'m^3/(mol*s)'), n=-0.327244, w0=(259.438,'kJ/mol'), E0=(199.541,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30866442523833626, var=11.5734004122372, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C
    Total Standard Deviation in ln(k): 7.595587504677689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 7.595587504677689""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 7.595587504677689
""",
)

entry(
    index = 415,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C",
    kinetics = ArrheniusBM(A=(9.21755e-12,'m^3/(mol*s)'), n=4.71074, w0=(239.916,'kJ/mol'), E0=(23.9916,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3586642100319011, var=83.73718451706712, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C
    Total Standard Deviation in ln(k): 19.246100909322426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C
Total Standard Deviation in ln(k): 19.246100909322426""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C
Total Standard Deviation in ln(k): 19.246100909322426
""",
)

entry(
    index = 416,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00383132,'m^3/(mol*s)'), n=2.39773, w0=(221.274,'kJ/mol'), E0=(22.1274,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20179233402612407, var=13.427087771809207, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C
    Total Standard Deviation in ln(k): 7.8529648209756715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 7.8529648209756715""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 7.8529648209756715
""",
)

entry(
    index = 417,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(3.92632e+06,'m^3/(mol*s)'), n=-0.178517, w0=(222.247,'kJ/mol'), E0=(204.153,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8629513207983656, var=3.447500474738627, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 5.89050040953728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 5.89050040953728""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 5.89050040953728
""",
)

entry(
    index = 418,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(5.53171e+09,'m^3/(mol*s)'), n=-0.92153, w0=(179,'kJ/mol'), E0=(35.0894,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13759714402666742, var=4.326678593649991, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 4.515704682583406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 4.515704682583406""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 4.515704682583406
""",
)

entry(
    index = 419,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C_Sp-5C-1BrCNO",
    kinetics = ArrheniusBM(A=(1.32152e+08,'m^3/(mol*s)'), n=-0.0163218, w0=(203.748,'kJ/mol'), E0=(101.874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C_Sp-5C-1BrCNO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C_Sp-5C-1BrCNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C_Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C_Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 420,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C_N-Sp-5C-1BrCNO",
    kinetics = ArrheniusBM(A=(1.8084e+07,'m^3/(mol*s)'), n=0.148656, w0=(234.358,'kJ/mol'), E0=(174.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C_N-Sp-5C-1BrCNO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C_N-Sp-5C-1BrCNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C_N-Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_N-7R!H->C_N-Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 421,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.39084e+11,'m^3/(mol*s)'), n=-1.45358, w0=(173,'kJ/mol'), E0=(85.9904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20548865407396646, var=0.36625241772088707, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.7295446012653048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.7295446012653048""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.7295446012653048
""",
)

entry(
    index = 422,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4437.65,'m^3/(mol*s)'), n=0.940006, w0=(206.719,'kJ/mol'), E0=(20.6719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18527098789369356, var=1.6024207651335087, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 3.003234163414728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 3.003234163414728""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 3.003234163414728
""",
)

entry(
    index = 423,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.64189e+10,'m^3/(mol*s)'), n=-1.09052, w0=(191.184,'kJ/mol'), E0=(146.197,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.36610070628390023, var=2.5588843416481826, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 4.126728131155322"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 4.126728131155322""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 4.126728131155322
""",
)

entry(
    index = 424,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R",
    kinetics = ArrheniusBM(A=(542068,'m^3/(mol*s)'), n=0.666984, w0=(213.751,'kJ/mol'), E0=(21.3751,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.32435980182103324, var=0.48881859155191304, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R
    Total Standard Deviation in ln(k): 2.216596187566236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 2.216596187566236""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 2.216596187566236
""",
)

entry(
    index = 425,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(1.80345e+13,'m^3/(mol*s)'), n=-2.05221, w0=(173,'kJ/mol'), E0=(84.3599,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-1BrCNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 426,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R_Sp-6R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.10694e+07,'m^3/(mol*s)'), n=0.199192, w0=(224.755,'kJ/mol'), E0=(165.22,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R_Sp-6R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R_Sp-6R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R_Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R_Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 427,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R_N-Sp-6R!H-4R!H",
    kinetics = ArrheniusBM(A=(5.80475e+06,'m^3/(mol*s)'), n=0.152054, w0=(179,'kJ/mol'), E0=(60.7945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R_N-Sp-6R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R_N-Sp-6R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R_N-Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_N-2CNO->C_Ext-4R!H-R_Ext-6R!H-R_N-7R!H->O_Ext-1BrCNO-R_N-Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 428,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(6.1576e+11,'m^3/(mol*s)'), n=-0.948728, w0=(173,'kJ/mol'), E0=(81.224,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1BrCNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 429,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(1.24e+10,'m^3/(mol*s)'), n=-1.5, w0=(173,'kJ/mol'), E0=(69.3328,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1BrCNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 430,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(7.75e+08,'m^3/(mol*s)'), n=-0.75, w0=(173,'kJ/mol'), E0=(69.7441,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-1BrCNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 431,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_2R->C_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(4.98065e+08,'m^3/(mol*s)'), n=-0.75, w0=(177.753,'kJ/mol'), E0=(88.8765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09619936845727288, var=0.8575717470917584, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_2R->C_Ext-1BrCNO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_2R->C_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 2.098195278084049"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_2R->C_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 2.098195278084049""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_2R->C_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 2.098195278084049
""",
)

entry(
    index = 432,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_N-2R->C_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(9.04e+06,'m^3/(mol*s)'), n=4.07933e-08, w0=(179,'kJ/mol'), E0=(72.4227,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_N-2R->C_Ext-1BrCNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_N-2R->C_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_N-2R->C_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-1BrCNO-R_3BrCClINOPSSi->C_4R!H->C_Ext-2R-R_5R!H->C_N-2R->C_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 433,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.91473e+06,'m^3/(mol*s)'), n=0.213499, w0=(183.183,'kJ/mol'), E0=(78.8683,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0002843643556459568, var=0.015202055380165683, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.24789153321199428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.24789153321199428""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.24789153321199428
""",
)

entry(
    index = 434,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(3.406e+06,'m^3/(mol*s)'), n=0.211, w0=(183.012,'kJ/mol'), E0=(136.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 435,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00346801,'m^3/(mol*s)'), n=2.7688, w0=(263.003,'kJ/mol'), E0=(26.3003,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7587707250274617, var=108.71031556684093, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R
    Total Standard Deviation in ln(k): 22.808676853788114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R
Total Standard Deviation in ln(k): 22.808676853788114""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R
Total Standard Deviation in ln(k): 22.808676853788114
""",
)

entry(
    index = 436,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.74e+37,'m^3/(mol*s)'), n=-10.5, w0=(277.811,'kJ/mol'), E0=(197.941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 437,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-2C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, w0=(288.403,'kJ/mol'), E0=(209.138,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-2C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-2C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-2C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_N-Sp-4C-2C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 438,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(2.79114e+07,'m^3/(mol*s)'), n=0.21356, w0=(205.917,'kJ/mol'), E0=(102.959,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00020750917090565628, var=0.01529032030782134, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 0.2484149607337448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.2484149607337448""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.2484149607337448
""",
)

entry(
    index = 439,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.888,'kJ/mol'), E0=(102.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 440,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(3.203e+07,'m^3/(mol*s)'), n=0.214, w0=(211.524,'kJ/mol'), E0=(157.481,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 441,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.17785e+10,'m^3/(mol*s)'), n=-0.611491, w0=(227.553,'kJ/mol'), E0=(113.776,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 442,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C",
    kinetics = ArrheniusBM(A=(1.59893e+08,'m^3/(mol*s)'), n=-0.00251802, w0=(218.841,'kJ/mol'), E0=(156.09,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4558687086139027, var=0.9394751407096138, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C
    Total Standard Deviation in ln(k): 3.0885188277291884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C
Total Standard Deviation in ln(k): 3.0885188277291884""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C
Total Standard Deviation in ln(k): 3.0885188277291884
""",
)

entry(
    index = 443,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(490958,'m^3/(mol*s)'), n=1.14475, w0=(219.088,'kJ/mol'), E0=(156.238,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 444,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C",
    kinetics = ArrheniusBM(A=(1.06706e+07,'m^3/(mol*s)'), n=0.222663, w0=(175.492,'kJ/mol'), E0=(87.7462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12379079540963607, var=0.007507979556341192, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C
    Total Standard Deviation in ln(k): 0.4847396333307152"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C
Total Standard Deviation in ln(k): 0.4847396333307152""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C
Total Standard Deviation in ln(k): 0.4847396333307152
""",
)

entry(
    index = 445,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_N-4R!H->C",
    kinetics = ArrheniusBM(A=(7.64581e+08,'m^3/(mol*s)'), n=-0.158759, w0=(197.495,'kJ/mol'), E0=(145.431,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 446,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C_Ext-4C-R_8R!H->O",
    kinetics = ArrheniusBM(A=(2.0472e+13,'m^3/(mol*s)'), n=-2.1772, w0=(173,'kJ/mol'), E0=(65.6017,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C_Ext-4C-R_8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C_Ext-4C-R_8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C_Ext-4C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C_Ext-4C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 447,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C_Ext-4C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(180089,'m^3/(mol*s)'), n=0.450629, w0=(180.788,'kJ/mol'), E0=(133.281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C_Ext-4C-R_N-8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C_Ext-4C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C_Ext-4C-R_N-8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_N-7R!H->O_4R!H->C_Ext-4C-R_N-8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 448,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_Sp-7C-4R!H",
    kinetics = ArrheniusBM(A=(4.33204e+11,'m^3/(mol*s)'), n=-1.10729, w0=(179.281,'kJ/mol'), E0=(89.6405,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_Sp-7C-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_Sp-7C-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_Sp-7C-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_Sp-7C-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 449,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-Sp-7C-4R!H",
    kinetics = ArrheniusBM(A=(7.22101e+23,'m^3/(mol*s)'), n=-5.20574, w0=(179,'kJ/mol'), E0=(7.92692,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-Sp-7C-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-Sp-7C-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-Sp-7C-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-Sp-7C-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 450,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_6FO->O",
    kinetics = ArrheniusBM(A=(0.141937,'m^3/(mol*s)'), n=1.2083, w0=(265.628,'kJ/mol'), E0=(181.021,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_6FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_6FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_6FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_6FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 451,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_N-6FO->O",
    kinetics = ArrheniusBM(A=(0.122385,'m^3/(mol*s)'), n=1.62727, w0=(256.343,'kJ/mol'), E0=(169.396,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40701024171272276, var=3.9504691486879797, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_N-6FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_N-6FO->O
    Total Standard Deviation in ln(k): 5.007207567500679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_N-6FO->O
Total Standard Deviation in ln(k): 5.007207567500679""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_N-6FO->O
Total Standard Deviation in ln(k): 5.007207567500679
""",
)

entry(
    index = 452,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C",
    kinetics = ArrheniusBM(A=(1.27255e+07,'m^3/(mol*s)'), n=0.200075, w0=(187.807,'kJ/mol'), E0=(18.7807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6176630156679969, var=163.21002422592716, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C
    Total Standard Deviation in ln(k): 27.163145221346227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C
Total Standard Deviation in ln(k): 27.163145221346227""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C
Total Standard Deviation in ln(k): 27.163145221346227
""",
)

entry(
    index = 453,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C",
    kinetics = ArrheniusBM(A=(8.27807e-18,'m^3/(mol*s)'), n=6.2143, w0=(257.285,'kJ/mol'), E0=(25.7285,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09599981394349306, var=26.08730386956245, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C
    Total Standard Deviation in ln(k): 10.480536692775221"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C
Total Standard Deviation in ln(k): 10.480536692775221""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C
Total Standard Deviation in ln(k): 10.480536692775221
""",
)

entry(
    index = 454,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R",
    kinetics = ArrheniusBM(A=(2.85706e+07,'m^3/(mol*s)'), n=-0.367494, w0=(210.315,'kJ/mol'), E0=(154.009,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17889909341928814, var=0.02696567863445068, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R
    Total Standard Deviation in ln(k): 0.778697362437623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R
Total Standard Deviation in ln(k): 0.778697362437623""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R
Total Standard Deviation in ln(k): 0.778697362437623
""",
)

entry(
    index = 455,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R",
    kinetics = ArrheniusBM(A=(80115.1,'m^3/(mol*s)'), n=0.326023, w0=(186.829,'kJ/mol'), E0=(18.6829,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03207674917548805, var=4.416177331550232, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R
    Total Standard Deviation in ln(k): 4.293486028647422"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R
Total Standard Deviation in ln(k): 4.293486028647422""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R
Total Standard Deviation in ln(k): 4.293486028647422
""",
)

entry(
    index = 456,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_6FO->O",
    kinetics = ArrheniusBM(A=(1454.87,'m^3/(mol*s)'), n=0.456325, w0=(266.042,'kJ/mol'), E0=(183.959,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_6FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_6FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_6FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_6FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 457,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O",
    kinetics = ArrheniusBM(A=(3.78419e+06,'m^3/(mol*s)'), n=-0.18273, w0=(255.487,'kJ/mol'), E0=(189.197,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2226003853506497, var=6.433192927180804, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O
    Total Standard Deviation in ln(k): 5.644055322217914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O
Total Standard Deviation in ln(k): 5.644055322217914""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O
Total Standard Deviation in ln(k): 5.644055322217914
""",
)

entry(
    index = 458,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C_Sp-5C-1BrCNO",
    kinetics = ArrheniusBM(A=(11871.3,'m^3/(mol*s)'), n=0.590055, w0=(231.206,'kJ/mol'), E0=(167.918,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C_Sp-5C-1BrCNO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C_Sp-5C-1BrCNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C_Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C_Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 459,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C_N-Sp-5C-1BrCNO",
    kinetics = ArrheniusBM(A=(4.97296e+07,'m^3/(mol*s)'), n=-0.541139, w0=(213.289,'kJ/mol'), E0=(106.644,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C_N-Sp-5C-1BrCNO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C_N-Sp-5C-1BrCNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C_N-Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_8R!H->C_N-Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 460,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(7.74786e+13,'m^3/(mol*s)'), n=-2.05942, w0=(179,'kJ/mol'), E0=(88.3615,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18066768939043745, var=3.3185722720078696, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 4.105954564224683"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O
Total Standard Deviation in ln(k): 4.105954564224683""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O
Total Standard Deviation in ln(k): 4.105954564224683
""",
)

entry(
    index = 461,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.29484e+08,'m^3/(mol*s)'), n=-0.542231, w0=(179,'kJ/mol'), E0=(11.6162,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09323379390472047, var=4.4881414181581425, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 4.481333946159539"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O
Total Standard Deviation in ln(k): 4.481333946159539""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O
Total Standard Deviation in ln(k): 4.481333946159539
""",
)

entry(
    index = 462,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H_7R!H->C",
    kinetics = ArrheniusBM(A=(9.33668e+12,'m^3/(mol*s)'), n=-1.82998, w0=(173,'kJ/mol'), E0=(81.1553,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 463,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.11258e+10,'m^3/(mol*s)'), n=-1.07717, w0=(181.651,'kJ/mol'), E0=(90.8255,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 464,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C",
    kinetics = ArrheniusBM(A=(5674.88,'m^3/(mol*s)'), n=0.853744, w0=(206.598,'kJ/mol'), E0=(20.6598,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08684862592921092, var=1.9089270708655988, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C
    Total Standard Deviation in ln(k): 2.988033335719422"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C
Total Standard Deviation in ln(k): 2.988033335719422""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C
Total Standard Deviation in ln(k): 2.988033335719422
""",
)

entry(
    index = 465,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-7R!H->C",
    kinetics = ArrheniusBM(A=(85564.3,'m^3/(mol*s)'), n=0.794442, w0=(207.207,'kJ/mol'), E0=(153.211,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 466,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_5BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.4e+06,'m^3/(mol*s)'), n=0, w0=(178.973,'kJ/mol'), E0=(89.4864,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_5BrClFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_5BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_5BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_5BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 467,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(4.29223e+09,'m^3/(mol*s)'), n=-0.898459, w0=(195.254,'kJ/mol'), E0=(98.2004,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30111127107187524, var=2.497701634940937, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 3.924868067270938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 3.924868067270938""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 3.924868067270938
""",
)

entry(
    index = 468,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_4BrF->Br",
    kinetics = ArrheniusBM(A=(1.53438e+14,'m^3/(mol*s)'), n=-2.29604, w0=(200.993,'kJ/mol'), E0=(159.17,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5694360602228291, var=1.2705019286776806, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_4BrF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_4BrF->Br
    Total Standard Deviation in ln(k): 3.6904119650984097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_4BrF->Br
Total Standard Deviation in ln(k): 3.6904119650984097""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_4BrF->Br
Total Standard Deviation in ln(k): 3.6904119650984097
""",
)

entry(
    index = 469,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br",
    kinetics = ArrheniusBM(A=(2.33726e+10,'m^3/(mol*s)'), n=-0.658161, w0=(220.13,'kJ/mol'), E0=(173.939,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1480640741027007, var=0.693935862777533, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br
    Total Standard Deviation in ln(k): 2.042020996236215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br
Total Standard Deviation in ln(k): 2.042020996236215""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br
Total Standard Deviation in ln(k): 2.042020996236215
""",
)

entry(
    index = 470,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.83408e+06,'m^3/(mol*s)'), n=0.21354, w0=(183.599,'kJ/mol'), E0=(18.3599,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00013833946776604204, var=0.009545124806212434, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.19620850882650892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.19620850882650892""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.19620850882650892
""",
)

entry(
    index = 471,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(1.92552e+06,'m^3/(mol*s)'), n=0.212513, w0=(182.445,'kJ/mol'), E0=(91.2227,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 472,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(71244.8,'m^3/(mol*s)'), n=0.431732, w0=(274.726,'kJ/mol'), E0=(193.206,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 473,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.22587e+08,'m^3/(mol*s)'), n=-0.0152069, w0=(260.072,'kJ/mol'), E0=(119.327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.748819874560249, var=25.914521652838886, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 17.11194867330147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 17.11194867330147""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 17.11194867330147
""",
)

entry(
    index = 474,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.888,'kJ/mol'), E0=(102.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00036890525002828464, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.0009268976131363935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.0009268976131363935""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.0009268976131363935
""",
)

entry(
    index = 475,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.888,'kJ/mol'), E0=(102.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 476,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(4.00279e+08,'m^3/(mol*s)'), n=-0.187532, w0=(218.548,'kJ/mol'), E0=(155.918,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 477,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(6.39094e+07,'m^3/(mol*s)'), n=0.182418, w0=(219.134,'kJ/mol'), E0=(156.265,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_8R!H->O_Ext-8O-R_Ext-9R!H-R_Ext-8O-R_Ext-10R!H-R_Ext-8O-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 478,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C_Ext-4C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.50858e+07,'m^3/(mol*s)'), n=0.160637, w0=(173,'kJ/mol'), E0=(84.8795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C_Ext-4C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C_Ext-4C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C_Ext-4C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C_Ext-4C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 479,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C_Ext-4C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(4.35356e+07,'m^3/(mol*s)'), n=0.0666425, w0=(181.226,'kJ/mol'), E0=(134.461,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C_Ext-4C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C_Ext-4C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C_Ext-4C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C_2CNO->C_Ext-5C-R_7R!H->O_Ext-2C-R_Ext-2C-R_N-8R!H->O_4R!H->C_Ext-4C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 480,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(11.0219,'m^3/(mol*s)'), n=1.16221, w0=(257.309,'kJ/mol'), E0=(176.941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_4R!H->C_N-6R!H->C_N-6FO->O_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-4C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 481,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C_Ext-6C-R_8R!H->O",
    kinetics = ArrheniusBM(A=(74400,'m^3/(mol*s)'), n=0.546769, w0=(219.277,'kJ/mol'), E0=(158.87,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C_Ext-6C-R_8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C_Ext-6C-R_8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 482,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C_Ext-6C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(1.11241e+16,'m^3/(mol*s)'), n=-2.06869, w0=(173,'kJ/mol'), E0=(78.1686,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C_Ext-6C-R_N-8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C_Ext-6C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_Sp-7R!H=6C_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 483,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_7R!H->C",
    kinetics = ArrheniusBM(A=(2842.4,'m^3/(mol*s)'), n=0.906541, w0=(202.697,'kJ/mol'), E0=(148.927,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 484,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C",
    kinetics = ArrheniusBM(A=(5.27538e+06,'m^3/(mol*s)'), n=-0.721173, w0=(268.203,'kJ/mol'), E0=(208.711,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2504168525905014, var=6.810548417232182, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C
    Total Standard Deviation in ln(k): 5.860950706297799"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C
Total Standard Deviation in ln(k): 5.860950706297799""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C
Total Standard Deviation in ln(k): 5.860950706297799
""",
)

entry(
    index = 485,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_9R!H->O",
    kinetics = ArrheniusBM(A=(1.34728e+10,'m^3/(mol*s)'), n=-1.22262, w0=(212.562,'kJ/mol'), E0=(155.378,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 486,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O",
    kinetics = ArrheniusBM(A=(3.67062e+06,'m^3/(mol*s)'), n=-0.0824516, w0=(209.567,'kJ/mol'), E0=(153.552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17862246590330175, var=0.031795519483423164, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O
    Total Standard Deviation in ln(k): 0.8062704549835842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O
Total Standard Deviation in ln(k): 0.8062704549835842""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O
Total Standard Deviation in ln(k): 0.8062704549835842
""",
)

entry(
    index = 487,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.68007e+08,'m^3/(mol*s)'), n=-0.643134, w0=(173,'kJ/mol'), E0=(84.4692,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15950408905465088, var=1.2115179929499227, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 2.607355455196551"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 2.607355455196551""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 2.607355455196551
""",
)

entry(
    index = 488,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(38.2033,'m^3/(mol*s)'), n=1.29518, w0=(204.719,'kJ/mol'), E0=(20.4719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.37607165517066626, var=13.877725030264747, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 8.41310689937398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 8.41310689937398""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 8.41310689937398
""",
)

entry(
    index = 489,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_4FO->O",
    kinetics = ArrheniusBM(A=(781.022,'m^3/(mol*s)'), n=0.566143, w0=(254.574,'kJ/mol'), E0=(177.583,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 490,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O",
    kinetics = ArrheniusBM(A=(12751.5,'m^3/(mol*s)'), n=0.627989, w0=(255.791,'kJ/mol'), E0=(175.202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2573721330414631, var=2.849858633118123, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O
    Total Standard Deviation in ln(k): 4.0309620469503535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O
Total Standard Deviation in ln(k): 4.0309620469503535""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O
Total Standard Deviation in ln(k): 4.0309620469503535
""",
)

entry(
    index = 491,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O_6R!H->C",
    kinetics = ArrheniusBM(A=(1.6581e+13,'m^3/(mol*s)'), n=-1.93086, w0=(179,'kJ/mol'), E0=(89.0175,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 492,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.62037e+14,'m^3/(mol*s)'), n=-2.18799, w0=(179,'kJ/mol'), E0=(87.7055,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_8BrClFINOPSSi->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 493,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H",
    kinetics = ArrheniusBM(A=(75777.1,'m^3/(mol*s)'), n=0.508548, w0=(210.122,'kJ/mol'), E0=(21.0122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009187335424704764, var=5.144187510899786, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H
    Total Standard Deviation in ln(k): 4.569983567679396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H
Total Standard Deviation in ln(k): 4.569983567679396""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H
Total Standard Deviation in ln(k): 4.569983567679396
""",
)

entry(
    index = 494,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H",
    kinetics = ArrheniusBM(A=(2.10465e+15,'m^3/(mol*s)'), n=-2.64379, w0=(179,'kJ/mol'), E0=(32.1593,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.35134617794056355, var=5.893995491999996, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H
    Total Standard Deviation in ln(k): 5.749785425003742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H
Total Standard Deviation in ln(k): 5.749785425003742""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H
Total Standard Deviation in ln(k): 5.749785425003742
""",
)

entry(
    index = 495,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_8R!H->O",
    kinetics = ArrheniusBM(A=(5.66199e+07,'m^3/(mol*s)'), n=-0.275895, w0=(200.733,'kJ/mol'), E0=(149.45,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 496,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(251453,'m^3/(mol*s)'), n=0.376621, w0=(208.552,'kJ/mol'), E0=(177.691,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04970361310757584, var=0.37018495091040976, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 1.344620930427695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O
Total Standard Deviation in ln(k): 1.344620930427695""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O
Total Standard Deviation in ln(k): 1.344620930427695
""",
)

entry(
    index = 497,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_5ClF->Cl",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(180.281,'kJ/mol'), E0=(90.1406,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_5ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_5ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_5ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_5ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 498,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_N-5ClF->Cl",
    kinetics = ArrheniusBM(A=(1.99254e+10,'m^3/(mol*s)'), n=-1.08237, w0=(202.741,'kJ/mol'), E0=(25.6248,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5154054111887338, var=1.1502832924200275, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_N-5ClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_N-5ClF->Cl
    Total Standard Deviation in ln(k): 3.445092114753777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_N-5ClF->Cl
Total Standard Deviation in ln(k): 3.445092114753777""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_N-5ClF->Cl
Total Standard Deviation in ln(k): 3.445092114753777
""",
)

entry(
    index = 499,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_4BrF->Br_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(177.664,'kJ/mol'), E0=(88.8321,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_4BrF->Br_Ext-1BrCNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_4BrF->Br_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_4BrF->Br_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_4BrF->Br_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 500,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(2.15533e+10,'m^3/(mol*s)'), n=-0.646668, w0=(218.691,'kJ/mol'), E0=(178.521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13420903103072734, var=0.7252761720312222, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br_Ext-1BrCNO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 2.0445041149453993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 2.0445041149453993""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 2.0445041149453993
""",
)

entry(
    index = 501,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(2.03116e+06,'m^3/(mol*s)'), n=0.193234, w0=(183.528,'kJ/mol'), E0=(145.665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0693853095667973, var=0.007005448011209662, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.342128376623813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.342128376623813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.342128376623813
""",
)

entry(
    index = 502,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.942e+06,'m^3/(mol*s)'), n=0.212, w0=(183.721,'kJ/mol'), E0=(136.78,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 503,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.52625e+07,'m^3/(mol*s)'), n=0.261644, w0=(236.172,'kJ/mol'), E0=(120.919,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11640500085374506, var=0.03486355421638742, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 0.6667946930503881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 0.6667946930503881""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 0.6667946930503881
""",
)

entry(
    index = 504,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.77e+40,'m^3/(mol*s)'), n=-10.8, w0=(292.431,'kJ/mol'), E0=(207.155,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->F_Sp-4C-2C_Ext-4C-R_N-6R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 505,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.888,'kJ/mol'), E0=(102.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_1BrCClHNO->H_N-2R->O_N-2BrCClHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 506,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_7FO->O",
    kinetics = ArrheniusBM(A=(0.413045,'m^3/(mol*s)'), n=1.07287, w0=(280.484,'kJ/mol'), E0=(189.996,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_7FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_7FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_7FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_7FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 507,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O",
    kinetics = ArrheniusBM(A=(3303.27,'m^3/(mol*s)'), n=0.257119, w0=(265.133,'kJ/mol'), E0=(193.497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31674609539196097, var=5.247559262067128, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O
    Total Standard Deviation in ln(k): 5.3882017095743295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O
Total Standard Deviation in ln(k): 5.3882017095743295""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O
Total Standard Deviation in ln(k): 5.3882017095743295
""",
)

entry(
    index = 508,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_10R!H->O",
    kinetics = ArrheniusBM(A=(7.45304e+06,'m^3/(mol*s)'), n=-0.171776, w0=(208.838,'kJ/mol'), E0=(153.108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_10R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_10R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_10R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_10R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 509,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O",
    kinetics = ArrheniusBM(A=(2.57599e+06,'m^3/(mol*s)'), n=-0.0377895, w0=(209.931,'kJ/mol'), E0=(153.775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17875719170705073, var=0.0034916745760332738, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O
    Total Standard Deviation in ln(k): 0.5675992567431025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O
Total Standard Deviation in ln(k): 0.5675992567431025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O
Total Standard Deviation in ln(k): 0.5675992567431025
""",
)

entry(
    index = 510,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H_8R!H->C",
    kinetics = ArrheniusBM(A=(2.86822e+09,'m^3/(mol*s)'), n=-0.992691, w0=(173,'kJ/mol'), E0=(80.3819,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 511,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-8R!H->C",
    kinetics = ArrheniusBM(A=(9.84107e+06,'m^3/(mol*s)'), n=-0.293577, w0=(177.113,'kJ/mol'), E0=(88.5564,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 512,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-8R!H-R_9R!H->O",
    kinetics = ArrheniusBM(A=(1.66595e+07,'m^3/(mol*s)'), n=-0.290889, w0=(197.529,'kJ/mol'), E0=(146.037,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-8R!H-R_9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-8R!H-R_9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-8R!H-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-8R!H-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 513,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-8R!H-R_N-9R!H->O",
    kinetics = ArrheniusBM(A=(926.405,'m^3/(mol*s)'), n=0.868703, w0=(211.909,'kJ/mol'), E0=(154.312,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-8R!H-R_N-9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-8R!H-R_N-9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-8R!H-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-4FO-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-8R!H-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 514,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O_Ext-5C-R_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(62.2427,'m^3/(mol*s)'), n=1.33303, w0=(256.476,'kJ/mol'), E0=(163.903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28490826011366893, var=8.123677645940152, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O_Ext-5C-R_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O_Ext-5C-R_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 6.4297590427349975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O_Ext-5C-R_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 6.4297590427349975""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O_Ext-5C-R_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 6.4297590427349975
""",
)

entry(
    index = 515,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO",
    kinetics = ArrheniusBM(A=(141.627,'m^3/(mol*s)'), n=1.30317, w0=(214.945,'kJ/mol'), E0=(21.4945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15884201611458648, var=2.066020498437109, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO
    Total Standard Deviation in ln(k): 3.2806382199612902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 3.2806382199612902""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 3.2806382199612902
""",
)

entry(
    index = 516,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_N-Sp-5C-1BrCNO",
    kinetics = ArrheniusBM(A=(1.16067e+13,'m^3/(mol*s)'), n=-1.87531, w0=(195.651,'kJ/mol'), E0=(97.8256,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_N-Sp-5C-1BrCNO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_N-Sp-5C-1BrCNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_N-Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_N-Sp-5C-1BrCNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 517,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H_6R!H->C",
    kinetics = ArrheniusBM(A=(9.88258e+13,'m^3/(mol*s)'), n=-2.32699, w0=(179,'kJ/mol'), E0=(33.2299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 518,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H_N-6R!H->C",
    kinetics = ArrheniusBM(A=(4.48217e+16,'m^3/(mol*s)'), n=-2.96058, w0=(179,'kJ/mol'), E0=(31.0887,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_N-Sp-7C-4R!H_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 519,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(891.31,'m^3/(mol*s)'), n=1.09, w0=(205.647,'kJ/mol'), E0=(89.2952,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09626040852683278, var=0.015744078644659605, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.49340527974759596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.49340527974759596""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.49340527974759596
""",
)

entry(
    index = 520,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_N-5ClF->Cl_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(1.4e+07,'m^3/(mol*s)'), n=0, w0=(180.051,'kJ/mol'), E0=(90.0254,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_N-5ClF->Cl_Ext-1BrCNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_N-5ClF->Cl_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_N-5ClF->Cl_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_4BrCClF->Cl_Ext-2C-R_Ext-2C-R_N-5BrClFINOPSSi->Br_N-5ClF->Cl_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 521,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br_Ext-1BrCNO-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.69632e+07,'m^3/(mol*s)'), n=0.134221, w0=(214.162,'kJ/mol'), E0=(157.923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br_Ext-1BrCNO-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br_Ext-1BrCNO-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br_Ext-1BrCNO-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_N-4R!H->O_N-4BrCClF->Cl_Ext-2C-R_N-4BrF->Br_Ext-1BrCNO-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 522,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.76821e+06,'m^3/(mol*s)'), n=0.213187, w0=(184.052,'kJ/mol'), E0=(92.026,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-Sp-3BrBrBrBrBrCCCCCClClClIIINNNNNOOOOOPPPSSSSiSiSi#1BrBrBrBrBrBrCCCCCCClClClIIINNNNNNOOOOOOPPPSSSSiSiSi_Ext-3BrCClINOPSSi-R_N-Sp-3BrBrBrCCCClClIINNNOOOPPSSSiSi=1BrBrBrBrCCCCClClIINNNNOOOOPPSSSiSi_Ext-2R-R_N-Sp-4R!H=3BrBrCCClClIINNOOPPSSSiSi_Sp-4R!H-3BrCClINOPSSi_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 523,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_4FO->O",
    kinetics = ArrheniusBM(A=(0.306352,'m^3/(mol*s)'), n=1.17601, w0=(259.989,'kJ/mol'), E0=(179.386,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 524,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O",
    kinetics = ArrheniusBM(A=(85730.9,'m^3/(mol*s)'), n=-0.0692218, w0=(266.848,'kJ/mol'), E0=(198.325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3050000611410718, var=5.114649881832767, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O
    Total Standard Deviation in ln(k): 5.300158810686939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O
Total Standard Deviation in ln(k): 5.300158810686939""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O
Total Standard Deviation in ln(k): 5.300158810686939
""",
)

entry(
    index = 525,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_Sp-8R!H-7R!H",
    kinetics = ArrheniusBM(A=(3.77114e+06,'m^3/(mol*s)'), n=-0.0927661, w0=(210.3,'kJ/mol'), E0=(154,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_Sp-8R!H-7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_Sp-8R!H-7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_Sp-8R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_Sp-8R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 526,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_N-Sp-8R!H-7R!H",
    kinetics = ArrheniusBM(A=(1.75959e+06,'m^3/(mol*s)'), n=0.0171875, w0=(209.562,'kJ/mol'), E0=(153.549,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_N-Sp-8R!H-7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_N-Sp-8R!H-7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_N-Sp-8R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_Ext-6FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_N-Sp-8R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 527,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(130719,'m^3/(mol*s)'), n=0.51445, w0=(256.635,'kJ/mol'), E0=(179.122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_N-6R!H->C_N-6FO->O_N-4FO->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 528,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_6R!H->C",
    kinetics = ArrheniusBM(A=(9919.91,'m^3/(mol*s)'), n=0.675528, w0=(215.613,'kJ/mol'), E0=(158.279,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 529,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_N-6R!H->C",
    kinetics = ArrheniusBM(A=(7685.83,'m^3/(mol*s)'), n=0.855654, w0=(214.611,'kJ/mol'), E0=(119.833,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.259770284919825, var=0.10404037696819299, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_N-6R!H->C
    Total Standard Deviation in ln(k): 1.2993222824394568"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_N-6R!H->C
Total Standard Deviation in ln(k): 1.2993222824394568""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_N-6R!H->C
Total Standard Deviation in ln(k): 1.2993222824394568
""",
)

entry(
    index = 530,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R_8BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(9705.04,'m^3/(mol*s)'), n=0.74494, w0=(200.086,'kJ/mol'), E0=(100.043,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R_8BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R_8BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R_8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R_8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 531,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R_N-8BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(57189.5,'m^3/(mol*s)'), n=0.620146, w0=(211.207,'kJ/mol'), E0=(155.468,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R_N-8BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R_N-8BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R_N-8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_N-5R!H->C_2CNO->C_4R!H->O_Ext-4O-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_7R!H->C_Ext-7C-R_N-8R!H->O_Ext-7C-R_Ext-7C-R_Ext-6R!H-R_N-8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 532,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O_Ext-6C-R_Ext-6C-R",
    kinetics = ArrheniusBM(A=(313.963,'m^3/(mol*s)'), n=0.694173, w0=(261.224,'kJ/mol'), E0=(185.037,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3497432570621352, var=2.869706724707405, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O_Ext-6C-R_Ext-6C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O_Ext-6C-R_Ext-6C-R
    Total Standard Deviation in ln(k): 4.274814971981449"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 4.274814971981449""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 4.274814971981449
""",
)

entry(
    index = 533,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_N-6R!H->C_Ext-1BrCNO-R",
    kinetics = ArrheniusBM(A=(218671,'m^3/(mol*s)'), n=0.432585, w0=(213.076,'kJ/mol'), E0=(157.29,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_N-6R!H->C_Ext-1BrCNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_N-6R!H->C_Ext-1BrCNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_N-6R!H->C_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_N-2CNO->C_Ext-5C-R_Ext-4R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C_N-8BrClFINOPSSi->O_Sp-7C-4R!H_Sp-5C-1BrCNO_N-6R!H->C_Ext-1BrCNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 534,
    label = "Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O_Ext-6C-R_Ext-6C-R_Ext-5C-R_Ext-5C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(44.3716,'m^3/(mol*s)'), n=1.03011, w0=(263.137,'kJ/mol'), E0=(181.579,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O_Ext-6C-R_Ext-6C-R_Ext-5C-R_Ext-5C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O_Ext-6C-R_Ext-6C-R_Ext-5C-R_Ext-5C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O_Ext-6C-R_Ext-6C-R_Ext-5C-R_Ext-5C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->F_N-1BrCClHNOS->S_N-1BrCClHNO->H_N-1BrCClNO->Cl_Ext-1BrCNO-R_3R!H->F_N-2R->Br_Ext-2CNO-R_N-Sp-4R!H=2CCNNOO_4R!H-u0_Ext-1BrCNO-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C_2CNO->C_N-4R!H->C_6R!H->C_Ext-6C-R_N-Sp-7R!H=6C_N-7R!H->C_N-7FO->O_N-4FO->O_Ext-6C-R_Ext-6C-R_Ext-5C-R_Ext-5C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

