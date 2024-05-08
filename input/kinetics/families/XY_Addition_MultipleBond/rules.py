#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.90909e-81,'m^3/(mol*s)'), n=24.5974, w0=(793.155,'kJ/mol'), E0=(6.76689,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3875172954707042, var=45.95495471000477, Tref=1000.0, N=55, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 55 training reactions at node Root
    Total Standard Deviation in ln(k): 17.076340263697507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 55 training reactions at node Root
Total Standard Deviation in ln(k): 17.076340263697507""",
    longDesc = 
"""
BM rule fitted to 55 training reactions at node Root
Total Standard Deviation in ln(k): 17.076340263697507
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(9.00859e-87,'m^3/(mol*s)'), n=26.3263, w0=(886.804,'kJ/mol'), E0=(5.69475,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5250744809422958, var=42.966383313164656, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 28 training reactions at node Root_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 16.972632818448663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 16.972632818448663""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 16.972632818448663
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.72419e-07,'m^3/(mol*s)'), n=3.69682, w0=(696.037,'kJ/mol'), E0=(164.04,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.584098125493885, var=49.788984109709894, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 15.613256473957627"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 15.613256473957627""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 15.613256473957627
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.30251e-34,'m^3/(mol*s)'), n=11.2888, w0=(857.781,'kJ/mol'), E0=(205.411,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17288335253040926, var=20.48755044305631, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 16 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 9.508447819990486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 9.508447819990486""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 9.508447819990486
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(2.57016e+31,'m^3/(mol*s)'), n=-7.53001, w0=(847,'kJ/mol'), E0=(355.217,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(5.63276e-16,'m^3/(mol*s)'), n=5.80002, w0=(932.636,'kJ/mol'), E0=(141.285,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02843439358022823, var=14.887713917044232, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 11 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 7.806633396413499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 7.806633396413499""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 7.806633396413499
""",
)

entry(
    index = 7,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(5.93272e-05,'m^3/(mol*s)'), n=2.63647, w0=(575,'kJ/mol'), E0=(143.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(2.51141e-07,'m^3/(mol*s)'), n=3.71209, w0=(700.692,'kJ/mol'), E0=(164.286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5919047792805596, var=50.79742699400918, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 15.775408668978502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 15.775408668978502""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 15.775408668978502
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.91429e-32,'m^3/(mol*s)'), n=10.5863, w0=(855.625,'kJ/mol'), E0=(200.978,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07422443939678203, var=1.4319271806964784, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.5854229050199917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.5854229050199917""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.5854229050199917
""",
)

entry(
    index = 10,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.03853e-39,'m^3/(mol*s)'), n=12.6747, w0=(858.5,'kJ/mol'), E0=(203.486,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20807412730457003, var=47.699987663344054, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 10 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 14.368537744617292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 14.368537744617292""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 14.368537744617292
""",
)

entry(
    index = 11,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(63.877,'m^3/(mol*s)'), n=1.05901, w0=(858.5,'kJ/mol'), E0=(249.24,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.44925e-16,'m^3/(mol*s)'), n=5.80391, w0=(940.05,'kJ/mol'), E0=(141.214,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0289860353022806, var=14.909602932760706, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 10 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 7.813703766018739"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 7.813703766018739""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 7.813703766018739
""",
)

entry(
    index = 13,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(0.415772,'m^3/(mol*s)'), n=1.8082, w0=(693,'kJ/mol'), E0=(204.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20328030983623113, var=13.65367140645754, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 7.918426011256817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 7.918426011256817""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 7.918426011256817
""",
)

entry(
    index = 14,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(2.05453e-44,'m^3/(mol*s)'), n=14.5196, w0=(718,'kJ/mol'), E0=(15.6247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.3417543448732765, var=32.657229036762544, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 17.34016497092213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 17.34016497092213""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 17.34016497092213
""",
)

entry(
    index = 15,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(3.60487e+39,'m^3/(mol*s)'), n=-9.93467, w0=(847,'kJ/mol'), E0=(360.535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(5.26371e-32,'m^3/(mol*s)'), n=10.6207, w0=(858.5,'kJ/mol'), E0=(200.708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07231419455600904, var=1.4282537120994365, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 2.5775442099795614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 2.5775442099795614""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 2.5775442099795614
""",
)

entry(
    index = 17,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.79815e-57,'m^3/(mol*s)'), n=17.6003, w0=(858.5,'kJ/mol'), E0=(172.559,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08999601536478366, var=0.819382087149775, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C
    Total Standard Deviation in ln(k): 2.04080134916133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C
Total Standard Deviation in ln(k): 2.04080134916133""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C
Total Standard Deviation in ln(k): 2.04080134916133
""",
)

entry(
    index = 18,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.81738e-32,'m^3/(mol*s)'), n=10.7934, w0=(858.5,'kJ/mol'), E0=(198.439,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.314224453363084, var=18.740375298614772, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C
    Total Standard Deviation in ln(k): 14.493163551375078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C
Total Standard Deviation in ln(k): 14.493163551375078""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C
Total Standard Deviation in ln(k): 14.493163551375078
""",
)

entry(
    index = 19,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.47171e-22,'m^3/(mol*s)'), n=7.45395, w0=(975,'kJ/mol'), E0=(132.437,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09645316148466385, var=5.447398172799303, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 4.921328515989122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 4.921328515989122""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 4.921328515989122
""",
)

entry(
    index = 20,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.4412e-11,'m^3/(mol*s)'), n=4.77399, w0=(925.071,'kJ/mol'), E0=(142.404,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003459835178213878, var=10.34397100876503, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 6.4563309129208095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.4563309129208095""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.4563309129208095
""",
)

entry(
    index = 21,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(12854.2,'m^3/(mol*s)'), n=0.363005, w0=(711,'kJ/mol'), E0=(209.858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13092469948580424, var=2.188844571310541, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 3.294910805299027"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.294910805299027""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.294910805299027
""",
)

entry(
    index = 22,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.00593317,'m^3/(mol*s)'), n=2.39407, w0=(657,'kJ/mol'), E0=(201.372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20958374420548082, var=23.189467532974728, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 10.18048302773957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 10.18048302773957""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 10.18048302773957
""",
)

entry(
    index = 23,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.9004e-47,'m^3/(mol*s)'), n=15.3086, w0=(720.833,'kJ/mol'), E0=(14.2022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.410497798294987, var=107.12484544893874, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 36.85601358740187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 36.85601358740187""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 36.85601358740187
""",
)

entry(
    index = 24,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.05542e-40,'m^3/(mol*s)'), n=13.4925, w0=(709.5,'kJ/mol'), E0=(11.844,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-15.39377220837538, var=629.3066547495009, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 88.96857415220366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 88.96857415220366""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 88.96857415220366
""",
)

entry(
    index = 25,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.7072e-32,'m^3/(mol*s)'), n=10.6641, w0=(858.5,'kJ/mol'), E0=(205.722,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10150844521884926, var=0.9739776605708466, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 2.2335255380422594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 2.2335255380422594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 2.2335255380422594
""",
)

entry(
    index = 26,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.426e-34,'m^3/(mol*s)'), n=11.2313, w0=(858.5,'kJ/mol'), E0=(184.207,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.49559e-59,'m^3/(mol*s)'), n=18.0744, w0=(858.5,'kJ/mol'), E0=(169.914,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(5.90471e-56,'m^3/(mol*s)'), n=17.182, w0=(858.5,'kJ/mol'), E0=(174.72,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(2.27623,'m^3/(mol*s)'), n=1.65169, w0=(858.5,'kJ/mol'), E0=(267.403,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11850573188331674, var=20.13791141603896, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 9.294058750944533"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 9.294058750944533""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 9.294058750944533
""",
)

entry(
    index = 30,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(4.21137e-35,'m^3/(mol*s)'), n=11.6452, w0=(858.5,'kJ/mol'), E0=(191.969,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.244894965209739, var=81.81036767728605, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br',), comment="""BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 33.823335976840745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 33.823335976840745""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 33.823335976840745
""",
)

entry(
    index = 31,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.42838e-22,'m^3/(mol*s)'), n=7.45902, w0=(975,'kJ/mol'), E0=(127.877,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.071251794730129, var=0.1538326540706309, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 0.9653119005319127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 0.9653119005319127""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 0.9653119005319127
""",
)

entry(
    index = 32,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.75808e-23,'m^3/(mol*s)'), n=7.59676, w0=(975,'kJ/mol'), E0=(140.227,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(5.55843e-19,'m^3/(mol*s)'), n=6.84857, w0=(916.75,'kJ/mol'), E0=(129.081,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.6650717562627406, var=15.051701822064967, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 14.473835207581896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 14.473835207581896""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 14.473835207581896
""",
)

entry(
    index = 34,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(1.18385e-06,'m^3/(mol*s)'), n=3.41154, w0=(936.167,'kJ/mol'), E0=(150.021,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9033657735519757, var=23.552825030798168, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.998993743729615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.998993743729615""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.998993743729615
""",
)

entry(
    index = 35,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(513.484,'m^3/(mol*s)'), n=0.745458, w0=(711,'kJ/mol'), E0=(208.015,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17663466986814985, var=3.301651939390025, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 4.086499224964572"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.086499224964572""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.086499224964572
""",
)

entry(
    index = 36,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.25801e+07,'m^3/(mol*s)'), n=-0.70794, w0=(711,'kJ/mol'), E0=(214.596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12884397773077047, var=0.8149612070781448, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 2.133507225129886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.133507225129886""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.133507225129886
""",
)

entry(
    index = 37,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(0.00284361,'m^3/(mol*s)'), n=2.5143, w0=(657,'kJ/mol'), E0=(210.075,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2720987557455209, var=35.40549888651742, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 12.612344123052404"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 12.612344123052404""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 12.612344123052404
""",
)

entry(
    index = 38,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(7.85783,'m^3/(mol*s)'), n=1.416, w0=(657,'kJ/mol'), E0=(183.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R",
    kinetics = ArrheniusBM(A=(23.9499,'m^3/(mol*s)'), n=1.57664, w0=(699.5,'kJ/mol'), E0=(220.022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11479703517840109, var=2.220048147829502, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R
    Total Standard Deviation in ln(k): 3.2754551443633115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R
Total Standard Deviation in ln(k): 3.2754551443633115""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R
Total Standard Deviation in ln(k): 3.2754551443633115
""",
)

entry(
    index = 40,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(6.69772e-21,'m^3/(mol*s)'), n=7.80389, w0=(763.5,'kJ/mol'), E0=(85.9267,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-9.156981682821263, var=216.45374797489583, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 52.50189021825118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.50189021825118""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.50189021825118
""",
)

entry(
    index = 41,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3CtO2d->Ct",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=-8.46126e-09, w0=(645.5,'kJ/mol'), E0=(276.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3CtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3CtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3CtO2d->Ct",
    kinetics = ArrheniusBM(A=(2.01929e-06,'m^3/(mol*s)'), n=3.68936, w0=(773.5,'kJ/mol'), E0=(107.273,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3CtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3CtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(6.67386e-32,'m^3/(mol*s)'), n=10.6691, w0=(858.5,'kJ/mol'), E0=(206.019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(3.32008e-32,'m^3/(mol*s)'), n=10.6591, w0=(858.5,'kJ/mol'), E0=(205.424,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-5R!H-R_N-3COCdCddCtO2d->Ct_Ext-6R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->F",
    kinetics = ArrheniusBM(A=(4.19774,'m^3/(mol*s)'), n=1.56561, w0=(858.5,'kJ/mol'), E0=(279.617,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09696238288917447, var=20.18938508515505, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->F
    Total Standard Deviation in ln(k): 9.251419935069492"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->F
Total Standard Deviation in ln(k): 9.251419935069492""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->F
Total Standard Deviation in ln(k): 9.251419935069492
""",
)

entry(
    index = 46,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_N-5R!H->F",
    kinetics = ArrheniusBM(A=(3.14941,'m^3/(mol*s)'), n=1.63113, w0=(858.5,'kJ/mol'), E0=(244.653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.64266e-35,'m^3/(mol*s)'), n=11.6647, w0=(858.5,'kJ/mol'), E0=(192.277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.2017971312038895, var=106.71551490547407, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 38.80452288065966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 38.80452288065966""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 38.80452288065966
""",
)

entry(
    index = 48,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.34415,'m^3/(mol*s)'), n=1.33734, w0=(858.5,'kJ/mol'), E0=(230.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.33914e-22,'m^3/(mol*s)'), n=7.52612, w0=(975,'kJ/mol'), E0=(127.622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(5.12094e-22,'m^3/(mol*s)'), n=7.38956, w0=(975,'kJ/mol'), E0=(128.152,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_5R!H->C_Ext-5C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.53378e-19,'m^3/(mol*s)'), n=6.84919, w0=(936.167,'kJ/mol'), E0=(128.922,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.3584487366122215, var=12.07838669496569, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.893001556830352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.893001556830352""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.893001556830352
""",
)

entry(
    index = 52,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F_3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(3.42263e-07,'m^3/(mol*s)'), n=3.56825, w0=(975,'kJ/mol'), E0=(145.992,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.226613633291675, var=24.606396859456062, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F_3CdO2d->O2d',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F_3CdO2d->O2d
    Total Standard Deviation in ln(k): 18.05152476543561"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F_3CdO2d->O2d
Total Standard Deviation in ln(k): 18.05152476543561""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F_3CdO2d->O2d
Total Standard Deviation in ln(k): 18.05152476543561
""",
)

entry(
    index = 53,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(24.851,'m^3/(mol*s)'), n=1.25249, w0=(858.5,'kJ/mol'), E0=(239.116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3CdO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3CdO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(24408.1,'m^3/(mol*s)'), n=0.242663, w0=(711,'kJ/mol'), E0=(208.95,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1534023098182822, var=3.4199111846926074, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
    Total Standard Deviation in ln(k): 4.092789894407894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.092789894407894""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.092789894407894
""",
)

entry(
    index = 55,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.10391,'m^3/(mol*s)'), n=1.64361, w0=(711,'kJ/mol'), E0=(221.034,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.25612e+07,'m^3/(mol*s)'), n=-0.637747, w0=(711,'kJ/mol'), E0=(216.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.6085e+08,'m^3/(mol*s)'), n=-0.88707, w0=(711,'kJ/mol'), E0=(213.432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(8.97967e+06,'m^3/(mol*s)'), n=-0.518739, w0=(711,'kJ/mol'), E0=(212.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.18878,'m^3/(mol*s)'), n=1.76475, w0=(657,'kJ/mol'), E0=(181.27,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.215904,'m^3/(mol*s)'), n=1.97485, w0=(657,'kJ/mol'), E0=(231.46,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15132305593789663, var=27.93122780529816, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.975234099349544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.975234099349544""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.975234099349544
""",
)

entry(
    index = 61,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(40.7026,'m^3/(mol*s)'), n=1.65435, w0=(699.5,'kJ/mol'), E0=(224.765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3CtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.62705,'m^3/(mol*s)'), n=1.85266, w0=(699.5,'kJ/mol'), E0=(214.967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3CtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3CtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.09358e-06,'m^3/(mol*s)'), n=3.74071, w0=(827.5,'kJ/mol'), E0=(116.096,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->F_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(12.1292,'m^3/(mol*s)'), n=1.44664, w0=(858.5,'kJ/mol'), E0=(294.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->F_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->F_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->F_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->F_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.87929e-35,'m^3/(mol*s)'), n=11.696, w0=(858.5,'kJ/mol'), E0=(192.335,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.845888739012167, var=158.76614346500145, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 47.48600180442763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 47.48600180442763""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->C_N-6BrClFINOPSSi->Br_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 47.48600180442763
""",
)

entry(
    index = 66,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R_3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(8.6637e-19,'m^3/(mol*s)'), n=6.79375, w0=(975,'kJ/mol'), E0=(129.226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11741340389425983, var=0.05674950254267688, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R_3CdO2d->O2d',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R_3CdO2d->O2d
    Total Standard Deviation in ln(k): 0.7725796317056121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R_3CdO2d->O2d
Total Standard Deviation in ln(k): 0.7725796317056121""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R_3CdO2d->O2d
Total Standard Deviation in ln(k): 0.7725796317056121
""",
)

entry(
    index = 67,
    label = "Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(14.8208,'m^3/(mol*s)'), n=1.21604, w0=(858.5,'kJ/mol'), E0=(215.271,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(25761.3,'m^3/(mol*s)'), n=0.211093, w0=(711,'kJ/mol'), E0=(206.552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1695122552558417, var=13.236968003731597, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
    Total Standard Deviation in ln(k): 7.719666496521855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.719666496521855""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.719666496521855
""",
)

entry(
    index = 69,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.59096e+06,'m^3/(mol*s)'), n=-0.339093, w0=(711,'kJ/mol'), E0=(221.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.825331,'m^3/(mol*s)'), n=1.69758, w0=(657,'kJ/mol'), E0=(221.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(3.63667,'m^3/(mol*s)'), n=1.59996, w0=(657,'kJ/mol'), E0=(251.549,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4061.07,'m^3/(mol*s)'), n=0.468608, w0=(711,'kJ/mol'), E0=(200.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18985986566819624, var=36.555013946038976, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.597811986024832"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.597811986024832""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.597811986024832
""",
)

entry(
    index = 73,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.0823032,'m^3/(mol*s)'), n=1.92336, w0=(711,'kJ/mol'), E0=(212.188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

