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
    kinetics = ArrheniusBM(A=(1.31612e-49,'m^3/(mol*s)'), n=15.8276, w0=(825.643,'kJ/mol'), E0=(196.172,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5466747306268277, var=52.20812903668609, Tref=1000.0, N=14, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 14 training reactions at node Root
    Total Standard Deviation in ln(k): 15.85880657629542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 15.85880657629542""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 15.85880657629542
""",
)

entry(
    index = 2,
    label = "Root_5R->C",
    kinetics = ArrheniusBM(A=(7.3e-05,'m^3/(mol*s)'), n=3.13, w0=(745.5,'kJ/mol'), E0=(460.067,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->C
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
    kinetics = ArrheniusBM(A=(1.24627e-49,'m^3/(mol*s)'), n=15.8344, w0=(831.808,'kJ/mol'), E0=(196.032,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5459374163510355, var=52.08449070887143, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-5R->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-5R->C
    Total Standard Deviation in ln(k): 15.839792007925164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-5R->C
Total Standard Deviation in ln(k): 15.839792007925164""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-5R->C
Total Standard Deviation in ln(k): 15.839792007925164
""",
)

entry(
    index = 4,
    label = "Root_N-5R->C_Ext-4R-R",
    kinetics = ArrheniusBM(A=(2.51446e-51,'m^3/(mol*s)'), n=16.3088, w0=(828.5,'kJ/mol'), E0=(192.18,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5815693285778208, var=53.826343699507646, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-5R->C_Ext-4R-R
    Total Standard Deviation in ln(k): 16.169256843295923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-5R->C_Ext-4R-R
Total Standard Deviation in ln(k): 16.169256843295923""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-5R->C_Ext-4R-R
Total Standard Deviation in ln(k): 16.169256843295923
""",
)

entry(
    index = 5,
    label = "Root_N-5R->C_4R->C",
    kinetics = ArrheniusBM(A=(0.00453,'m^3/(mol*s)'), n=2.83, w0=(828.5,'kJ/mol'), E0=(313.018,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-5R->C_N-4R->C",
    kinetics = ArrheniusBM(A=(1510,'m^3/(mol*s)'), n=1.23, w0=(871.5,'kJ/mol'), E0=(301.639,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-5R->C_Ext-4R-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.43704e-42,'m^3/(mol*s)'), n=14.2172, w0=(828.5,'kJ/mol'), E0=(204.525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6576773304206417, var=0.2537607453920134, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O
    Total Standard Deviation in ln(k): 2.6623342988680996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O
Total Standard Deviation in ln(k): 2.6623342988680996""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O
Total Standard Deviation in ln(k): 2.6623342988680996
""",
)

entry(
    index = 8,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(2.45792e-51,'m^3/(mol*s)'), n=16.1135, w0=(828.5,'kJ/mol'), E0=(196.589,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4102724092738063, var=72.38368488900359, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O
    Total Standard Deviation in ln(k): 18.086840941078375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O
Total Standard Deviation in ln(k): 18.086840941078375""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O
Total Standard Deviation in ln(k): 18.086840941078375
""",
)

entry(
    index = 9,
    label = "Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(6.89256e-41,'m^3/(mol*s)'), n=13.6746, w0=(828.5,'kJ/mol'), E0=(204.405,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6862868745850521, var=0.32368499779072174, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 2.8648992442647296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 2.8648992442647296""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 2.8648992442647296
""",
)

entry(
    index = 10,
    label = "Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(6.53205e-46,'m^3/(mol*s)'), n=15.297, w0=(828.5,'kJ/mol'), E0=(204.813,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_6BrBrCCClClFFIINNPPSSSiSi-u1",
    kinetics = ArrheniusBM(A=(2.42175e-14,'m^3/(mol*s)'), n=4.70665, w0=(828.5,'kJ/mol'), E0=(137.124,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_6BrBrCCClClFFIINNPPSSSiSi-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_6BrBrCCClClFFIINNPPSSSiSi-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_6BrBrCCClClFFIINNPPSSSiSi-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_6BrBrCCClClFFIINNPPSSSiSi-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1",
    kinetics = ArrheniusBM(A=(9.6449e-59,'m^3/(mol*s)'), n=18.3873, w0=(828.5,'kJ/mol'), E0=(206.561,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40388009691612303, var=21.563746007475604, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1',), comment="""BM rule fitted to 7 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1
    Total Standard Deviation in ln(k): 10.32411842568112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1
Total Standard Deviation in ln(k): 10.32411842568112""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1
Total Standard Deviation in ln(k): 10.32411842568112
""",
)

entry(
    index = 13,
    label = "Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.19876e-39,'m^3/(mol*s)'), n=13.3095, w0=(828.5,'kJ/mol'), E0=(205.515,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(3.96304e-42,'m^3/(mol*s)'), n=14.0396, w0=(828.5,'kJ/mol'), E0=(203.295,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F",
    kinetics = ArrheniusBM(A=(7.53332e-62,'m^3/(mol*s)'), n=19.2674, w0=(828.5,'kJ/mol'), E0=(201.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4789990201906329, var=19.654840087052047, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F
    Total Standard Deviation in ln(k): 10.091263422749917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F
Total Standard Deviation in ln(k): 10.091263422749917""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F
Total Standard Deviation in ln(k): 10.091263422749917
""",
)

entry(
    index = 16,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_N-6BrCClFINPSSi->F",
    kinetics = ArrheniusBM(A=(0.0352626,'m^3/(mol*s)'), n=2.34043, w0=(828.5,'kJ/mol'), E0=(309.89,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3856732288912227, var=3.3416351026023525, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_N-6BrCClFINPSSi->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_N-6BrCClFINPSSi->F
    Total Standard Deviation in ln(k): 4.633711956321281"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_N-6BrCClFINPSSi->F
Total Standard Deviation in ln(k): 4.633711956321281""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_N-6BrCClFINPSSi->F
Total Standard Deviation in ln(k): 4.633711956321281
""",
)

entry(
    index = 17,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.54749e-61,'m^3/(mol*s)'), n=18.9735, w0=(828.5,'kJ/mol'), E0=(203.521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4528008633840073, var=22.476133691453306, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C
    Total Standard Deviation in ln(k): 10.641939326300951"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C
Total Standard Deviation in ln(k): 10.641939326300951""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C
Total Standard Deviation in ln(k): 10.641939326300951
""",
)

entry(
    index = 18,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.68462e-61,'m^3/(mol*s)'), n=19.4743, w0=(828.5,'kJ/mol'), E0=(200.137,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_N-6BrCClFINPSSi->F_Ext-4R-R",
    kinetics = ArrheniusBM(A=(0.106,'m^3/(mol*s)'), n=2.13, w0=(828.5,'kJ/mol'), E0=(312.367,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_N-6BrCClFINPSSi->F_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_N-6BrCClFINPSSi->F_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_N-6BrCClFINPSSi->F_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_N-6BrCClFINPSSi->F_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_8R!H-u1",
    kinetics = ArrheniusBM(A=(6.50208e-61,'m^3/(mol*s)'), n=18.4201, w0=(828.5,'kJ/mol'), E0=(217.337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_8R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_8R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_8R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_8R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1",
    kinetics = ArrheniusBM(A=(1.52575e-58,'m^3/(mol*s)'), n=18.3783, w0=(828.5,'kJ/mol'), E0=(205.718,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43276928274968585, var=5.020720204078667, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1
    Total Standard Deviation in ln(k): 5.579362609382798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1
Total Standard Deviation in ln(k): 5.579362609382798""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1
Total Standard Deviation in ln(k): 5.579362609382798
""",
)

entry(
    index = 22,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C",
    kinetics = ArrheniusBM(A=(2.43299e-57,'m^3/(mol*s)'), n=18.0466, w0=(828.5,'kJ/mol'), E0=(202.584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3956984006482632, var=1.6673563187876537, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C
    Total Standard Deviation in ln(k): 3.582854354756594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C
Total Standard Deviation in ln(k): 3.582854354756594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C
Total Standard Deviation in ln(k): 3.582854354756594
""",
)

entry(
    index = 23,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_N-8R!H->C",
    kinetics = ArrheniusBM(A=(5.93638e-58,'m^3/(mol*s)'), n=18.1836, w0=(828.5,'kJ/mol'), E0=(219.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(2.45776e-58,'m^3/(mol*s)'), n=18.2371, w0=(828.5,'kJ/mol'), E0=(197.839,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(1.5224e-56,'m^3/(mol*s)'), n=17.9131, w0=(828.5,'kJ/mol'), E0=(206.846,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_Ext-4R-R_N-6R!H->O_N-6BrBrCCClClFFIINNPPSSSiSi-u1_6BrCClFINPSSi->F_Ext-4R-R_7R!H->C_Ext-7C-R_N-8R!H-u1_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

