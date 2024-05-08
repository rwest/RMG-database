#!/usr/bin/env python
# encoding: utf-8

name = "F_Abstraction/rules"
shortDesc = ""
longDesc = """
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')


.. [MRHCBSQB3RRHO] M.R. Harper (mrharper_at_mit_dot_edu or michael.harper.jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 calculations.  The zero-point
energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the
temperatures used were: 300, 331, 370, 419, 482, 568, 692, 885, 1227, 2000 (evenly spaced on inverse temperature scale).

.. [Tsang1990] W. Tsang; "Chemical kinetic database for combustion chemistry. Part IV. Isobutane" J. Phys. Chem. Ref. Data 19 (1990) 1-68

.. [Tsang1991] W. Tsang; "Chemical kinetic database for combustion chemistry. Part V. Propene" J. Phys. Chem. Ref. Data 20 (1991) 221-273
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.18275e+32,'m^3/(mol*s)'), n=-7.21551, w0=(412.907,'kJ/mol'), E0=(253.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0483388487029361, var=15.78707158741778, Tref=1000.0, N=242, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 242 training reactions at node Root
    Total Standard Deviation in ln(k): 10.599420671156583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 242 training reactions at node Root
Total Standard Deviation in ln(k): 10.599420671156583""",
    longDesc = 
"""
BM rule fitted to 242 training reactions at node Root
Total Standard Deviation in ln(k): 10.599420671156583
""",
)

entry(
    index = 2,
    label = "Root_1R->O",
    kinetics = ArrheniusBM(A=(1.73475e-08,'m^3/(mol*s)'), n=4.31664, w0=(337.688,'kJ/mol'), E0=(90.8082,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23667947009167778, var=5.657209055592099, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_1R->O',), comment="""BM rule fitted to 64 training reactions at node Root_1R->O
    Total Standard Deviation in ln(k): 5.362911999299268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 5.362911999299268""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 5.362911999299268
""",
)

entry(
    index = 3,
    label = "Root_N-1R->O",
    kinetics = ArrheniusBM(A=(2.17787e+32,'m^3/(mol*s)'), n=-7.1671, w0=(439.952,'kJ/mol'), E0=(257.186,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0511232967320965, var=15.450865490332328, Tref=1000.0, N=178, data_mean=0.0, correlation='Root_N-1R->O',), comment="""BM rule fitted to 178 training reactions at node Root_N-1R->O
    Total Standard Deviation in ln(k): 10.521143545883834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 178 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 10.521143545883834""",
    longDesc = 
"""
BM rule fitted to 178 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 10.521143545883834
""",
)

entry(
    index = 4,
    label = "Root_1R->O_3R->O",
    kinetics = ArrheniusBM(A=(0.00260556,'m^3/(mol*s)'), n=3.27627, w0=(222,'kJ/mol'), E0=(115.626,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.036752845216295384, var=0.5693204511070572, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_3R->O',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
    Total Standard Deviation in ln(k): 1.604983139746785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.604983139746785""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.604983139746785
""",
)

entry(
    index = 5,
    label = "Root_1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(43664.4,'m^3/(mol*s)'), n=0.69816, w0=(354.214,'kJ/mol'), E0=(142.573,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1996541663901872, var=4.918396511160094, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_1R->O_N-3R->O',), comment="""BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
    Total Standard Deviation in ln(k): 4.947636467287426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 4.947636467287426""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 4.947636467287426
""",
)

entry(
    index = 6,
    label = "Root_N-1R->O_3R->O",
    kinetics = ArrheniusBM(A=(2.22035e-08,'m^3/(mol*s)'), n=4.54728, w0=(354.214,'kJ/mol'), E0=(78.5583,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21046015635618792, var=5.189897932001944, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->O_3R->O',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
    Total Standard Deviation in ln(k): 5.095851003911071"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.095851003911071""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.095851003911071
""",
)

entry(
    index = 7,
    label = "Root_N-1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(1.90268e+18,'m^3/(mol*s)'), n=-3.19717, w0=(479.308,'kJ/mol'), E0=(226.955,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7002480375764546, var=11.918367279291203, Tref=1000.0, N=122, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O',), comment="""BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
    Total Standard Deviation in ln(k): 8.680361761636437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.680361761636437""",
    longDesc = 
"""
BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.680361761636437
""",
)

entry(
    index = 8,
    label = "Root_1R->O_3R->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.055903,'m^3/(mol*s)'), n=2.89378, w0=(222,'kJ/mol'), E0=(116.309,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1724090644624907, var=5.673959632543975, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
    Total Standard Deviation in ln(k): 7.721045367079437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 7.721045367079437""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 7.721045367079437
""",
)

entry(
    index = 9,
    label = "Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.78103e-05,'m^3/(mol*s)'), n=4.01585, w0=(222,'kJ/mol'), E0=(70.6039,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R->O_3R->O_1O-u0",
    kinetics = ArrheniusBM(A=(1.23762e-05,'m^3/(mol*s)'), n=3.94655, w0=(222,'kJ/mol'), E0=(112.656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1R->O_3R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(0.00783498,'m^3/(mol*s)'), n=2.69738, w0=(222,'kJ/mol'), E0=(118.453,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33657502554653357, var=0.8872667435796786, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 2.7340228443593158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 2.7340228443593158""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 2.7340228443593158
""",
)

entry(
    index = 12,
    label = "Root_1R->O_N-3R->O_1O-u0",
    kinetics = ArrheniusBM(A=(101.717,'m^3/(mol*s)'), n=1.46541, w0=(354.37,'kJ/mol'), E0=(125.705,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14955065124664535, var=3.1616447996638546, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0',), comment="""BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
    Total Standard Deviation in ln(k): 3.940377771822579"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
Total Standard Deviation in ln(k): 3.940377771822579""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
Total Standard Deviation in ln(k): 3.940377771822579
""",
)

entry(
    index = 13,
    label = "Root_1R->O_N-3R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(1.36024e-18,'m^3/(mol*s)'), n=7.09782, w0=(353.5,'kJ/mol'), E0=(35.7787,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7622302010161461, var=9.457882443919765, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 8.080447444087097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
Total Standard Deviation in ln(k): 8.080447444087097""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
Total Standard Deviation in ln(k): 8.080447444087097
""",
)

entry(
    index = 14,
    label = "Root_N-1R->O_3R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(5.58569e-09,'m^3/(mol*s)'), n=4.6612, w0=(355.318,'kJ/mol'), E0=(51.8051,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5052751173514685, var=2.2904690720075918, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 4.303560822610654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.303560822610654""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.303560822610654
""",
)

entry(
    index = 15,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(8.54156,'m^3/(mol*s)'), n=2.20434, w0=(353.5,'kJ/mol'), E0=(115.715,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1451643580745743, var=11.836223581781356, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 7.261787666666046"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.261787666666046""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.261787666666046
""",
)

entry(
    index = 16,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(3.96794e+11,'m^3/(mol*s)'), n=-1.05053, w0=(353.5,'kJ/mol'), E0=(176.513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.013459375624522, var=8.189175368670764, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 8.283277638128807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 8.283277638128807""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 8.283277638128807
""",
)

entry(
    index = 17,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(0.226765,'m^3/(mol*s)'), n=2.32228, w0=(326.667,'kJ/mol'), E0=(102.333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18791384503514852, var=1.3699378876207615, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 2.818574394997453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 2.818574394997453""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 2.818574394997453
""",
)

entry(
    index = 18,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(2.29041e+12,'m^3/(mol*s)'), n=-1.50257, w0=(487.203,'kJ/mol'), E0=(213.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5484146766600575, var=11.64434360815262, Tref=1000.0, N=116, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F',), comment="""BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 8.218846070106268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 8.218846070106268""",
    longDesc = 
"""
BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 8.218846070106268
""",
)

entry(
    index = 19,
    label = "Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.0487535,'m^3/(mol*s)'), n=3.06244, w0=(222,'kJ/mol'), E0=(73.7386,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0050127,'m^3/(mol*s)'), n=3.19461, w0=(222,'kJ/mol'), E0=(113.917,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2816212367218442, var=4.885137075355415, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 7.651088733053727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 7.651088733053727""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 7.651088733053727
""",
)

entry(
    index = 21,
    label = "Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(16.3524,'m^3/(mol*s)'), n=1.88723, w0=(222,'kJ/mol'), E0=(114.005,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000349001,'m^3/(mol*s)'), n=3.12783, w0=(222,'kJ/mol'), E0=(120.019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00111026,'m^3/(mol*s)'), n=2.89721, w0=(222,'kJ/mol'), E0=(111.151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1",
    kinetics = ArrheniusBM(A=(372.444,'m^3/(mol*s)'), n=1.2849, w0=(354.611,'kJ/mol'), E0=(126.283,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11993696686466995, var=4.090808654949423, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1',), comment="""BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
    Total Standard Deviation in ln(k): 4.3560757286021055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 4.3560757286021055""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 4.3560757286021055
""",
)

entry(
    index = 25,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1",
    kinetics = ArrheniusBM(A=(1.18258e-06,'m^3/(mol*s)'), n=3.82407, w0=(353.5,'kJ/mol'), E0=(68.1009,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.021426051066772273, var=1.1600349527496812, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
    Total Standard Deviation in ln(k): 2.213032585846549"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 2.213032585846549""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 2.213032585846549
""",
)

entry(
    index = 26,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(5.85564e-18,'m^3/(mol*s)'), n=6.8523, w0=(353.5,'kJ/mol'), E0=(40.1464,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8065048810866946, var=27.31167461846304, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 15.015817318884356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
Total Standard Deviation in ln(k): 15.015817318884356""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
Total Standard Deviation in ln(k): 15.015817318884356
""",
)

entry(
    index = 27,
    label = "Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1",
    kinetics = ArrheniusBM(A=(0.00154,'m^3/(mol*s)'), n=2.64, w0=(353.5,'kJ/mol'), E0=(109.474,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1",
    kinetics = ArrheniusBM(A=(0.000996795,'m^3/(mol*s)'), n=2.97758, w0=(353.5,'kJ/mol'), E0=(143.478,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O",
    kinetics = ArrheniusBM(A=(8.25845e-08,'m^3/(mol*s)'), n=4.30169, w0=(353.5,'kJ/mol'), E0=(55.6824,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5320389674504705, var=7.212378013463658, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
    Total Standard Deviation in ln(k): 6.720671966288587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
Total Standard Deviation in ln(k): 6.720671966288587""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
Total Standard Deviation in ln(k): 6.720671966288587
""",
)

entry(
    index = 30,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(3.13552e-09,'m^3/(mol*s)'), n=4.76996, w0=(357.136,'kJ/mol'), E0=(83.1722,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30536411420096377, var=3.4549529161927404, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
    Total Standard Deviation in ln(k): 4.493548573204615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.493548573204615""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.493548573204615
""",
)

entry(
    index = 31,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(5.66274,'m^3/(mol*s)'), n=2.25343, w0=(353.5,'kJ/mol'), E0=(114.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16262981494737486, var=13.020683692902718, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 7.642540661294257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 7.642540661294257""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 7.642540661294257
""",
)

entry(
    index = 32,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1",
    kinetics = ArrheniusBM(A=(0.00178228,'m^3/(mol*s)'), n=3.45178, w0=(353.5,'kJ/mol'), E0=(103.593,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.00777061,'m^3/(mol*s)'), n=2.94264, w0=(353.5,'kJ/mol'), E0=(110.122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.0296322,'m^3/(mol*s)'), n=2.63787, w0=(353.5,'kJ/mol'), E0=(85.6902,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.454935461017857, var=9.979557397852652, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 12.501225361688878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 12.501225361688878""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 12.501225361688878
""",
)

entry(
    index = 35,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1",
    kinetics = ArrheniusBM(A=(0.00226498,'m^3/(mol*s)'), n=3.15133, w0=(353.5,'kJ/mol'), E0=(127.791,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.0286832,'m^3/(mol*s)'), n=2.78907, w0=(353.5,'kJ/mol'), E0=(145.222,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C",
    kinetics = ArrheniusBM(A=(0.0789065,'m^3/(mol*s)'), n=2.39473, w0=(320,'kJ/mol'), E0=(92.9853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04515383313028233, var=0.6729740906603394, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
    Total Standard Deviation in ln(k): 1.7580362238719847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
Total Standard Deviation in ln(k): 1.7580362238719847""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
Total Standard Deviation in ln(k): 1.7580362238719847
""",
)

entry(
    index = 38,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C",
    kinetics = ArrheniusBM(A=(29364.5,'m^3/(mol*s)'), n=0.785655, w0=(360,'kJ/mol'), E0=(105.951,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H",
    kinetics = ArrheniusBM(A=(6.88924,'m^3/(mol*s)'), n=2.05277, w0=(518.487,'kJ/mol'), E0=(170.86,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5390853411515534, var=5.414673541319147, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
    Total Standard Deviation in ln(k): 6.019394265410274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 6.019394265410274""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 6.019394265410274
""",
)

entry(
    index = 40,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H",
    kinetics = ArrheniusBM(A=(9.0243e+14,'m^3/(mol*s)'), n=-2.32233, w0=(481.457,'kJ/mol'), E0=(224.373,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5069678137043281, var=10.25557490908337, Tref=1000.0, N=98, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H',), comment="""BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
    Total Standard Deviation in ln(k): 7.693817552887421"""),
    rank = 11,
    shortDesc = """BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 7.693817552887421""",
    longDesc = 
"""
BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 7.693817552887421
""",
)

entry(
    index = 41,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.0049864,'m^3/(mol*s)'), n=3.19625, w0=(222,'kJ/mol'), E0=(113.899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.640932,'m^3/(mol*s)'), n=2.39839, w0=(222,'kJ/mol'), E0=(121.66,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.0497566,'m^3/(mol*s)'), n=2.34816, w0=(353.5,'kJ/mol'), E0=(109.126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0811141239584698, var=3.891783489645067, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R',), comment="""BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 4.15866625078613"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 4.15866625078613""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 4.15866625078613
""",
)

entry(
    index = 44,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C",
    kinetics = ArrheniusBM(A=(5.15234e-10,'m^3/(mol*s)'), n=4.89163, w0=(353.5,'kJ/mol'), E0=(58.4821,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11556907246477377, var=4.555154169616789, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C
    Total Standard Deviation in ln(k): 4.569041967920268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C
Total Standard Deviation in ln(k): 4.569041967920268""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C
Total Standard Deviation in ln(k): 4.569041967920268
""",
)

entry(
    index = 45,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C",
    kinetics = ArrheniusBM(A=(1.04105,'m^3/(mol*s)'), n=2.3137, w0=(393.5,'kJ/mol'), E0=(121.365,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000243512,'m^3/(mol*s)'), n=3.10269, w0=(353.5,'kJ/mol'), E0=(63.061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.1735962744220383, var=15.055681404681717, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 13.240000305999205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 13.240000305999205""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 13.240000305999205
""",
)

entry(
    index = 47,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000178698,'m^3/(mol*s)'), n=3.25898, w0=(353.5,'kJ/mol'), E0=(114.976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH",
    kinetics = ArrheniusBM(A=(3.84155e-15,'m^3/(mol*s)'), n=6.04112, w0=(353.5,'kJ/mol'), E0=(67.6656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5510540352146855, var=10.776145545379674, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH',), comment="""BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
    Total Standard Deviation in ln(k): 10.478072547091966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 10.478072547091966""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 10.478072547091966
""",
)

entry(
    index = 49,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH",
    kinetics = ArrheniusBM(A=(0.00171,'m^3/(mol*s)'), n=2.75, w0=(353.5,'kJ/mol'), E0=(229.203,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(6.48899e-06,'m^3/(mol*s)'), n=3.82442, w0=(353.5,'kJ/mol'), E0=(85.4083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9396428849760203, var=1.0004219207875718, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 4.366069723791786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 4.366069723791786""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 4.366069723791786
""",
)

entry(
    index = 51,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(2.87155e-06,'m^3/(mol*s)'), n=3.81738, w0=(353.5,'kJ/mol'), E0=(116.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2040684330408316, var=12.148287206055842, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 10.012680021770944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 10.012680021770944""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 10.012680021770944
""",
)

entry(
    index = 52,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(1.36063,'m^3/(mol*s)'), n=2.30961, w0=(353.5,'kJ/mol'), E0=(120.785,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2181402138809169, var=2.046637930924142, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 3.41608010526488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 3.41608010526488""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 3.41608010526488
""",
)

entry(
    index = 53,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(4.02018e-06,'m^3/(mol*s)'), n=3.69274, w0=(393.5,'kJ/mol'), E0=(112.743,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.72013,'m^3/(mol*s)'), n=2.4493, w0=(353.5,'kJ/mol'), E0=(175.466,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(7.6846,'m^3/(mol*s)'), n=2.21538, w0=(353.5,'kJ/mol'), E0=(115.203,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16533244088372143, var=13.014345148295261, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 7.647570206464167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.647570206464167""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.647570206464167
""",
)

entry(
    index = 56,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(0.0330707,'m^3/(mol*s)'), n=2.62302, w0=(353.5,'kJ/mol'), E0=(85.6902,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.4830505825211278, var=15.980728412116331, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
    Total Standard Deviation in ln(k): 16.765492924147406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 16.765492924147406""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 16.765492924147406
""",
)

entry(
    index = 57,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(0.0387235,'m^3/(mol*s)'), n=2.8378, w0=(353.5,'kJ/mol'), E0=(143.541,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0108084,'m^3/(mol*s)'), n=2.63211, w0=(320,'kJ/mol'), E0=(83.1131,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.38328272815508785, var=1.386136735584043, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.3232829070777314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.3232829070777314""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.3232829070777314
""",
)

entry(
    index = 59,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C",
    kinetics = ArrheniusBM(A=(1.28736e-10,'m^3/(mol*s)'), n=5.14452, w0=(525,'kJ/mol'), E0=(147.122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3450931838080353, var=3.7522211847802573, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C
    Total Standard Deviation in ln(k): 4.750370645467857"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C
Total Standard Deviation in ln(k): 4.750370645467857""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C
Total Standard Deviation in ln(k): 4.750370645467857
""",
)

entry(
    index = 60,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C",
    kinetics = ArrheniusBM(A=(650.29,'m^3/(mol*s)'), n=1.25799, w0=(407.77,'kJ/mol'), E0=(121.038,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C",
    kinetics = ArrheniusBM(A=(3.30002e-10,'m^3/(mol*s)'), n=4.65594, w0=(492.473,'kJ/mol'), E0=(167.787,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12632863240400832, var=4.565427046515618, Tref=1000.0, N=91, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C',), comment="""BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
    Total Standard Deviation in ln(k): 4.600897990163967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 4.600897990163967""",
    longDesc = 
"""
BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 4.600897990163967
""",
)

entry(
    index = 62,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C",
    kinetics = ArrheniusBM(A=(54.4407,'m^3/(mol*s)'), n=1.73634, w0=(338.253,'kJ/mol'), E0=(105.167,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7973113264661945, var=16.620561348476333, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
    Total Standard Deviation in ln(k): 10.176263444166322"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 10.176263444166322""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 10.176263444166322
""",
)

entry(
    index = 63,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(6.00396e-06,'m^3/(mol*s)'), n=3.34586, w0=(353.5,'kJ/mol'), E0=(99.0453,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.8745163303647105, var=15.325387050022494, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
    Total Standard Deviation in ln(k): 15.070470078933367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.070470078933367""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.070470078933367
""",
)

entry(
    index = 64,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000248734,'m^3/(mol*s)'), n=3.02608, w0=(353.5,'kJ/mol'), E0=(96.3708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04233874692314541, var=4.590416442976733, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl',), comment="""BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.401575217849266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.401575217849266""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.401575217849266
""",
)

entry(
    index = 65,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.0397008,'m^3/(mol*s)'), n=2.50107, w0=(353.5,'kJ/mol'), E0=(107.938,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12437712088793257, var=0.09164906457635345, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R
    Total Standard Deviation in ln(k): 0.919410737326386"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R
Total Standard Deviation in ln(k): 0.919410737326386""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R
Total Standard Deviation in ln(k): 0.919410737326386
""",
)

entry(
    index = 66,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000339668,'m^3/(mol*s)'), n=3.06046, w0=(353.5,'kJ/mol'), E0=(73.613,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.908353259024145, var=69.27972454642182, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 31.53140938750785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 31.53140938750785""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 31.53140938750785
""",
)

entry(
    index = 67,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.86239e-05,'m^3/(mol*s)'), n=3.19145, w0=(353.5,'kJ/mol'), E0=(113.238,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C",
    kinetics = ArrheniusBM(A=(6.428e-13,'m^3/(mol*s)'), n=5.70143, w0=(353.5,'kJ/mol'), E0=(76.2381,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3091925662492475, var=2.7326877652302333, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
    Total Standard Deviation in ln(k): 4.090861864235122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 4.090861864235122""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 4.090861864235122
""",
)

entry(
    index = 69,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(7.68958e-06,'m^3/(mol*s)'), n=3.64649, w0=(353.5,'kJ/mol'), E0=(106.985,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F",
    kinetics = ArrheniusBM(A=(9.10924e-11,'m^3/(mol*s)'), n=4.70432, w0=(353.5,'kJ/mol'), E0=(116.625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19091325327397948, var=1.7019013969710648, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F
    Total Standard Deviation in ln(k): 3.0949976375536687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F
Total Standard Deviation in ln(k): 3.0949976375536687""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F
Total Standard Deviation in ln(k): 3.0949976375536687
""",
)

entry(
    index = 71,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F",
    kinetics = ArrheniusBM(A=(0.000306618,'m^3/(mol*s)'), n=2.97029, w0=(353.5,'kJ/mol'), E0=(109.815,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3131898711653833, var=3.1154562374237282, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F
    Total Standard Deviation in ln(k): 6.837960770150062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F
Total Standard Deviation in ln(k): 6.837960770150062""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F
Total Standard Deviation in ln(k): 6.837960770150062
""",
)

entry(
    index = 72,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(6.52868e-06,'m^3/(mol*s)'), n=3.82325, w0=(353.5,'kJ/mol'), E0=(85.4083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9618926764242669, var=1.0652005473589135, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 4.485873840719345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 4.485873840719345""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 4.485873840719345
""",
)

entry(
    index = 73,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(1.07573e+15,'m^3/(mol*s)'), n=-2.16232, w0=(353.5,'kJ/mol'), E0=(179.737,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2868794112918802, var=91.80779699984247, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 19.929449409333007"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 19.929449409333007""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 19.929449409333007
""",
)

entry(
    index = 74,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F",
    kinetics = ArrheniusBM(A=(1338.35,'m^3/(mol*s)'), n=1.49764, w0=(353.5,'kJ/mol'), E0=(132.52,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01522775266368761, var=0.5148570069190597, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F
    Total Standard Deviation in ln(k): 1.47672901020071"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F
Total Standard Deviation in ln(k): 1.47672901020071""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F
Total Standard Deviation in ln(k): 1.47672901020071
""",
)

entry(
    index = 75,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F",
    kinetics = ArrheniusBM(A=(0.000635818,'m^3/(mol*s)'), n=3.24928, w0=(353.5,'kJ/mol'), E0=(107.269,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7853855271379451, var=4.633895826089613, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F
    Total Standard Deviation in ln(k): 6.288820549228972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F
Total Standard Deviation in ln(k): 6.288820549228972""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F
Total Standard Deviation in ln(k): 6.288820549228972
""",
)

entry(
    index = 76,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F",
    kinetics = ArrheniusBM(A=(134348,'m^3/(mol*s)'), n=1.03897, w0=(353.5,'kJ/mol'), E0=(147.751,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.31182430643289655, var=2.124957582806492, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F
    Total Standard Deviation in ln(k): 3.7058274394243407"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F
Total Standard Deviation in ln(k): 3.7058274394243407""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F
Total Standard Deviation in ln(k): 3.7058274394243407
""",
)

entry(
    index = 77,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F",
    kinetics = ArrheniusBM(A=(233179,'m^3/(mol*s)'), n=0.91632, w0=(353.5,'kJ/mol'), E0=(126.178,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11083354023640649, var=24.09184131655612, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F
    Total Standard Deviation in ln(k): 10.118405721394973"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F
Total Standard Deviation in ln(k): 10.118405721394973""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F
Total Standard Deviation in ln(k): 10.118405721394973
""",
)

entry(
    index = 78,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O",
    kinetics = ArrheniusBM(A=(0.045959,'m^3/(mol*s)'), n=2.57537, w0=(353.5,'kJ/mol'), E0=(96.496,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.238499049893909, var=14.682147066525392, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O
    Total Standard Deviation in ln(k): 15.818533803075436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O
Total Standard Deviation in ln(k): 15.818533803075436""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O
Total Standard Deviation in ln(k): 15.818533803075436
""",
)

entry(
    index = 79,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.79251e+20,'m^3/(mol*s)'), n=-3.40625, w0=(353.5,'kJ/mol'), E0=(173.367,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3731970243679851, var=68.968334589228, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O
    Total Standard Deviation in ln(k): 17.586439667259707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O
Total Standard Deviation in ln(k): 17.586439667259707""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O
Total Standard Deviation in ln(k): 17.586439667259707
""",
)

entry(
    index = 80,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0823982,'m^3/(mol*s)'), n=2.3774, w0=(320,'kJ/mol'), E0=(92.9853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03260278863169289, var=0.347577085683609, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.2638215223370808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.2638215223370808""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.2638215223370808
""",
)

entry(
    index = 81,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.82491e-11,'m^3/(mol*s)'), n=5.19131, w0=(525,'kJ/mol'), E0=(146.929,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34424079816654224, var=3.718841962090094, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.730917736462499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.730917736462499""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.730917736462499
""",
)

entry(
    index = 82,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1",
    kinetics = ArrheniusBM(A=(3.08184e-10,'m^3/(mol*s)'), n=4.6642, w0=(493,'kJ/mol'), E0=(167.728,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12714455365360736, var=4.5456045184191805, Tref=1000.0, N=85, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1',), comment="""BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
    Total Standard Deviation in ln(k): 4.593638733073305"""),
    rank = 11,
    shortDesc = """BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
Total Standard Deviation in ln(k): 4.593638733073305""",
    longDesc = 
"""
BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
Total Standard Deviation in ln(k): 4.593638733073305
""",
)

entry(
    index = 83,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(1.81911e-05,'m^3/(mol*s)'), n=3.64993, w0=(485,'kJ/mol'), E0=(159.215,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04751116821897129, var=12.86647698666389, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
    Total Standard Deviation in ln(k): 7.310333804463108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
Total Standard Deviation in ln(k): 7.310333804463108""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
Total Standard Deviation in ln(k): 7.310333804463108
""",
)

entry(
    index = 84,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C",
    kinetics = ArrheniusBM(A=(9.70862e+09,'m^3/(mol*s)'), n=-0.320692, w0=(320,'kJ/mol'), E0=(138.359,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7370596477159201, var=2.067169622597872, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
    Total Standard Deviation in ln(k): 4.734247586274672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 4.734247586274672""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 4.734247586274672
""",
)

entry(
    index = 85,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C",
    kinetics = ArrheniusBM(A=(2414.59,'m^3/(mol*s)'), n=1.01268, w0=(383.885,'kJ/mol'), E0=(122.328,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12188664853806606, var=0.369005135039208, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
    Total Standard Deviation in ln(k): 1.5240400781873493"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 1.5240400781873493""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 1.5240400781873493
""",
)

entry(
    index = 86,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.42685e-06,'m^3/(mol*s)'), n=3.52292, w0=(353.5,'kJ/mol'), E0=(95.762,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.678878104703291, var=25.06900197371709, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
    Total Standard Deviation in ln(k): 19.280911246117956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 19.280911246117956""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 19.280911246117956
""",
)

entry(
    index = 87,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(1.72385e-06,'m^3/(mol*s)'), n=3.75017, w0=(353.5,'kJ/mol'), E0=(138.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(2.04603e-05,'m^3/(mol*s)'), n=3.06072, w0=(353.5,'kJ/mol'), E0=(93.5234,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11066358317943598, var=0.8117894835479568, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 2.0843026965378053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.0843026965378053""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.0843026965378053
""",
)

entry(
    index = 89,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(0.00359875,'m^3/(mol*s)'), n=2.93856, w0=(353.5,'kJ/mol'), E0=(174.015,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.24326e-07,'m^3/(mol*s)'), n=4.02037, w0=(353.5,'kJ/mol'), E0=(65.9482,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19860192570691124, var=4.0385871769330945, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 4.527762818042527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 4.527762818042527""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 4.527762818042527
""",
)

entry(
    index = 91,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000476496,'m^3/(mol*s)'), n=3.27616, w0=(353.5,'kJ/mol'), E0=(125.819,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0280123,'m^3/(mol*s)'), n=2.53752, w0=(353.5,'kJ/mol'), E0=(106.354,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34171721664271737, var=0.16752579831068934, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 1.6791223447064547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.6791223447064547""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.6791223447064547
""",
)

entry(
    index = 93,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000289741,'m^3/(mol*s)'), n=3.07832, w0=(353.5,'kJ/mol'), E0=(80.6712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.431870994480663, var=60.40321347953343, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
    Total Standard Deviation in ln(k): 29.228618717466222"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 29.228618717466222""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 29.228618717466222
""",
)

entry(
    index = 94,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.59209e+10,'m^3/(mol*s)'), n=-0.474654, w0=(353.5,'kJ/mol'), E0=(52.4382,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH",
    kinetics = ArrheniusBM(A=(2.17762e-05,'m^3/(mol*s)'), n=3.50846, w0=(353.5,'kJ/mol'), E0=(113.605,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH",
    kinetics = ArrheniusBM(A=(7.05247e-05,'m^3/(mol*s)'), n=3.43177, w0=(353.5,'kJ/mol'), E0=(140.804,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(2.37446e-06,'m^3/(mol*s)'), n=3.44243, w0=(353.5,'kJ/mol'), E0=(138.858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08828646739904035, var=1.4677587508292358, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 2.6505837673197075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.6505837673197075""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.6505837673197075
""",
)

entry(
    index = 98,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.0252187,'m^3/(mol*s)'), n=2.42645, w0=(353.5,'kJ/mol'), E0=(142.092,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_3CClFH-u1",
    kinetics = ArrheniusBM(A=(0.000576508,'m^3/(mol*s)'), n=2.8908, w0=(353.5,'kJ/mol'), E0=(110.658,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_N-3CClFH-u1",
    kinetics = ArrheniusBM(A=(0.00047228,'m^3/(mol*s)'), n=3.09369, w0=(353.5,'kJ/mol'), E0=(133.332,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_N-3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_N-3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->F_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(5.88791e-05,'m^3/(mol*s)'), n=3.4316, w0=(353.5,'kJ/mol'), E0=(85.5844,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.688637211175987, var=2.189873414412509, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 7.209458312916735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 7.209458312916735""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 7.209458312916735
""",
)

entry(
    index = 102,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(0.00513281,'m^3/(mol*s)'), n=2.97791, w0=(353.5,'kJ/mol'), E0=(94.5856,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.596999790956798, var=12.141404594050993, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 13.51052792306163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 13.51052792306163""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 13.51052792306163
""",
)

entry(
    index = 103,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(450643,'m^3/(mol*s)'), n=0.690342, w0=(353.5,'kJ/mol'), E0=(91.0421,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.6918,'m^3/(mol*s)'), n=2.2228, w0=(353.5,'kJ/mol'), E0=(121.476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.045463766634745634, var=0.6170109517659911, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R
    Total Standard Deviation in ln(k): 1.6889508682424024"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 1.6889508682424024""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 1.6889508682424024
""",
)

entry(
    index = 105,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000645275,'m^3/(mol*s)'), n=3.24695, w0=(353.5,'kJ/mol'), E0=(107.244,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7850264791316793, var=4.658032934219402, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R
    Total Standard Deviation in ln(k): 6.299143116378881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 6.299143116378881""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 6.299143116378881
""",
)

entry(
    index = 106,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(7.26182e+07,'m^3/(mol*s)'), n=0.26175, w0=(353.5,'kJ/mol'), E0=(160.172,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.46235599898190827, var=2.4812921040457065, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 4.319580769174553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 4.319580769174553""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 4.319580769174553
""",
)

entry(
    index = 107,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1",
    kinetics = ArrheniusBM(A=(0.210456,'m^3/(mol*s)'), n=2.65955, w0=(353.5,'kJ/mol'), E0=(105.566,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.289877,'m^3/(mol*s)'), n=2.67041, w0=(353.5,'kJ/mol'), E0=(131.563,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(7.62225e+10,'m^3/(mol*s)'), n=-0.687208, w0=(353.5,'kJ/mol'), E0=(208.95,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.37179537283404446, var=176.43434677711284, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 27.56277286249962"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 27.56277286249962""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 27.56277286249962
""",
)

entry(
    index = 110,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(4.83305e+09,'m^3/(mol*s)'), n=-0.317818, w0=(353.5,'kJ/mol'), E0=(133.886,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5290899694846325, var=17.522490518828587, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 9.72116755834015"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 9.72116755834015""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 9.72116755834015
""",
)

entry(
    index = 111,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.038815,'m^3/(mol*s)'), n=2.59891, w0=(353.5,'kJ/mol'), E0=(91.4986,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.403464253598608, var=58.461707866188966, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 28.904799124895185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 28.904799124895185""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 28.904799124895185
""",
)

entry(
    index = 112,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1",
    kinetics = ArrheniusBM(A=(0.00474579,'m^3/(mol*s)'), n=2.96408, w0=(353.5,'kJ/mol'), E0=(109.437,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.32859,'m^3/(mol*s)'), n=2.43214, w0=(353.5,'kJ/mol'), E0=(135.83,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(1.83482e+07,'m^3/(mol*s)'), n=0.383926, w0=(353.5,'kJ/mol'), E0=(82.5558,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00484591,'m^3/(mol*s)'), n=2.74561, w0=(320,'kJ/mol'), E0=(86.9193,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(0.367477,'m^3/(mol*s)'), n=2.16709, w0=(320,'kJ/mol'), E0=(90.9595,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14303334114946303, var=1.953665245539029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 3.1614701545154973"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.1614701545154973""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.1614701545154973
""",
)

entry(
    index = 117,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(1.96362e-11,'m^3/(mol*s)'), n=5.32919, w0=(525,'kJ/mol'), E0=(148.309,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3744683044870602, var=3.8479145956581067, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 4.873383922681224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 4.873383922681224""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 4.873383922681224
""",
)

entry(
    index = 118,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.84325e-15,'m^3/(mol*s)'), n=6.60344, w0=(525,'kJ/mol'), E0=(130.482,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15234857676553273, var=2.925406115640531, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 3.81164788429202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.81164788429202""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.81164788429202
""",
)

entry(
    index = 119,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C",
    kinetics = ArrheniusBM(A=(1.04239e-06,'m^3/(mol*s)'), n=3.76371, w0=(485,'kJ/mol'), E0=(179.665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007412696986269543, var=3.2119615290120844, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C',), comment="""BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C
    Total Standard Deviation in ln(k): 3.6115002719605664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C
Total Standard Deviation in ln(k): 3.6115002719605664""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C
Total Standard Deviation in ln(k): 3.6115002719605664
""",
)

entry(
    index = 120,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C",
    kinetics = ArrheniusBM(A=(5.9857e-16,'m^3/(mol*s)'), n=6.04452, w0=(525,'kJ/mol'), E0=(145.854,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.37795179550333924, var=8.172242792270408, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C
    Total Standard Deviation in ln(k): 6.6805908275261645"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C
Total Standard Deviation in ln(k): 6.6805908275261645""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C
Total Standard Deviation in ln(k): 6.6805908275261645
""",
)

entry(
    index = 121,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.24206e-07,'m^3/(mol*s)'), n=4.41751, w0=(485,'kJ/mol'), E0=(146.158,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05122312627766323, var=0.10807146951858823, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.787742450179583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.787742450179583""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.787742450179583
""",
)

entry(
    index = 122,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(2.19995e-06,'m^3/(mol*s)'), n=3.79688, w0=(485,'kJ/mol'), E0=(176.429,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3545102319141808, var=33.37437654867942, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 12.472196123677417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 12.472196123677417""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 12.472196123677417
""",
)

entry(
    index = 123,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(1.71492e-09,'m^3/(mol*s)'), n=4.37345, w0=(485,'kJ/mol'), E0=(128.047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(193952,'m^3/(mol*s)'), n=1.03354, w0=(320,'kJ/mol'), E0=(112.267,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.095394245171406, var=3.7731004721111843, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.646338548187419"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.646338548187419""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.646338548187419
""",
)

entry(
    index = 125,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F",
    kinetics = ArrheniusBM(A=(67.4331,'m^3/(mol*s)'), n=1.41481, w0=(360,'kJ/mol'), E0=(102.333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F",
    kinetics = ArrheniusBM(A=(9.23785,'m^3/(mol*s)'), n=1.76247, w0=(407.77,'kJ/mol'), E0=(118.527,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.19658e-06,'m^3/(mol*s)'), n=3.30549, w0=(353.5,'kJ/mol'), E0=(98.8969,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.4887e-05,'m^3/(mol*s)'), n=2.97943, w0=(353.5,'kJ/mol'), E0=(149.06,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(1.97415e-06,'m^3/(mol*s)'), n=3.34913, w0=(353.5,'kJ/mol'), E0=(87.6062,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11483857188927193, var=0.27873158038921275, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 1.3469397269215733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 1.3469397269215733""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 1.3469397269215733
""",
)

entry(
    index = 130,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(1.59396e-05,'m^3/(mol*s)'), n=3.60095, w0=(353.5,'kJ/mol'), E0=(151.865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(2.53629e-08,'m^3/(mol*s)'), n=4.20727, w0=(353.5,'kJ/mol'), E0=(71.1999,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3108453557563125, var=5.7710368712483335, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 5.596990045470736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 5.596990045470736""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 5.596990045470736
""",
)

entry(
    index = 132,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(1.23167e-06,'m^3/(mol*s)'), n=3.81099, w0=(353.5,'kJ/mol'), E0=(91.2995,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.29933226901369286, var=0.7436309417277837, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 2.4808551491091992"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 2.4808551491091992""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 2.4808551491091992
""",
)

entry(
    index = 133,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.01745,'m^3/(mol*s)'), n=2.59, w0=(353.5,'kJ/mol'), E0=(104.922,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.000849095,'m^3/(mol*s)'), n=3.17369, w0=(353.5,'kJ/mol'), E0=(115.897,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(4.80329e+07,'m^3/(mol*s)'), n=0.129644, w0=(353.5,'kJ/mol'), E0=(73.7502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22159137377388166, var=1.7717784905338503, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 3.2252284193699587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 3.2252284193699587""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 3.2252284193699587
""",
)

entry(
    index = 136,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0002226,'m^3/(mol*s)'), n=3.1084, w0=(353.5,'kJ/mol'), E0=(94.5131,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000214,'m^3/(mol*s)'), n=2.82, w0=(353.5,'kJ/mol'), E0=(150.926,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.000591,'m^3/(mol*s)'), n=2.76, w0=(353.5,'kJ/mol'), E0=(139.614,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.000778,'m^3/(mol*s)'), n=2.78, w0=(353.5,'kJ/mol'), E0=(151.201,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->F_Ext-3CClFH-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C",
    kinetics = ArrheniusBM(A=(4.61842e-05,'m^3/(mol*s)'), n=3.71313, w0=(353.5,'kJ/mol'), E0=(141.492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5344518780934079, var=0.01870432115466507, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
    Total Standard Deviation in ln(k): 1.6170189859218844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
Total Standard Deviation in ln(k): 1.6170189859218844""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
Total Standard Deviation in ln(k): 1.6170189859218844
""",
)

entry(
    index = 141,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000215618,'m^3/(mol*s)'), n=3.25406, w0=(353.5,'kJ/mol'), E0=(87.5269,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.000540606,'m^3/(mol*s)'), n=3.25765, w0=(353.5,'kJ/mol'), E0=(85.4083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.69582e-06,'m^3/(mol*s)'), n=3.94767, w0=(353.5,'kJ/mol'), E0=(137.723,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->Cl",
    kinetics = ArrheniusBM(A=(6.65995e-06,'m^3/(mol*s)'), n=3.94804, w0=(353.5,'kJ/mol'), E0=(146.663,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(5.27349e-06,'m^3/(mol*s)'), n=3.9638, w0=(353.5,'kJ/mol'), E0=(132.566,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5397.54,'m^3/(mol*s)'), n=1.36912, w0=(353.5,'kJ/mol'), E0=(140.433,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21342508700089668, var=1.1512734776934375, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.687272807171737"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.687272807171737""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.687272807171737
""",
)

entry(
    index = 147,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.0117015,'m^3/(mol*s)'), n=2.97295, w0=(353.5,'kJ/mol'), E0=(103.134,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.0215072,'m^3/(mol*s)'), n=2.81865, w0=(353.5,'kJ/mol'), E0=(100.151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(23683.8,'m^3/(mol*s)'), n=1.01364, w0=(353.5,'kJ/mol'), E0=(138.828,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5311374402950297, var=7.859704199276205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 6.954823846704389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 6.954823846704389""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 6.954823846704389
""",
)

entry(
    index = 150,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.6139e-06,'m^3/(mol*s)'), n=3.99356, w0=(353.5,'kJ/mol'), E0=(98.0064,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O",
    kinetics = ArrheniusBM(A=(8935.3,'m^3/(mol*s)'), n=1.34866, w0=(353.5,'kJ/mol'), E0=(151.656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30526714973959157, var=6.872819221832647, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O
    Total Standard Deviation in ln(k): 6.022628855911065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O
Total Standard Deviation in ln(k): 6.022628855911065""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O
Total Standard Deviation in ln(k): 6.022628855911065
""",
)

entry(
    index = 152,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(347392,'m^3/(mol*s)'), n=0.943199, w0=(353.5,'kJ/mol'), E0=(148.884,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4050191230830496, var=3.3858705644187372, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O
    Total Standard Deviation in ln(k): 4.706495921122942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.706495921122942""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.706495921122942
""",
)

entry(
    index = 153,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R",
    kinetics = ArrheniusBM(A=(0.000377996,'m^3/(mol*s)'), n=3.50982, w0=(353.5,'kJ/mol'), E0=(152.796,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.258527,'m^3/(mol*s)'), n=2.72329, w0=(353.5,'kJ/mol'), E0=(133.631,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07200219551069688, var=0.14315380185102225, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 0.9394150121745278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 0.9394150121745278""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 0.9394150121745278
""",
)

entry(
    index = 155,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1",
    kinetics = ArrheniusBM(A=(0.408862,'m^3/(mol*s)'), n=2.51526, w0=(353.5,'kJ/mol'), E0=(108.245,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.485796,'m^3/(mol*s)'), n=2.53612, w0=(353.5,'kJ/mol'), E0=(230.68,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(270265,'m^3/(mol*s)'), n=1.09984, w0=(353.5,'kJ/mol'), E0=(89.7338,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.6663590025617117, var=54.889048925235045, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 24.064466910606715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 24.064466910606715""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 24.064466910606715
""",
)

entry(
    index = 158,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1",
    kinetics = ArrheniusBM(A=(0.0023214,'m^3/(mol*s)'), n=2.96335, w0=(353.5,'kJ/mol'), E0=(94.1971,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02591528482106802, var=0.39841112792181, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
    Total Standard Deviation in ln(k): 1.330498890142781"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 1.330498890142781""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 1.330498890142781
""",
)

entry(
    index = 159,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.210075,'m^3/(mol*s)'), n=2.70299, w0=(353.5,'kJ/mol'), E0=(112.922,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0330058,'m^3/(mol*s)'), n=2.61871, w0=(353.5,'kJ/mol'), E0=(91.9667,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.45049e+12,'m^3/(mol*s)'), n=-1.28192, w0=(353.5,'kJ/mol'), E0=(71.4198,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.145146,'m^3/(mol*s)'), n=2.24269, w0=(320,'kJ/mol'), E0=(93.1337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.85719e-06,'m^3/(mol*s)'), n=3.90483, w0=(525,'kJ/mol'), E0=(163.449,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4049650114109864, var=4.238660316142718, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 5.144850006316648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 5.144850006316648""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 5.144850006316648
""",
)

entry(
    index = 164,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(2.96659e-18,'m^3/(mol*s)'), n=7.56742, w0=(525,'kJ/mol'), E0=(130.518,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.39558998382226235, var=0.04397856131571197, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 1.4143590010786944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 1.4143590010786944""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 1.4143590010786944
""",
)

entry(
    index = 165,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(3.80148e-14,'m^3/(mol*s)'), n=6.1794, w0=(525,'kJ/mol'), E0=(131.773,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11674205888142385, var=4.6622567867611515, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 4.621997796780991"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.621997796780991""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.621997796780991
""",
)

entry(
    index = 166,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.42402e-07,'m^3/(mol*s)'), n=3.77581, w0=(485,'kJ/mol'), E0=(179.648,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014576587959134218, var=3.2820665453679188, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.668497818205738"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.668497818205738""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.668497818205738
""",
)

entry(
    index = 167,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(4.97708e-05,'m^3/(mol*s)'), n=3.41316, w0=(485,'kJ/mol'), E0=(181.191,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2740281621639529, var=0.960841089372717, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 2.653604451122851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.653604451122851""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.653604451122851
""",
)

entry(
    index = 168,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(1.04396e-05,'m^3/(mol*s)'), n=3.41775, w0=(485,'kJ/mol'), E0=(178.695,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23338911014725236, var=0.33630971388662706, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 1.7489950995253618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.7489950995253618""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.7489950995253618
""",
)

entry(
    index = 169,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.10868e-16,'m^3/(mol*s)'), n=6.12386, w0=(525,'kJ/mol'), E0=(145.452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3918336506975836, var=8.086043304611866, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 6.685165102603498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.685165102603498""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.685165102603498
""",
)

entry(
    index = 170,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(7.83906e-10,'m^3/(mol*s)'), n=5.14485, w0=(485,'kJ/mol'), E0=(139.646,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06543906391629187, var=0.010784333405798029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
    Total Standard Deviation in ln(k): 0.3726067755457056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 0.3726067755457056""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 0.3726067755457056
""",
)

entry(
    index = 171,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(8.68377e-05,'m^3/(mol*s)'), n=3.62888, w0=(485,'kJ/mol'), E0=(152.865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.08267e-06,'m^3/(mol*s)'), n=3.44277, w0=(485,'kJ/mol'), E0=(172.692,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.03653e-08,'m^3/(mol*s)'), n=4.6553, w0=(485,'kJ/mol'), E0=(175.804,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.53283e+07,'m^3/(mol*s)'), n=0.481206, w0=(320,'kJ/mol'), E0=(124.304,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3887130938131378, var=3.3667999420822414, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 7.167685551010779"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.167685551010779""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.167685551010779
""",
)

entry(
    index = 175,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(6.33001e-06,'m^3/(mol*s)'), n=3.64469, w0=(353.5,'kJ/mol'), E0=(118.088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R",
    kinetics = ArrheniusBM(A=(2.67941e-06,'m^3/(mol*s)'), n=3.30717, w0=(353.5,'kJ/mol'), E0=(87.9629,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7400290755681809, var=0.45092521150562737, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R
    Total Standard Deviation in ln(k): 3.20556848895022"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R
Total Standard Deviation in ln(k): 3.20556848895022""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R
Total Standard Deviation in ln(k): 3.20556848895022
""",
)

entry(
    index = 177,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.54636e-06,'m^3/(mol*s)'), n=3.6841, w0=(353.5,'kJ/mol'), E0=(71.1999,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41228709333201696, var=14.051487791945302, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 8.550709641862497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.550709641862497""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.550709641862497
""",
)

entry(
    index = 178,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000688634,'m^3/(mol*s)'), n=2.91877, w0=(353.5,'kJ/mol'), E0=(109.89,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02266409186108921, var=0.4195488023761085, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 1.3554637260989224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.3554637260989224""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.3554637260989224
""",
)

entry(
    index = 179,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.0852e-05,'m^3/(mol*s)'), n=3.56626, w0=(353.5,'kJ/mol'), E0=(105.03,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.014814487542789, var=6.895903420980853, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 10.326792738708912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 10.326792738708912""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 10.326792738708912
""",
)

entry(
    index = 180,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(7.08191e-06,'m^3/(mol*s)'), n=3.53568, w0=(353.5,'kJ/mol'), E0=(71.7919,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2387065873008323, var=1.9014913255610233, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.3641861689531356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.3641861689531356""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.3641861689531356
""",
)

entry(
    index = 181,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.43837e+08,'m^3/(mol*s)'), n=-0.0969087, w0=(353.5,'kJ/mol'), E0=(81.4744,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(8.38302e-05,'m^3/(mol*s)'), n=3.60203, w0=(353.5,'kJ/mol'), E0=(138.304,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.05616,'m^3/(mol*s)'), n=2.3798, w0=(353.5,'kJ/mol'), E0=(126.609,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(0.285485,'m^3/(mol*s)'), n=2.54097, w0=(353.5,'kJ/mol'), E0=(126.586,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.340714,'m^3/(mol*s)'), n=2.59484, w0=(353.5,'kJ/mol'), E0=(110.612,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_4BrCClFINPSSi->F_Ext-1C-R_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.37515e-06,'m^3/(mol*s)'), n=3.75034, w0=(353.5,'kJ/mol'), E0=(86.9747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->C_N-4BrCClFINPSSi->F_Ext-1C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1",
    kinetics = ArrheniusBM(A=(6.76663,'m^3/(mol*s)'), n=2.21757, w0=(353.5,'kJ/mol'), E0=(126.395,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(7.91945,'m^3/(mol*s)'), n=2.24843, w0=(353.5,'kJ/mol'), E0=(153.837,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(2.15224e+07,'m^3/(mol*s)'), n=0.433043, w0=(353.5,'kJ/mol'), E0=(155.587,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.47110491481021965, var=19.781505320533533, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 10.10002145544949"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 10.10002145544949""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 10.10002145544949
""",
)

entry(
    index = 190,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1",
    kinetics = ArrheniusBM(A=(6.13119,'m^3/(mol*s)'), n=2.27145, w0=(353.5,'kJ/mol'), E0=(117.855,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(7.7908,'m^3/(mol*s)'), n=2.30231, w0=(353.5,'kJ/mol'), E0=(142.173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.0379121,'m^3/(mol*s)'), n=2.90824, w0=(353.5,'kJ/mol'), E0=(126.403,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(7.30096,'m^3/(mol*s)'), n=2.36151, w0=(353.5,'kJ/mol'), E0=(142.571,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C",
    kinetics = ArrheniusBM(A=(1013.62,'m^3/(mol*s)'), n=1.79593, w0=(353.5,'kJ/mol'), E0=(72.8374,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.063348891324565, var=16.540723846898153, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C
    Total Standard Deviation in ln(k): 13.337609137568322"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C
Total Standard Deviation in ln(k): 13.337609137568322""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C
Total Standard Deviation in ln(k): 13.337609137568322
""",
)

entry(
    index = 195,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->C",
    kinetics = ArrheniusBM(A=(0.0308105,'m^3/(mol*s)'), n=2.88761, w0=(353.5,'kJ/mol'), E0=(141.325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl",
    kinetics = ArrheniusBM(A=(0.00381903,'m^3/(mol*s)'), n=3.24993, w0=(353.5,'kJ/mol'), E0=(137.478,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl",
    kinetics = ArrheniusBM(A=(0.00192701,'m^3/(mol*s)'), n=2.98477, w0=(353.5,'kJ/mol'), E0=(93.5621,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24454729070336428, var=0.36493714534411276, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl
    Total Standard Deviation in ln(k): 1.8255014455844252"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl
Total Standard Deviation in ln(k): 1.8255014455844252""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl
Total Standard Deviation in ln(k): 1.8255014455844252
""",
)

entry(
    index = 198,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(5.25388e-06,'m^3/(mol*s)'), n=3.75609, w0=(525,'kJ/mol'), E0=(167.213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4178469448477018, var=3.6552170373879327, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 4.882643893045157"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 4.882643893045157""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 4.882643893045157
""",
)

entry(
    index = 199,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(5.8619e-10,'m^3/(mol*s)'), n=4.99656, w0=(525,'kJ/mol'), E0=(142.533,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9423040482511109, var=6.107333969659828, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 7.321904077410443"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.321904077410443""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.321904077410443
""",
)

entry(
    index = 200,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.80067e-20,'m^3/(mol*s)'), n=8.17077, w0=(525,'kJ/mol'), E0=(126.397,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.18265e-09,'m^3/(mol*s)'), n=4.74784, w0=(525,'kJ/mol'), E0=(136.975,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.38353e-15,'m^3/(mol*s)'), n=6.43499, w0=(525,'kJ/mol'), E0=(132.021,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10674984827458836, var=6.364789869515815, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 5.3258686403466315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.3258686403466315""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.3258686403466315
""",
)

entry(
    index = 203,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0",
    kinetics = ArrheniusBM(A=(8.64116e-07,'m^3/(mol*s)'), n=3.78655, w0=(485,'kJ/mol'), E0=(179.584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.013163617278834092, var=3.2673803958764562, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0',), comment="""BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0
    Total Standard Deviation in ln(k): 3.656812821602809"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.656812821602809""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.656812821602809
""",
)

entry(
    index = 204,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0",
    kinetics = ArrheniusBM(A=(226.686,'m^3/(mol*s)'), n=1.41927, w0=(485,'kJ/mol'), E0=(172.862,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.476202477337676, var=9.700063949958636, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0
    Total Standard Deviation in ln(k): 7.440221133894459"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 7.440221133894459""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 7.440221133894459
""",
)

entry(
    index = 205,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.8148e-05,'m^3/(mol*s)'), n=3.38383, w0=(485,'kJ/mol'), E0=(179.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2149616755423855, var=2.1237975861441836, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.974219057081788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 5.974219057081788""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 5.974219057081788
""",
)

entry(
    index = 206,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_4R!H->C",
    kinetics = ArrheniusBM(A=(3.70857e-08,'m^3/(mol*s)'), n=4.36701, w0=(485,'kJ/mol'), E0=(179.598,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.95e-05,'m^3/(mol*s)'), n=3.43, w0=(485,'kJ/mol'), E0=(182.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.48449e-05,'m^3/(mol*s)'), n=3.39528, w0=(485,'kJ/mol'), E0=(181.012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2840078072331988, var=0.783376808139735, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.487949931258856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.487949931258856""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.487949931258856
""",
)

entry(
    index = 209,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.26291e-08,'m^3/(mol*s)'), n=4.37484, w0=(485,'kJ/mol'), E0=(173.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24436438432485788, var=0.014235358056973308, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
    Total Standard Deviation in ln(k): 0.8531698562866517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 0.8531698562866517""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 0.8531698562866517
""",
)

entry(
    index = 210,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.972e-05,'m^3/(mol*s)'), n=3.28397, w0=(485,'kJ/mol'), E0=(175.447,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1309384567838423, var=3.7654530018551067, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
    Total Standard Deviation in ln(k): 6.731697260808422"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 6.731697260808422""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 6.731697260808422
""",
)

entry(
    index = 211,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(6.1955e-18,'m^3/(mol*s)'), n=6.5823, w0=(525,'kJ/mol'), E0=(142.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.42578061332016637, var=0.0689064662312766, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 1.5960443194840586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.5960443194840586""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.5960443194840586
""",
)

entry(
    index = 212,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.95231e-15,'m^3/(mol*s)'), n=5.90064, w0=(525,'kJ/mol'), E0=(147.139,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3742301382083374, var=10.071285727906062, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 7.302361449525102"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.302361449525102""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.302361449525102
""",
)

entry(
    index = 213,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C",
    kinetics = ArrheniusBM(A=(1.10332e-07,'m^3/(mol*s)'), n=4.39237, w0=(485,'kJ/mol'), E0=(138.074,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.88042e-12,'m^3/(mol*s)'), n=5.91377, w0=(485,'kJ/mol'), E0=(141.07,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(830.61,'m^3/(mol*s)'), n=1.7707, w0=(320,'kJ/mol'), E0=(89.765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(14.1008,'m^3/(mol*s)'), n=2.18545, w0=(320,'kJ/mol'), E0=(90.1727,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(814.812,'m^3/(mol*s)'), n=1.79633, w0=(320,'kJ/mol'), E0=(82.2358,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.20903e-06,'m^3/(mol*s)'), n=3.28294, w0=(353.5,'kJ/mol'), E0=(88.1477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.000106598,'m^3/(mol*s)'), n=3.19974, w0=(353.5,'kJ/mol'), E0=(140.344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(5.4276e-05,'m^3/(mol*s)'), n=3.31018, w0=(353.5,'kJ/mol'), E0=(55.3573,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02230053974573934, var=14.29753774719782, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 7.63635282887443"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 7.63635282887443""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 7.63635282887443
""",
)

entry(
    index = 221,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000106781,'m^3/(mol*s)'), n=3.23554, w0=(353.5,'kJ/mol'), E0=(135.072,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(5.62416e-08,'m^3/(mol*s)'), n=4.11181, w0=(353.5,'kJ/mol'), E0=(79.5433,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06842683671089847, var=0.9569025966268359, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 2.132986610414133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 2.132986610414133""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 2.132986610414133
""",
)

entry(
    index = 223,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F",
    kinetics = ArrheniusBM(A=(0.000850269,'m^3/(mol*s)'), n=2.86942, w0=(353.5,'kJ/mol'), E0=(110.055,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07280454633633433, var=0.32493789106620613, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F
    Total Standard Deviation in ln(k): 1.3256916209301546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F
Total Standard Deviation in ln(k): 1.3256916209301546""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F
Total Standard Deviation in ln(k): 1.3256916209301546
""",
)

entry(
    index = 224,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->F",
    kinetics = ArrheniusBM(A=(8.49172e-05,'m^3/(mol*s)'), n=3.34587, w0=(353.5,'kJ/mol'), E0=(109.205,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.82278e-05,'m^3/(mol*s)'), n=3.44719, w0=(353.5,'kJ/mol'), E0=(107.142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000486816,'m^3/(mol*s)'), n=3.11618, w0=(353.5,'kJ/mol'), E0=(147.245,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000246125,'m^3/(mol*s)'), n=3.06199, w0=(353.5,'kJ/mol'), E0=(76.3051,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15395769877952278, var=3.6278400976082357, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 4.20522519182327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 4.20522519182327""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 4.20522519182327
""",
)

entry(
    index = 228,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1",
    kinetics = ArrheniusBM(A=(48.7171,'m^3/(mol*s)'), n=2.03641, w0=(353.5,'kJ/mol'), E0=(106.443,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(27.1545,'m^3/(mol*s)'), n=2.13727, w0=(353.5,'kJ/mol'), E0=(154.084,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 230,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(188.487,'m^3/(mol*s)'), n=2.00503, w0=(353.5,'kJ/mol'), E0=(69.9638,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(0.00210966,'m^3/(mol*s)'), n=3.19123, w0=(353.5,'kJ/mol'), E0=(120.266,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1715053003348904, var=0.08524532494522667, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
    Total Standard Deviation in ln(k): 1.0162363720412833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 1.0162363720412833""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 1.0162363720412833
""",
)

entry(
    index = 232,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C",
    kinetics = ArrheniusBM(A=(0.00151992,'m^3/(mol*s)'), n=3.0105, w0=(353.5,'kJ/mol'), E0=(92.7053,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.00678858,'m^3/(mol*s)'), n=3.1372, w0=(353.5,'kJ/mol'), E0=(110.962,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.95758e-06,'m^3/(mol*s)'), n=3.73977, w0=(525,'kJ/mol'), E0=(167.632,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4148396562433757, var=3.7970808767613327, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 4.948757484773534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.948757484773534""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.948757484773534
""",
)

entry(
    index = 235,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.84864e-10,'m^3/(mol*s)'), n=5.13872, w0=(525,'kJ/mol'), E0=(139.045,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.15e-07,'m^3/(mol*s)'), n=4.14, w0=(525,'kJ/mol'), E0=(164.014,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.71142e-12,'m^3/(mol*s)'), n=5.47558, w0=(525,'kJ/mol'), E0=(152.791,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_4ClO->Cl",
    kinetics = ArrheniusBM(A=(3.57367e-11,'m^3/(mol*s)'), n=5.32561, w0=(525,'kJ/mol'), E0=(142.138,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_4ClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_4ClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_N-4ClO->Cl",
    kinetics = ArrheniusBM(A=(3.31829e-08,'m^3/(mol*s)'), n=4.48236, w0=(525,'kJ/mol'), E0=(137.567,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_N-4ClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_N-4ClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_N-4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_N-4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.4072e-05,'m^3/(mol*s)'), n=3.45455, w0=(485,'kJ/mol'), E0=(188.572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0985724558137202, var=6.0960489654238526, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 5.197396105233193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 5.197396105233193""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 5.197396105233193
""",
)

entry(
    index = 241,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(7.98998e-08,'m^3/(mol*s)'), n=4.06507, w0=(485,'kJ/mol'), E0=(170.994,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0628102702633848, var=0.5772292955492786, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 1.680924405925733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.680924405925733""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.680924405925733
""",
)

entry(
    index = 242,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(6.93639e-07,'m^3/(mol*s)'), n=3.84128, w0=(485,'kJ/mol'), E0=(181.27,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17614469304775013, var=1.308476701639213, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 2.7357643269006675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.7357643269006675""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.7357643269006675
""",
)

entry(
    index = 243,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(86.3197,'m^3/(mol*s)'), n=1.5824, w0=(485,'kJ/mol'), E0=(174.861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4039562151170453, var=13.200382787736764, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 8.298635212481031"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.298635212481031""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.298635212481031
""",
)

entry(
    index = 244,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.28573e-06,'m^3/(mol*s)'), n=3.56699, w0=(485,'kJ/mol'), E0=(129.946,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(4.362e-07,'m^3/(mol*s)'), n=3.96684, w0=(485,'kJ/mol'), E0=(178.635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(8.35e-05,'m^3/(mol*s)'), n=3.36, w0=(485,'kJ/mol'), E0=(179.463,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.34e-05,'m^3/(mol*s)'), n=3.35, w0=(485,'kJ/mol'), E0=(183.315,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(6.36303e-10,'m^3/(mol*s)'), n=4.82658, w0=(485,'kJ/mol'), E0=(166.608,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4745848157928954, var=0.005426392301841526, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 1.34010106579823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.34010106579823""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.34010106579823
""",
)

entry(
    index = 249,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.35e-05,'m^3/(mol*s)'), n=3.34, w0=(485,'kJ/mol'), E0=(179.728,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.894e-08,'m^3/(mol*s)'), n=4.35365, w0=(485,'kJ/mol'), E0=(174.899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->F",
    kinetics = ArrheniusBM(A=(2.43e-05,'m^3/(mol*s)'), n=3.25, w0=(485,'kJ/mol'), E0=(175.575,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->F",
    kinetics = ArrheniusBM(A=(7.33269e-08,'m^3/(mol*s)'), n=4.23045, w0=(485,'kJ/mol'), E0=(172.474,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.71288e-19,'m^3/(mol*s)'), n=6.96688, w0=(525,'kJ/mol'), E0=(148.279,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.5015e-15,'m^3/(mol*s)'), n=5.80677, w0=(525,'kJ/mol'), E0=(156.224,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5112164103887401, var=10.588737646641077, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 7.807939560566177"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 7.807939560566177""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 7.807939560566177
""",
)

entry(
    index = 255,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.99667e-12,'m^3/(mol*s)'), n=4.90505, w0=(525,'kJ/mol'), E0=(159.7,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4861684503161386, var=9.431603751730098, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 7.378253870483329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 7.378253870483329""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 7.378253870483329
""",
)

entry(
    index = 256,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.05303e-14,'m^3/(mol*s)'), n=5.67916, w0=(525,'kJ/mol'), E0=(133.638,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.53174e-29,'m^3/(mol*s)'), n=10.0614, w0=(525,'kJ/mol'), E0=(93.6931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4501896732417744, var=0.6008575980312036, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.685100325179278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.685100325179278""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.685100325179278
""",
)

entry(
    index = 258,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000936334,'m^3/(mol*s)'), n=3.09886, w0=(353.5,'kJ/mol'), E0=(69.3516,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH",
    kinetics = ArrheniusBM(A=(3.83336e-06,'m^3/(mol*s)'), n=3.49829, w0=(353.5,'kJ/mol'), E0=(56.86,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.537258459862933, var=3.824063287802492, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
    Total Standard Deviation in ln(k): 7.782760449733318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 7.782760449733318""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 7.782760449733318
""",
)

entry(
    index = 260,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH",
    kinetics = ArrheniusBM(A=(7.98561e-13,'m^3/(mol*s)'), n=5.49027, w0=(353.5,'kJ/mol'), E0=(69.3249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09989298412020639, var=4.613005043965805, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
    Total Standard Deviation in ln(k): 4.556738823863509"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 4.556738823863509""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 4.556738823863509
""",
)

entry(
    index = 261,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000211362,'m^3/(mol*s)'), n=3.09043, w0=(353.5,'kJ/mol'), E0=(111.923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0038106886467686625, var=1.0722664004442908, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 2.085483720874051"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.085483720874051""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.085483720874051
""",
)

entry(
    index = 262,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.296329,'m^3/(mol*s)'), n=2.14549, w0=(353.5,'kJ/mol'), E0=(124.382,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0016896164896032955, var=0.21146075685506038, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 0.9261199340816746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 0.9261199340816746""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 0.9261199340816746
""",
)

entry(
    index = 263,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O",
    kinetics = ArrheniusBM(A=(0.002697,'m^3/(mol*s)'), n=2.63489, w0=(353.5,'kJ/mol'), E0=(82.4005,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 264,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.02065,'m^3/(mol*s)'), n=2.64, w0=(353.5,'kJ/mol'), E0=(99.8313,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 265,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(0.00185843,'m^3/(mol*s)'), n=3.22261, w0=(353.5,'kJ/mol'), E0=(119.935,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 266,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.57088e-06,'m^3/(mol*s)'), n=3.85599, w0=(525,'kJ/mol'), E0=(165.109,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41851646072910137, var=5.496367776292629, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 5.751516688346116"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 5.751516688346116""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 5.751516688346116
""",
)

entry(
    index = 267,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00402118,'m^3/(mol*s)'), n=3.10034, w0=(525,'kJ/mol'), E0=(178.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0850955224706764, var=0.3972049085178087, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.4772759786458678"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.4772759786458678""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.4772759786458678
""",
)

entry(
    index = 268,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(2.00179e-06,'m^3/(mol*s)'), n=3.59463, w0=(485,'kJ/mol'), E0=(184.963,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07127630849995228, var=7.212345980836135, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 5.56296488743793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 5.56296488743793""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 5.56296488743793
""",
)

entry(
    index = 269,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000112375,'m^3/(mol*s)'), n=3.34717, w0=(485,'kJ/mol'), E0=(193.047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11649476807305856, var=6.542463448122908, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 5.420459851507813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.420459851507813""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.420459851507813
""",
)

entry(
    index = 270,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F",
    kinetics = ArrheniusBM(A=(8.0722e-08,'m^3/(mol*s)'), n=4.09577, w0=(485,'kJ/mol'), E0=(171.561,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16555178975853388, var=1.197265706866839, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
    Total Standard Deviation in ln(k): 2.6095331250902634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
Total Standard Deviation in ln(k): 2.6095331250902634""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
Total Standard Deviation in ln(k): 2.6095331250902634
""",
)

entry(
    index = 271,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F",
    kinetics = ArrheniusBM(A=(8.39474e-08,'m^3/(mol*s)'), n=4.02792, w0=(485,'kJ/mol'), E0=(170.508,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028020092662087215, var=0.06812965528928436, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
    Total Standard Deviation in ln(k): 0.59367133755393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
Total Standard Deviation in ln(k): 0.59367133755393""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
Total Standard Deviation in ln(k): 0.59367133755393
""",
)

entry(
    index = 272,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(5.7299e-06,'m^3/(mol*s)'), n=3.76087, w0=(485,'kJ/mol'), E0=(180.492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 273,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(6.7827e-07,'m^3/(mol*s)'), n=3.84344, w0=(485,'kJ/mol'), E0=(181.257,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18844180021896278, var=1.32438726038431, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 2.78056159374933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.78056159374933""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.78056159374933
""",
)

entry(
    index = 274,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(18908.5,'m^3/(mol*s)'), n=0.81744, w0=(485,'kJ/mol'), E0=(176.149,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.513238060813226, var=34.9716148721854, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 13.144905231046868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 13.144905231046868""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 13.144905231046868
""",
)

entry(
    index = 275,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0158687,'m^3/(mol*s)'), n=2.79423, w0=(485,'kJ/mol'), E0=(172.35,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1575084340451707, var=8.568385324107215, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 6.263971138772223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.263971138772223""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.263971138772223
""",
)

entry(
    index = 276,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(3.19591e-10,'m^3/(mol*s)'), n=4.92231, w0=(485,'kJ/mol'), E0=(166.297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.29256e-09,'m^3/(mol*s)'), n=4.72835, w0=(485,'kJ/mol'), E0=(166.942,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.06741e-10,'m^3/(mol*s)'), n=4.20891, w0=(525,'kJ/mol'), E0=(172.181,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.544929187416684, var=17.376525681403344, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C
    Total Standard Deviation in ln(k): 9.725939067896848"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C
Total Standard Deviation in ln(k): 9.725939067896848""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C
Total Standard Deviation in ln(k): 9.725939067896848
""",
)

entry(
    index = 279,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.95098e-18,'m^3/(mol*s)'), n=6.63346, w0=(525,'kJ/mol'), E0=(147.666,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47012614306605033, var=14.73093751072793, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-5R!H->C
    Total Standard Deviation in ln(k): 8.8755758135659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-5R!H->C
Total Standard Deviation in ln(k): 8.8755758135659""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-5R!H->C
Total Standard Deviation in ln(k): 8.8755758135659
""",
)

entry(
    index = 280,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.66415e-17,'m^3/(mol*s)'), n=6.35482, w0=(525,'kJ/mol'), E0=(135.01,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.04999e-10,'m^3/(mol*s)'), n=4.52925, w0=(525,'kJ/mol'), E0=(171.013,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12066619227620501, var=1.144107657873343, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.447505532134808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.447505532134808""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.447505532134808
""",
)

entry(
    index = 282,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->F",
    kinetics = ArrheniusBM(A=(2.92246e-47,'m^3/(mol*s)'), n=15.2293, w0=(525,'kJ/mol'), E0=(47.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F",
    kinetics = ArrheniusBM(A=(1.84248e-12,'m^3/(mol*s)'), n=5.20563, w0=(525,'kJ/mol'), E0=(136.878,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.633508779011236, var=0.5351165166025463, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F
    Total Standard Deviation in ln(k): 3.058227561563756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F
Total Standard Deviation in ln(k): 3.058227561563756""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F
Total Standard Deviation in ln(k): 3.058227561563756
""",
)

entry(
    index = 284,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R",
    kinetics = ArrheniusBM(A=(4.11983e-05,'m^3/(mol*s)'), n=3.20075, w0=(353.5,'kJ/mol'), E0=(86.129,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.00426481,'m^3/(mol*s)'), n=2.657, w0=(353.5,'kJ/mol'), E0=(142.941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 286,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.00442,'m^3/(mol*s)'), n=2.67, w0=(353.5,'kJ/mol'), E0=(124.435,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->F",
    kinetics = ArrheniusBM(A=(0.00705,'m^3/(mol*s)'), n=2.66, w0=(353.5,'kJ/mol'), E0=(109.14,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(0.00765,'m^3/(mol*s)'), n=2.68, w0=(353.5,'kJ/mol'), E0=(125.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.00175,'m^3/(mol*s)'), n=2.74, w0=(353.5,'kJ/mol'), E0=(102.483,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 290,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.00212,'m^3/(mol*s)'), n=2.75, w0=(353.5,'kJ/mol'), E0=(115.442,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.00303,'m^3/(mol*s)'), n=2.77, w0=(353.5,'kJ/mol'), E0=(123.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 292,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(0.00762744,'m^3/(mol*s)'), n=2.67175, w0=(525,'kJ/mol'), E0=(177.076,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4325450759493888, var=15.202418859255678, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 8.90331474776127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 8.90331474776127""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 8.90331474776127
""",
)

entry(
    index = 293,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.10667e-09,'m^3/(mol*s)'), n=4.67466, w0=(525,'kJ/mol'), E0=(156.354,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4438465967016666, var=1.18807412141415, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 3.3003298902227405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 3.3003298902227405""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 3.3003298902227405
""",
)

entry(
    index = 294,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.58883e-06,'m^3/(mol*s)'), n=3.55742, w0=(485,'kJ/mol'), E0=(187.883,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.058908738351432434, var=7.3507010348261606, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 5.58328498982993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.58328498982993""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.58328498982993
""",
)

entry(
    index = 295,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C",
    kinetics = ArrheniusBM(A=(2.5027e-05,'m^3/(mol*s)'), n=3.59925, w0=(485,'kJ/mol'), E0=(178.513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C",
    kinetics = ArrheniusBM(A=(1.59331e-06,'m^3/(mol*s)'), n=3.65749, w0=(485,'kJ/mol'), E0=(166.464,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.181595671093109, var=7.03809268974634, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
    Total Standard Deviation in ln(k): 10.799838807848376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 10.799838807848376""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 10.799838807848376
""",
)

entry(
    index = 297,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O",
    kinetics = ArrheniusBM(A=(0.161782,'m^3/(mol*s)'), n=2.43248, w0=(485,'kJ/mol'), E0=(190.562,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2894535009314283, var=26.574338000377352, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
    Total Standard Deviation in ln(k): 11.06174028820509"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.06174028820509""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.06174028820509
""",
)

entry(
    index = 298,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(7.52259e-05,'m^3/(mol*s)'), n=3.39773, w0=(485,'kJ/mol'), E0=(193.259,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09250277953740067, var=6.906895070230772, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
    Total Standard Deviation in ln(k): 5.501057755436018"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 5.501057755436018""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 5.501057755436018
""",
)

entry(
    index = 299,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.17544e-08,'m^3/(mol*s)'), n=4.12767, w0=(485,'kJ/mol'), E0=(171.42,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17797988810844184, var=1.217229011632701, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 2.6589718118389447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.6589718118389447""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.6589718118389447
""",
)

entry(
    index = 300,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.34353e-08,'m^3/(mol*s)'), n=4.02818, w0=(485,'kJ/mol'), E0=(170.502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.026983944685405336, var=0.06263505290286348, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 0.5695238237214809"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 0.5695238237214809""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 0.5695238237214809
""",
)

entry(
    index = 301,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C",
    kinetics = ArrheniusBM(A=(3.39606e-06,'m^3/(mol*s)'), n=3.8002, w0=(485,'kJ/mol'), E0=(174.472,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24993611629262544, var=0.04764147309766436, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
    Total Standard Deviation in ln(k): 1.0655522483929907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
Total Standard Deviation in ln(k): 1.0655522483929907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
Total Standard Deviation in ln(k): 1.0655522483929907
""",
)

entry(
    index = 302,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C",
    kinetics = ArrheniusBM(A=(5.29538e-06,'m^3/(mol*s)'), n=3.74, w0=(485,'kJ/mol'), E0=(173.466,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 303,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.22395e-07,'m^3/(mol*s)'), n=3.97282, w0=(485,'kJ/mol'), E0=(180.817,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7406508044333014, var=2.8104200778925885, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.221731209747573"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.221731209747573""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.221731209747573
""",
)

entry(
    index = 304,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.009208,'m^3/(mol*s)'), n=2.80941, w0=(485,'kJ/mol'), E0=(151.694,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.332656919811769, var=4.25485772067976, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.9710498891419785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.9710498891419785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.9710498891419785
""",
)

entry(
    index = 305,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.71639e-05,'m^3/(mol*s)'), n=3.56319, w0=(485,'kJ/mol'), E0=(152.498,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(4.42409e-10,'m^3/(mol*s)'), n=3.80428, w0=(525,'kJ/mol'), E0=(173.286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 307,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(6.7402e-11,'m^3/(mol*s)'), n=4.49383, w0=(525,'kJ/mol'), E0=(172.117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-5R!H->C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.99899e-17,'m^3/(mol*s)'), n=6.17724, w0=(525,'kJ/mol'), E0=(151.814,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5391605746294693, var=1.1872961343063502, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-5R!H->C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-5R!H->C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.5390966824008614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-5R!H->C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.5390966824008614""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-5R!H->C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.5390966824008614
""",
)

entry(
    index = 309,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O",
    kinetics = ArrheniusBM(A=(4.28469e-13,'m^3/(mol*s)'), n=5.32117, w0=(525,'kJ/mol'), E0=(160.082,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 310,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(1.14832e-10,'m^3/(mol*s)'), n=4.5051, w0=(525,'kJ/mol'), E0=(171.708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2724107185851959, var=0.5154939006054772, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 2.1238068062147035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 2.1238068062147035""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 2.1238068062147035
""",
)

entry(
    index = 311,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_Sp-4O-3C",
    kinetics = ArrheniusBM(A=(6.45811e-13,'m^3/(mol*s)'), n=5.31977, w0=(525,'kJ/mol'), E0=(134.062,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_N-Sp-4O-3C",
    kinetics = ArrheniusBM(A=(1.71498e-10,'m^3/(mol*s)'), n=4.74348, w0=(525,'kJ/mol'), E0=(152.116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_N-Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_N-Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 313,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(0.104833,'m^3/(mol*s)'), n=2.12, w0=(525,'kJ/mol'), E0=(178.386,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(0.001275,'m^3/(mol*s)'), n=3.12, w0=(525,'kJ/mol'), E0=(176.666,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.68723e-05,'m^3/(mol*s)'), n=2.95314, w0=(485,'kJ/mol'), E0=(193.721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0030046029818384134, var=14.743691214756458, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
    Total Standard Deviation in ln(k): 7.705233678445662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 7.705233678445662""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 7.705233678445662
""",
)

entry(
    index = 316,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(8.96824e-07,'m^3/(mol*s)'), n=3.83775, w0=(485,'kJ/mol'), E0=(185.213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07754259444220443, var=1.754056388859614, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 2.849917691374449"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.849917691374449""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.849917691374449
""",
)

entry(
    index = 317,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.5333e-06,'m^3/(mol*s)'), n=3.65941, w0=(485,'kJ/mol'), E0=(166.429,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 318,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.21333e-05,'m^3/(mol*s)'), n=3.66599, w0=(485,'kJ/mol'), E0=(168.262,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 319,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.38922e-05,'m^3/(mol*s)'), n=3.5758, w0=(485,'kJ/mol'), E0=(168.916,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00331206,'m^3/(mol*s)'), n=2.81802, w0=(485,'kJ/mol'), E0=(196.029,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 321,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.13872e-05,'m^3/(mol*s)'), n=3.55176, w0=(485,'kJ/mol'), E0=(193.142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.027783525579027298, var=7.287454963942901, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 5.481647642096425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.481647642096425""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.481647642096425
""",
)

entry(
    index = 322,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.839925,'m^3/(mol*s)'), n=2.36463, w0=(485,'kJ/mol'), E0=(184.976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.73445e-08,'m^3/(mol*s)'), n=4.20668, w0=(485,'kJ/mol'), E0=(169.253,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1699640488159558, var=1.181990833198972, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 2.6065813329923846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.6065813329923846""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.6065813329923846
""",
)

entry(
    index = 324,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.84573e-07,'m^3/(mol*s)'), n=3.87954, w0=(485,'kJ/mol'), E0=(178.087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9426494161731698, var=6.57708312571278, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 7.509774259468916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.509774259468916""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.509774259468916
""",
)

entry(
    index = 325,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C",
    kinetics = ArrheniusBM(A=(1.00712e-07,'m^3/(mol*s)'), n=4.01588, w0=(485,'kJ/mol'), E0=(170.299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10014952334378734, var=0.022957014575159668, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C
    Total Standard Deviation in ln(k): 0.5553808545883934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C
Total Standard Deviation in ln(k): 0.5553808545883934""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C
Total Standard Deviation in ln(k): 0.5553808545883934
""",
)

entry(
    index = 326,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C",
    kinetics = ArrheniusBM(A=(6.28297e-08,'m^3/(mol*s)'), n=4.04865, w0=(485,'kJ/mol'), E0=(170.739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07071074998058823, var=0.23643663099245127, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C
    Total Standard Deviation in ln(k): 1.1524626199576522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C
Total Standard Deviation in ln(k): 1.1524626199576522""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C
Total Standard Deviation in ln(k): 1.1524626199576522
""",
)

entry(
    index = 327,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.51365e-06,'m^3/(mol*s)'), n=3.78897, w0=(485,'kJ/mol'), E0=(175.572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 328,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.63e-05,'m^3/(mol*s)'), n=3.37, w0=(485,'kJ/mol'), E0=(197.415,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(2.58576e-05,'m^3/(mol*s)'), n=3.2457, w0=(485,'kJ/mol'), E0=(186.26,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 330,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(3.56033e-08,'m^3/(mol*s)'), n=4.21745, w0=(485,'kJ/mol'), E0=(177.011,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 331,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.47723e-05,'m^3/(mol*s)'), n=3.46134, w0=(485,'kJ/mol'), E0=(152.048,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.5032e-05,'m^3/(mol*s)'), n=3.5135, w0=(485,'kJ/mol'), E0=(138.997,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.24742e-10,'m^3/(mol*s)'), n=4.43268, w0=(525,'kJ/mol'), E0=(174.259,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7737090826312919, var=0.397284904770115, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 3.2075880267074934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 3.2075880267074934""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 3.2075880267074934
""",
)

entry(
    index = 334,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000145249,'m^3/(mol*s)'), n=2.84864, w0=(485,'kJ/mol'), E0=(194.031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F",
    kinetics = ArrheniusBM(A=(4.86925e-07,'m^3/(mol*s)'), n=3.84755, w0=(485,'kJ/mol'), E0=(182.435,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0960091925402666, var=2.0878679097954644, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F
    Total Standard Deviation in ln(k): 3.1379623414440583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F
Total Standard Deviation in ln(k): 3.1379623414440583""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F
Total Standard Deviation in ln(k): 3.1379623414440583
""",
)

entry(
    index = 336,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->F",
    kinetics = ArrheniusBM(A=(2.47232e-06,'m^3/(mol*s)'), n=3.97637, w0=(485,'kJ/mol'), E0=(194.828,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 337,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.50054e-05,'m^3/(mol*s)'), n=3.79284, w0=(485,'kJ/mol'), E0=(187.083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005088736941093816, var=2.1376794914896005, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
    Total Standard Deviation in ln(k): 2.943869906153487"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
Total Standard Deviation in ln(k): 2.943869906153487""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
Total Standard Deviation in ln(k): 2.943869906153487
""",
)

entry(
    index = 338,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(7.70504e-06,'m^3/(mol*s)'), n=3.51763, w0=(485,'kJ/mol'), E0=(196.685,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04959390361496888, var=1.7912645786841095, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 2.8077077928577854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.8077077928577854""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.8077077928577854
""",
)

entry(
    index = 339,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.6394e-08,'m^3/(mol*s)'), n=4.20067, w0=(485,'kJ/mol'), E0=(170.79,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22661832906730353, var=4.962422799104255, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.035240106288148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.035240106288148""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.035240106288148
""",
)

entry(
    index = 340,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.43184e-08,'m^3/(mol*s)'), n=4.29567, w0=(485,'kJ/mol'), E0=(166.374,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1435250581045639, var=0.3600922451326483, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 1.5636108663242876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.5636108663242876""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.5636108663242876
""",
)

entry(
    index = 341,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(5.94508e-05,'m^3/(mol*s)'), n=3.37621, w0=(485,'kJ/mol'), E0=(190.622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14501143760179874, var=0.535319801453646, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 1.8311258333110374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 1.8311258333110374""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 1.8311258333110374
""",
)

entry(
    index = 342,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(2.46703e-07,'m^3/(mol*s)'), n=4.01498, w0=(485,'kJ/mol'), E0=(174.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.847640735516106, var=15.359050616724181, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 12.498995403011742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 12.498995403011742""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 12.498995403011742
""",
)

entry(
    index = 343,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F",
    kinetics = ArrheniusBM(A=(1.04194e-07,'m^3/(mol*s)'), n=3.9712, w0=(485,'kJ/mol'), E0=(168.055,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12341804144031279, var=0.03795975742173232, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F
    Total Standard Deviation in ln(k): 0.7006834081722779"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F
Total Standard Deviation in ln(k): 0.7006834081722779""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F
Total Standard Deviation in ln(k): 0.7006834081722779
""",
)

entry(
    index = 344,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->F",
    kinetics = ArrheniusBM(A=(9.11574e-08,'m^3/(mol*s)'), n=4.14961, w0=(485,'kJ/mol'), E0=(177.038,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.02769e-08,'m^3/(mol*s)'), n=4.09467, w0=(485,'kJ/mol'), E0=(170.981,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1344579195349335, var=0.5134742245781766, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.7743693047131563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.7743693047131563""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.7743693047131563
""",
)

entry(
    index = 346,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_Sp-6R!H=4C",
    kinetics = ArrheniusBM(A=(3.8501e-07,'m^3/(mol*s)'), n=3.92844, w0=(485,'kJ/mol'), E0=(191.208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_Sp-6R!H=4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_Sp-6R!H=4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_Sp-6R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_Sp-6R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 347,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C",
    kinetics = ArrheniusBM(A=(9.19499e-07,'m^3/(mol*s)'), n=3.75122, w0=(485,'kJ/mol'), E0=(180.122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16931566407085466, var=3.515915180339681, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C
    Total Standard Deviation in ln(k): 4.1844496375519515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C
Total Standard Deviation in ln(k): 4.1844496375519515""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C
Total Standard Deviation in ln(k): 4.1844496375519515
""",
)

entry(
    index = 348,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.68364e-05,'m^3/(mol*s)'), n=3.9376, w0=(485,'kJ/mol'), E0=(195.002,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 349,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C",
    kinetics = ArrheniusBM(A=(2.28891e-06,'m^3/(mol*s)'), n=3.82239, w0=(485,'kJ/mol'), E0=(176.853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C",
    kinetics = ArrheniusBM(A=(0.00168439,'m^3/(mol*s)'), n=3.12619, w0=(485,'kJ/mol'), E0=(197.881,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1.43033e-06,'m^3/(mol*s)'), n=3.73989, w0=(485,'kJ/mol'), E0=(195.288,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.029338637895178165, var=3.7318857833729817, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 3.9464803168381426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9464803168381426""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9464803168381426
""",
)

entry(
    index = 352,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(0.00139189,'m^3/(mol*s)'), n=2.83127, w0=(485,'kJ/mol'), E0=(200.974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13039190977957113, var=3.2232542925893632, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 3.9268037262861055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9268037262861055""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9268037262861055
""",
)

entry(
    index = 353,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.31087e-08,'m^3/(mol*s)'), n=4.12499, w0=(485,'kJ/mol'), E0=(171.382,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 354,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.14559e-08,'m^3/(mol*s)'), n=4.27069, w0=(485,'kJ/mol'), E0=(170.247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.45985e-08,'m^3/(mol*s)'), n=4.20193, w0=(485,'kJ/mol'), E0=(166.436,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(6.21207e-09,'m^3/(mol*s)'), n=4.38354, w0=(485,'kJ/mol'), E0=(166.362,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0001135,'m^3/(mol*s)'), n=3.32, w0=(485,'kJ/mol'), E0=(195.165,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 358,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.05889e-05,'m^3/(mol*s)'), n=3.30617, w0=(485,'kJ/mol'), E0=(194.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21443168705568316, var=0.0840085163809187, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.1198299618386542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 1.1198299618386542""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 1.1198299618386542
""",
)

entry(
    index = 359,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9.11391e-08,'m^3/(mol*s)'), n=3.97251, w0=(485,'kJ/mol'), E0=(166.8,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12852274226468113, var=0.13186923682206217, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R
    Total Standard Deviation in ln(k): 1.05091703170753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 1.05091703170753""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 1.05091703170753
""",
)

entry(
    index = 360,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.11856e-08,'m^3/(mol*s)'), n=4.0381, w0=(485,'kJ/mol'), E0=(165.871,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.32707e-08,'m^3/(mol*s)'), n=4.09227, w0=(485,'kJ/mol'), E0=(176.621,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.83125e-07,'m^3/(mol*s)'), n=3.8806, w0=(485,'kJ/mol'), E0=(197.6,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 363,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_6R!H->F",
    kinetics = ArrheniusBM(A=(3.50479e-07,'m^3/(mol*s)'), n=3.85832, w0=(485,'kJ/mol'), E0=(171.028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 364,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_N-6R!H->F",
    kinetics = ArrheniusBM(A=(6.55056e-06,'m^3/(mol*s)'), n=3.42741, w0=(485,'kJ/mol'), E0=(172.504,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 365,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.76532e-06,'m^3/(mol*s)'), n=3.58647, w0=(485,'kJ/mol'), E0=(192.053,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.00057e-07,'m^3/(mol*s)'), n=4.05084, w0=(485,'kJ/mol'), E0=(197.154,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 367,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00676358,'m^3/(mol*s)'), n=2.69434, w0=(485,'kJ/mol'), E0=(203.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1920396451478112, var=11.520881032749676, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.287068342570407"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.287068342570407""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.287068342570407
""",
)

entry(
    index = 368,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.96e-05,'m^3/(mol*s)'), n=3.23, w0=(485,'kJ/mol'), E0=(204.744,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 369,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.915e-05,'m^3/(mol*s)'), n=3.31, w0=(485,'kJ/mol'), E0=(197.747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 370,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(7.80562e-08,'m^3/(mol*s)'), n=3.96948, w0=(485,'kJ/mol'), E0=(166.513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 371,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.03271e-07,'m^3/(mol*s)'), n=3.97927, w0=(485,'kJ/mol'), E0=(167.054,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->F_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000284922,'m^3/(mol*s)'), n=3.00496, w0=(485,'kJ/mol'), E0=(205.158,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

