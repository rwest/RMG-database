#!/usr/bin/env python
# encoding: utf-8

name = "Lactone_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.46777e+09,'s^-1'), n=1.13725, w0=(933.5,'kJ/mol'), E0=(138.317,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12324515815024707, var=8.659678693840467, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 6.209061673375274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 6.209061673375274""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 6.209061673375274
""",
)

entry(
    index = 2,
    label = "Root_Ext-3C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(1.97606e+14,'s^-1'), n=-0.206666, w0=(933.5,'kJ/mol'), E0=(140.966,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29093603314774896, var=3.5250112642600393, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3C-R_7R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3C-R_7R!H->O
    Total Standard Deviation in ln(k): 4.494887843000792"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3C-R_7R!H->O
Total Standard Deviation in ln(k): 4.494887843000792""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3C-R_7R!H->O
Total Standard Deviation in ln(k): 4.494887843000792
""",
)

entry(
    index = 3,
    label = "Root_Ext-3C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(4.90633e+12,'s^-1'), n=0.146438, w0=(933.5,'kJ/mol'), E0=(154.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19191950144071035, var=10.119420777467154, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3C-R_N-7R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 6.859479983439603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3C-R_N-7R!H->O
Total Standard Deviation in ln(k): 6.859479983439603""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3C-R_N-7R!H->O
Total Standard Deviation in ln(k): 6.859479983439603
""",
)

entry(
    index = 4,
    label = "Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(2.07046e+15,'s^-1'), n=-0.52, w0=(933.5,'kJ/mol'), E0=(147.81,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2887201774172706, var=4.0581280935656485, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 4.763925515556031"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C
Total Standard Deviation in ln(k): 4.763925515556031""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C
Total Standard Deviation in ln(k): 4.763925515556031
""",
)

entry(
    index = 5,
    label = "Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(1.8e+12,'s^-1'), n=0.42, w0=(933.5,'kJ/mol'), E0=(127.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(6.4337e+09,'s^-1'), n=1.0211, w0=(933.5,'kJ/mol'), E0=(158.872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1667551952002459, var=5.298095833126881, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 5.0334004926470515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C
Total Standard Deviation in ln(k): 5.0334004926470515""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C
Total Standard Deviation in ln(k): 5.0334004926470515
""",
)

entry(
    index = 7,
    label = "Root_Ext-3C-R_N-7R!H->O_N-7BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.19e+11,'s^-1'), n=0.34, w0=(933.5,'kJ/mol'), E0=(115.347,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-7R!H->O_N-7BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_N-7BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_N-7BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_N-7BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(7.78e+15,'s^-1'), n=-0.84, w0=(933.5,'kJ/mol'), E0=(133.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(5.51e+14,'s^-1'), n=-0.2, w0=(933.5,'kJ/mol'), E0=(161.772,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_7R!H->O_Ext-7O-R_Ext-8R!H-R_Ext-8R!H-R_Ext-8R!H-R_Ext-9R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(8.47246e+08,'s^-1'), n=1.14859, w0=(933.5,'kJ/mol'), E0=(141.027,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16138661830925283, var=1.533747576877891, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.8882494104734158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.8882494104734158""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.8882494104734158
""",
)

entry(
    index = 11,
    label = "Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2.22e+11,'s^-1'), n=0.83, w0=(933.5,'kJ/mol'), E0=(193.263,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(3.66e+07,'s^-1'), n=1.61, w0=(933.5,'kJ/mol'), E0=(137.287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(5.3e+09,'s^-1'), n=0.85, w0=(933.5,'kJ/mol'), E0=(143.216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_N-7R!H->O_7BrCClFINPSSi->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

