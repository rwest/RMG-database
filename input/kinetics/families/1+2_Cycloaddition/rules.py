#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 576,
    label = "elec_def;multiplebond",
    group1 = "OR{carbene, me_carbene, dime_carbene, ph_carbene, o_atom}",
    group2 = 
"""
1 *1 {Cd,CO} 0 {2,D}
2 *2 {Cd,O}  0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 584,
    label = "o_atom;mb_db_twocdisub_Nd",
    group1 = 
"""
1 *3 O {2S,2T}
""",
    group2 = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.54e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (298,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Cvetanovic [197]""",
    longDesc = 
u"""
[197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (Z)-2-C4H8 --> cis-2,3-dimethyloxirane/O + C2H4 = Oxirane --> 2.2E+01) 

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 585,
    label = "o_atom;mb_db_tetrasub_Nd",
    group1 = 
"""
1 *3 O {2S,2T}
""",
    group2 = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (3.18e+13,"cm^3/(mol*s)","*|/",1.2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (298,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Cvetanovic [197]""",
    longDesc = 
u"""
[197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (CH3)2C=C(CH3)2 --> tetramethyl-oxirane/O + iso-C4H8 --> 2,2-Dimethyloxirane = 4.18)  

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

