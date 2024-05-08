#!/usr/bin/env python
# encoding: utf-8

name = "Singlet_Carbene_Intra_Disproportionation/rules"
shortDesc = "Convert a singlet carbene to a closed-shell molecule through a concerted 1,2-H shift + 1,2-bond formation"
longDesc = """
Reaction site *1 should always be a singlet in this family.
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.92661e+11,'s^-1'), n=0.204614, w0=(561.2,'kJ/mol'), E0=(240.356,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6201298929491859, var=222.8563075233871, Tref=1000.0, N=10, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 10 training reactions at node Root
    Total Standard Deviation in ln(k): 33.99811025808797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root
Total Standard Deviation in ln(k): 33.99811025808797""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root
Total Standard Deviation in ln(k): 33.99811025808797
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(1.63761e+17,'s^-1'), n=-1.46865, w0=(539,'kJ/mol'), E0=(113.319,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4939511260774467, var=15.669273958062641, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 9.176713518352656"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 9.176713518352656""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 9.176713518352656
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(0.00660817,'s^-1'), n=4.20908, w0=(613,'kJ/mol'), E0=(247.136,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06259186006358099, var=131.86650097204395, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 23.178268408551176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 23.178268408551176""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 23.178268408551176
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_4R!H->Br",
    kinetics = ArrheniusBM(A=(5e+12,'s^-1'), n=4.22455e-09, w0=(539,'kJ/mol'), E0=(101.409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_4R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_4R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(1.61075e+17,'s^-1'), n=-1.46796, w0=(539,'kJ/mol'), E0=(113.263,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5314684430102796, var=16.185369680971416, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br
    Total Standard Deviation in ln(k): 9.400606523810508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br
Total Standard Deviation in ln(k): 9.400606523810508""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br
Total Standard Deviation in ln(k): 9.400606523810508
""",
)

entry(
    index = 6,
    label = "Root_N-2Br1sCl1sF1sH->H_Ext-3C-R_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(2.89e+09,'s^-1'), n=0.81, w0=(613,'kJ/mol'), E0=(308.683,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_Ext-3C-R_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_Ext-3C-R_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_Ext-3C-R_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_Ext-3C-R_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-2Br1sCl1sF1sH->H_Ext-3C-R_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(8.03543e+09,'s^-1'), n=0.810086, w0=(613,'kJ/mol'), E0=(247.431,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.075988800153154, var=35.134796762848474, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_Ext-3C-R_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_Ext-3C-R_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 22.12416735943905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_Ext-3C-R_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 22.12416735943905""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_Ext-3C-R_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 22.12416735943905
""",
)

entry(
    index = 8,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(3.33333e+12,'s^-1'), n=-5.49881e-09, w0=(539,'kJ/mol'), E0=(148.602,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(2.04679e+17,'s^-1'), n=-1.49877, w0=(539,'kJ/mol'), E0=(113.179,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5003116698842066, var=16.093728851325515, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F',), comment="""BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F
    Total Standard Deviation in ln(k): 9.29945819862672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F
Total Standard Deviation in ln(k): 9.29945819862672""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F
Total Standard Deviation in ln(k): 9.29945819862672
""",
)

entry(
    index = 10,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing",
    kinetics = ArrheniusBM(A=(2.60686e+17,'s^-1'), n=-1.52988, w0=(539,'kJ/mol'), E0=(113.256,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.48966038971723974, var=16.231730917401148, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing
    Total Standard Deviation in ln(k): 9.30710393340717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing
Total Standard Deviation in ln(k): 9.30710393340717""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing
Total Standard Deviation in ln(k): 9.30710393340717
""",
)

entry(
    index = 11,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing",
    kinetics = ArrheniusBM(A=(3.33333e+12,'s^-1'), n=8.2394e-08, w0=(539,'kJ/mol'), E0=(130.615,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(2.16138e+20,'s^-1'), n=-2.10785, w0=(539,'kJ/mol'), E0=(144.984,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6086442714880358, var=5.8188942736807565, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 6.365155971875667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 6.365155971875667""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 6.365155971875667
""",
)

entry(
    index = 13,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(7.26313e-09,'s^-1'), n=5.53373, w0=(539,'kJ/mol'), E0=(4.64464,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5252400515168253, var=52.08222104918007, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 15.787473340914593"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 15.787473340914593""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 15.787473340914593
""",
)

entry(
    index = 14,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(8.067e+10,'s^-1'), n=0.649, w0=(539,'kJ/mol'), E0=(122.998,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl",
    kinetics = ArrheniusBM(A=(1.61832e+16,'s^-1'), n=-0.885455, w0=(539,'kJ/mol'), E0=(106.175,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl",
    kinetics = ArrheniusBM(A=(4.66894e+13,'s^-1'), n=-1.27142, w0=(539,'kJ/mol'), E0=(76.0866,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

