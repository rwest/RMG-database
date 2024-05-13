#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.75329e+17,'m^3/(mol*s)'), n=-3.27013, w0=(490.05,'kJ/mol'), E0=(144.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12545146432007043, var=3.6548751292832975, Tref=1000.0, N=20, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 20 training reactions at node Root
    Total Standard Deviation in ln(k): 4.147802618957837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 4.147802618957837""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 4.147802618957837
""",
)

entry(
    index = 2,
    label = "Root_Ext-3R-R",
    kinetics = ArrheniusBM(A=(6.66057e-08,'m^3/(mol*s)'), n=3.77507, w0=(510.938,'kJ/mol'), E0=(79.4751,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5656263926106384, var=2.448833520872592, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-3R-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-3R-R
    Total Standard Deviation in ln(k): 4.558331488193289"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 4.558331488193289""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 4.558331488193289
""",
)

entry(
    index = 3,
    label = "Root_Ext-1R-R",
    kinetics = ArrheniusBM(A=(2.5716e+09,'m^3/(mol*s)'), n=-0.704858, w0=(474.2,'kJ/mol'), E0=(76.9274,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05741501950261313, var=0.5893390070868847, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1R-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1R-R
    Total Standard Deviation in ln(k): 1.683262255941087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1R-R
Total Standard Deviation in ln(k): 1.683262255941087""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1R-R
Total Standard Deviation in ln(k): 1.683262255941087
""",
)

entry(
    index = 4,
    label = "Root_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.33384e+09,'m^3/(mol*s)'), n=-0.775738, w0=(480,'kJ/mol'), E0=(85.117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03181634111081507, var=0.14337316328675037, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R-R
    Total Standard Deviation in ln(k): 0.8390264530712139"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264530712139""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264530712139
""",
)

entry(
    index = 5,
    label = "Root_Sp-2R=1R",
    kinetics = ArrheniusBM(A=(5.30859e+06,'m^3/(mol*s)'), n=-0.130328, w0=(480,'kJ/mol'), E0=(154.657,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7979378620014449, var=0.4192186486563715, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Sp-2R=1R',), comment="""BM rule fitted to 2 training reactions at node Root_Sp-2R=1R
    Total Standard Deviation in ln(k): 3.3028767522512736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Sp-2R=1R
Total Standard Deviation in ln(k): 3.3028767522512736""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Sp-2R=1R
Total Standard Deviation in ln(k): 3.3028767522512736
""",
)

entry(
    index = 6,
    label = "Root_N-Sp-2R=1R",
    kinetics = ArrheniusBM(A=(1.52735e+09,'m^3/(mol*s)'), n=-0.643653, w0=(462.5,'kJ/mol'), E0=(85.8622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-Sp-2R=1R',), comment="""BM rule fitted to 1 training reactions at node Root_N-Sp-2R=1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-Sp-2R=1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-Sp-2R=1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-3R-R_4R!H->F",
    kinetics = ArrheniusBM(A=(2.62709e-20,'m^3/(mol*s)'), n=7.32271, w0=(523.25,'kJ/mol'), E0=(45.7061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5578640797649229, var=1.6799701240706584, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_4R!H->F
    Total Standard Deviation in ln(k): 4.000079078787853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_4R!H->F
Total Standard Deviation in ln(k): 4.000079078787853""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_4R!H->F
Total Standard Deviation in ln(k): 4.000079078787853
""",
)

entry(
    index = 8,
    label = "Root_Ext-3R-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(0.531386,'m^3/(mol*s)'), n=1.91075, w0=(474,'kJ/mol'), E0=(98.7387,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0577200283147992, var=2.936408170988897, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-4R!H->F
    Total Standard Deviation in ln(k): 3.5803294046746075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.5803294046746075""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.5803294046746075
""",
)

entry(
    index = 9,
    label = "Root_Ext-1R-R_Ext-1R-R",
    kinetics = ArrheniusBM(A=(3.18e+07,'m^3/(mol*s)'), n=3.3438e-08, w0=(486,'kJ/mol'), E0=(121.323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R-R_Ext-1R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Ext-1R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Ext-1R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Ext-1R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-1R-R_Sp-2R=1R",
    kinetics = ArrheniusBM(A=(9.41381e+08,'m^3/(mol*s)'), n=-0.607357, w0=(480,'kJ/mol'), E0=(101.897,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8061640705246433, var=0.27679018700136016, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R-R_Sp-2R=1R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R-R_Sp-2R=1R
    Total Standard Deviation in ln(k): 3.080246093414736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R-R_Sp-2R=1R
Total Standard Deviation in ln(k): 3.080246093414736""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R-R_Sp-2R=1R
Total Standard Deviation in ln(k): 3.080246093414736
""",
)

entry(
    index = 11,
    label = "Root_Ext-1R-R_N-Sp-2R=1R",
    kinetics = ArrheniusBM(A=(4.65123e+09,'m^3/(mol*s)'), n=-0.763972, w0=(462.5,'kJ/mol'), E0=(90.9129,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13960078154398048, var=0.8124977917121713, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R-R_N-Sp-2R=1R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R
    Total Standard Deviation in ln(k): 2.1577970556617916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R
Total Standard Deviation in ln(k): 2.1577970556617916""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R
Total Standard Deviation in ln(k): 2.1577970556617916
""",
)

entry(
    index = 12,
    label = "Root_Ext-2R-R_3R->C",
    kinetics = ArrheniusBM(A=(4.13595e+09,'m^3/(mol*s)'), n=-0.801251, w0=(474,'kJ/mol'), E0=(97.1562,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18237254735357986, var=0.005024605625150487, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R-R_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R-R_3R->C
    Total Standard Deviation in ln(k): 0.6003270294241436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.6003270294241436""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.6003270294241436
""",
)

entry(
    index = 13,
    label = "Root_Ext-2R-R_N-3R->C",
    kinetics = ArrheniusBM(A=(3.86082e+06,'m^3/(mol*s)'), n=0.0243326, w0=(486,'kJ/mol'), E0=(92.826,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0038925227441374026, var=1.6818078495915973, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R-R_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-3R->C
    Total Standard Deviation in ln(k): 2.609611561551256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.609611561551256""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.609611561551256
""",
)

entry(
    index = 14,
    label = "Root_Sp-2R=1R_3R->C",
    kinetics = ArrheniusBM(A=(1.98e+06,'m^3/(mol*s)'), n=-1.4347e-08, w0=(474,'kJ/mol'), E0=(153.583,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-2R=1R_3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_Sp-2R=1R_N-3R->C",
    kinetics = ArrheniusBM(A=(700000,'m^3/(mol*s)'), n=1.22665e-08, w0=(486,'kJ/mol'), E0=(119.69,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-2R=1R_N-3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_N-3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-2R=1R_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_Ext-3R-R_4R!H->F_Ext-1R-R",
    kinetics = ArrheniusBM(A=(5.95205e-05,'m^3/(mol*s)'), n=2.93905, w0=(539.667,'kJ/mol'), E0=(85.9268,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40468144849022886, var=0.12740114560488622, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-1R-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R
    Total Standard Deviation in ln(k): 1.7323436057517703"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R
Total Standard Deviation in ln(k): 1.7323436057517703""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R
Total Standard Deviation in ln(k): 1.7323436057517703
""",
)

entry(
    index = 17,
    label = "Root_Ext-3R-R_4R!H->F_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.01799e-05,'m^3/(mol*s)'), n=2.87159, w0=(474,'kJ/mol'), E0=(101.042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_Ext-3R-R_4R!H->F_2R->C",
    kinetics = ArrheniusBM(A=(2.07011e-05,'m^3/(mol*s)'), n=2.98446, w0=(474,'kJ/mol'), E0=(119.563,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_Ext-3R-R_4R!H->F_N-2R->C",
    kinetics = ArrheniusBM(A=(4.81575e-05,'m^3/(mol*s)'), n=2.76922, w0=(572.5,'kJ/mol'), E0=(109.078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->Br",
    kinetics = ArrheniusBM(A=(0.000161154,'m^3/(mol*s)'), n=2.94391, w0=(474,'kJ/mol'), E0=(70.9316,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->Br",
    kinetics = ArrheniusBM(A=(8.68219e-05,'m^3/(mol*s)'), n=2.97056, w0=(474,'kJ/mol'), E0=(87.4167,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_Ext-1R-R_Sp-2R=1R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.54e+07,'m^3/(mol*s)'), n=2.17787e-08, w0=(486,'kJ/mol'), E0=(120.733,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R-R_Sp-2R=1R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Sp-2R=1R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Sp-2R=1R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R-R_Sp-2R=1R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_Ext-1R-R_N-Sp-2R=1R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.29568e+09,'m^3/(mol*s)'), n=-0.811807, w0=(462.5,'kJ/mol'), E0=(82.3565,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R-R_N-Sp-2R=1R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R-R_N-Sp-2R=1R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_Ext-2R-R_3R->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.40609e+09,'m^3/(mol*s)'), n=-0.732703, w0=(474,'kJ/mol'), E0=(102.225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_3R->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_3R->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_3R->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_3R->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_Ext-2R-R_N-3R->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(7.2835e+06,'m^3/(mol*s)'), n=-2.41431e-09, w0=(486,'kJ/mol'), E0=(122.28,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-3R->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-3R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-1R-R",
    kinetics = ArrheniusBM(A=(4.10298e-06,'m^3/(mol*s)'), n=3.07477, w0=(474,'kJ/mol'), E0=(78.6589,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-1R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-1R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-1R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-1R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-3R-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.16512e-05,'m^3/(mol*s)'), n=3.02553, w0=(572.5,'kJ/mol'), E0=(84.8245,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-3R-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-3R-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-3R-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-3R-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-3R-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00422096,'m^3/(mol*s)'), n=2.4132, w0=(572.5,'kJ/mol'), E0=(91.0734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-3R-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-3R-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-3R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_4R!H->F_Ext-1R-R_Ext-3R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

