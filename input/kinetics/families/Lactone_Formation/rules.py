#!/usr/bin/env python
# encoding: utf-8

name = "Lactone_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(5.52667e+21,'s^-1'), n=-2.50656, w0=(903.059,'kJ/mol'), E0=(156.48,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4883561437622537, var=36.33335450910224, Tref=1000.0, N=17, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 17 training reactions at node Root
    Total Standard Deviation in ln(k): 13.310998246134611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 13.310998246134611""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 13.310998246134611
""",
)

entry(
    index = 2,
    label = "Root_6F1sH->F1s",
    kinetics = ArrheniusBM(A=(1.66338e+33,'s^-1'), n=-5.77943, w0=(933.5,'kJ/mol'), E0=(180.954,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7365847853194132, var=23.93243541328722, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_6F1sH->F1s',), comment="""BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
    Total Standard Deviation in ln(k): 11.658037600410212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
Total Standard Deviation in ln(k): 11.658037600410212""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
Total Standard Deviation in ln(k): 11.658037600410212
""",
)

entry(
    index = 3,
    label = "Root_N-6F1sH->F1s",
    kinetics = ArrheniusBM(A=(1.02399e+31,'s^-1'), n=-5.20005, w0=(830,'kJ/mol'), E0=(201.37,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1575075501979748, var=121.2279004227387, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-6F1sH->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
    Total Standard Deviation in ln(k): 24.981153780946922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
Total Standard Deviation in ln(k): 24.981153780946922""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
Total Standard Deviation in ln(k): 24.981153780946922
""",
)

entry(
    index = 4,
    label = "Root_6F1sH->F1s_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.01209e+34,'s^-1'), n=-6.08418, w0=(933.5,'kJ/mol'), E0=(183.365,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7515706963454412, var=26.63341221003022, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R',), comment="""BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
    Total Standard Deviation in ln(k): 12.23431905046623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 12.23431905046623""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 12.23431905046623
""",
)

entry(
    index = 5,
    label = "Root_N-6F1sH->F1s_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.62776e+13,'s^-1'), n=-0.129257, w0=(830,'kJ/mol'), E0=(48.6581,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.31029594752371215, var=19.321435940869822, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
    Total Standard Deviation in ln(k): 9.59168271098696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 9.59168271098696""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 9.59168271098696
""",
)

entry(
    index = 6,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F",
    kinetics = ArrheniusBM(A=(2.22707e+12,'s^-1'), n=0.153066, w0=(933.5,'kJ/mol'), E0=(140.535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4047515370289699, var=2.223344091328114, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
    Total Standard Deviation in ln(k): 4.006200526734331"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
Total Standard Deviation in ln(k): 4.006200526734331""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
Total Standard Deviation in ln(k): 4.006200526734331
""",
)

entry(
    index = 7,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(2.53936e+53,'s^-1'), n=-11.4634, w0=(933.5,'kJ/mol'), E0=(207.012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7243484799348991, var=66.58113892913723, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
    Total Standard Deviation in ln(k): 18.178061283276364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
Total Standard Deviation in ln(k): 18.178061283276364""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
Total Standard Deviation in ln(k): 18.178061283276364
""",
)

entry(
    index = 8,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.62372e+23,'s^-1'), n=-3.06876, w0=(830,'kJ/mol'), E0=(56.1398,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13124447713284335, var=0.05760902517956809, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.8109341038402156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.8109341038402156""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.8109341038402156
""",
)

entry(
    index = 9,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(19200.7,'s^-1'), n=2.47962, w0=(830,'kJ/mol'), E0=(89.4078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
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
    kinetics = ArrheniusBM(A=(2.92778e+11,'s^-1'), n=0.414686, w0=(933.5,'kJ/mol'), E0=(141.825,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4416677090460515, var=0.9456242263097355, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
    Total Standard Deviation in ln(k): 3.059186641523265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 3.059186641523265""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 3.059186641523265
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
    kinetics = ArrheniusBM(A=(3.46017e+15,'s^-1'), n=-0.562889, w0=(933.5,'kJ/mol'), E0=(137.357,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28615640417524235, var=5.281222496048584, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 5.326049688697035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 5.326049688697035""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 5.326049688697035
""",
)

entry(
    index = 13,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(4.16138e+23,'s^-1'), n=-3.19211, w0=(830,'kJ/mol'), E0=(55.0422,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
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
    kinetics = ArrheniusBM(A=(1.94789e+11,'s^-1'), n=0.477128, w0=(933.5,'kJ/mol'), E0=(139.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48744150394561675, var=0.8574591397903147, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 3.081093827748556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 3.081093827748556""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 3.081093827748556
""",
)

entry(
    index = 15,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(4.465e+10,'s^-1'), n=0.59, w0=(933.5,'kJ/mol'), E0=(146.646,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
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
    kinetics = ArrheniusBM(A=(2.51191e+15,'s^-1'), n=-0.54405, w0=(933.5,'kJ/mol'), E0=(143.518,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29711920535730707, var=0.09231132949195588, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
    Total Standard Deviation in ln(k): 1.3556249064257007"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 1.3556249064257007""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 1.3556249064257007
""",
)

entry(
    index = 17,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(1.8e+12,'s^-1'), n=0.42, w0=(933.5,'kJ/mol'), E0=(115.08,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
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
    kinetics = ArrheniusBM(A=(7.67811e+10,'s^-1'), n=0.61187, w0=(933.5,'kJ/mol'), E0=(136.938,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.564092017796201, var=0.46888700659853527, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 2.790065477328175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 2.790065477328175""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 2.790065477328175
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
    kinetics = ArrheniusBM(A=(7.78e+15,'s^-1'), n=-0.84, w0=(933.5,'kJ/mol'), E0=(136.001,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
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
    kinetics = ArrheniusBM(A=(5.51e+14,'s^-1'), n=-0.2, w0=(933.5,'kJ/mol'), E0=(150.683,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
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

entry(
    index = 22,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(3.77795e+11,'s^-1'), n=0.398136, w0=(933.5,'kJ/mol'), E0=(135.689,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6695154483129632, var=0.5131215304289671, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 3.118241507899819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 3.118241507899819""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 3.118241507899819
""",
)

entry(
    index = 23,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(3.66e+07,'s^-1'), n=1.61, w0=(933.5,'kJ/mol'), E0=(137.287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C",
    kinetics = ArrheniusBM(A=(1.4948e+11,'s^-1'), n=0.513313, w0=(933.5,'kJ/mol'), E0=(131.681,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8508919403261304, var=0.9936358957726661, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
    Total Standard Deviation in ln(k): 4.136265172106268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
Total Standard Deviation in ln(k): 4.136265172106268""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
Total Standard Deviation in ln(k): 4.136265172106268
""",
)

entry(
    index = 25,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C",
    kinetics = ArrheniusBM(A=(3.35e+10,'s^-1'), n=0.7, w0=(933.5,'kJ/mol'), E0=(138.531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C",
    kinetics = ArrheniusBM(A=(1.59e+10,'s^-1'), n=0.8, w0=(933.5,'kJ/mol'), E0=(126.028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C",
    kinetics = ArrheniusBM(A=(1.045e+11,'s^-1'), n=0.55, w0=(933.5,'kJ/mol'), E0=(134.118,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

