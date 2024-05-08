#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.08139e+79,'m^3/(mol*s)'), n=-21.0676, w0=(585.636,'kJ/mol'), E0=(440.861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.303593808499054, var=167.10726370247784, Tref=1000.0, N=66, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 66 training reactions at node Root
    Total Standard Deviation in ln(k): 31.70312942422083"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 31.70312942422083""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 31.70312942422083
""",
)

entry(
    index = 2,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(8.80904e+31,'m^3/(mol*s)'), n=-7.35367, w0=(606.851,'kJ/mol'), E0=(231.682,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9162813369244622, var=10.509372038621716, Tref=1000.0, N=47, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 47 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 8.80119699202872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 47 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 8.80119699202872""",
    longDesc = 
"""
BM rule fitted to 47 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 8.80119699202872
""",
)

entry(
    index = 3,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(2.64496e+15,'m^3/(mol*s)'), n=-2.91244, w0=(533.158,'kJ/mol'), E0=(410.899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5410780916747112, var=48.52907646879991, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 19 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 15.32504136340994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 15.32504136340994""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 15.32504136340994
""",
)

entry(
    index = 4,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R",
    kinetics = ArrheniusBM(A=(1.67081e+07,'m^3/(mol*s)'), n=-0.25099, w0=(584,'kJ/mol'), E0=(109.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05783420702249951, var=0.11014630093021238, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R',), comment="""BM rule fitted to 12 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R
    Total Standard Deviation in ln(k): 0.8106494948591996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R
Total Standard Deviation in ln(k): 0.8106494948591996""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R
Total Standard Deviation in ln(k): 0.8106494948591996
""",
)

entry(
    index = 5,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s",
    kinetics = ArrheniusBM(A=(396.492,'m^3/(mol*s)'), n=1.28632, w0=(529,'kJ/mol'), E0=(73.8371,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3399281776762524, var=2.6054747618552025, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s',), comment="""BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
    Total Standard Deviation in ln(k): 4.090030632863941"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 4.090030632863941""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 4.090030632863941
""",
)

entry(
    index = 6,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s",
    kinetics = ArrheniusBM(A=(1.05103e+16,'m^3/(mol*s)'), n=-2.85196, w0=(636.107,'kJ/mol'), E0=(208.488,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8300234516971726, var=18.09478891179236, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s',), comment="""BM rule fitted to 28 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
    Total Standard Deviation in ln(k): 10.61322211627819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 10.61322211627819""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 10.61322211627819
""",
)

entry(
    index = 7,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.62201e+08,'m^3/(mol*s)'), n=-0.844427, w0=(563.583,'kJ/mol'), E0=(395.318,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21386923338533487, var=45.29186556511072, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 12 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 14.029072883922378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 14.029072883922378""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 14.029072883922378
""",
)

entry(
    index = 8,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.0284835,'m^3/(mol*s)'), n=1.92223, w0=(481,'kJ/mol'), E0=(274.257,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12519303801036796, var=152.9648024618525, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 7 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 25.108906344995162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 25.108906344995162""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 25.108906344995162
""",
)

entry(
    index = 9,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.13979e+06,'m^3/(mol*s)'), n=0.0863482, w0=(584,'kJ/mol'), E0=(109.454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028930780883000492, var=0.07206277511555077, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 0.6108517252544917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.6108517252544917""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.6108517252544917
""",
)

entry(
    index = 10,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(4.08908e+07,'m^3/(mol*s)'), n=-0.363436, w0=(584,'kJ/mol'), E0=(109.908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06746868097934366, var=0.08249864412907129, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 0.7453308793010623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.7453308793010623""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.7453308793010623
""",
)

entry(
    index = 11,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(214000,'m^3/(mol*s)'), n=-5.39641e-08, w0=(529,'kJ/mol'), E0=(113.496,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.28047e+06,'m^3/(mol*s)'), n=0.110072, w0=(529,'kJ/mol'), E0=(66.8802,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12288527419543319, var=1.6630932776143392, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 2.8940828492449993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.8940828492449993""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.8940828492449993
""",
)

entry(
    index = 13,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(0.00918265,'m^3/(mol*s)'), n=2.50916, w0=(621.938,'kJ/mol'), E0=(100.558,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23190099874689737, var=12.90112592130073, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 8 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 7.78330081602691"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 7.78330081602691""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 7.78330081602691
""",
)

entry(
    index = 14,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(7044.07,'m^3/(mol*s)'), n=0.59591, w0=(641.775,'kJ/mol'), E0=(180.282,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3173505146521799, var=14.753631500526675, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 20 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 8.497642002327563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 8.497642002327563""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 8.497642002327563
""",
)

entry(
    index = 15,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(7.88152e-13,'m^3/(mol*s)'), n=5.26076, w0=(530.8,'kJ/mol'), E0=(296.217,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34736943139838355, var=44.30548161135061, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 14.216777899556018"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 14.216777899556018""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 14.216777899556018
""",
)

entry(
    index = 16,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(2.94674,'m^3/(mol*s)'), n=1.34598, w0=(587,'kJ/mol'), E0=(378.034,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2804116905084691, var=49.697255149881414, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 7 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 14.837188550454282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 14.837188550454282""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 14.837188550454282
""",
)

entry(
    index = 17,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O",
    kinetics = ArrheniusBM(A=(1.15378e+28,'m^3/(mol*s)'), n=-6.55063, w0=(531,'kJ/mol'), E0=(379.899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5907290644159902, var=52.21530071762169, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O
    Total Standard Deviation in ln(k): 15.970490721766238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O
Total Standard Deviation in ln(k): 15.970490721766238""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O
Total Standard Deviation in ln(k): 15.970490721766238
""",
)

entry(
    index = 18,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O",
    kinetics = ArrheniusBM(A=(2.84494e+11,'m^3/(mol*s)'), n=-1.89521, w0=(443.5,'kJ/mol'), E0=(137.781,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4540614453766039, var=34.02892319839725, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O
    Total Standard Deviation in ln(k): 12.835342675470992"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O
Total Standard Deviation in ln(k): 12.835342675470992""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O
Total Standard Deviation in ln(k): 12.835342675470992
""",
)

entry(
    index = 19,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.16448e+06,'m^3/(mol*s)'), n=-0.144618, w0=(584,'kJ/mol'), E0=(102.716,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(490107,'m^3/(mol*s)'), n=0.201831, w0=(584,'kJ/mol'), E0=(107.984,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.043461663341785264, var=0.18543765059589312, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.9724886431361681"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9724886431361681""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9724886431361681
""",
)

entry(
    index = 21,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(9.16873e+07,'m^3/(mol*s)'), n=-0.471498, w0=(584,'kJ/mol'), E0=(108.904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07514139785501385, var=0.03091755307632206, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.5412978274845682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.5412978274845682""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.5412978274845682
""",
)

entry(
    index = 22,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCbCdCl1sCtF1sHO-R",
    kinetics = ArrheniusBM(A=(3.11579e+08,'m^3/(mol*s)'), n=-0.607843, w0=(584,'kJ/mol'), E0=(113.807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCbCdCl1sCtF1sHO-R',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCbCdCl1sCtF1sHO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCbCdCl1sCtF1sHO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCbCdCl1sCtF1sHO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->Ct",
    kinetics = ArrheniusBM(A=(21122.7,'m^3/(mol*s)'), n=0.671539, w0=(584,'kJ/mol'), E0=(111.077,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->Ct",
    kinetics = ArrheniusBM(A=(8.17451e+07,'m^3/(mol*s)'), n=-0.50563, w0=(584,'kJ/mol'), E0=(110.86,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=-3.02437e-08, w0=(529,'kJ/mol'), E0=(77.1661,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(1.69679e+06,'m^3/(mol*s)'), n=0.132087, w0=(529,'kJ/mol'), E0=(63.6229,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14746229057662447, var=1.9511959628444138, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 3.1708267951342735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 3.1708267951342735""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 3.1708267951342735
""",
)

entry(
    index = 27,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(2.33736e+17,'m^3/(mol*s)'), n=-4.54388, w0=(583,'kJ/mol'), E0=(180.008,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(478.68,'m^3/(mol*s)'), n=1.17575, w0=(627.5,'kJ/mol'), E0=(125.964,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07307801853040206, var=10.788442746172983, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H',), comment="""BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 6.768318824168564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 6.768318824168564""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 6.768318824168564
""",
)

entry(
    index = 29,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C",
    kinetics = ArrheniusBM(A=(6.46741e-12,'m^3/(mol*s)'), n=4.8544, w0=(665.278,'kJ/mol'), E0=(4.22338,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2750952851610726, var=15.963039559573014, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C',), comment="""BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C
    Total Standard Deviation in ln(k): 8.700867151925497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C
Total Standard Deviation in ln(k): 8.700867151925497""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C
Total Standard Deviation in ln(k): 8.700867151925497
""",
)

entry(
    index = 30,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C",
    kinetics = ArrheniusBM(A=(1.20997e-10,'m^3/(mol*s)'), n=4.55836, w0=(622.545,'kJ/mol'), E0=(151.82,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1501747152865962, var=14.57284815923706, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C',), comment="""BM rule fitted to 11 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C
    Total Standard Deviation in ln(k): 10.542842094640674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C
Total Standard Deviation in ln(k): 10.542842094640674""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C
Total Standard Deviation in ln(k): 10.542842094640674
""",
)

entry(
    index = 31,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(3.86563e+11,'m^3/(mol*s)'), n=-1.60162, w0=(519,'kJ/mol'), E0=(415.127,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03913943208487893, var=50.08635003616798, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 14.28619332934611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 14.28619332934611""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 14.28619332934611
""",
)

entry(
    index = 32,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(3.32355e-13,'m^3/(mol*s)'), n=5.41799, w0=(538.667,'kJ/mol'), E0=(263.22,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2953183197622949, var=10.482611598668074, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 7.232708820807121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 7.232708820807121""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 7.232708820807121
""",
)

entry(
    index = 33,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R",
    kinetics = ArrheniusBM(A=(2.55706e-14,'m^3/(mol*s)'), n=5.20608, w0=(658,'kJ/mol'), E0=(351.292,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3891865519816142, var=48.665620594149125, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R
    Total Standard Deviation in ln(k): 14.963037652992984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R
Total Standard Deviation in ln(k): 14.963037652992984""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R
Total Standard Deviation in ln(k): 14.963037652992984
""",
)

entry(
    index = 34,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(2.22791e-07,'m^3/(mol*s)'), n=3.59921, w0=(519,'kJ/mol'), E0=(453.689,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(7.42882e-09,'m^3/(mol*s)'), n=4.10708, w0=(538.667,'kJ/mol'), E0=(330.883,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4596141129689573, var=10.261223394413749, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 10.089168962707916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 10.089168962707916""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 10.089168962707916
""",
)

entry(
    index = 36,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.25816e+07,'m^3/(mol*s)'), n=-0.647497, w0=(531,'kJ/mol'), E0=(341.875,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1729810615647431, var=29.595679055428437, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.340767681253052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.340767681253052""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.340767681253052
""",
)

entry(
    index = 37,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1.26474e-05,'m^3/(mol*s)'), n=2.95311, w0=(531,'kJ/mol'), E0=(223.917,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.55933e+21,'m^3/(mol*s)'), n=-4.1602, w0=(473.5,'kJ/mol'), E0=(191.487,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10182381630602674, var=65.36862007498478, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 16.464294793785744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 16.464294793785744""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 16.464294793785744
""",
)

entry(
    index = 39,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.18345,'m^3/(mol*s)'), n=0.764042, w0=(413.5,'kJ/mol'), E0=(18.2016,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5714753952207856, var=30.93276804447263, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 12.585649974073238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 12.585649974073238""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 12.585649974073238
""",
)

entry(
    index = 40,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(486642,'m^3/(mol*s)'), n=0.225671, w0=(584,'kJ/mol'), E0=(107.293,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-6R!H-4Br1sCbCdCl1sCtF1sHO",
    kinetics = ArrheniusBM(A=(3.55364e+07,'m^3/(mol*s)'), n=-0.357533, w0=(584,'kJ/mol'), E0=(108.811,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-6R!H-4Br1sCbCdCl1sCtF1sHO',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO",
    kinetics = ArrheniusBM(A=(1.10825e+08,'m^3/(mol*s)'), n=-0.494291, w0=(584,'kJ/mol'), E0=(108.923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0739562917847758, var=0.02913633587331158, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO',), comment="""BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
    Total Standard Deviation in ln(k): 0.5280154568341594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
Total Standard Deviation in ln(k): 0.5280154568341594""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
Total Standard Deviation in ln(k): 0.5280154568341594
""",
)

entry(
    index = 43,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R",
    kinetics = ArrheniusBM(A=(216154,'m^3/(mol*s)'), n=0.41647, w0=(529,'kJ/mol'), E0=(66.7368,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12186484916728252, var=2.9149039752247594, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R',), comment="""BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R
    Total Standard Deviation in ln(k): 3.7288953014534947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 3.7288953014534947""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 3.7288953014534947
""",
)

entry(
    index = 44,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1055.25,'m^3/(mol*s)'), n=0.961814, w0=(638.875,'kJ/mol'), E0=(136.818,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11384999573343373, var=11.623092508058996, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s',), comment="""BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s
    Total Standard Deviation in ln(k): 7.120729771696797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s
Total Standard Deviation in ln(k): 7.120729771696797""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s
Total Standard Deviation in ln(k): 7.120729771696797
""",
)

entry(
    index = 45,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.26572,'m^3/(mol*s)'), n=2.06839, w0=(612.333,'kJ/mol'), E0=(44.6016,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.44852704105077745, var=7.396308348801246, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s
    Total Standard Deviation in ln(k): 6.5790609104498206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.5790609104498206""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.5790609104498206
""",
)

entry(
    index = 46,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs",
    kinetics = ArrheniusBM(A=(0.00743558,'m^3/(mol*s)'), n=2.17678, w0=(584,'kJ/mol'), E0=(172.173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0015775257810840206, var=3.3721000331987425, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs
    Total Standard Deviation in ln(k): 3.6853145201378923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 3.6853145201378923""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 3.6853145201378923
""",
)

entry(
    index = 47,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs",
    kinetics = ArrheniusBM(A=(1.02129e-05,'m^3/(mol*s)'), n=3.11928, w0=(705.917,'kJ/mol'), E0=(64.7805,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17238204190427817, var=2.527929626737791, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs',), comment="""BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs
    Total Standard Deviation in ln(k): 3.620542072865273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 3.620542072865273""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 3.620542072865273
""",
)

entry(
    index = 48,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s",
    kinetics = ArrheniusBM(A=(1.3079e+13,'m^3/(mol*s)'), n=-2.4865, w0=(583,'kJ/mol'), E0=(113.481,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6133978504265836, var=23.534621185699624, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s
    Total Standard Deviation in ln(k): 11.266670562463746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.266670562463746""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.266670562463746
""",
)

entry(
    index = 49,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s",
    kinetics = ArrheniusBM(A=(2.37456e-10,'m^3/(mol*s)'), n=4.47749, w0=(631.333,'kJ/mol'), E0=(153.42,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2339389967999186, var=14.733795489721459, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s',), comment="""BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s
    Total Standard Deviation in ln(k): 10.795449949195598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 10.795449949195598""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 10.795449949195598
""",
)

entry(
    index = 50,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(5.7066e-06,'m^3/(mol*s)'), n=3.19155, w0=(519,'kJ/mol'), E0=(387.707,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(0.000166864,'m^3/(mol*s)'), n=2.82973, w0=(519,'kJ/mol'), E0=(345.531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Br1s",
    kinetics = ArrheniusBM(A=(3.01249e-05,'m^3/(mol*s)'), n=3.17037, w0=(458,'kJ/mol'), E0=(273.783,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s",
    kinetics = ArrheniusBM(A=(7.00651e-11,'m^3/(mol*s)'), n=4.73603, w0=(579,'kJ/mol'), E0=(277.591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17583084543988076, var=14.15160542533727, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s
    Total Standard Deviation in ln(k): 7.9833226764726355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s
Total Standard Deviation in ln(k): 7.9833226764726355""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s
Total Standard Deviation in ln(k): 7.9833226764726355
""",
)

entry(
    index = 54,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(5.95816e-06,'m^3/(mol*s)'), n=3.33132, w0=(658,'kJ/mol'), E0=(382.315,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3783529558413224, var=0.002291619234345544, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 1.0466039596090275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 1.0466039596090275""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 1.0466039596090275
""",
)

entry(
    index = 55,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1.24014e-13,'m^3/(mol*s)'), n=4.45435, w0=(658,'kJ/mol'), E0=(342.586,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.42311e-06,'m^3/(mol*s)'), n=3.42841, w0=(500,'kJ/mol'), E0=(332.447,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.54272e-08,'m^3/(mol*s)'), n=3.94901, w0=(558,'kJ/mol'), E0=(332.159,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.338121361554936, var=17.352834998220086, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 14.225748403311552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 14.225748403311552""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 14.225748403311552
""",
)

entry(
    index = 58,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1.40908e-07,'m^3/(mol*s)'), n=3.45227, w0=(531,'kJ/mol'), E0=(321.12,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.12553e-07,'m^3/(mol*s)'), n=3.34134, w0=(531,'kJ/mol'), E0=(278.421,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=-8.99768e-08, w0=(447,'kJ/mol'), E0=(131.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(739000,'m^3/(mol*s)'), n=6.88368e-08, w0=(500,'kJ/mol'), E0=(155.898,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(321,'m^3/(mol*s)'), n=-1.19733e-08, w0=(447,'kJ/mol'), E0=(95.9985,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(3200,'m^3/(mol*s)'), n=-7.50016e-09, w0=(380,'kJ/mol'), E0=(65.7993,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.36692e+07,'m^3/(mol*s)'), n=-0.382746, w0=(584,'kJ/mol'), E0=(106.821,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.27295e+08,'m^3/(mol*s)'), n=-0.522177, w0=(584,'kJ/mol'), E0=(109.449,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07236308446794819, var=0.011171575725256783, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.39370862245649435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.39370862245649435""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.39370862245649435
""",
)

entry(
    index = 66,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R",
    kinetics = ArrheniusBM(A=(380.996,'m^3/(mol*s)'), n=1.18611, w0=(529,'kJ/mol'), E0=(74.7001,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06508466769699056, var=2.630327248685747, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
    Total Standard Deviation in ln(k): 3.414865530607326"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 3.414865530607326""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 3.414865530607326
""",
)

entry(
    index = 67,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_6R!H->F",
    kinetics = ArrheniusBM(A=(38122,'m^3/(mol*s)'), n=0.735896, w0=(529,'kJ/mol'), E0=(69.6061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(3.94494e+11,'m^3/(mol*s)'), n=-1.44224, w0=(529,'kJ/mol'), E0=(47.9409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cs",
    kinetics = ArrheniusBM(A=(2.79957e-05,'m^3/(mol*s)'), n=3.10993, w0=(584,'kJ/mol'), E0=(140.098,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs",
    kinetics = ArrheniusBM(A=(165851,'m^3/(mol*s)'), n=0.340055, w0=(657.167,'kJ/mol'), E0=(134.392,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18272129701871265, var=8.92167142433622, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs
    Total Standard Deviation in ln(k): 6.447075435287595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 6.447075435287595""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 6.447075435287595
""",
)

entry(
    index = 71,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H",
    kinetics = ArrheniusBM(A=(7.59922,'m^3/(mol*s)'), n=1.89141, w0=(627,'kJ/mol'), E0=(126.771,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11978490780322452, var=0.564746332911407, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H
    Total Standard Deviation in ln(k): 1.8075176233288979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H
Total Standard Deviation in ln(k): 1.8075176233288979""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H
Total Standard Deviation in ln(k): 1.8075176233288979
""",
)

entry(
    index = 72,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->H",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=5.28703e-09, w0=(583,'kJ/mol'), E0=(75.2086,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(3.33872e-07,'m^3/(mol*s)'), n=3.38172, w0=(584,'kJ/mol'), E0=(170.293,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(5.00804e-06,'m^3/(mol*s)'), n=3.10588, w0=(584,'kJ/mol'), E0=(155.248,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07414110820516438, var=0.5320293693245935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 1.64854484089816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 1.64854484089816""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 1.64854484089816
""",
)

entry(
    index = 75,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.44246e-08,'m^3/(mol*s)'), n=3.90274, w0=(730.5,'kJ/mol'), E0=(68.9596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31265671212618057, var=8.370718467893711, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R
    Total Standard Deviation in ln(k): 6.585708036311589"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R
Total Standard Deviation in ln(k): 6.585708036311589""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R
Total Standard Deviation in ln(k): 6.585708036311589
""",
)

entry(
    index = 76,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(112.911,'m^3/(mol*s)'), n=1.11181, w0=(730.5,'kJ/mol'), E0=(109.212,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(17.8899,'m^3/(mol*s)'), n=1.2765, w0=(656.75,'kJ/mol'), E0=(94.5563,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03894514063739418, var=0.033048589049686085, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 0.4622983327238187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 0.4622983327238187""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 0.4622983327238187
""",
)

entry(
    index = 78,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.70149e+08,'m^3/(mol*s)'), n=-1.26599, w0=(583,'kJ/mol'), E0=(35.9196,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.9521,'m^3/(mol*s)'), n=1.31015, w0=(583,'kJ/mol'), E0=(96.173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(4.82235e-09,'m^3/(mol*s)'), n=4.10375, w0=(657.2,'kJ/mol'), E0=(157.08,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.845048158243338, var=38.11076692923683, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 19.524377394119636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 19.524377394119636""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 19.524377394119636
""",
)

entry(
    index = 81,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.68318e-16,'m^3/(mol*s)'), n=6.23477, w0=(599,'kJ/mol'), E0=(134.63,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.39893927807539725, var=3.2804722042908736, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 4.6333509793997845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.6333509793997845""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.6333509793997845
""",
)

entry(
    index = 82,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_5Cl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.78425e-05,'m^3/(mol*s)'), n=3.22746, w0=(500,'kJ/mol'), E0=(286.001,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_5Cl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_5Cl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_5Cl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_5Cl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_N-5Cl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(4.96165e-06,'m^3/(mol*s)'), n=3.30609, w0=(658,'kJ/mol'), E0=(300.662,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_N-5Cl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_N-5Cl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_N-5Cl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_N-5Cl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_5Br1sF1s->F1s",
    kinetics = ArrheniusBM(A=(6.158e-07,'m^3/(mol*s)'), n=3.54561, w0=(658,'kJ/mol'), E0=(335.087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_5Br1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_5Br1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_N-5Br1sF1s->F1s",
    kinetics = ArrheniusBM(A=(7.43831e-06,'m^3/(mol*s)'), n=3.35156, w0=(458,'kJ/mol'), E0=(323.834,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_N-5Br1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_N-5Br1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_N-5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_N-5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(5.40342e+08,'m^3/(mol*s)'), n=-0.740623, w0=(584,'kJ/mol'), E0=(109.227,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07212098919745502, var=0.007692440233300485, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 0.35703692796408437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.35703692796408437""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.35703692796408437
""",
)

entry(
    index = 87,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_4Br1sCbCdCl1sCtF1sHO->Ct",
    kinetics = ArrheniusBM(A=(1.16958e+06,'m^3/(mol*s)'), n=0.171554, w0=(584,'kJ/mol'), E0=(108.019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_4Br1sCbCdCl1sCtF1sHO->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_4Br1sCbCdCl1sCtF1sHO->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_N-4Br1sCbCdCl1sCtF1sHO->Ct",
    kinetics = ArrheniusBM(A=(7.68921e+08,'m^3/(mol*s)'), n=-0.779019, w0=(584,'kJ/mol'), E0=(111.321,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_N-4Br1sCbCdCl1sCtF1sHO->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_N-4Br1sCbCdCl1sCtF1sHO->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_N-4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_N-4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R",
    kinetics = ArrheniusBM(A=(6.69104,'m^3/(mol*s)'), n=1.68518, w0=(529,'kJ/mol'), E0=(78.4695,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_4Cl1sF1sHO->O",
    kinetics = ArrheniusBM(A=(4.67448e-06,'m^3/(mol*s)'), n=3.15288, w0=(614,'kJ/mol'), E0=(90.2155,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_4Cl1sF1sHO->O',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_4Cl1sF1sHO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_4Cl1sF1sHO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_4Cl1sF1sHO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O",
    kinetics = ArrheniusBM(A=(3.5601,'m^3/(mol*s)'), n=1.78252, w0=(678.75,'kJ/mol'), E0=(108.813,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40942070288400106, var=0.43398079069183415, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O
    Total Standard Deviation in ln(k): 2.349358939078819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O
Total Standard Deviation in ln(k): 2.349358939078819""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O
Total Standard Deviation in ln(k): 2.349358939078819
""",
)

entry(
    index = 92,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H_3Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.39739,'m^3/(mol*s)'), n=2.08325, w0=(627,'kJ/mol'), E0=(124.993,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H_3Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H_3Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H_3Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H_3Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H_N-3Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.50896,'m^3/(mol*s)'), n=2.11145, w0=(627,'kJ/mol'), E0=(120.316,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H_N-3Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H_N-3Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H_N-3Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->H_N-3Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.24049e-06,'m^3/(mol*s)'), n=3.20888, w0=(584,'kJ/mol'), E0=(157.205,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.9253e-06,'m^3/(mol*s)'), n=3.16987, w0=(584,'kJ/mol'), E0=(151.196,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.1333,'m^3/(mol*s)'), n=1.51168, w0=(730.5,'kJ/mol'), E0=(133.165,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02734802108121189, var=0.0027343189908062234, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.17354265360544022"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.17354265360544022""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.17354265360544022
""",
)

entry(
    index = 97,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_4Cl1sF1sHO->Cl1s",
    kinetics = ArrheniusBM(A=(2.57491,'m^3/(mol*s)'), n=1.58614, w0=(583,'kJ/mol'), E0=(98.4535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_4Cl1sF1sHO->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_4Cl1sF1sHO->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_4Cl1sF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_4Cl1sF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_N-4Cl1sF1sHO->Cl1s",
    kinetics = ArrheniusBM(A=(11.2646,'m^3/(mol*s)'), n=1.26561, w0=(730.5,'kJ/mol'), E0=(81.3593,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_N-4Cl1sF1sHO->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_N-4Cl1sF1sHO->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_N-4Cl1sF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_N-4Cl1sF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_4CsF1sHO->F1s",
    kinetics = ArrheniusBM(A=(1.3853e-05,'m^3/(mol*s)'), n=3.10186, w0=(730.5,'kJ/mol'), E0=(157.77,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5012164720726492, var=0.4755927601649538, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_4CsF1sHO->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_4CsF1sHO->F1s
    Total Standard Deviation in ln(k): 2.641868005915079"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_4CsF1sHO->F1s
Total Standard Deviation in ln(k): 2.641868005915079""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_4CsF1sHO->F1s
Total Standard Deviation in ln(k): 2.641868005915079
""",
)

entry(
    index = 100,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s",
    kinetics = ArrheniusBM(A=(1.55164e-10,'m^3/(mol*s)'), n=4.59393, w0=(608.333,'kJ/mol'), E0=(205.17,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028135371717832404, var=14.645750433484576, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s
    Total Standard Deviation in ln(k): 7.742766259655403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s
Total Standard Deviation in ln(k): 7.742766259655403""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s
Total Standard Deviation in ln(k): 7.742766259655403
""",
)

entry(
    index = 101,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O",
    kinetics = ArrheniusBM(A=(2.63834e-09,'m^3/(mol*s)'), n=4.14506, w0=(614,'kJ/mol'), E0=(143.296,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2329687186890622, var=0.044032669466732094, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O
    Total Standard Deviation in ln(k): 1.0060214022392366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O
Total Standard Deviation in ln(k): 1.0060214022392366""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O
Total Standard Deviation in ln(k): 1.0060214022392366
""",
)

entry(
    index = 102,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O",
    kinetics = ArrheniusBM(A=(1.61487e-06,'m^3/(mol*s)'), n=3.40297, w0=(584,'kJ/mol'), E0=(180.353,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12584235004834907, var=1.018724795505057, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O
    Total Standard Deviation in ln(k): 2.3396039648234845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O
Total Standard Deviation in ln(k): 2.3396039648234845""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O
Total Standard Deviation in ln(k): 2.3396039648234845
""",
)

entry(
    index = 103,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_4Br1sCbCdCl1sCtF1sHO->Cb",
    kinetics = ArrheniusBM(A=(1.57523e+09,'m^3/(mol*s)'), n=-0.891994, w0=(584,'kJ/mol'), E0=(110.285,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_4Br1sCbCdCl1sCtF1sHO->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_4Br1sCbCdCl1sCtF1sHO->Cb
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_4Br1sCbCdCl1sCtF1sHO->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_4Br1sCbCdCl1sCtF1sHO->Cb
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4Br1sCbCdCl1sCtF1sHO->Cb",
    kinetics = ArrheniusBM(A=(1.8535e+08,'m^3/(mol*s)'), n=-0.589251, w0=(584,'kJ/mol'), E0=(108.169,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4Br1sCbCdCl1sCtF1sHO->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4Br1sCbCdCl1sCtF1sHO->Cb
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4Br1sCbCdCl1sCtF1sHO->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4Br1sCbCdCl1sCtF1sHO->Cb
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_4F1sH->F1s",
    kinetics = ArrheniusBM(A=(0.0514528,'m^3/(mol*s)'), n=2.19387, w0=(730.5,'kJ/mol'), E0=(79.8219,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_4F1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_4F1sH->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_4F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_4F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_N-4F1sH->F1s",
    kinetics = ArrheniusBM(A=(2.13948,'m^3/(mol*s)'), n=1.96174, w0=(627,'kJ/mol'), E0=(121.68,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_N-4F1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_N-4F1sH->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_N-4F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_N-4F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.46471,'m^3/(mol*s)'), n=1.46279, w0=(730.5,'kJ/mol'), E0=(137.708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_4CsHO->Cs",
    kinetics = ArrheniusBM(A=(6.68017e-11,'m^3/(mol*s)'), n=4.72997, w0=(584,'kJ/mol'), E0=(229.176,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_4CsHO->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_4CsHO->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_4CsHO->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_4CsHO->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs",
    kinetics = ArrheniusBM(A=(1.00483e-13,'m^3/(mol*s)'), n=5.49196, w0=(620.5,'kJ/mol'), E0=(183.467,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0229658265255075, var=15.90274489936186, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs
    Total Standard Deviation in ln(k): 8.05223490439545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs
Total Standard Deviation in ln(k): 8.05223490439545""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs
Total Standard Deviation in ln(k): 8.05223490439545
""",
)

entry(
    index = 110,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.23354e-09,'m^3/(mol*s)'), n=4.16722, w0=(614,'kJ/mol'), E0=(144.226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.67625e-09,'m^3/(mol*s)'), n=4.20006, w0=(614,'kJ/mol'), E0=(141.51,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->O_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.3398e-07,'m^3/(mol*s)'), n=3.60759, w0=(584,'kJ/mol'), E0=(182.408,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(5.49685e-07,'m^3/(mol*s)'), n=3.52855, w0=(584,'kJ/mol'), E0=(174.75,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->O_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_4HO->O",
    kinetics = ArrheniusBM(A=(1.76395e-12,'m^3/(mol*s)'), n=5.02686, w0=(614,'kJ/mol'), E0=(167.114,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_4HO->O',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_4HO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_4HO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_4HO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_N-4HO->O",
    kinetics = ArrheniusBM(A=(3.26413e-09,'m^3/(mol*s)'), n=4.30786, w0=(627,'kJ/mol'), E0=(215.723,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_N-4HO->O',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_N-4HO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_N-4HO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_N-4HO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

