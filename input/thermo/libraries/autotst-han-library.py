#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "N[N]OO",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u1 p1 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90299,0.00614381,8.55768e-05,-2.00625e-07,1.36698e-10,23854.5,8.94714], Tmin=(10,'K'), Tmax=(512.97,'K')),
            NASAPolynomial(coeffs=[4.76276,0.0196367,-1.2938e-05,4.16178e-09,-5.13339e-13,23500.6,2.78305], Tmin=(512.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (198.31,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 51.1 kcal/mol   or 213.8 kJ/mol
""",
)

entry(
    index = 1,
    label = "NON(OO)N",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u0 p2 c0 {2,S} {11,S}
4  N u0 p1 c0 {1,S} {2,S} {5,S}
5  N u0 p1 c0 {4,S} {7,S} {8,S}
6  N u0 p1 c0 {1,S} {9,S} {10,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80702,0.0135751,0.000165803,-4.47096e-07,3.51964e-10,20642.8,10.5924], Tmin=(10,'K'), Tmax=(440.597,'K')),
            NASAPolynomial(coeffs=[4.80426,0.0369686,-2.43043e-05,7.69984e-09,-9.3153e-13,20240,3.02463], Tmin=(440.597,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (171.619,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 46.0 kcal/mol   or 192.3 kJ/mol
""",
)

entry(
    index = 2,
    label = "[N-][N+](=O)OO",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,D} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u0 p2 c0 {1,D}
5 N u1 p2 c-1 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88826,0.00755756,8.34898e-05,-2.20531e-07,1.65413e-10,38767,10.07], Tmin=(10,'K'), Tmax=(471.937,'K')),
            NASAPolynomial(coeffs=[4.94591,0.0182781,-1.31503e-05,4.36651e-09,-5.41527e-13,38447.9,3.43909], Tmin=(471.937,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (322.308,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 80.8 kcal/mol   or 337.9 kJ/mol
""",
)

entry(
    index = 3,
    label = "NNO[O]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91846,0.0067813,8.21289e-05,-2.38829e-07,2.15453e-10,25873.9,9.46799], Tmin=(10,'K'), Tmax=(353.25,'K')),
            NASAPolynomial(coeffs=[3.29178,0.0216229,-1.37818e-05,4.24654e-09,-5.0273e-13,25869.9,11.1553], Tmin=(353.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (215.139,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 55.0 kcal/mol   or 230.3 kJ/mol
""",
)

entry(
    index = 4,
    label = "[O-][N+]=O",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {3,D}
2 O u0 p3 c-1 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03052,-0.00198698,1.67501e-05,-2.04844e-08,7.97573e-12,5126.84,5.85518], Tmin=(10,'K'), Tmax=(811.143,'K')),
            NASAPolynomial(coeffs=[3.01319,0.00609918,-3.87926e-06,1.13566e-09,-1.25553e-13,5190.91,9.9278], Tmin=(811.143,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (42.6345,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 12.6 kcal/mol   or 52.8 kJ/mol
""",
)

entry(
    index = 5,
    label = "ON=N[O]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,D} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95162,0.00292566,5.02665e-05,-1.05936e-07,6.59968e-11,20072,8.62838], Tmin=(10,'K'), Tmax=(545.381,'K')),
            NASAPolynomial(coeffs=[3.86994,0.0141443,-9.79656e-06,3.18687e-09,-3.91012e-13,19923,7.52503], Tmin=(545.381,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (166.871,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 43.0 kcal/mol   or 180.0 kJ/mol
""",
)

entry(
    index = 6,
    label = "OONN=O",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,S} {6,D}
4 O u0 p2 c0 {2,S} {7,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83954,0.0124711,8.74357e-05,-2.74397e-07,2.3922e-10,15861.2,9.53011], Tmin=(10,'K'), Tmax=(407.675,'K')),
            NASAPolynomial(coeffs=[4.79174,0.0217127,-1.49471e-05,4.84854e-09,-5.93916e-13,15629.1,3.8966], Tmin=(407.675,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (131.879,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 35.6 kcal/mol   or 148.8 kJ/mol
""",
)

entry(
    index = 7,
    label = "O=NO[N+](=O)[O-]",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {6,S}
2 O u0 p3 c-1 {5,S}
3 O u0 p2 c0 {5,D}
4 O u0 p2 c0 {6,D}
5 N u0 p0 c+1 {1,S} {2,S} {3,D}
6 N u0 p1 c0 {1,S} {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72078,0.0308655,-5.14459e-05,6.11841e-08,-3.33456e-11,6365.47,10.7384], Tmin=(10,'K'), Tmax=(427.342,'K')),
            NASAPolynomial(coeffs=[4.81046,0.0206659,-1.56447e-05,5.3332e-09,-6.72195e-13,6272.34,6.40778], Tmin=(427.342,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (52.9511,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 16.9 kcal/mol   or 70.6 kJ/mol
""",
)

entry(
    index = 8,
    label = "NO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03072,-0.00243896,3.5739e-05,-5.27946e-08,2.6162e-11,-5532.33,4.78721], Tmin=(10,'K'), Tmax=(559.827,'K')),
            NASAPolynomial(coeffs=[2.24421,0.0117544,-6.11851e-06,1.60954e-09,-1.68711e-13,-5354.69,12.1698], Tmin=(559.827,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-45.9966,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -8.4 kcal/mol   or -35.1 kJ/mol
""",
)

entry(
    index = 9,
    label = "O=NN=O",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 N u0 p1 c0 {1,S} {4,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92296,0.00588847,4.92178e-05,-1.70783e-07,1.60943e-10,26140.3,7.23998], Tmin=(10,'K'), Tmax=(390.39,'K')),
            NASAPolynomial(coeffs=[4.88719,0.00806713,-5.48488e-06,1.75233e-09,-2.13179e-13,25973.1,2.31826], Tmin=(390.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (217.347,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 55.1 kcal/mol   or 230.7 kJ/mol
""",
)

entry(
    index = 10,
    label = "OCNC=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  N u0 p1 c0 {1,S} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {8,D} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85594,0.0122743,6.15621e-05,-1.19353e-07,6.78774e-11,-46612.7,9.53201], Tmin=(10,'K'), Tmax=(548.543,'K')),
            NASAPolynomial(coeffs=[1.75657,0.0350756,-2.12766e-05,6.22493e-09,-7.03358e-13,-46495.1,17.3721], Tmin=(548.543,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-387.58,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -88.6 kcal/mol   or -370.7 kJ/mol
""",
)

entry(
    index = 11,
    label = "CO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02178,-0.00144007,3.30595e-05,-3.95611e-08,1.53708e-11,-25281.9,5.04853], Tmin=(10,'K'), Tmax=(671.149,'K')),
            NASAPolynomial(coeffs=[0.853887,0.0174384,-9.12921e-06,2.34152e-09,-2.36148e-13,-24856.7,19.0689], Tmin=(671.149,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-210.201,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -47.5 kcal/mol   or -198.9 kJ/mol
""",
)

entry(
    index = 12,
    label = "NNNN",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {5,S}
2  N u0 p1 c0 {1,S} {4,S} {6,S}
3  N u0 p1 c0 {1,S} {7,S} {8,S}
4  N u0 p1 c0 {2,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9436,0.00348848,0.0001028,-2.00204e-07,1.22884e-10,33770.7,8.53211], Tmin=(10,'K'), Tmax=(506.626,'K')),
            NASAPolynomial(coeffs=[1.5395,0.0337975,-2.04764e-05,6.14837e-09,-7.20708e-13,33868.9,17.061], Tmin=(506.626,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (280.768,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 70.9 kcal/mol   or 296.6 kJ/mol
""",
)

entry(
    index = 13,
    label = "N[NH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u1 p1 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05353,-0.0047661,5.29897e-05,-9.00223e-08,5.20435e-11,26291.3,5.25509], Tmin=(10,'K'), Tmax=(498.25,'K')),
            NASAPolynomial(coeffs=[2.36308,0.0118724,-6.33535e-06,1.71123e-09,-1.83936e-13,26421.7,11.8508], Tmin=(498.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (218.598,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 54.9 kcal/mol   or 229.5 kJ/mol
""",
)

entry(
    index = 14,
    label = "[NH-][NH+]=O",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 N u0 p2 c-1 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08219,-0.00558402,4.4875e-05,-5.58868e-08,2.26221e-11,15071.4,6.44971], Tmin=(10,'K'), Tmax=(761.909,'K')),
            NASAPolynomial(coeffs=[1.41903,0.0150247,-8.74536e-06,2.44708e-09,-2.64541e-13,15284.8,17.3114], Tmin=(761.909,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (125.328,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 32.5 kcal/mol   or 135.8 kJ/mol
""",
)

entry(
    index = 15,
    label = "[NH]OCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {7,S}
3 N u1 p1 c0 {1,S} {8,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95488,0.00285179,8.36406e-05,-1.68034e-07,1.06429e-10,-11960.7,9.23096], Tmin=(10,'K'), Tmax=(488.948,'K')),
            NASAPolynomial(coeffs=[2.07134,0.0269182,-1.67504e-05,5.05963e-09,-5.90408e-13,-11880,15.912], Tmin=(488.948,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-99.4586,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -20.3 kcal/mol   or -84.8 kJ/mol
""",
)

entry(
    index = 16,
    label = "[O]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02939,-0.00177212,1.08504e-05,-1.12259e-08,3.79676e-12,721.889,4.66014], Tmin=(10,'K'), Tmax=(904.176,'K')),
            NASAPolynomial(coeffs=[3.03647,0.00437111,-2.24528e-06,5.71189e-10,-5.71528e-14,829.883,8.95465], Tmin=(904.176,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (6.00998,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 3.8 kcal/mol   or 16.0 kJ/mol
""",
)

entry(
    index = 17,
    label = "[CH2]",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00393,-0.00019779,3.40617e-06,-2.45227e-09,5.47486e-13,44837.8,0.591954], Tmin=(10,'K'), Tmax=(915.786,'K')),
            NASAPolynomial(coeffs=[3.22363,0.00277554,-7.51684e-07,5.6009e-11,4.30117e-15,44998.9,4.38733], Tmin=(915.786,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (372.804,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 91.5 kcal/mol   or 382.9 kJ/mol
""",
)

entry(
    index = 18,
    label = "[N]=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u1 p1 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5056,-0.000299994,6.59625e-07,1.51624e-09,-1.43304e-12,10966.4,4.72781], Tmin=(10,'K'), Tmax=(712.48,'K')),
            NASAPolynomial(coeffs=[2.91564,0.00166529,-6.42322e-07,8.11939e-11,1.49677e-15,11084.6,7.61395], Tmin=(712.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (91.182,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 23.9 kcal/mol   or 99.8 kJ/mol
""",
)

entry(
    index = 19,
    label = "NN(N=O)OO",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {5,S}
4 N u0 p1 c0 {1,S} {8,D}
5 O u0 p2 c0 {3,S} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {4,D}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83601,0.010907,0.000134719,-3.43837e-07,2.52496e-10,24376,10.1732], Tmin=(10,'K'), Tmax=(478.977,'K')),
            NASAPolynomial(coeffs=[5.33533,0.0293495,-2.00047e-05,6.48205e-09,-7.96283e-13,23877.2,0.33577], Tmin=(478.977,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (202.643,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 52.9 kcal/mol   or 221.4 kJ/mol
""",
)

entry(
    index = 20,
    label = "O=C[N+](=O)[O-]",
    molecule = 
"""
1 O u0 p3 c-1 {4,S}
2 O u0 p2 c0 {5,D}
3 O u0 p2 c0 {4,D}
4 N u0 p0 c+1 {1,S} {3,D} {5,S}
5 C u0 p0 c0 {2,D} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88092,0.0114878,1.85161e-05,-4.09094e-08,2.10747e-11,-15513.1,9.3916], Tmin=(10,'K'), Tmax=(705.713,'K')),
            NASAPolynomial(coeffs=[4.32151,0.0171505,-1.08643e-05,3.22995e-09,-3.66013e-13,-15778.4,5.97994], Tmin=(705.713,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-128.994,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -27.3 kcal/mol   or -114.4 kJ/mol
""",
)

entry(
    index = 21,
    label = "ON=[N+]([O])[O-]",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,D} {4,S} {5,S}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u1 p2 c0 {1,S}
5 O u0 p3 c-1 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9444,0.00322112,6.53081e-05,-1.26524e-07,7.30069e-11,11823.7,9.71332], Tmin=(10,'K'), Tmax=(577.69,'K')),
            NASAPolynomial(coeffs=[3.18743,0.0213455,-1.52042e-05,4.99277e-09,-6.1406e-13,11696.2,11.0893], Tmin=(577.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (98.2843,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 26.8 kcal/mol   or 112.3 kJ/mol
""",
)

entry(
    index = 22,
    label = "[N-]([NH2+])OO",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {5,S} {6,S}
2 N u0 p2 c-1 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90646,0.00605078,8.58346e-05,-2.05054e-07,1.43398e-10,24248.2,9.17785], Tmin=(10,'K'), Tmax=(495.894,'K')),
            NASAPolynomial(coeffs=[4.50016,0.0200078,-1.30869e-05,4.16467e-09,-5.08001e-13,23958.8,4.40601], Tmin=(495.894,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (201.588,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 51.9 kcal/mol   or 217.0 kJ/mol
""",
)

entry(
    index = 23,
    label = "O1NN1",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10215,-0.00702705,5.26525e-05,-6.71541e-08,2.77884e-11,39067.8,6.48171], Tmin=(10,'K'), Tmax=(757.613,'K')),
            NASAPolynomial(coeffs=[1.47837,0.0155775,-9.42991e-06,2.72321e-09,-3.01369e-13,39214.2,16.754], Tmin=(757.613,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (324.849,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 80.1 kcal/mol   or 335.3 kJ/mol
""",
)

entry(
    index = 24,
    label = "[O-][NH+]=O",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 O u0 p3 c-1 {1,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06061,-0.00380639,2.79624e-05,-3.18501e-08,1.16783e-11,-3823.94,5.6277], Tmin=(10,'K'), Tmax=(848.018,'K')),
            NASAPolynomial(coeffs=[1.97005,0.010826,-6.35968e-06,1.7671e-09,-1.88301e-13,-3640.94,14.3573], Tmin=(848.018,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-31.7782,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -5.2 kcal/mol   or -21.6 kJ/mol
""",
)

entry(
    index = 25,
    label = "C=C",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10346,-0.00715168,5.47077e-05,-6.72882e-08,2.73047e-11,5584.75,3.21758], Tmin=(10,'K'), Tmax=(738.508,'K')),
            NASAPolynomial(coeffs=[0.53942,0.0184367,-1.00298e-05,2.67425e-09,-2.79621e-13,5939.79,18.1714], Tmin=(738.508,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (46.4546,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 13.6 kcal/mol   or 57.0 kJ/mol
""",
)

entry(
    index = 26,
    label = "[H][H]",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49732,0.000137814,-6.65169e-07,9.25717e-10,-3.10184e-13,-529.691,-4.28924], Tmin=(10,'K'), Tmax=(1120.23,'K')),
            NASAPolynomial(coeffs=[3.57713,-0.000555165,8.09041e-07,-2.76721e-10,3.07174e-14,-521.973,-4.56909], Tmin=(1120.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-4.40473,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 1.0 kcal/mol   or 4.3 kJ/mol
""",
)

entry(
    index = 27,
    label = "[OH]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49677,0.000195375,-1.08774e-06,1.75854e-09,-7.05589e-13,4216.7,1.4728], Tmin=(10,'K'), Tmax=(958.045,'K')),
            NASAPolynomial(coeffs=[3.42174,-0.000221542,7.08238e-07,-2.86738e-10,3.57125e-14,4264.59,2.00643], Tmin=(958.045,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (35.0586,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 10.5 kcal/mol   or 43.7 kJ/mol
""",
)

entry(
    index = 28,
    label = "N=N",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03248,-0.00200048,8.83734e-06,3.64736e-09,-8.76239e-12,24738.6,3.42045], Tmin=(10,'K'), Tmax=(585.686,'K')),
            NASAPolynomial(coeffs=[1.5148,0.00914966,-4.23847e-06,9.0981e-10,-7.22094e-14,25137.2,15.105], Tmin=(585.686,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (205.699,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 51.5 kcal/mol   or 215.6 kJ/mol
""",
)

entry(
    index = 29,
    label = "ON(O)[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,S} {6,S}
3 O u1 p2 c0 {4,S}
4 N u0 p1 c0 {1,S} {2,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90971,0.00629089,7.30806e-05,-1.93877e-07,1.49234e-10,-9120.52,9.20419], Tmin=(10,'K'), Tmax=(451.629,'K')),
            NASAPolynomial(coeffs=[4.39352,0.0168657,-1.13957e-05,3.67497e-09,-4.4896e-13,-9315.77,5.5769], Tmin=(451.629,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-75.8422,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -14.6 kcal/mol   or -61.1 kJ/mol
""",
)

entry(
    index = 30,
    label = "[O-]C=[NH+]CO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  N u0 p0 c+1 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p3 c-1 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78971,0.0224984,7.45904e-06,-2.1285e-08,8.6293e-12,-45105,9.69015], Tmin=(10,'K'), Tmax=(966.596,'K')),
            NASAPolynomial(coeffs=[4.68522,0.0278706,-1.49651e-05,3.89731e-09,-3.96844e-13,-45702.2,3.20658], Tmin=(966.596,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-375.02,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -85.3 kcal/mol   or -357.1 kJ/mol
""",
)

entry(
    index = 31,
    label = "[O-]N=[NH2+]",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 N u0 p1 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p3 c-1 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93909,0.00711848,4.73076e-06,-8.98138e-09,3.36716e-12,9242.95,6.56466], Tmin=(10,'K'), Tmax=(992.947,'K')),
            NASAPolynomial(coeffs=[4.02795,0.0102797,-5.36108e-06,1.36366e-09,-1.36154e-13,9051.81,5.26302], Tmin=(992.947,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (76.8546,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 21.4 kcal/mol   or 89.5 kJ/mol
""",
)

entry(
    index = 32,
    label = "ONC=O",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94869,0.00340704,7.67231e-05,-1.71089e-07,1.18776e-10,-24283.7,8.07609], Tmin=(10,'K'), Tmax=(461.189,'K')),
            NASAPolynomial(coeffs=[2.9527,0.0215834,-1.34165e-05,4.05361e-09,-4.73312e-13,-24293.3,11.0106], Tmin=(461.189,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-201.915,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -44.8 kcal/mol   or -187.6 kJ/mol
""",
)

entry(
    index = 33,
    label = "[NH2]",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00668,-0.00033722,1.37598e-06,1.42413e-09,-1.39651e-12,22414.2,0.597446], Tmin=(10,'K'), Tmax=(780.506,'K')),
            NASAPolynomial(coeffs=[3.19945,0.0020794,3.78643e-08,-2.56912e-10,4.64763e-14,22592.6,4.62751], Tmin=(780.506,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (186.364,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 46.9 kcal/mol   or 196.3 kJ/mol
""",
)

entry(
    index = 34,
    label = "[O-][N+](=[N])OO",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,S} {5,D}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u0 p3 c-1 {1,S}
5 N u1 p1 c0 {1,D}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86508,0.00959879,8.65381e-05,-2.539e-07,2.06658e-10,37490.2,10.1149], Tmin=(10,'K'), Tmax=(442.636,'K')),
            NASAPolynomial(coeffs=[5.3391,0.0175764,-1.26705e-05,4.22457e-09,-5.26374e-13,37151,1.84816], Tmin=(442.636,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (311.7,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 78.4 kcal/mol   or 327.8 kJ/mol
""",
)

entry(
    index = 35,
    label = "N[O]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93604,0.00543028,-9.14095e-06,1.77531e-08,-1.13081e-11,6241.36,4.95279], Tmin=(10,'K'), Tmax=(613.713,'K')),
            NASAPolynomial(coeffs=[3.08942,0.00696953,-3.17835e-06,7.12165e-10,-6.31086e-14,6420.21,9.23438], Tmin=(613.713,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (51.8907,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 15.1 kcal/mol   or 63.2 kJ/mol
""",
)

entry(
    index = 36,
    label = "[CH]=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01436,-0.000862624,5.03655e-06,-3.18818e-10,-2.61454e-12,4438.24,4.13282], Tmin=(10,'K'), Tmax=(613.992,'K')),
            NASAPolynomial(coeffs=[2.72707,0.00483137,-2.29652e-06,5.0154e-10,-4.06205e-14,4647.07,10.1286], Tmin=(613.992,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (36.9068,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 11.2 kcal/mol   or 46.9 kJ/mol
""",
)

entry(
    index = 37,
    label = "O=C=O",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53549,-0.00354738,4.04383e-05,-7.43658e-08,4.47213e-11,-48428.9,5.38077], Tmin=(10,'K'), Tmax=(525.115,'K')),
            NASAPolynomial(coeffs=[2.79356,0.00719226,-4.77369e-06,1.48564e-09,-1.75304e-13,-48421.1,7.81432], Tmin=(525.115,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-402.664,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -94.0 kcal/mol   or -393.3 kJ/mol
""",
)

entry(
    index = 38,
    label = "[N-]=[N+]OO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u1 p0 c+1 {1,S} {4,D}
4 N u0 p2 c-1 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38563,0.0619644,-0.000268072,5.1705e-07,-3.58758e-10,281.736,10.5635], Tmin=(10,'K'), Tmax=(439.777,'K')),
            NASAPolynomial(coeffs=[7.05325,0.00643619,-3.06014e-06,6.85287e-10,-5.82187e-14,173.531,-1.68032], Tmin=(439.777,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (2.32985,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 5.0 kcal/mol   or 21.0 kJ/mol
""",
)

entry(
    index = 39,
    label = "[O-][N+](=O)CO",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {8,S}
2 O u0 p3 c-1 {4,S}
3 O u0 p2 c0 {4,D}
4 N u0 p0 c+1 {2,S} {3,D} {5,S}
5 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85736,0.013905,2.76198e-05,-5.37204e-08,2.62481e-11,-29358.1,9.48269], Tmin=(10,'K'), Tmax=(713.092,'K')),
            NASAPolynomial(coeffs=[3.54627,0.0249049,-1.49863e-05,4.31217e-09,-4.78047e-13,-29549,9.2284], Tmin=(713.092,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-244.108,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -54.5 kcal/mol   or -228.2 kJ/mol
""",
)

entry(
    index = 40,
    label = "NNOO",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {3,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92183,0.00486119,8.92994e-05,-1.91351e-07,1.23508e-10,9881.58,8.42535], Tmin=(10,'K'), Tmax=(519.536,'K')),
            NASAPolynomial(coeffs=[3.53367,0.0245036,-1.54954e-05,4.82131e-09,-5.80219e-13,9697.15,7.88072], Tmin=(519.536,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (82.1357,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 23.3 kcal/mol   or 97.6 kJ/mol
""",
)

entry(
    index = 41,
    label = "[O-][N+](=O)[O]",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 O u1 p2 c0 {1,S}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97229,0.00155053,3.36936e-05,-6.20281e-08,3.38522e-11,12385.3,7.88315], Tmin=(10,'K'), Tmax=(607.663,'K')),
            NASAPolynomial(coeffs=[3.36808,0.0122152,-9.13947e-06,3.07447e-09,-3.82673e-13,12335.3,9.48121], Tmin=(607.663,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (102.965,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 27.5 kcal/mol   or 115.0 kJ/mol
""",
)

entry(
    index = 42,
    label = "C[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0214,-0.0015237,3.01088e-05,-3.93438e-08,1.68268e-11,326.182,5.38905], Tmin=(10,'K'), Tmax=(574.815,'K')),
            NASAPolynomial(coeffs=[1.76012,0.0135116,-7.29888e-06,1.92192e-09,-1.98696e-13,597.715,15.1469], Tmin=(574.815,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (2.71529,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 3.3 kcal/mol   or 13.7 kJ/mol
""",
)

entry(
    index = 43,
    label = "[NH]C=O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 N u1 p1 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98455,0.00103187,4.13611e-05,-8.44372e-08,5.67781e-11,7273.43,7.36863], Tmin=(10,'K'), Tmax=(380.457,'K')),
            NASAPolynomial(coeffs=[2.78933,0.013598,-8.18226e-06,2.37595e-09,-2.66947e-13,7364.38,11.9799], Tmin=(380.457,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (60.4719,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 17.4 kcal/mol   or 72.6 kJ/mol
""",
)

entry(
    index = 44,
    label = "[O-]N=[NH+]N",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p3 c-1 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80575,0.0200661,-3.71651e-05,9.17985e-08,-8.4547e-11,20370.9,10.0889], Tmin=(10,'K'), Tmax=(404.992,'K')),
            NASAPolynomial(coeffs=[2.86039,0.0214816,-1.30685e-05,3.83603e-09,-4.3481e-13,20512.5,14.5973], Tmin=(404.992,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (169.368,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 44.1 kcal/mol   or 184.7 kJ/mol
""",
)

entry(
    index = 45,
    label = "NNN=O",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80573,0.020069,-3.71896e-05,9.18646e-08,-8.46054e-11,20370.7,10.0959], Tmin=(10,'K'), Tmax=(404.981,'K')),
            NASAPolynomial(coeffs=[2.8603,0.0214819,-1.30687e-05,3.83607e-09,-4.34815e-13,20512.2,14.6048], Tmin=(404.981,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (169.366,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 44.1 kcal/mol   or 184.7 kJ/mol
""",
)

entry(
    index = 46,
    label = "[NH-][NH+]N[NH]",
    molecule = 
"""
multiplicity 3
1 N u1 p0 c+1 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u1 p1 c0 {2,S} {8,S}
4 N u0 p2 c-1 {1,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93539,0.00401521,8.67286e-05,-1.79689e-07,1.14067e-10,66825.6,8.87799], Tmin=(10,'K'), Tmax=(514.491,'K')),
            NASAPolynomial(coeffs=[2.8874,0.025741,-1.61994e-05,4.97829e-09,-5.91316e-13,66753.7,11.4911], Tmin=(514.491,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (555.599,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 136.4 kcal/mol   or 570.7 kJ/mol
""",
)

entry(
    index = 47,
    label = "NO[O]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97856,0.00681315,5.05116e-06,-8.4772e-09,2.9034e-12,17416,7.45033], Tmin=(10,'K'), Tmax=(1115.82,'K')),
            NASAPolynomial(coeffs=[4.7175,0.00899146,-4.36648e-06,1.02673e-09,-9.46567e-14,16950.6,2.45782], Tmin=(1115.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (144.822,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 37.6 kcal/mol   or 157.4 kJ/mol
""",
)

entry(
    index = 48,
    label = "CC=O",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97472,0.00135676,4.58316e-05,-6.95672e-08,3.40711e-11,-21163.2,7.0971], Tmin=(10,'K'), Tmax=(527.935,'K')),
            NASAPolynomial(coeffs=[1.30513,0.0215849,-1.16459e-05,3.01958e-09,-3.044e-13,-20881.3,18.2709], Tmin=(527.935,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.974,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -39.0 kcal/mol   or -163.3 kJ/mol
""",
)

entry(
    index = 49,
    label = "[N-]([NH+]=N)N",
    molecule = 
"""
1 N u0 p0 c+1 {3,S} {4,D} {5,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 N u0 p2 c-1 {1,S} {2,S}
4 N u0 p1 c0 {1,D} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97042,0.0017367,7.29814e-05,-1.26697e-07,6.962e-11,45310.4,7.5346], Tmin=(10,'K'), Tmax=(532.78,'K')),
            NASAPolynomial(coeffs=[0.8725,0.0298256,-1.97004e-05,6.29252e-09,-7.68671e-13,45572,19.8863], Tmin=(532.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (376.72,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 93.4 kcal/mol   or 390.8 kJ/mol
""",
)

entry(
    index = 50,
    label = "[NH-][NH2+]",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {3,S} {4,S}
2 N u0 p2 c-1 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05353,-0.0047659,5.29897e-05,-9.00241e-08,5.20456e-11,26291.2,5.25509], Tmin=(10,'K'), Tmax=(498.236,'K')),
            NASAPolynomial(coeffs=[2.36313,0.0118722,-6.33524e-06,1.71119e-09,-1.83931e-13,26421.6,11.8506], Tmin=(498.236,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (218.598,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 54.9 kcal/mol   or 229.5 kJ/mol
""",
)

entry(
    index = 51,
    label = "[O-]C=[NH+]O",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 O u0 p3 c-1 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95041,0.00315426,7.32702e-05,-1.5419e-07,1.00512e-10,-24909.4,8.08234], Tmin=(10,'K'), Tmax=(493.03,'K')),
            NASAPolynomial(coeffs=[2.87919,0.0217764,-1.36008e-05,4.13166e-09,-4.85171e-13,-24924.5,11.2687], Tmin=(493.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-207.122,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -46.1 kcal/mol   or -192.9 kJ/mol
""",
)

entry(
    index = 52,
    label = "[O]N=O",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 O u1 p2 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03052,-0.001987,1.67501e-05,-2.04843e-08,7.97563e-12,5126.84,5.8552], Tmin=(10,'K'), Tmax=(811.154,'K')),
            NASAPolynomial(coeffs=[3.01322,0.00609913,-3.87921e-06,1.13564e-09,-1.2555e-13,5190.9,9.92768], Tmin=(811.154,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (42.6345,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 12.6 kcal/mol   or 52.8 kJ/mol
""",
)

entry(
    index = 53,
    label = "OCO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {3,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02972,-0.00301927,7.94217e-05,-1.41678e-07,8.27682e-11,-48940.8,6.36051], Tmin=(10,'K'), Tmax=(515.307,'K')),
            NASAPolynomial(coeffs=[1.73455,0.0217252,-1.27744e-05,3.6905e-09,-4.15246e-13,-48796.3,15.0191], Tmin=(515.307,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-406.923,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -94.2 kcal/mol   or -394.2 kJ/mol
""",
)

entry(
    index = 54,
    label = "[O]",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,29269.9,4.09089], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,29269.9,4.09089], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (243.363,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 59.6 kcal/mol   or 249.6 kJ/mol
""",
)

entry(
    index = 55,
    label = "NN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05735,-0.0046056,5.34589e-05,-7.9071e-08,3.93931e-11,11429.2,4.24356], Tmin=(10,'K'), Tmax=(565.68,'K')),
            NASAPolynomial(coeffs=[1.51466,0.0160522,-8.42026e-06,2.22413e-09,-2.33671e-13,11674.1,14.6832], Tmin=(565.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (95.0316,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 25.4 kcal/mol   or 106.2 kJ/mol
""",
)

entry(
    index = 56,
    label = "N=O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01584,-0.000896284,3.04035e-06,3.06515e-09,-3.99756e-12,13720.2,3.73773], Tmin=(10,'K'), Tmax=(660.578,'K')),
            NASAPolynomial(coeffs=[2.52368,0.00473315,-2.00833e-06,3.54776e-10,-1.77269e-14,13991.6,10.8803], Tmin=(660.578,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (114.082,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 29.6 kcal/mol   or 124.0 kJ/mol
""",
)

entry(
    index = 57,
    label = "O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00508,-0.000259529,1.08197e-06,1.22882e-09,-1.14022e-12,-28544.3,-0.11789], Tmin=(10,'K'), Tmax=(770.071,'K')),
            NASAPolynomial(coeffs=[3.46471,0.00130206,4.65821e-07,-3.37681e-10,5.00725e-14,-28424.1,2.58764], Tmin=(770.071,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-237.329,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -54.4 kcal/mol   or -227.4 kJ/mol
""",
)

entry(
    index = 58,
    label = "OONNNNOO",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {9,S}
2  N u0 p1 c0 {1,S} {4,S} {10,S}
3  N u0 p1 c0 {1,S} {5,S} {11,S}
4  N u0 p1 c0 {2,S} {6,S} {12,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {4,S} {8,S}
7  O u0 p2 c0 {5,S} {13,S}
8  O u0 p2 c0 {6,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3713,0.0583534,-4.39548e-05,1.5892e-08,-2.07127e-12,36583.8,13.8718], Tmin=(10,'K'), Tmax=(1149.46,'K')),
            NASAPolynomial(coeffs=[12.1608,0.0329594,-1.75928e-05,4.5325e-09,-4.55413e-13,34220.2,-31.2489], Tmin=(1149.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (304.134,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 79.1 kcal/mol   or 331.1 kJ/mol
""",
)

entry(
    index = 59,
    label = "ONO",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96697,0.0019293,4.93082e-05,-9.13694e-08,5.21904e-11,-12421,6.82294], Tmin=(10,'K'), Tmax=(562.144,'K')),
            NASAPolynomial(coeffs=[2.89717,0.016982,-1.07113e-05,3.3551e-09,-4.07216e-13,-12418.3,10.3222], Tmin=(562.144,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-103.288,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -21.6 kcal/mol   or -90.4 kJ/mol
""",
)

entry(
    index = 60,
    label = "[O-]N=[NH+]NOO",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {7,S}
2 N u0 p0 c+1 {1,S} {4,D} {6,S}
3 O u0 p2 c0 {1,S} {5,S}
4 N u0 p1 c0 {2,D} {8,S}
5 O u0 p2 c0 {3,S} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 O u0 p3 c-1 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77389,0.0184035,9.53708e-05,-2.94731e-07,2.4992e-10,23644.8,10.5637], Tmin=(10,'K'), Tmax=(414.553,'K')),
            NASAPolynomial(coeffs=[4.51263,0.0309206,-2.10039e-05,6.73066e-09,-8.16325e-13,23414.8,5.61414], Tmin=(414.553,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (196.592,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 51.6 kcal/mol   or 215.9 kJ/mol
""",
)

entry(
    index = 61,
    label = "[CH2]O",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98829,0.000678672,2.92815e-05,-4.84709e-08,2.61194e-11,-3418.6,5.10133], Tmin=(10,'K'), Tmax=(479.677,'K')),
            NASAPolynomial(coeffs=[2.59903,0.0122762,-7.0245e-06,2.04273e-09,-2.35951e-13,-3285.47,10.7816], Tmin=(479.677,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-28.4294,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -4.0 kcal/mol   or -16.8 kJ/mol
""",
)

entry(
    index = 62,
    label = "N=C=O",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,D} {4,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98371,0.00092206,2.46493e-05,-4.36721e-08,2.37442e-11,-16025.2,5.00311], Tmin=(10,'K'), Tmax=(588.519,'K')),
            NASAPolynomial(coeffs=[3.31771,0.00920577,-6.03988e-06,1.93979e-09,-2.39456e-13,-16011.9,7.31033], Tmin=(588.519,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.248,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -29.1 kcal/mol   or -121.8 kJ/mol
""",
)

entry(
    index = 63,
    label = "OONNN=O",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {6,S}
2 N u0 p1 c0 {1,S} {4,S} {7,S}
3 O u0 p2 c0 {1,S} {5,S}
4 N u0 p1 c0 {2,S} {8,D}
5 O u0 p2 c0 {3,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 O u0 p2 c0 {4,D}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73105,0.0229851,6.33404e-05,-2.14534e-07,1.8167e-10,25600,10.8714], Tmin=(10,'K'), Tmax=(425.655,'K')),
            NASAPolynomial(coeffs=[4.64738,0.0305988,-2.06651e-05,6.58477e-09,-7.94814e-13,25375,5.50674], Tmin=(425.655,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (212.843,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 55.5 kcal/mol   or 232.4 kJ/mol
""",
)

entry(
    index = 64,
    label = "OC[N-][N+](=O)OO",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  N u0 p0 c+1 {3,S} {5,S} {9,D}
3  N u0 p2 c-1 {1,S} {2,S}
4  O u0 p2 c0 {1,S} {10,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5876,0.0359393,5.01814e-06,-5.11539e-08,3.34291e-11,-8083.75,11.3569], Tmin=(10,'K'), Tmax=(634.013,'K')),
            NASAPolynomial(coeffs=[5.40497,0.0360568,-2.26649e-05,6.77127e-09,-7.74313e-13,-8547.01,1.58123], Tmin=(634.013,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-67.2626,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -10.8 kcal/mol   or -45.4 kJ/mol
""",
)

entry(
    index = 65,
    label = "OON=[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u1 p1 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25556,0.0807108,-0.00044723,1.00952e-06,-7.94555e-10,841.424,12.5562], Tmin=(10,'K'), Tmax=(404.03,'K')),
            NASAPolynomial(coeffs=[6.30236,0.0056828,-2.11999e-06,2.32412e-10,1.30385e-14,961.405,5.14994], Tmin=(404.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (6.97146,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (99.7737,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 6.1 kcal/mol   or 25.5 kJ/mol
""",
)

entry(
    index = 66,
    label = "[O][O]",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50726,-0.000428331,1.36598e-06,1.5945e-09,-2.19009e-12,-1286.12,4.69554], Tmin=(10,'K'), Tmax=(617.39,'K')),
            NASAPolynomial(coeffs=[2.875,0.00213387,-1.1317e-06,2.66641e-10,-2.26025e-14,-1178.81,7.67773], Tmin=(617.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-10.6906,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -0.5 kcal/mol   or -2.0 kJ/mol
""",
)

entry(
    index = 67,
    label = "[N]O",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 N u2 p1 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0318,-0.00215323,1.47161e-05,-1.79918e-08,7.22873e-12,23763.6,4.898], Tmin=(10,'K'), Tmax=(769.268,'K')),
            NASAPolynomial(coeffs=[3.20785,0.00438336,-2.42138e-06,6.65922e-10,-7.16365e-14,23823.7,8.22377], Tmin=(769.268,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (197.589,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 49.6 kcal/mol   or 207.6 kJ/mol
""",
)

entry(
    index = 68,
    label = "N1NNN1",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u0 p1 c0 {2,S} {4,S} {7,S}
4 N u0 p1 c0 {1,S} {3,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14234,-0.0105951,0.00010604,-1.49982e-07,6.84608e-11,66755.1,7.95253], Tmin=(10,'K'), Tmax=(688.773,'K')),
            NASAPolynomial(coeffs=[-0.00963099,0.0300607,-1.85282e-05,5.45977e-09,-6.16222e-13,66934.7,23.5867], Tmin=(688.773,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (555.05,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 135.5 kcal/mol   or 567.0 kJ/mol
""",
)

entry(
    index = 69,
    label = "NCO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9759,0.001465,6.70527e-05,-1.18586e-07,6.8409e-11,-25413.3,7.00237], Tmin=(10,'K'), Tmax=(446.977,'K')),
            NASAPolynomial(coeffs=[1.23506,0.0260166,-1.54194e-05,4.54026e-09,-5.24014e-13,-25168.5,18.0156], Tmin=(446.977,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-211.307,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -47.2 kcal/mol   or -197.7 kJ/mol
""",
)

entry(
    index = 70,
    label = "OCONCO",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {5,S} {13,S}
3  O u0 p2 c0 {6,S} {12,S}
4  N u0 p1 c0 {1,S} {5,S} {11,S}
5  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70377,0.0355166,-3.20053e-06,-1.43658e-08,6.14675e-12,-50003.5,10.8536], Tmin=(10,'K'), Tmax=(1095.68,'K')),
            NASAPolynomial(coeffs=[7.58164,0.0335273,-1.7135e-05,4.24794e-09,-4.12895e-13,-51583.7,-11.5422], Tmin=(1095.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-415.739,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -94.1 kcal/mol   or -393.9 kJ/mol
""",
)

entry(
    index = 71,
    label = "N",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01978,-0.001173,7.45025e-06,-1.88758e-09,-2.0629e-12,-5152.31,0.271682], Tmin=(10,'K'), Tmax=(648.453,'K')),
            NASAPolynomial(coeffs=[2.36238,0.00593012,-1.76211e-06,1.62222e-10,7.99592e-15,-4871.75,8.05563], Tmin=(648.453,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-42.8315,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -7.8 kcal/mol   or -32.8 kJ/mol
""",
)

entry(
    index = 72,
    label = "OCN=[N+](OO)[O-]",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  N u0 p0 c+1 {3,D} {5,S} {9,S}
3  N u0 p1 c0 {1,S} {2,D}
4  O u0 p2 c0 {1,S} {10,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p3 c-1 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61391,0.0334555,2.24553e-05,-9.05761e-08,6.18814e-11,-8004.76,11.315], Tmin=(10,'K'), Tmax=(558.859,'K')),
            NASAPolynomial(coeffs=[4.8753,0.0376355,-2.42155e-05,7.38823e-09,-8.6009e-13,-8352.01,4.11813], Tmin=(558.859,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-66.6019,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -10.7 kcal/mol   or -44.8 kJ/mol
""",
)

entry(
    index = 73,
    label = "[NH][O]",
    molecule = 
"""
multiplicity 3
1 N u1 p1 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02435,-0.00148705,1.01249e-05,-1.05274e-08,3.58291e-12,20219.4,4.71855], Tmin=(10,'K'), Tmax=(878.336,'K')),
            NASAPolynomial(coeffs=[3.01019,0.00444114,-2.23567e-06,5.51999e-10,-5.37871e-14,20347,9.19215], Tmin=(878.336,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (168.12,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 42.6 kcal/mol   or 178.1 kJ/mol
""",
)

entry(
    index = 74,
    label = "[NH-][NH+]OO",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {3,S} {5,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p2 c-1 {1,S} {6,S}
4 O u0 p2 c0 {2,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90234,0.00707925,8.72327e-05,-2.35562e-07,1.88629e-10,29000.8,9.43959], Tmin=(10,'K'), Tmax=(424.862,'K')),
            NASAPolynomial(coeffs=[3.9976,0.0209121,-1.36094e-05,4.27524e-09,-5.13558e-13,28859.7,7.49703], Tmin=(424.862,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (241.123,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 61.3 kcal/mol   or 256.7 kJ/mol
""",
)

entry(
    index = 75,
    label = "C",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0432,-0.0026308,1.26271e-05,2.72754e-09,-9.696e-12,-9703.63,-0.436126], Tmin=(10,'K'), Tmax=(601.439,'K')),
            NASAPolynomial(coeffs=[0.649382,0.0122013,-5.06253e-06,9.40449e-10,-5.98451e-14,-9155.42,15.3752], Tmin=(601.439,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-80.6656,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -16.9 kcal/mol   or -70.7 kJ/mol
""",
)

entry(
    index = 76,
    label = "O[N-][N+](=O)[O]",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,S} {5,D}
2 N u0 p2 c-1 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u1 p2 c0 {1,S}
5 O u0 p2 c0 {1,D}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94444,0.00321957,6.53214e-05,-1.2656e-07,7.30364e-11,11823.6,9.71325], Tmin=(10,'K'), Tmax=(577.593,'K')),
            NASAPolynomial(coeffs=[3.1865,0.0213482,-1.52067e-05,4.99376e-09,-6.14197e-13,11696.4,11.094], Tmin=(577.593,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (98.2838,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 26.8 kcal/mol   or 112.3 kJ/mol
""",
)

entry(
    index = 77,
    label = "[NH]",
    molecule = 
"""
multiplicity 3
1 N u2 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49646,0.000246946,-1.53786e-06,2.78813e-09,-1.27129e-12,42378.4,1.81088], Tmin=(10,'K'), Tmax=(858.808,'K')),
            NASAPolynomial(coeffs=[3.29242,0.000132422,5.22071e-07,-2.54722e-10,3.4779e-14,42452.7,2.99283], Tmin=(858.808,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (352.353,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 86.3 kcal/mol   or 361.0 kJ/mol
""",
)

entry(
    index = 78,
    label = "ONCO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {8,S}
2 O u0 p2 c0 {3,S} {9,S}
3 N u0 p1 c0 {2,S} {4,S} {7,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94561,0.00338421,9.41836e-05,-1.8678e-07,1.16158e-10,-29531.4,8.54766], Tmin=(10,'K'), Tmax=(503.911,'K')),
            NASAPolynomial(coeffs=[1.91705,0.0304094,-1.87769e-05,5.68061e-09,-6.66255e-13,-29465.6,15.5679], Tmin=(503.911,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-245.555,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -55.0 kcal/mol   or -230.2 kJ/mol
""",
)

entry(
    index = 79,
    label = "[NH]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u1 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04758,-0.00351274,2.92753e-05,-3.94701e-08,1.76656e-11,10748,5.05678], Tmin=(10,'K'), Tmax=(673.061,'K')),
            NASAPolynomial(coeffs=[2.59657,0.00838092,-4.51942e-06,1.22258e-09,-1.30621e-13,10869.2,10.9323], Tmin=(673.061,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (89.3703,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 23.8 kcal/mol   or 99.7 kJ/mol
""",
)

entry(
    index = 80,
    label = "[NH-][NH+]=NN",
    molecule = 
"""
1 N u0 p0 c+1 {3,D} {4,S} {5,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 N u0 p1 c0 {1,D} {2,S}
4 N u0 p2 c-1 {1,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97692,0.00152672,8.11198e-05,-1.59581e-07,1.0306e-10,47240.6,8.04356], Tmin=(10,'K'), Tmax=(396.865,'K')),
            NASAPolynomial(coeffs=[1.39501,0.0275236,-1.70395e-05,5.14331e-09,-6.01129e-13,47445.8,18.1163], Tmin=(396.865,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (392.778,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 97.3 kcal/mol   or 406.9 kJ/mol
""",
)

entry(
    index = 81,
    label = "[O-][N+](=NN=O)OO",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {6,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,D} {5,S}
4 O u0 p2 c0 {2,S} {8,S}
5 N u0 p1 c0 {3,S} {7,D}
6 O u0 p3 c-1 {1,S}
7 O u0 p2 c0 {5,D}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53709,0.0418306,-4.778e-05,2.85527e-08,-6.96715e-12,35318.8,11.3819], Tmin=(10,'K'), Tmax=(949.596,'K')),
            NASAPolynomial(coeffs=[8.86668,0.0193807,-1.23176e-05,3.65623e-09,-4.12649e-13,34306.6,-14.0547], Tmin=(949.596,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (293.609,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 75.2 kcal/mol   or 314.8 kJ/mol
""",
)

entry(
    index = 82,
    label = "[NH]NOO",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u1 p1 c0 {1,S} {6,S}
4 O u0 p2 c0 {2,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92578,0.00448248,7.74176e-05,-1.62472e-07,1.01173e-10,27814.9,8.90642], Tmin=(10,'K'), Tmax=(546.268,'K')),
            NASAPolynomial(coeffs=[3.87779,0.0213293,-1.41368e-05,4.53896e-09,-5.57537e-13,27574,6.85621], Tmin=(546.268,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (231.239,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 58.8 kcal/mol   or 246.1 kJ/mol
""",
)

entry(
    index = 83,
    label = "[H]",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.5266e-15,6.3226e-18,-7.59355e-21,2.67359e-24,25472.6,-0.461279], Tmin=(10,'K'), Tmax=(1363.47,'K')),
            NASAPolynomial(coeffs=[2.5,-1.01797e-13,8.3758e-17,-2.93808e-20,3.72101e-24,25472.6,-0.461279], Tmin=(1363.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (211.791,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 52.1 kcal/mol   or 218.0 kJ/mol
""",
)

entry(
    index = 84,
    label = "OONNOO",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {1,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  N u0 p1 c0 {1,S} {6,S} {7,S}
6  N u0 p1 c0 {2,S} {5,S} {8,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83357,0.0109122,0.00014652,-3.591e-07,2.56054e-10,11327.6,10.7962], Tmin=(10,'K'), Tmax=(487.736,'K')),
            NASAPolynomial(coeffs=[4.93079,0.0339777,-2.30267e-05,7.43376e-09,-9.09933e-13,10839.2,2.38092], Tmin=(487.736,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (94.1471,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 27.1 kcal/mol   or 113.6 kJ/mol
""",
)

entry(
    index = 85,
    label = "[O-]O[N+]=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u1 p0 c+1 {1,S} {4,D}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89601,0.00877898,4.4239e-05,-1.91204e-07,2.07791e-10,18578.7,8.65317], Tmin=(10,'K'), Tmax=(347.85,'K')),
            NASAPolynomial(coeffs=[4.8956,0.00891531,-6.50357e-06,2.16879e-09,-2.7009e-13,18438.8,3.8748], Tmin=(347.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (154.484,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 40.2 kcal/mol   or 168.3 kJ/mol
""",
)

entry(
    index = 86,
    label = "[O-][NH+]=N",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 N u0 p1 c0 {1,D} {5,S}
3 O u0 p3 c-1 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08196,-0.00570837,4.68514e-05,-6.00346e-08,2.50598e-11,17900.5,6.39957], Tmin=(10,'K'), Tmax=(737.981,'K')),
            NASAPolynomial(coeffs=[1.50136,0.0149615,-8.74436e-06,2.45887e-09,-2.6723e-13,18099.4,16.8325], Tmin=(737.981,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (148.849,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 38.1 kcal/mol   or 159.4 kJ/mol
""",
)

entry(
    index = 87,
    label = "[O-]C=[NH+]OCO",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  N u0 p0 c+1 {3,D} {4,S} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p3 c-1 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72925,0.0336026,-1.37372e-05,-1.27973e-09,1.58644e-12,-45479.6,10.5695], Tmin=(10,'K'), Tmax=(1252.05,'K')),
            NASAPolynomial(coeffs=[9.64271,0.0229947,-1.09533e-05,2.52248e-09,-2.27946e-13,-47609.7,-21.8818], Tmin=(1252.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-378.136,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -85.4 kcal/mol   or -357.5 kJ/mol
""",
)

entry(
    index = 88,
    label = "[O-][N+]=NO",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {5,S}
3 N u1 p0 c+1 {1,D} {4,S}
4 O u0 p3 c-1 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95162,0.00292611,5.02643e-05,-1.05932e-07,6.59934e-11,20072,8.62841], Tmin=(10,'K'), Tmax=(545.392,'K')),
            NASAPolynomial(coeffs=[3.87014,0.0141437,-9.79598e-06,3.18663e-09,-3.90979e-13,19923,7.52406], Tmin=(545.392,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (166.871,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 43.0 kcal/mol   or 180.0 kJ/mol
""",
)

entry(
    index = 89,
    label = "[O]C=N",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 N u0 p1 c0 {1,D} {5,S}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06996,-0.00519279,4.63082e-05,-6.40859e-08,2.89699e-11,8594.4,7.1695], Tmin=(10,'K'), Tmax=(682.656,'K')),
            NASAPolynomial(coeffs=[2.00455,0.013179,-7.83623e-06,2.24387e-09,-2.48093e-13,8730.31,15.2754], Tmin=(682.656,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (71.4668,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (99.7737,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 19.6 kcal/mol   or 82.1 kJ/mol
""",
)

entry(
    index = 90,
    label = "NNCO",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  N u0 p1 c0 {3,S} {4,S} {7,S}
3  N u0 p1 c0 {2,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95416,0.00294987,0.000106064,-2.11561e-07,1.3554e-10,-12325.7,8.63447], Tmin=(10,'K'), Tmax=(465.965,'K')),
            NASAPolynomial(coeffs=[1.19477,0.0345008,-2.08155e-05,6.18425e-09,-7.16035e-13,-12153.9,18.9237], Tmin=(465.965,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-102.492,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -20.7 kcal/mol   or -86.8 kJ/mol
""",
)

entry(
    index = 91,
    label = "O[N]N=O",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97049,0.0016534,4.39638e-05,-7.78401e-08,4.17366e-11,22380.2,8.41049], Tmin=(10,'K'), Tmax=(598.178,'K')),
            NASAPolynomial(coeffs=[2.66223,0.0172554,-1.23463e-05,4.07138e-09,-5.02339e-13,22414.1,13.0249], Tmin=(598.178,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (186.066,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 47.5 kcal/mol   or 198.6 kJ/mol
""",
)

entry(
    index = 92,
    label = "[N-]([N+](=O)OO)N=O",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {6,D}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p2 c-1 {1,S} {5,S}
4 O u0 p2 c0 {2,S} {8,S}
5 N u0 p1 c0 {3,S} {7,D}
6 O u0 p2 c0 {1,D}
7 O u0 p2 c0 {5,D}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53715,0.0418336,-4.77924e-05,2.85686e-08,-6.97349e-12,35318.6,11.382], Tmin=(10,'K'), Tmax=(949.232,'K')),
            NASAPolynomial(coeffs=[8.86336,0.0193892,-1.23251e-05,3.659e-09,-4.13012e-13,34307.5,-14.0363], Tmin=(949.232,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (293.608,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 75.2 kcal/mol   or 314.8 kJ/mol
""",
)

entry(
    index = 93,
    label = "[O-]N=[N+](OO)N",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {5,S}
4 N u0 p1 c0 {1,D} {8,S}
5 O u0 p2 c0 {3,S} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 O u0 p3 c-1 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80097,0.0147562,0.000131944,-3.90034e-07,3.26683e-10,24334.3,10.3657], Tmin=(10,'K'), Tmax=(421.625,'K')),
            NASAPolynomial(coeffs=[5.11781,0.0299328,-2.04885e-05,6.63838e-09,-8.13246e-13,23977.4,2.23345], Tmin=(421.625,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (202.323,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 53.0 kcal/mol   or 221.8 kJ/mol
""",
)

entry(
    index = 94,
    label = "[O]ON=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 O u1 p2 c0 {1,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41333,0.0616203,-0.000306071,6.46731e-07,-4.86662e-10,9264.44,10.1621], Tmin=(10,'K'), Tmax=(410.146,'K')),
            NASAPolynomial(coeffs=[6.69254,0.00405996,-2.00922e-06,4.37419e-10,-3.35389e-14,9210.6,-0.112836], Tmin=(410.146,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.0136,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 22.6 kcal/mol   or 94.5 kJ/mol
""",
)

entry(
    index = 95,
    label = "[O-][N+]#N",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,T}
2 O u0 p3 c-1 {1,S}
3 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53434,-0.0037595,4.56062e-05,-8.99371e-08,5.79954e-11,10368.7,5.99938], Tmin=(10,'K'), Tmax=(492.863,'K')),
            NASAPolynomial(coeffs=[2.8825,0.00717344,-4.84083e-06,1.52873e-09,-1.82583e-13,10364.4,7.98769], Tmin=(492.863,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (86.2068,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 22.9 kcal/mol   or 95.7 kJ/mol
""",
)

entry(
    index = 96,
    label = "CC",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07078,-0.00315596,5.16192e-05,-5.81772e-08,2.08008e-11,-11322.8,3.39647], Tmin=(10,'K'), Tmax=(859.436,'K')),
            NASAPolynomial(coeffs=[-0.446024,0.0260358,-1.35885e-05,3.46495e-09,-3.4757e-13,-10848.1,22.748], Tmin=(859.436,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-94.1152,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -19.7 kcal/mol   or -82.3 kJ/mol
""",
)

entry(
    index = 97,
    label = "OON=O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94908,0.00303887,5.08655e-05,-1.06225e-07,6.51682e-11,-559.605,7.94457], Tmin=(10,'K'), Tmax=(557.719,'K')),
            NASAPolynomial(coeffs=[3.98628,0.0142144,-9.96585e-06,3.2751e-09,-4.0545e-13,-741.711,6.19143], Tmin=(557.719,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-4.67232,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 2.0 kcal/mol   or 8.5 kJ/mol
""",
)

entry(
    index = 98,
    label = "OON(N(OO)N)N",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {4,S} {5,S}
2  N u0 p1 c0 {1,S} {3,S} {6,S}
3  N u0 p1 c0 {2,S} {9,S} {10,S}
4  N u0 p1 c0 {1,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {5,S} {13,S}
8  O u0 p2 c0 {6,S} {14,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66436,0.0244678,0.000228613,-6.67925e-07,5.52492e-10,33095.5,12.6224], Tmin=(10,'K'), Tmax=(428.564,'K')),
            NASAPolynomial(coeffs=[6.27148,0.0498126,-3.39727e-05,1.10292e-08,-1.35501e-12,32415.8,-3.06895], Tmin=(428.564,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (275.158,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 72.0 kcal/mol   or 301.3 kJ/mol
""",
)

entry(
    index = 99,
    label = "C=O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03299,-0.00204616,9.99546e-06,2.25257e-09,-8.39925e-12,-13736.3,3.46069], Tmin=(10,'K'), Tmax=(580.545,'K')),
            NASAPolynomial(coeffs=[1.43185,0.00976991,-4.75815e-06,1.07796e-09,-9.17712e-14,-13331.4,15.4814], Tmin=(580.545,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-114.2,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -24.9 kcal/mol   or -104.2 kJ/mol
""",
)

entry(
    index = 100,
    label = "[O-]N=[N+]=O",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p0 c+1 {1,D} {4,D}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15104,0.0236233,-4.15088e-05,3.57706e-08,-1.16424e-11,31986.8,7.00111], Tmin=(10,'K'), Tmax=(904.659,'K')),
            NASAPolynomial(coeffs=[5.60329,0.00697249,-4.27029e-06,1.23184e-09,-1.36508e-13,31780.7,-3.2703], Tmin=(904.659,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (265.884,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (87.302,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 66.9 kcal/mol   or 280.0 kJ/mol
""",
)

entry(
    index = 101,
    label = "ON=O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05951,-0.00506897,5.05339e-05,-8.28503e-08,4.41166e-11,-8861.26,6.45445], Tmin=(10,'K'), Tmax=(599.005,'K')),
            NASAPolynomial(coeffs=[2.95925,0.00997239,-6.39914e-06,1.95728e-09,-2.28261e-13,-8867.48,10.0465], Tmin=(599.005,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.6773,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -15.0 kcal/mol   or -63.0 kJ/mol
""",
)

entry(
    index = 102,
    label = "[N-]=[N+]=O",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 N u0 p2 c-1 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53434,-0.00375945,4.56049e-05,-8.99333e-08,5.7992e-11,10368.7,5.99938], Tmin=(10,'K'), Tmax=(492.87,'K')),
            NASAPolynomial(coeffs=[2.88248,0.00717346,-4.84083e-06,1.52873e-09,-1.82583e-13,10364.4,7.98777], Tmin=(492.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (86.2068,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 22.9 kcal/mol   or 95.7 kJ/mol
""",
)

entry(
    index = 103,
    label = "NOO",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96025,0.0024572,5.40783e-05,-1.10732e-07,6.9734e-11,625.236,6.92839], Tmin=(10,'K'), Tmax=(518.161,'K')),
            NASAPolynomial(coeffs=[3.29989,0.0160309,-9.75229e-06,2.96183e-09,-3.51596e-13,579.885,8.58212], Tmin=(518.161,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (5.18576,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 4.4 kcal/mol   or 18.3 kJ/mol
""",
)

entry(
    index = 104,
    label = "N#N",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50355,-0.000172626,9.38847e-08,1.40082e-09,-9.44579e-13,438.008,3.08124], Tmin=(10,'K'), Tmax=(808.677,'K')),
            NASAPolynomial(coeffs=[3.07646,0.000896232,4.71663e-08,-1.56598e-10,3.02667e-14,541.209,5.262], Tmin=(808.677,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (3.64306,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 2.9 kcal/mol   or 12.3 kJ/mol
""",
)

entry(
    index = 105,
    label = "O=NC=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 N u0 p1 c0 {1,S} {5,D}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91273,0.0104154,1.63563e-07,-6.34007e-09,2.75437e-12,920.671,7.94751], Tmin=(10,'K'), Tmax=(1024.15,'K')),
            NASAPolynomial(coeffs=[5.13526,0.00994916,-5.4642e-06,1.43119e-09,-1.45396e-13,444.3,0.917162], Tmin=(1024.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (7.66125,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 5.0 kcal/mol   or 21.1 kJ/mol
""",
)

entry(
    index = 106,
    label = "[O-][N+](=O)[N]O",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,S} {5,D}
2 N u1 p1 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u0 p3 c-1 {1,S}
5 O u0 p2 c0 {1,D}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94444,0.00321931,6.53214e-05,-1.26559e-07,7.30356e-11,11823.6,9.71327], Tmin=(10,'K'), Tmax=(577.589,'K')),
            NASAPolynomial(coeffs=[3.18628,0.0213487,-1.52072e-05,4.9939e-09,-6.14215e-13,11696.4,11.0951], Tmin=(577.589,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (98.2836,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 26.8 kcal/mol   or 112.3 kJ/mol
""",
)

entry(
    index = 107,
    label = "OCONC=O",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  N u0 p1 c0 {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {9,D} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72887,0.0246652,2.54821e-05,-5.86514e-08,2.92381e-11,-47605,10.463], Tmin=(10,'K'), Tmax=(718.245,'K')),
            NASAPolynomial(coeffs=[3.60359,0.036273,-2.15449e-05,6.14719e-09,-6.77658e-13,-47868.5,9.06686], Tmin=(718.245,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-395.837,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -90.0 kcal/mol   or -376.4 kJ/mol
""",
)

entry(
    index = 108,
    label = "[N-]([N+]=O)O",
    molecule = 
"""
multiplicity 2
1 N u0 p2 c-1 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u1 p0 c+1 {1,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9379,0.00417961,5.61418e-05,-1.41011e-07,1.03709e-10,20047.7,8.33126], Tmin=(10,'K'), Tmax=(468.964,'K')),
            NASAPolynomial(coeffs=[4.1968,0.0132558,-8.98243e-06,2.87746e-09,-3.493e-13,19899.3,5.95524], Tmin=(468.964,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (166.676,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 43.1 kcal/mol   or 180.2 kJ/mol
""",
)

entry(
    index = 109,
    label = "O=NON=O",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,D}
3 O u0 p2 c0 {5,D}
4 N u0 p1 c0 {1,S} {2,D}
5 N u0 p1 c0 {1,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84618,0.0124915,6.91031e-05,-2.76827e-07,2.82942e-10,12378.6,8.24255], Tmin=(10,'K'), Tmax=(368.494,'K')),
            NASAPolynomial(coeffs=[5.50619,0.0131548,-9.64703e-06,3.23153e-09,-4.03824e-13,12129.4,0.170098], Tmin=(368.494,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (102.936,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 28.4 kcal/mol   or 118.7 kJ/mol
""",
)

entry(
    index = 110,
    label = "[O-]C=[N+]=O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 N u0 p0 c+1 {1,D} {5,D}
3 O u0 p3 c-1 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93268,0.0112819,-2.93411e-06,-2.6948e-09,1.34978e-12,2424.72,8.09125], Tmin=(10,'K'), Tmax=(1161.29,'K')),
            NASAPolynomial(coeffs=[6.04397,0.00808552,-4.07017e-06,9.79667e-10,-9.18819e-14,1659.52,-3.59352], Tmin=(1161.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.1733,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 8.1 kcal/mol   or 33.8 kJ/mol
""",
)

entry(
    index = 111,
    label = "OCN=O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {7,S}
3 N u0 p1 c0 {1,S} {6,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {3,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96696,0.00226759,7.76463e-05,-1.69309e-07,1.19047e-10,-12669,8.32192], Tmin=(10,'K'), Tmax=(420.601,'K')),
            NASAPolynomial(coeffs=[2.26468,0.0233055,-1.46746e-05,4.43279e-09,-5.14305e-13,-12568.7,14.5503], Tmin=(420.601,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-105.337,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -21.8 kcal/mol   or -91.3 kJ/mol
""",
)

entry(
    index = 112,
    label = "[O-][N+](=O)O",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08303,-0.0078461,9.24864e-05,-1.67295e-07,9.71345e-11,-16340.7,8.17314], Tmin=(10,'K'), Tmax=(560.769,'K')),
            NASAPolynomial(coeffs=[2.92394,0.0155547,-1.05874e-05,3.36743e-09,-4.0359e-13,-16448.7,10.9731], Tmin=(560.769,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-135.873,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -29.7 kcal/mol   or -124.2 kJ/mol
""",
)

entry(
    index = 113,
    label = "[NH]NN[NH]",
    molecule = 
"""
multiplicity 3
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {4,S} {6,S}
3 N u1 p1 c0 {1,S} {7,S}
4 N u1 p1 c0 {2,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93496,0.00395449,8.48344e-05,-1.71239e-07,1.05417e-10,66070.7,9.41262], Tmin=(10,'K'), Tmax=(533.067,'K')),
            NASAPolynomial(coeffs=[2.91085,0.0257785,-1.6363e-05,5.07915e-09,-6.0886e-13,65979,11.8248], Tmin=(533.067,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (549.32,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 134.9 kcal/mol   or 564.4 kJ/mol
""",
)

entry(
    index = 114,
    label = "[CH3]",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98027,0.00122414,9.56928e-06,-1.56615e-08,8.95649e-12,16655.8,0.225796], Tmin=(10,'K'), Tmax=(430.751,'K')),
            NASAPolynomial(coeffs=[3.67458,0.00406291,-3.1624e-07,-3.61596e-10,7.6607e-14,16682.2,1.44313], Tmin=(430.751,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (138.475,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 35.7 kcal/mol   or 149.3 kJ/mol
""",
)

entry(
    index = 115,
    label = "NON=O",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u0 p1 c0 {1,S} {2,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9463,0.0035344,6.53896e-05,-1.49608e-07,1.04135e-10,10661.3,8.15205], Tmin=(10,'K'), Tmax=(474.795,'K')),
            NASAPolynomial(coeffs=[3.50058,0.0175406,-1.12454e-05,3.46998e-09,-4.11035e-13,10588,8.75363], Tmin=(474.795,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (88.6322,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 24.5 kcal/mol   or 102.5 kJ/mol
""",
)

entry(
    index = 116,
    label = "CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97358,0.00123468,8.13208e-05,-1.18198e-07,5.55531e-11,-14222.8,6.77555], Tmin=(10,'K'), Tmax=(550.819,'K')),
            NASAPolynomial(coeffs=[-1.19047,0.0387362,-2.08059e-05,5.41031e-09,-5.49765e-13,-13653.9,28.6094], Tmin=(550.819,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-118.273,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -24.8 kcal/mol   or -103.7 kJ/mol
""",
)

entry(
    index = 117,
    label = "OO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99357,0.00040098,2.03922e-05,-3.66698e-08,2.17532e-11,-16344.3,3.82053], Tmin=(10,'K'), Tmax=(433.241,'K')),
            NASAPolynomial(coeffs=[3.2254,0.00750101,-4.21687e-06,1.23962e-09,-1.46058e-13,-16277.8,6.88311], Tmin=(433.241,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-135.896,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) -29.8 kcal/mol   or -124.9 kJ/mol
""",
)

entry(
    index = 118,
    label = "NOON",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {5,S} {6,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92731,0.00457602,8.88994e-05,-1.91139e-07,1.24891e-10,17682,8.41699], Tmin=(10,'K'), Tmax=(507.642,'K')),
            NASAPolynomial(coeffs=[3.29735,0.0247108,-1.54239e-05,4.73547e-09,-5.6387e-13,17550.5,9.10367], Tmin=(507.642,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (146.996,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 38.8 kcal/mol   or 162.3 kJ/mol
""",
)

entry(
    index = 119,
    label = "C[CH2]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96774,0.00647681,1.59172e-05,-1.8669e-08,5.90438e-12,12937.2,5.7762], Tmin=(10,'K'), Tmax=(1080.43,'K')),
            NASAPolynomial(coeffs=[2.84829,0.0172588,-8.26693e-06,1.93955e-09,-1.79897e-13,12791.6,9.47061], Tmin=(1080.43,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (107.58,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 28.8 kcal/mol   or 120.7 kJ/mol
""",
)

entry(
    index = 120,
    label = "O1O[N]1",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u1 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0414,-0.00343588,3.38878e-05,-5.51023e-08,2.84378e-11,42757.4,6.23268], Tmin=(10,'K'), Tmax=(637.821,'K')),
            NASAPolynomial(coeffs=[3.56833,0.00621438,-4.52516e-06,1.47659e-09,-1.78267e-13,42681.8,7.2365], Tmin=(637.821,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (355.505,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 87.5 kcal/mol   or 365.9 kJ/mol
""",
)

entry(
    index = 121,
    label = "OO[N+](=[N-])[O]",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,S} {5,D}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u1 p2 c0 {1,S}
5 N u0 p2 c-1 {1,D}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88825,0.00755827,8.34898e-05,-2.20541e-07,1.65427e-10,38767,10.0701], Tmin=(10,'K'), Tmax=(471.919,'K')),
            NASAPolynomial(coeffs=[4.94586,0.0182782,-1.31504e-05,4.36655e-09,-5.41532e-13,38448,3.43956], Tmin=(471.919,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (322.308,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 80.8 kcal/mol   or 337.9 kJ/mol
""",
)

entry(
    index = 122,
    label = "NN=O",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93906,0.00711699,4.73821e-06,-8.99224e-09,3.37205e-12,9242.98,6.56467], Tmin=(10,'K'), Tmax=(992.509,'K')),
            NASAPolynomial(coeffs=[4.02629,0.0102834,-5.36401e-06,1.36467e-09,-1.36279e-13,9052.39,5.2716], Tmin=(992.509,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (76.8548,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 21.4 kcal/mol   or 89.5 kJ/mol
""",
)

entry(
    index = 123,
    label = "[O-]N=[NH+]OO",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {5,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,D} {6,S}
4 O u0 p2 c0 {2,S} {7,S}
5 H u0 p0 c0 {1,S}
6 O u0 p3 c-1 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89626,0.00661988,9.21391e-05,-2.17361e-07,1.48966e-10,14167.7,9.27461], Tmin=(10,'K'), Tmax=(507.588,'K')),
            NASAPolynomial(coeffs=[4.61246,0.0219476,-1.51312e-05,4.92602e-09,-6.05988e-13,13824.9,3.64373], Tmin=(507.588,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (117.769,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 31.9 kcal/mol   or 133.7 kJ/mol
""",
)

entry(
    index = 124,
    label = "[NH]OO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u1 p1 c0 {1,S} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96021,0.00273934,4.84563e-05,-1.17663e-07,8.74214e-11,17998.5,7.54055], Tmin=(10,'K'), Tmax=(443.89,'K')),
            NASAPolynomial(coeffs=[3.67876,0.0123117,-7.66787e-06,2.3379e-09,-2.75477e-13,17954.2,7.88894], Tmin=(443.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (149.644,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """m06-2x/cc-pVTZ""",
    longDesc = 
"""
AutoTST calculated thermo using Gaussian 16,
m06-2x/cc-pVTZ, Arkane, with atomization energies but
no Bond Corrections, frequency scaled by 0.955.
Gives Hf(298) 38.8 kcal/mol   or 162.4 kJ/mol
""",
)

