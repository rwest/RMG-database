#!/usr/bin/env python
# encoding: utf-8

name = "CombFlame2017/45-Olm"
shortDesc = "/Users/rwest/Code/RMG-importer/RMG-models/CombFlame2017/45-Olm/olm_mech.txt"
longDesc = """
Carsten Olm, Tam?s Varga, ?va Valk?, Henry J. Curran, Tam?s Tur?nyi,
Uncertainty quantification of a newly optimized methanol and formaldehyde combustion mechanism,
Combustion and Flame,
Volume 186,
2017,
Pages 45-64,
ISSN 0010-2180,
https://doi.org/10.1016/j.combustflame.2017.07.029.
(http://www.sciencedirect.com/science/article/pii/S0010218017302742)
Abstract: A detailed reaction mechanism for methanol combustion that is capable of describing ignition, flame propagation and species concentration profiles with high accuracy has been developed. Starting from a modified version of the methanol combustion mechanism of Li et al. (2007) and adopting the H2/CO base chemistry from the joint optimized hydrogen and syngas combustion mechanism of Varga et al. (2016), an optimization of 57 Arrhenius parameters of 17 important elementary reactions was performed, using several thousand indirect measurement data points, as well as direct and theoretical determinations of reaction rate coefficients as optimization targets. The final optimized mechanism was compared to 18 reaction mechanisms published in recent years, with respect to their accuracy in reproducing the available indirect experimental data for methanol and formaldehyde combustion. The utilized indirect measurement data, in total 24,900 data points in 265 datasets, include measurements of ignition delay times, laminar burning velocities and species profiles captured using a variety of experimental techniques. In addition to new best fit values for all rate parameters, the covariance matrix of the optimized parameters, which provides a quantitative description of the temperature-dependent ranges of uncertainty for the optimized rate coefficients, was calculated. These posterior uncertainty limits are much narrower than the prior limits in the temperature range for which experimental data are available. The uncertainty of the self-reaction of H?2 radicals and important H-atom abstraction reactions from the methanol molecule are discussed in detail.
Keywords: Methanol combustion; Formaldehyde combustion; Chemical kinetic mechanisms; Mechanism optimization; Parameter uncertainty

Note: the following reaction was commented out
OHEX<=>OH+HV                        1.4500E+06    0.0000       0.000
"""
entry(
    index = 0,
    label = "OHEX",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63727,0.000185091,-1.67616e-06,2.3872e-09,-8.43144e-13,50021.3,1.35886], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.88273,0.00101397,-2.27688e-07,2.17468e-11,-5.12631e-16,50265,5.59571], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (416.033,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[OH]
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 1,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99198,-0.00240107,4.61664e-06,-3.87916e-09,1.3632e-12,3368.9,-0.103998], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.83853,0.00110741,-2.94e-07,4.20699e-11,-2.4229e-15,3697.81,5.84495], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (28.5525,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism.
Duplicate of species OHEX (i.e. same molecular structure according to RMG)
[OH]
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 2,
    label = "CH3OH",
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
            NASAPolynomial(coeffs=[5.65851,-0.0162983,6.91938e-05,-7.58373e-08,2.80428e-11,-25612,-0.897331], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.52727,0.0103179,-3.62893e-06,5.77448e-10,-3.42183e-14,-26002.9,5.16759], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-211.797,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """Methanol""",
    longDesc = 
"""
Methanol
taken from Burcat thermo database. Last update: 03/13/2015.
CO
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 3,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78246,-0.00299673,9.8473e-06,-9.6813e-09,3.24373e-12,-1063.94,3.65768], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.66096,0.000656366,-1.4115e-07,2.05798e-11,-1.29913e-15,-1215.98,3.41536], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-8.64442,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism.
[O][O]
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 4,
    label = "CO",
    molecule = 
"""
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57953,-0.000610354,1.01681e-06,9.07006e-10,-9.04424e-13,-14344.1,3.50841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.04849,0.00135173,-4.85794e-07,7.88536e-11,-4.69807e-15,-14266.1,6.0171], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-119.173,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism.
[C-]#[O+]
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 5,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35681,0.00898413,-7.12206e-06,2.4573e-09,-1.42885e-13,-48372,9.9009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.63651,0.00274146,-9.95898e-07,1.60387e-10,-9.16199e-15,-49024.9,-1.9349], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-403.138,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (62.3585,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism.
O=C=O
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 6,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19864,-0.0020364,6.52034e-06,-5.48793e-09,1.77197e-12,-30293.7,-0.849009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67704,0.00297318,-7.73769e-07,9.44335e-11,-4.269e-15,-29885.9,6.88255], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-251.768,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism.
O
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 7,
    label = "CH4",
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
            NASAPolynomial(coeffs=[5.14911,-0.0136622,4.91454e-05,-4.84247e-08,1.66603e-11,-10246.6,-4.63849], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.65326,0.0100263,-3.31661e-06,5.36483e-10,-3.14697e-14,-10009.6,9.90506], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-84.8428,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """Methane Anharmonic""",
    longDesc = 
"""
Methane Anharmonic
taken from Burcat thermo database. Last update: 03/13/2015.
C
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 8,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34433,0.00798052,-1.94782e-05,2.01572e-08,-7.37612e-12,-917.935,0.68301], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.93287,0.000826608,-1.46402e-07,1.541e-11,-6.88805e-16,-813.066,-1.02433], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-8.64239,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism.
[H][H]
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 9,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38875,0.00656923,-1.48501e-07,-4.62581e-09,2.47151e-12,-17663.2,6.78536], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57317,0.00433614,-1.47469e-06,2.3489e-10,-1.43165e-14,-18007,0.501137], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-147.353,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (78.9875,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OO
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 10,
    label = "CH3",
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
            NASAPolynomial(coeffs=[3.65718,0.0021266,5.45839e-06,-6.6181e-09,2.46571e-12,16422.7,1.67354], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.97812,0.00579785,-1.97558e-06,3.07298e-10,-1.79174e-14,16509.5,4.72248], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (136.188,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """Methyl Radical""",
    longDesc = 
"""
Methyl Radical
taken from Burcat thermo database. Last update: 03/13/2015.
[CH3]
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 11,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (211.8,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism.
[H]
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 12,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,264.018,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.17229,0.00188118,-3.46277e-07,1.94658e-11,1.76257e-16,31.0207,2.95768], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
        E0 = (2.49013,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """taken from Burcat thermo database. Last update: 03/13/2015""",
    longDesc = 
"""
taken from Burcat thermo database. Last update: 03/13/2015.
[O]O
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 13,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16827,-0.00327932,6.64306e-06,-6.12807e-09,2.11266e-12,29122.3,2.05193], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54364,-2.73162e-05,-4.1903e-09,4.95482e-12,-4.79554e-16,29226,4.92229], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (242.976,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """taken from Burcat thermo database. Last update: 03/13/2015""",
    longDesc = 
"""
taken from Burcat thermo database. Last update: 03/13/2015.
[O]
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 14,
    label = "C2H6",
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
            NASAPolynomial(coeffs=[0.532635,0.0211904,-7.09804e-06,-4.386e-10,5.13743e-13,-11112.8,18.5651], Tmin=(298,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[5.84723,0.012908,-4.36843e-06,6.73225e-10,-3.88531e-14,-13406.6,-11.5009], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-95.64,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """Ethane""",
    longDesc = 
"""
Ethane
taken from S.M. Burke, J.M. Simmie, H. Curran, J. Phys. Chem. Ref. Data, 44, 013101 (2015)
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 15,
    label = "AR",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-6.19738,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism.
[Ar]
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 16,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53101,-0.000123661,-5.02999e-07,2.43531e-09,-1.40881e-12,-1046.98,2.96747], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.95258,0.0013969,-4.92632e-07,7.8601e-11,-4.60755e-15,-923.949,5.87189], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-8.64286,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism.
N#N
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 17,
    label = "HE",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-6.19738,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism.
[He]
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 18,
    label = "CH2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.79372,-0.00990833,3.7322e-05,-3.79285e-08,1.31773e-11,-14379.2,0.602798], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16953,0.00619321,-2.25056e-06,3.65976e-10,-2.20149e-14,-14548.7,6.04208], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-119.054,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """Formaldehyde""",
    longDesc = 
"""
Formaldehyde
taken from Burcat thermo database. Last update: 03/13/2015.
C=O
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 19,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.23755,-0.00332075,1.4003e-05,-1.3424e-08,4.37416e-12,3872.41,3.30835], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.92002,0.00252279,-6.71004e-07,1.05616e-10,-7.43798e-15,3653.43,3.58077], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (32.4783,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """as in optimized syngas mechanism""",
    longDesc = 
"""
as in optimized syngas mechanism.
[CH]=O
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 20,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47834,-0.0013507,2.78485e-05,-3.64869e-08,1.47907e-11,-3500.73,3.30913], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.09314,0.00594761,-2.06497e-06,3.23008e-10,-1.88126e-14,-4034.1,-1.84691], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-28.7184,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (103.931,'J/mol/K'),
    ),
    shortDesc = """HydroxymethyleneR""",
    longDesc = 
"""
HydroxymethyleneR
taken from Burcat thermo database. Last update: 03/13/2015.
[CH2]O
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

entry(
    index = 21,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71181,-0.00280463,3.76551e-05,-4.73072e-08,1.86588e-11,1295.7,6.57241], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.75779,0.00744142,-2.69705e-06,4.38091e-10,-2.63537e-14,378.112,-1.9668], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (10.4739,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """Methoxy Radical""",
    longDesc = 
"""
Methoxy Radical
taken from Burcat thermo database. Last update: 03/13/2015.
C[O]
_imported from CombFlame2017/45-Olm/olm_mech.txt.
""",
)

