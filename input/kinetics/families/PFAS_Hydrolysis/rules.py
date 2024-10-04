#!/usr/bin/env python
# encoding: utf-8

name = "PFAS_Hydrolysis/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6.00053e-14,'m^3/(mol*s)'), n=5.27544, w0=(903.929,'kJ/mol'), E0=(234.835,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.45227371753950396, var=129.46787054727037, Tref=1000.0, N=21, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 21 training reactions at node Root
    Total Standard Deviation in ln(k): 23.947033509077382"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 23.947033509077382""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 23.947033509077382
""",
)

entry(
    index = 2,
    label = "Root_3F1sH->F1s",
    kinetics = ArrheniusBM(A=(1.57554e-06,'m^3/(mol*s)'), n=3.11382, w0=(933.5,'kJ/mol'), E0=(216.637,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21604687533062544, var=91.58729656635155, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_3F1sH->F1s',), comment="""BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
    Total Standard Deviation in ln(k): 19.728397051868342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
Total Standard Deviation in ln(k): 19.728397051868342""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
Total Standard Deviation in ln(k): 19.728397051868342
""",
)

entry(
    index = 3,
    label = "Root_N-3F1sH->F1s",
    kinetics = ArrheniusBM(A=(7.34322e-18,'m^3/(mol*s)'), n=6.48615, w0=(830,'kJ/mol'), E0=(316.739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6419659252578493, var=99.91310342076041, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3F1sH->F1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
    Total Standard Deviation in ln(k): 21.65161836157333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
Total Standard Deviation in ln(k): 21.65161836157333""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
Total Standard Deviation in ln(k): 21.65161836157333
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
    kinetics = ArrheniusBM(A=(3.58861e-07,'m^3/(mol*s)'), n=3.29271, w0=(933.5,'kJ/mol'), E0=(183.797,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2774802354811296, var=28.68660751159421, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F',), comment="""BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
    Total Standard Deviation in ln(k): 11.434523549388873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
Total Standard Deviation in ln(k): 11.434523549388873""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
Total Standard Deviation in ln(k): 11.434523549388873
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
    kinetics = ArrheniusBM(A=(3.25361e-13,'m^3/(mol*s)'), n=5.002, w0=(830,'kJ/mol'), E0=(254.112,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988502583851788, var=1.1190952415502595, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3F1sH->F1s_N-4R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
    Total Standard Deviation in ln(k): 3.6254039605985064"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
Total Standard Deviation in ln(k): 3.6254039605985064""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
Total Standard Deviation in ln(k): 3.6254039605985064
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
    kinetics = ArrheniusBM(A=(1.75791e-09,'m^3/(mol*s)'), n=3.8423, w0=(933.5,'kJ/mol'), E0=(151.49,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.38208759629321426, var=2.850726591038206, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H',), comment="""BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
    Total Standard Deviation in ln(k): 4.3448328069358135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 4.3448328069358135""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 4.3448328069358135
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
    kinetics = ArrheniusBM(A=(2.56e-13,'m^3/(mol*s)'), n=5.03, w0=(830,'kJ/mol'), E0=(251.033,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
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
    kinetics = ArrheniusBM(A=(1.63327e-09,'m^3/(mol*s)'), n=3.83599, w0=(933.5,'kJ/mol'), E0=(154.188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.39716845260591854, var=1.4147578976281063, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R',), comment="""BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
    Total Standard Deviation in ln(k): 3.3824146717880486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 3.3824146717880486""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 3.3824146717880486
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
    kinetics = ArrheniusBM(A=(1.42594e-09,'m^3/(mol*s)'), n=3.84874, w0=(933.5,'kJ/mol'), E0=(156.344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4384561888588486, var=1.062535261633299, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.168116624110227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 3.168116624110227""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 3.168116624110227
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
    kinetics = ArrheniusBM(A=(1.45172e-09,'m^3/(mol*s)'), n=3.84466, w0=(933.5,'kJ/mol'), E0=(158.988,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47735033115656605, var=0.5794141862792398, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.7253622130026196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.7253622130026196""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.7253622130026196
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

entry(
    index = 29,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.6816e-09,'m^3/(mol*s)'), n=3.82474, w0=(933.5,'kJ/mol'), E0=(161.644,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5418030025943525, var=0.1698435216454645, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 2.1875070225650295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 2.1875070225650295""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 2.1875070225650295
""",
)

entry(
    index = 30,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(1.335e-09,'m^3/(mol*s)'), n=3.86, w0=(933.5,'kJ/mol'), E0=(151.407,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(1.49519e-09,'m^3/(mol*s)'), n=3.83388, w0=(933.5,'kJ/mol'), E0=(162.23,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6660500796145656, var=0.4442376835010361, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 3.0096718020931323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 3.0096718020931323""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 3.0096718020931323
""",
)

entry(
    index = 32,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(2.24e-09,'m^3/(mol*s)'), n=3.8, w0=(933.5,'kJ/mol'), E0=(160.529,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(2.545e-09,'m^3/(mol*s)'), n=3.78, w0=(933.5,'kJ/mol'), E0=(162.328,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(9.35e-10,'m^3/(mol*s)'), n=3.88, w0=(933.5,'kJ/mol'), E0=(162.199,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

