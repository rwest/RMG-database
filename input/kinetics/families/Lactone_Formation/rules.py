#!/usr/bin/env python
# encoding: utf-8

name = "Lactone_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.53365e-25,'s^-1'), n=10.7308, w0=(896.536,'kJ/mol'), E0=(-4.62927,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.39045851935123, var=22.286803352081897, Tref=1000.0, N=14, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 14 training reactions at node Root
    Total Standard Deviation in ln(k): 12.957748353577498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 12.957748353577498""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 12.957748353577498
""",
)

entry(
    index = 2,
    label = "Root_6F1sH->F1s",
    kinetics = ArrheniusBM(A=(7.09217e+10,'s^-1'), n=0.686678, w0=(933.5,'kJ/mol'), E0=(134.823,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03143203692082163, var=9.067063741197403, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_6F1sH->F1s',), comment="""BM rule fitted to 9 training reactions at node Root_6F1sH->F1s
    Total Standard Deviation in ln(k): 6.115546117323314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_6F1sH->F1s
Total Standard Deviation in ln(k): 6.115546117323314""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_6F1sH->F1s
Total Standard Deviation in ln(k): 6.115546117323314
""",
)

entry(
    index = 3,
    label = "Root_N-6F1sH->F1s",
    kinetics = ArrheniusBM(A=(3.32126e-36,'s^-1'), n=13.85, w0=(830,'kJ/mol'), E0=(42.147,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.4030399281588446, var=44.34291538101973, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-6F1sH->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
    Total Standard Deviation in ln(k): 19.3874151365015"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
Total Standard Deviation in ln(k): 19.3874151365015""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
Total Standard Deviation in ln(k): 19.3874151365015
""",
)

entry(
    index = 4,
    label = "Root_6F1sH->F1s_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.87738e+10,'s^-1'), n=0.705078, w0=(933.5,'kJ/mol'), E0=(135.749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06875851324047871, var=10.668488082789208, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R',), comment="""BM rule fitted to 8 training reactions at node Root_6F1sH->F1s_Ext-3C-R
    Total Standard Deviation in ln(k): 6.7207564179619395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 6.7207564179619395""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 6.7207564179619395
""",
)

entry(
    index = 5,
    label = "Root_N-6F1sH->F1s_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.33812e-31,'s^-1'), n=12.388, w0=(830,'kJ/mol'), E0=(45.4647,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.4466977417075633, var=42.00044995780009, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
    Total Standard Deviation in ln(k): 19.13971956286603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 19.13971956286603""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 19.13971956286603
""",
)

entry(
    index = 6,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F",
    kinetics = ArrheniusBM(A=(4.90633e+12,'s^-1'), n=0.146438, w0=(933.5,'kJ/mol'), E0=(154.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19191950144071035, var=10.119420777467154, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
    Total Standard Deviation in ln(k): 6.859479983439603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
Total Standard Deviation in ln(k): 6.859479983439603""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
Total Standard Deviation in ln(k): 6.859479983439603
""",
)

entry(
    index = 7,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(1.3018e+17,'s^-1'), n=-1.06577, w0=(933.5,'kJ/mol'), E0=(138.296,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11864572597553953, var=5.55568418815028, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
    Total Standard Deviation in ln(k): 5.023365434572153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
Total Standard Deviation in ln(k): 5.023365434572153""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
Total Standard Deviation in ln(k): 5.023365434572153
""",
)

entry(
    index = 8,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.28596e+06,'s^-1'), n=1.585, w0=(830,'kJ/mol'), E0=(140.485,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4471904219735872, var=0.05056130323399081, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 4.086938375247346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.086938375247346""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.086938375247346
""",
)

entry(
    index = 9,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(26400,'s^-1'), n=2.44, w0=(830,'kJ/mol'), E0=(222.711,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(6.4337e+09,'s^-1'), n=1.0211, w0=(933.5,'kJ/mol'), E0=(158.872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1667551890719914, var=5.298095786199258, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
    Total Standard Deviation in ln(k): 5.033400456813439"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 5.033400456813439""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 5.033400456813439
""",
)

entry(
    index = 11,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(3.19e+11,'s^-1'), n=0.34, w0=(933.5,'kJ/mol'), E0=(115.347,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.97606e+14,'s^-1'), n=-0.206666, w0=(933.5,'kJ/mol'), E0=(140.966,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29093603314774896, var=3.5250112642600393, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 4.494887843000792"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 4.494887843000792""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 4.494887843000792
""",
)

entry(
    index = 13,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.17e+07,'s^-1'), n=1.55, w0=(830,'kJ/mol'), E0=(139.603,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(8.47245e+08,'s^-1'), n=1.14859, w0=(933.5,'kJ/mol'), E0=(141.027,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16138661830925283, var=1.533747576877891, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 2.8882494104734158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 2.8882494104734158""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 2.8882494104734158
""",
)

entry(
    index = 15,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.22e+11,'s^-1'), n=0.83, w0=(933.5,'kJ/mol'), E0=(193.263,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C",
    kinetics = ArrheniusBM(A=(2.07046e+15,'s^-1'), n=-0.52, w0=(933.5,'kJ/mol'), E0=(147.81,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2887201774172706, var=4.0581280935656485, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
    Total Standard Deviation in ln(k): 4.763925515556031"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 4.763925515556031""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 4.763925515556031
""",
)

entry(
    index = 17,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(1.8e+12,'s^-1'), n=0.42, w0=(933.5,'kJ/mol'), E0=(127.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(3.66e+07,'s^-1'), n=1.61, w0=(933.5,'kJ/mol'), E0=(137.287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(5.3e+09,'s^-1'), n=0.85, w0=(933.5,'kJ/mol'), E0=(143.216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(7.78e+15,'s^-1'), n=-0.84, w0=(933.5,'kJ/mol'), E0=(133.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(5.51e+14,'s^-1'), n=-0.2, w0=(933.5,'kJ/mol'), E0=(161.772,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

