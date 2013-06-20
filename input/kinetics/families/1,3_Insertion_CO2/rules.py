#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/rules"
shortDesc = u""
longDesc = u"""
572 - 575 Some of the tortional motions in the alkyl part of the 
transition states are treated as free rotations as they are relatively loose TSs. 

The dictionary defines CO2 in two ways, allowing the R-R' to insert either way
around. However, there are only rates for one of these ways. The other is
presumably matching the top level node.
"""
recommended = True

entry(
    index = 571,
    label = "CO2;RR'",
    group1 = "OR{CO2_Od, CO2_Cdd}",
    group2 = "OR{R_H, R_R'}",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 2,
        alpha = 0,
        E0 = (75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 572,
    label = "CO2_Cdd;H2",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Od  0 {1,D}
3    Od  0 {1,D}
""",
    group2 = 
"""
1 *3 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1510000000.0, 'cm^3/(mol*s)'),
        n = 1.23,
        alpha = 0,
        E0 = (73.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 573,
    label = "CO2_Cdd;C_methane",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Od  0 {1,D}
3    Od  0 {1,D}
""",
    group2 = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4530, 'cm^3/(mol*s)'),
        n = 2.83,
        alpha = 0,
        E0 = (79.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 574,
    label = "CO2_Cdd;C_pri/NonDeC",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Od  0 {1,D}
3    Od  0 {1,D}
""",
    group2 = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.56,
        alpha = 0,
        E0 = (76.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 575,
    label = "CO2_Cdd;C/H2/NonDeC",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Od  0 {1,D}
3    Od  0 {1,D}
""",
    group2 = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (106000, 'cm^3/(mol*s)'),
        n = 2.13,
        alpha = 0,
        E0 = (77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 576,
    label = "CO2_Cdd;CH3Os_CH3",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Od  0 {1,D}
3    Od  0 {1,D}
""",
    group2 = 
"""
1 *3 Os 0 {2,S} {3,S} 
2 *4 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs  0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    H  0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
""",
    kinetics = ArrheniusEP(
        A=(4375.48,'m^3/(mol*s)'),
        n=1.93476,
        alpha = 0,
        E0=(334.093,'kJ/mol'),
        Tmin=(303.03,'K'),
        Tmax=(2000,'K'),
        comment="""Reverse rate coefficient fitted to 29 data points; dA = *|/ 1.16576, dn = +|- 0.0203053, dEa = +|- 0.106152 kJ/mol"""
    ),
    reference = None,
    referenceType = "",
    rank = 2, # MEANING UNKNOWN!
    shortDesc = u"""Reverse rate coefficients from RMG""",
    longDesc = 
u"""
The forward (recombination) rate coefficent here was calcualted from the reverse (decomposition)
by RMG using thermochemistry from
  Dimethylcarbonate: Group additivity
  CO2: DFT_QCI_thermo
  Methoxymethane: DFT_QCI_thermo

The reverse (decomposition) rate coefficient was:
Arrhenius(A=(6.79e+19,'s^-1'), n=-0.766, Ea=(79.04,'kcal/mol'), T0=(1,'K'))

This is the high pressure limit rate taken from table S1 in the supplementary material of:
[1] Peukert, S. L.; Sivaramakrishnan, R.; Michael, J. V. "High Temperature Shock Tube and Theoretical
 Studies on the Thermal Decomposition of Dimethyl Carbonate and Its Bimolecular Reactions with H and
 D-Atoms." J. Phys. Chem. A 2013, 117, 3718–3728 [doi:10.1021/jp312643k].
 
(NB. the valid temperature range of this reverse rate is probably 1000-2000.
RMG may have extrapolated to 300 before fitting the forward rate)
""",
    history = [
        ("Thu Jun 19 14:05:30 2012","Fariba Seyedzadeh <seyedzadehkhanshan.fn@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> created this entry based on Peukert 2013 paper."""),
    ],
)


