#!/usr/bin/env python
# encoding: utf-8

name = "CO2_Elimination_From_Carboxylic_Acid/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.80482e-10,'s^-1'), n=6.31106, w0=(828.5,'kJ/mol'), E0=(150.238,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6856092744279924, var=3.5327637889060415, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 5.490665826843616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 5.490665826843616""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 5.490665826843616
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.27393e-08,'s^-1'), n=5.90556, w0=(828.5,'kJ/mol'), E0=(157.739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7517040852964281, var=1.7222243127773855, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R-R
    Total Standard Deviation in ln(k): 4.519588626127731"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 4.519588626127731""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 4.519588626127731
""",
)

entry(
    index = 3,
    label = "Root_Ext-2R-R_7R!H->F",
    kinetics = ArrheniusBM(A=(5.85e-12,'s^-1'), n=6.85, w0=(828.5,'kJ/mol'), E0=(150.204,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-2R-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(6.04935e-08,'s^-1'), n=5.7141, w0=(828.5,'kJ/mol'), E0=(159.267,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7863492527824393, var=2.3323173669545096, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
    Total Standard Deviation in ln(k): 5.037368551540366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
Total Standard Deviation in ln(k): 5.037368551540366""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
Total Standard Deviation in ln(k): 5.037368551540366
""",
)

entry(
    index = 5,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(5.28676e-07,'s^-1'), n=5.44313, w0=(828.5,'kJ/mol'), E0=(157.604,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7373054776067633, var=2.551637827218717, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 5.0548594328365075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 5.0548594328365075""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 5.0548594328365075
""",
)

entry(
    index = 6,
    label = "Root_Ext-2R-R_N-7R!H->F_6F1sH->H",
    kinetics = ArrheniusBM(A=(181000,'s^-1'), n=2.09, w0=(828.5,'kJ/mol'), E0=(186.523,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H",
    kinetics = ArrheniusBM(A=(2.54e-21,'s^-1'), n=9.6, w0=(828.5,'kJ/mol'), E0=(141.606,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(0.000484572,'s^-1'), n=4.57718, w0=(828.5,'kJ/mol'), E0=(168.64,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9153582868497624, var=0.6930500693151496, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 3.9688297031806234"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 3.9688297031806234""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 3.9688297031806234
""",
)

entry(
    index = 9,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(1.15e-12,'s^-1'), n=7.1, w0=(828.5,'kJ/mol'), E0=(136.199,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H",
    kinetics = ArrheniusBM(A=(1.36e+06,'s^-1'), n=1.81, w0=(828.5,'kJ/mol'), E0=(186.177,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H",
    kinetics = ArrheniusBM(A=(2.1e-13,'s^-1'), n=7.32, w0=(828.5,'kJ/mol'), E0=(151.28,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

