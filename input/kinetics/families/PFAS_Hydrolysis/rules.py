#!/usr/bin/env python
# encoding: utf-8

name = "PFAS_Hydrolysis/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.05331e+24,'m^3/(mol*s)'), n=-5.36618, w0=(899,'kJ/mol'), E0=(326.775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8522461413211586, var=178.96935625993535, Tref=1000.0, N=18, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 18 training reactions at node Root
    Total Standard Deviation in ln(k): 28.96055335994314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root
Total Standard Deviation in ln(k): 28.96055335994314""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root
Total Standard Deviation in ln(k): 28.96055335994314
""",
)

entry(
    index = 2,
    label = "Root_3F1sH->F1s",
    kinetics = ArrheniusBM(A=(1.84509e-06,'m^3/(mol*s)'), n=3.12929, w0=(933.5,'kJ/mol'), E0=(228.676,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1506702895399659, var=110.77277539903027, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_3F1sH->F1s',), comment="""BM rule fitted to 12 training reactions at node Root_3F1sH->F1s
    Total Standard Deviation in ln(k): 21.478133867574428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_3F1sH->F1s
Total Standard Deviation in ln(k): 21.478133867574428""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_3F1sH->F1s
Total Standard Deviation in ln(k): 21.478133867574428
""",
)

entry(
    index = 3,
    label = "Root_N-3F1sH->F1s",
    kinetics = ArrheniusBM(A=(1.53142e+66,'m^3/(mol*s)'), n=-17.386, w0=(830,'kJ/mol'), E0=(483.04,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.1786176853578314, var=406.5209735264, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3F1sH->F1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
    Total Standard Deviation in ln(k): 45.89411469451323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
Total Standard Deviation in ln(k): 45.89411469451323""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
Total Standard Deviation in ln(k): 45.89411469451323
""",
)

entry(
    index = 4,
    label = "Root_3F1sH->F1s_4R->F",
    kinetics = ArrheniusBM(A=(8.55538e-07,'m^3/(mol*s)'), n=3.20407, w0=(933.5,'kJ/mol'), E0=(301.805,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09695078777003853, var=175.31345209756907, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
    Total Standard Deviation in ln(k): 26.787487464676218"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
Total Standard Deviation in ln(k): 26.787487464676218""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
Total Standard Deviation in ln(k): 26.787487464676218
""",
)

entry(
    index = 5,
    label = "Root_3F1sH->F1s_N-4R->F",
    kinetics = ArrheniusBM(A=(1.30046e-06,'m^3/(mol*s)'), n=3.18325, w0=(933.5,'kJ/mol'), E0=(191.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18538777034567236, var=43.06496641839012, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F',), comment="""BM rule fitted to 8 training reactions at node Root_3F1sH->F1s_N-4R->F
    Total Standard Deviation in ln(k): 13.621652439157902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3F1sH->F1s_N-4R->F
Total Standard Deviation in ln(k): 13.621652439157902""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3F1sH->F1s_N-4R->F
Total Standard Deviation in ln(k): 13.621652439157902
""",
)

entry(
    index = 6,
    label = "Root_N-3F1sH->F1s_4R->H",
    kinetics = ArrheniusBM(A=(3.77657e-15,'m^3/(mol*s)'), n=5.78579, w0=(830,'kJ/mol'), E0=(360.677,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5226036276261342, var=93.83477153602148, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
    Total Standard Deviation in ln(k): 20.732612273864067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
Total Standard Deviation in ln(k): 20.732612273864067""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
Total Standard Deviation in ln(k): 20.732612273864067
""",
)

entry(
    index = 7,
    label = "Root_N-3F1sH->F1s_N-4R->H",
    kinetics = ArrheniusBM(A=(3.16399e+114,'m^3/(mol*s)'), n=-31.3818, w0=(830,'kJ/mol'), E0=(447.232,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=25.141295589918872, var=5334.3599879328685, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3F1sH->F1s_N-4R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
    Total Standard Deviation in ln(k): 209.58832487683708"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
Total Standard Deviation in ln(k): 209.58832487683708""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
Total Standard Deviation in ln(k): 209.58832487683708
""",
)

entry(
    index = 8,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.06791e-07,'m^3/(mol*s)'), n=3.44867, w0=(933.5,'kJ/mol'), E0=(344.847,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05469108280596011, var=3.6245072685428457, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 3.9540572358561623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.9540572358561623""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.9540572358561623
""",
)

entry(
    index = 9,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H",
    kinetics = ArrheniusBM(A=(3.68549e-06,'m^3/(mol*s)'), n=3.19929, w0=(933.5,'kJ/mol'), E0=(232.658,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16904418662065387, var=64.44114906527017, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
    Total Standard Deviation in ln(k): 16.517794020496094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 16.517794020496094""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 16.517794020496094
""",
)

entry(
    index = 10,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H",
    kinetics = ArrheniusBM(A=(6.27059e-09,'m^3/(mol*s)'), n=3.70138, w0=(933.5,'kJ/mol'), E0=(145.221,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2485509885266399, var=2.5143927626545985, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
    Total Standard Deviation in ln(k): 3.803375684854018"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 3.803375684854018""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 3.803375684854018
""",
)

entry(
    index = 11,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.23643e-16,'m^3/(mol*s)'), n=5.89853, w0=(830,'kJ/mol'), E0=(346.499,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5756353354417441, var=167.65312976958597, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
    Total Standard Deviation in ln(k): 27.403817510315836"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
Total Standard Deviation in ln(k): 27.403817510315836""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
Total Standard Deviation in ln(k): 27.403817510315836
""",
)

entry(
    index = 12,
    label = "Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(2.47108e+55,'m^3/(mol*s)'), n=-14.4485, w0=(830,'kJ/mol'), E0=(-211.037,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.76063e-08,'m^3/(mol*s)'), n=3.56442, w0=(933.5,'kJ/mol'), E0=(334.889,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.044184061457185106, var=10.911797374592682, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 6.733258578660325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 6.733258578660325""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 6.733258578660325
""",
)

entry(
    index = 14,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.1125e-06,'m^3/(mol*s)'), n=3.22, w0=(933.5,'kJ/mol'), E0=(364.738,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.23335e-06,'m^3/(mol*s)'), n=3.12813, w0=(933.5,'kJ/mol'), E0=(219.452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18366076901545392, var=109.29681314261776, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
    Total Standard Deviation in ln(k): 21.419985373549515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
Total Standard Deviation in ln(k): 21.419985373549515""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
Total Standard Deviation in ln(k): 21.419985373549515
""",
)

entry(
    index = 16,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.5992e-09,'m^3/(mol*s)'), n=3.74529, w0=(933.5,'kJ/mol'), E0=(147.622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24378405930103103, var=0.7909592402477703, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
    Total Standard Deviation in ln(k): 2.395451730902549"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 2.395451730902549""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 2.395451730902549
""",
)

entry(
    index = 17,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.62428e-12,'m^3/(mol*s)'), n=4.88194, w0=(854.346,'kJ/mol'), E0=(403.263,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4273585209561423, var=5.184817737285642, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 5.63858596249543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 5.63858596249543""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 5.63858596249543
""",
)

entry(
    index = 18,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.6075e-13,'m^3/(mol*s)'), n=5.03, w0=(830,'kJ/mol'), E0=(258.406,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(5.64167e-09,'m^3/(mol*s)'), n=3.77, w0=(933.5,'kJ/mol'), E0=(340.612,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.48333e-07,'m^3/(mol*s)'), n=3.36, w0=(933.5,'kJ/mol'), E0=(329.155,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.48217e-06,'m^3/(mol*s)'), n=3.2847, w0=(933.5,'kJ/mol'), E0=(255.154,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14567069815126504, var=1.3921033924788113, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 2.731342199764182"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 2.731342199764182""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 2.731342199764182
""",
)

entry(
    index = 22,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(4.305e-07,'m^3/(mol*s)'), n=3.26, w0=(933.5,'kJ/mol'), E0=(144.114,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.19211e-09,'m^3/(mol*s)'), n=3.80046, w0=(933.5,'kJ/mol'), E0=(149.13,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2756071386927434, var=1.0138669139709182, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 2.711067214384389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 2.711067214384389""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 2.711067214384389
""",
)

entry(
    index = 24,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.285e-08,'m^3/(mol*s)'), n=3.6, w0=(933.5,'kJ/mol'), E0=(144.912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(1.21667e-12,'m^3/(mol*s)'), n=4.98, w0=(852.662,'kJ/mol'), E0=(402.597,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(7.3e-07,'m^3/(mol*s)'), n=3.33, w0=(933.5,'kJ/mol'), E0=(255.115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.335e-09,'m^3/(mol*s)'), n=3.86, w0=(933.5,'kJ/mol'), E0=(151.407,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(4.615e-09,'m^3/(mol*s)'), n=3.71, w0=(933.5,'kJ/mol'), E0=(147.122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

