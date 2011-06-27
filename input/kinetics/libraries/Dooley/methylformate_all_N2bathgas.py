#!/usr/bin/env python
# encoding: utf-8

name = "Dooley/methylformate_all_N2bathgas"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
O
1     O     2T
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.547e+15,"cm^3/(mol*s)"),
        n = -0.406,
        Ea = (16599,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50800,"cm^3/(mol*s)"),
        n = 2.67,
        Ea = (6290,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+08,"cm^3/(mol*s)"),
        n = 1.51,
        Ea = (3430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
H2O
1     O     0
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.97e+06,"cm^3/(mol*s)"),
        n = 2.02,
        Ea = (13400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (823,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.079e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (295,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.25e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-497,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (4.2e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11982,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1629.3,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7950,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.55e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (3970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (5.8e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9557,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    reactant1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
O
1     O     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.53e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (47700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    reactant1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (23000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    reactant1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (222900,"cm^3/(mol*s)"),
        n = 1.89,
        Ea = (-1158.7,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.58e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (410,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.02e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.02e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
O2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     1 {2,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11660,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    reactant1 = 
"""
HO2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     0 {2,S}
""",
    product1 = 
"""
OCHO
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+14,"s^-1"),
        n = 0,
        Ea = (40150,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.74e+07,"cm^3/(mol*s)"),
        n = 1.9,
        Ea = (2748.6,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09,"cm^3/(mol*s)"),
        n = 1.18,
        Ea = (-447,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.23e+06,"cm^3/(mol*s)"),
        n = 3,
        Ea = (52000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (41100,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (10210,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.636e-06,"cm^3/(mol*s)"),
        n = 5.42,
        Ea = (998,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
OCH2O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     1 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    reactant1 = 
"""
OCH2O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     1 {1,S}
4     O     0 {2,S}
""",
    product1 = 
"""
HOCH2O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"s^-1"),
        n = 0,
        Ea = (8600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    reactant1 = 
"""
HOCH2O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S}
4     O     1 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
HOCH2O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S}
4     O     0 {2,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3275,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    reactant1 = 
"""
HOCH2O
1     C     0 {2,S} {3,S}
2     O     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HOCH2O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
O
1     O     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+18,"cm^3/(mol*s)"),
        n = -1.57,
        Ea = (29230,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.351,"cm^3/(mol*s)"),
        n = 3.524,
        Ea = (7380,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+10,"cm^3/(mol*s)"),
        n = 0.76,
        Ea = (-2325,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.47e+07,"cm^3/(mol*s)"),
        n = 1.97,
        Ea = (11210,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.15e+12,"cm^3/(mol*s)"),
        n = 0.5,
        Ea = (10290,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.72e+06,"cm^3/(mol*s)"),
        n = 1.96,
        Ea = (2639,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH4
1     C     0
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (18580,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH4
1     C     0
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14.4,"cm^3/(mol*s)"),
        n = 3.1,
        Ea = (6935,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11660,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (18480,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13710,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.08e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1411,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.47e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1570,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.11e+14,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (-1051,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product3 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    reactant1 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+14,"s^-1"),
        n = 0,
        Ea = (42300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.635e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (2.41e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5017,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.51e+15,"cm^3/(mol*s)"),
        n = -1,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
HOCH2O
1     C     0 {2,S} {3,S}
2     O     0 {1,S}
3     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (9.033e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11980,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (2.2e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1748,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6095,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6095,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (388000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (3080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+06,"cm^3/(mol*s)"),
        n = 2.1,
        Ea = (496.7,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.1e+06,"cm^3/(mol*s)"),
        n = 1.8,
        Ea = (-596,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (44900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9635,"cm^3/(mol*s)"),
        n = 2.9,
        Ea = (13110,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31.9,"cm^3/(mol*s)"),
        n = 3.17,
        Ea = (7172,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4060,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.99e+12,"cm^3/(mol*s)"),
        n = 0.1,
        Ea = (10600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.46e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (8270,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
CH2(S)
1     C     2S
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-570,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+07,"cm^3/(mol*s)"),
        n = 1.6,
        Ea = (5420,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2(S)
1     C     2S
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.501e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
CH2(S)
1     C     2S
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-570,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2(S)
1     C     2S
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (500000,"cm^3/(mol*s)"),
        n = 2,
        Ea = (7230,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
H2O
1     O     0
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH
1     C     3
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH
1     C     3
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1e+18,"cm^3/(mol*s)"),
        n = -1.56,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 121,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH
1     C     3
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (3000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
O
1     O     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C
1     C     4
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 126,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH
1     C     3
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (2.7e+11,"cm^3/(mol*s)"),
        n = 0.67,
        Ea = (25700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
H2O
1     O     0
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.713e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-755,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (685,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    reactant1 = 
"""
HOCH2O
1     C     0 {2,S} {3,S}
2     O     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 130,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HOCH2O
1     C     0 {2,S} {3,S}
2     O     0 {1,S}
3     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+15,"cm^3/(mol*s)"),
        n = -1.11,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
    reactant1 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+13,"s^-1"),
        n = 0,
        Ea = (50000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    reactant1 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+16,"s^-1"),
        n = 0,
        Ea = (57000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    reactant1 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.593e+18,"s^-1"),
        n = -0.46,
        Ea = (108300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    reactant1 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.62e+06,"cm^3/(mol*s)"),
        n = 2.06,
        Ea = (916,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    reactant1 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.85e+07,"cm^3/(mol*s)"),
        n = 1.51,
        Ea = (-962,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    reactant1 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+06,"cm^3/(mol*s)"),
        n = 2.1,
        Ea = (4868,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    reactant1 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+13,"cm^3/(mol*s)"),
        n = -0.35,
        Ea = (2988,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    reactant1 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH4
1     C     0
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e-07,"cm^3/(mol*s)"),
        n = 5.8,
        Ea = (2200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 139,
    reactant1 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 140,
    reactant1 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.77e+18,"cm^3/(mol*s)"),
        n = -1.9,
        Ea = (2975,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+08,"cm^3/(mol*s)"),
        n = 1.9,
        Ea = (7530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.55e+06,"cm^3/(mol*s)"),
        n = 2.4,
        Ea = (5830,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.48e+07,"cm^3/(mol*s)"),
        n = 1.9,
        Ea = (950,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (51870,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e-07,"cm^3/(mol*s)"),
        n = 6,
        Ea = (6047,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (34.6,"cm^3/(mol*s)"),
        n = 3.61,
        Ea = (16920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19.4,"cm^3/(mol*s)"),
        n = 3.64,
        Ea = (17100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7090,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH
1     C     3
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CH2
1     C     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-260,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    reactant1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (26030,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    reactant1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (26030,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (71530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH4
1     C     0
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11800,"cm^3/(mol*s)"),
        n = 2.45,
        Ea = (-2921,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 156,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 157,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 158,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 159,
    reactant1 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.28e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1097,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 160,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6336,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 161,
    reactant1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 162,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.876e+56,"cm^3/(mol*s)"),
        n = -13.82,
        Ea = (14620,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 163,
    reactant1 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11660,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (18480,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 165,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13710,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
    reactant1 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3275,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 167,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.6,"cm^3/(mol*s)"),
        n = 3.76,
        Ea = (17200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 168,
    reactant1 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    product1 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+14,"s^-1"),
        n = 0,
        Ea = (42300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 169,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H4O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     1 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.814e+45,"cm^3/(mol*s)"),
        n = -11.5,
        Ea = (14600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 170,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (7.561e+14,"cm^3/(mol*s)"),
        n = -1.01,
        Ea = (4749,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (0.4,"cm^3/(mol*s)"),
        n = 3.88,
        Ea = (13620,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 172,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.626e+11,"cm^3/(mol*s)"),
        n = -0.31,
        Ea = (6150,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 173,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (826.5,"cm^3/(mol*s)"),
        n = 2.41,
        Ea = (5285,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 174,
    reactant1 = 
"""
C2H4O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     1 {1,S}
4     O     0 {2,S}
""",
    product1 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.203e+36,"s^-1"),
        n = -8.13,
        Ea = (27020,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 175,
    reactant1 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+41,"s^-1"),
        n = -10.2,
        Ea = (43710,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 176,
    reactant1 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.815e+38,"s^-1"),
        n = -8.45,
        Ea = (37890,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 177,
    reactant1 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+43,"s^-1"),
        n = -10.46,
        Ea = (45580,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 178,
    reactant1 = 
"""
C2H4O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     1 {1,S}
4     O     0 {2,S}
""",
    product1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.848e+30,"s^-1"),
        n = -6.08,
        Ea = (20660,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 179,
    reactant1 = 
"""
C2H4O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     1 {1,S}
4     O     0 {2,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+34,"s^-1"),
        n = -7.25,
        Ea = (23250,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    reactant1 = 
"""
C2H4O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     1 {1,S}
4     O     0 {2,S}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.188e+34,"s^-1"),
        n = -9.02,
        Ea = (29210,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 181,
    reactant1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.63e+13,"s^-1"),
        n = 0,
        Ea = (57200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 182,
    reactant1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.407e+12,"s^-1"),
        n = 0,
        Ea = (53800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
    reactant1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C2H3O1-2
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.78e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3610,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    reactant1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H3O1-2
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9680,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    reactant1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H3O1-2
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    reactant1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C2H3O1-2
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 187,
    reactant1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
C2H3O1-2
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 188,
    reactant1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C2H3O1-2
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11830,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 189,
    reactant1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H3O1-2
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6750,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 190,
    reactant1 = 
"""
C2H3O1-2
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e+14,"s^-1"),
        n = 0,
        Ea = (14000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 191,
    reactant1 = 
"""
C2H3O1-2
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product1 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (14000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 192,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 193,
    reactant1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.11e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3110,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 194,
    reactant1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.94e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1868,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 195,
    reactant1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+06,"cm^3/(mol*s)"),
        n = 1.8,
        Ea = (1300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 196,
    reactant1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (39150,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 197,
    reactant1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1760,"cm^3/(mol*s)"),
        n = 2.79,
        Ea = (4950,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 198,
    reactant1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 199,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product1 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 200,
    reactant1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 201,
    reactant1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+15,"cm^3/(mol*s)"),
        n = -1.08,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 202,
    reactant1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (172000,"cm^3/(mol*s)"),
        n = 2.4,
        Ea = (815,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 203,
    reactant1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 204,
    reactant1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 205,
    reactant1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 206,
    reactant1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 207,
    reactant1 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3275,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 208,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9936,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 209,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (18480,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 210,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11660,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 211,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 212,
    reactant1 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    product1 = 
"""
CH3CO2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S}
3     O     0 {1,D}
4     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+14,"s^-1"),
        n = 0,
        Ea = (40150,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 213,
    reactant1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (12300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 214,
    reactant1 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 215,
    reactant1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 216,
    reactant1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 217,
    reactant1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1350,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 218,
    reactant1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 219,
    reactant1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 220,
    reactant1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1010,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 221,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 222,
    reactant1 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 223,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product1 = 
"""
CH2(S)
1     C     2S
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 224,
    reactant1 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 225,
    reactant1 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 226,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.46e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-515,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 227,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 228,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.07e+07,"cm^3/(mol*s)"),
        n = 1.93,
        Ea = (12950,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 229,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.564e+06,"cm^3/(mol*s)"),
        n = 1.88,
        Ea = (183,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 230,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.986e+06,"cm^3/(mol*s)"),
        n = 1.88,
        Ea = (183,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 231,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (2500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 232,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.62,"cm^3/(mol*s)"),
        n = 3.7,
        Ea = (9500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 233,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (58200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 234,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6750,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 235,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.23e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17190,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 236,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.23e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17190,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 237,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 238,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.82e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17110,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 239,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.82e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17110,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 240,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.23e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17190,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 241,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
CH4
1     C     0
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 242,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+16,"cm^3/(mol*s)"),
        n = -1.39,
        Ea = (1015,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 243,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.337e+06,"cm^3/(mol*s)"),
        n = 1.61,
        Ea = (-384,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 244,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
O
1     O     2T
""",
    product2 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0.29,
        Ea = (11,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 245,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
CH4
1     C     0
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.92e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 246,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 247,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 248,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+08,"cm^3/(mol*s)"),
        n = 1.5,
        Ea = (30100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 249,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
C2H
1     C     1 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+19,"cm^3/(mol*s)"),
        n = -1.4,
        Ea = (28950,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 250,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.94e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 251,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.35e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 252,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C2H
1     C     1 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.37e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (14000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 253,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.236e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (12000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 254,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000483,"cm^3/(mol*s)"),
        n = 4,
        Ea = (-2000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 255,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
HCCOH
1     C     0 {2,T} {3,S}
2     C     0 {1,T}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (504000,"cm^3/(mol*s)"),
        n = 2.3,
        Ea = (13500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 256,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
HCCOH
1     C     0 {2,T} {3,S}
2     C     0 {1,T}
3     O     0 {1,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 257,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
PC2H4OH
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (52800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 258,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (50150,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 259,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
PC2H4OH
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74e+11,"cm^3/(mol*s)"),
        n = 0.27,
        Ea = (600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 260,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.64e+11,"cm^3/(mol*s)"),
        n = 0.15,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 261,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.46e+11,"cm^3/(mol*s)"),
        n = 0.3,
        Ea = (1634,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 262,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
PC2H4OH
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.23e+07,"cm^3/(mol*s)"),
        n = 1.8,
        Ea = (5098,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 263,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.58e+07,"cm^3/(mol*s)"),
        n = 1.65,
        Ea = (2827,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 264,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+07,"cm^3/(mol*s)"),
        n = 1.6,
        Ea = (3038,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 265,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
PC2H4OH
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12300,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (15750,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 266,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8200,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (10750,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 267,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (24000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 268,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
PC2H4OH
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12300,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (15750,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 269,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8200,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (10750,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 270,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (24000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 271,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
PC2H4OH
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.41e+07,"cm^3/(mol*s)"),
        n = 1.7,
        Ea = (5459,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 272,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+07,"cm^3/(mol*s)"),
        n = 1.85,
        Ea = (1824,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 273,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (4448,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 274,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
PC2H4OH
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (133,"cm^3/(mol*s)"),
        n = 3.18,
        Ea = (9362,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 275,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (444,"cm^3/(mol*s)"),
        n = 2.9,
        Ea = (7690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 276,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (134,"cm^3/(mol*s)"),
        n = 2.92,
        Ea = (7452,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 277,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
PC2H4OH
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 278,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 279,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
PC2H4OH
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.17e+20,"cm^3/(mol*s)"),
        n = -2.84,
        Ea = (1240,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 280,
    reactant1 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (25000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 281,
    reactant1 = 
"""
O2C2H4OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     O     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
PC2H4OH
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+16,"s^-1"),
        n = -1,
        Ea = (30000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 282,
    reactant1 = 
"""
O2C2H4OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     O     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.125e+09,"s^-1"),
        n = 0,
        Ea = (18900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 283,
    reactant1 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.81e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (1641,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 284,
    reactant1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (125000,"cm^3/(mol*s)"),
        n = 2.48,
        Ea = (445,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 285,
    reactant1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (980000,"cm^3/(mol*s)"),
        n = 2.43,
        Ea = (5160,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 286,
    reactant1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.13e+11,"cm^3/(mol*s)"),
        n = 0.21,
        Ea = (4890,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 287,
    reactant1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.96e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9784,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 288,
    reactant1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.34e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 289,
    reactant1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (48500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 290,
    reactant1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 291,
    reactant1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 292,
    reactant1 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (31000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 293,
    reactant1 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3COCH2O2
1     C     0 {2,S} {4,D} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     O     0 {1,D}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 294,
    reactant1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3COCH2O2
1     C     0 {2,S} {4,D} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     O     0 {1,D}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    product1 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    product2 = 
"""
CH3COCH2O2H
1     C     0 {2,S} {4,D} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     O     0 {1,D}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 295,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
CH3COCH2O2
1     C     0 {2,S} {4,D} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     O     0 {1,D}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH3COCH2O2H
1     C     0 {2,S} {4,D} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     O     0 {1,D}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.288e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 296,
    reactant1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
CH3COCH2O2
1     C     0 {2,S} {4,D} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     O     0 {1,D}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    product1 = 
"""
CH3COCH2O2H
1     C     0 {2,S} {4,D} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     O     0 {1,D}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 297,
    reactant1 = 
"""
CH3COCH2O2H
1     C     0 {2,S} {4,D} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     O     0 {1,D}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product1 = 
"""
CH3COCH2O
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (43000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 298,
    reactant1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3COCH2O
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 299,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 300,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.34e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 301,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.94e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1868,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 302,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 303,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+07,"cm^3/(mol*s)"),
        n = 1.76,
        Ea = (76,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 304,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.24e+06,"cm^3/(mol*s)"),
        n = 1.5,
        Ea = (-962,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 305,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.005e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (40700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 306,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 307,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.608e+06,"cm^3/(mol*s)"),
        n = 1.78,
        Ea = (5911,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 308,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 309,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 310,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 311,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4810,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 312,
    reactant1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+20,"cm^3/(mol*s)"),
        n = -2.72,
        Ea = (7000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 313,
    reactant1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 314,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 315,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 316,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1790,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 317,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10,"cm^3/(mol*s)"),
        n = 0.76,
        Ea = (-340,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 318,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.608e+06,"cm^3/(mol*s)"),
        n = 1.78,
        Ea = (5911,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 319,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 320,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 321,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 322,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 323,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.026e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 324,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 325,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.005e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (40700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 326,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 327,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 328,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4810,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 329,
    reactant1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (935000,"cm^3/(mol*s)"),
        n = 2.29,
        Ea = (-781,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 330,
    reactant1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (36120,"cm^3/(mol*s)"),
        n = 2.88,
        Ea = (2996,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 331,
    reactant1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.75e+08,"cm^3/(mol*s)"),
        n = 1.36,
        Ea = (2250,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 332,
    reactant1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.344e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 333,
    reactant1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.344e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 334,
    reactant1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.445e-06,"cm^3/(mol*s)"),
        n = 5.73,
        Ea = (5699,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 335,
    reactant1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (44910,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 336,
    reactant1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4074,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 337,
    reactant1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3OCH2O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product2 = 
"""
CH3OCH2O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 338,
    reactant1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     1 {2,S}
""",
    product1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product2 = 
"""
HO2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (44250,"cm^3/(mol*s)"),
        n = 2.6,
        Ea = (13910,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 339,
    reactant1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
OCHO
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     1 {1,S}
""",
    product1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product2 = 
"""
HCOOH
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 340,
    reactant1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13,"s^-1"),
        n = 0,
        Ea = (25500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 341,
    reactant1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 342,
    reactant1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5490,"cm^3/(mol*s)"),
        n = 2.8,
        Ea = (5862,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 343,
    reactant1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product1 = 
"""
CH3OCH3
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8499,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 344,
    reactant1 = 
"""
CH3OCH2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     1 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3OCH2O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 345,
    reactant1 = 
"""
CH3OCH2O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3OCH2O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11660,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 346,
    reactant1 = 
"""
CH3OCH2O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product1 = 
"""
CH3OCH2O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 347,
    reactant1 = 
"""
CH3OCH2O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
CH3OCH2O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
CH3OCH2O
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product3 = 
"""
CH3OCH2O
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.21e+23,"cm^3/(mol*s)"),
        n = -4.5,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 348,
    reactant1 = 
"""
CH3OCH2O
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3OCH2O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 349,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3OCH2O
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 350,
    reactant1 = 
"""
CH3OCH2O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
CH2OCH2O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     1 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+10,"s^-1"),
        n = 0,
        Ea = (21580,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 351,
    reactant1 = 
"""
CH2OCH2O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     1 {2,S}
5     O     0 {3,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13,"s^-1"),
        n = 0,
        Ea = (20760,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 352,
    reactant1 = 
"""
CH2OCH2O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     1 {2,S}
5     O     0 {3,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
O2CH2OCH2O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S} {4,S}
4     O     0 {3,S} {6,S}
5     O     0 {2,S} {7,S}
6     O     0 {4,S}
7     O     1 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 353,
    reactant1 = 
"""
O2CH2OCH2O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S} {4,S}
4     O     0 {3,S} {6,S}
5     O     0 {2,S} {7,S}
6     O     0 {4,S}
7     O     1 {5,S}
""",
    product1 = 
"""
HO2CH2OCHO
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S} {6,D}
5     O     0 {3,S}
6     O     0 {4,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+10,"s^-1"),
        n = 0,
        Ea = (18580,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 354,
    reactant1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 355,
    reactant1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 356,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (49640,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 357,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (52290,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 358,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06,"cm^3/(mol*s)"),
        n = 2.4,
        Ea = (4471,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 359,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+06,"cm^3/(mol*s)"),
        n = 2.54,
        Ea = (6756,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 360,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (549000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (3140,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 361,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.71e+06,"cm^3/(mol*s)"),
        n = 2.4,
        Ea = (5505,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 362,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.054e+10,"cm^3/(mol*s)"),
        n = 0.97,
        Ea = (1586,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 363,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.67e+07,"cm^3/(mol*s)"),
        n = 1.61,
        Ea = (-35,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 364,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (58800,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (14860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 365,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (81000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (16690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 366,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
CH4
1     C     0
""",
    product2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (64000,"cm^3/(mol*s)"),
        n = 2.17,
        Ea = (7520,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 367,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
CH4
1     C     0
""",
    product2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.904,"cm^3/(mol*s)"),
        n = 3.65,
        Ea = (7154,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 368,
    reactant1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (12900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 369,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 370,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 371,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 372,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 373,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 374,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 375,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 376,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 377,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (81000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (16690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 378,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (58800,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (14860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 379,
    reactant1 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    product2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (81000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (16690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 380,
    reactant1 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    product2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (58800,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (14860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 381,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 382,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 383,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 384,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 385,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 386,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 387,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     1 {2,S}
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
HO2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (55200,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (16480,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 388,
    reactant1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     1 {2,S}
""",
    product1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
HO2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14750,"cm^3/(mol*s)"),
        n = 2.6,
        Ea = (13910,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 389,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.64e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2160,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 390,
    reactant1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 391,
    reactant1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e-19,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5020,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 392,
    reactant1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 393,
    reactant1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.818e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 394,
    reactant1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.818e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 395,
    reactant1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.97e+40,"s^-1"),
        n = -8.6,
        Ea = (41430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 396,
    reactant1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.78e+39,"s^-1"),
        n = -8.1,
        Ea = (46580,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 397,
    reactant1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e-19,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 398,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 399,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 400,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 401,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.71e+69,"s^-1"),
        n = -16.09,
        Ea = (140000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 402,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.62e+71,"s^-1"),
        n = -16.58,
        Ea = (139300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 403,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+07,"cm^3/(mol*s)"),
        n = 1.76,
        Ea = (-1216,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 404,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+07,"cm^3/(mol*s)"),
        n = 1.76,
        Ea = (76,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 405,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3CHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+07,"cm^3/(mol*s)"),
        n = 1.76,
        Ea = (76,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 406,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+11,"cm^3/(mol*s)"),
        n = 0.7,
        Ea = (5884,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 407,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11,"cm^3/(mol*s)"),
        n = 0.7,
        Ea = (8959,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 408,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+10,"cm^3/(mol*s)"),
        n = 0.7,
        Ea = (7632,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 409,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.12e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-298,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 410,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (2778,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 411,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.11e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (1451,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 412,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (27000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (12340,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 413,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (27620,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 414,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (23590,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 415,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (173000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (2490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 416,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (400000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (9790,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 417,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (804000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (12283,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 418,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (39900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 419,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (62900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 420,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (60700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 421,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.21,"cm^3/(mol*s)"),
        n = 3.5,
        Ea = (5675,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 422,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.348,"cm^3/(mol*s)"),
        n = 3.5,
        Ea = (12850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 423,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.84,"cm^3/(mol*s)"),
        n = 3.5,
        Ea = (11660,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 424,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 425,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 426,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 427,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H6O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.29e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 428,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 429,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 430,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 431,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H6OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.93e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-960,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 432,
    reactant1 = 
"""
C3H6OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HOC3H6O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     O     0 {2,S}
6     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 433,
    reactant1 = 
"""
HOC3H6O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     O     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25e+10,"s^-1"),
        n = 0,
        Ea = (18900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 434,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 435,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 436,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 437,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 438,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+12,"cm^3/(mol*s)"),
        n = -0.32,
        Ea = (-131,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 439,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C3H5O
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     1 {2,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 440,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 441,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 442,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 443,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-262,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 444,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H5O
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     1 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 445,
    reactant1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.34e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 446,
    reactant1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 447,
    reactant1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 448,
    reactant1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 449,
    reactant1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 450,
    reactant1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 451,
    reactant1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 452,
    reactant1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.34e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 453,
    reactant1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 454,
    reactant1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 455,
    reactant1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 456,
    reactant1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 457,
    reactant1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 458,
    reactant1 = 
"""
C3H5-T
1     C     1 {2,S} {3,D}
2     C     0 {1,S}
3     C     0 {1,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 459,
    reactant1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (5500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 460,
    reactant1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+07,"cm^3/(mol*s)"),
        n = 1.8,
        Ea = (1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 461,
    reactant1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (2000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 462,
    reactant1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 463,
    reactant1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    reactant2 = 
"""
C2H
1     C     1 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 464,
    reactant1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    reactant2 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (64746.7,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 465,
    reactant1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 466,
    reactant1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (5500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 467,
    reactant1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    reactant2 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    product2 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.14e+06,"cm^3/(mol*s)"),
        n = 1.74,
        Ea = (10450,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 468,
    reactant1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2250,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 469,
    reactant1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2250,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 470,
    reactant1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 471,
    reactant1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    reactant2 = 
"""
C2H
1     C     1 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 472,
    reactant1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 473,
    reactant1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 474,
    reactant1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 475,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 476,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 477,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 478,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H
1     C     1 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 479,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 480,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2868,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 481,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 482,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 483,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 484,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 485,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 486,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 487,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
CH
1     C     3
""",
    product1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 488,
    reactant1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 489,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
C2H
1     C     1 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 490,
    reactant1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 491,
    reactant1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 492,
    reactant1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 493,
    reactant1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 494,
    reactant1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
CH
1     C     3
""",
    product1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 495,
    reactant1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 496,
    reactant1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 497,
    reactant1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 498,
    reactant1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 499,
    reactant1 = 
"""
CH3CHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1010,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 500,
    reactant1 = 
"""
CH3CHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1010,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 501,
    reactant1 = 
"""
CH3CHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1459,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 502,
    reactant1 = 
"""
CH3CHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-437,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 503,
    reactant1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 504,
    reactant1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 505,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 506,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 507,
    reactant1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.52e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 508,
    reactant1 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.54e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 509,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 510,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product1 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 511,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 512,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product1 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 513,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3275,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 514,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3275,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 515,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 516,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 517,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19360,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 518,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19360,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 519,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 520,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 521,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (24640,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 522,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (24640,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 523,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 524,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 525,
    reactant1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (26030,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 526,
    reactant1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (26030,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 527,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 528,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 529,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product1 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product2 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 530,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product1 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 531,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
CH3CO2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S}
3     O     0 {1,D}
4     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 532,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
CH3CO2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S}
3     O     0 {1,D}
4     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 533,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 534,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 535,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product3 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 536,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product3 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 537,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 538,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 539,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 540,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 541,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 542,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
C3H5O
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 543,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 544,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 545,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 546,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 547,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
C3H5O
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 548,
    reactant1 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+16,"s^-1"),
        n = 0,
        Ea = (42500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 549,
    reactant1 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.45e+15,"s^-1"),
        n = 0,
        Ea = (42600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 550,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3496,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 551,
    reactant1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6260,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 552,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9256,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 553,
    reactant1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7270,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 554,
    reactant1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.09e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (390,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 555,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
C3H6OOH1-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"s^-1"),
        n = 0,
        Ea = (26850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 556,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
C3H6OOH1-3
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     1 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.125e+11,"s^-1"),
        n = 0,
        Ea = (24400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 557,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
C3H6OOH2-1
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     1 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12,"s^-1"),
        n = 0,
        Ea = (29400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 558,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
C3H6OOH2-2
1     C     1 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.23e+35,"s^-1"),
        n = -6.96,
        Ea = (48880,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 559,
    reactant1 = 
"""
C3H6OOH1-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product1 = 
"""
C3H6O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"s^-1"),
        n = 0,
        Ea = (22000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 560,
    reactant1 = 
"""
C3H6OOH1-3
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     1 {2,S}
5     O     0 {3,S}
""",
    product1 = 
"""
C3H6O1-3
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+10,"s^-1"),
        n = 0,
        Ea = (15250,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 561,
    reactant1 = 
"""
C3H6OOH2-1
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     1 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product1 = 
"""
C3H6O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"s^-1"),
        n = 0,
        Ea = (22000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 562,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H6OOH1-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 563,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H6OOH2-1
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     1 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11750,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 564,
    reactant1 = 
"""
C3H6OOH1-3
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     1 {2,S}
5     O     0 {3,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.035e+15,"s^-1"),
        n = -0.79,
        Ea = (27400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 565,
    reactant1 = 
"""
C3H6OOH2-1
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     1 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product1 = 
"""
C2H3OOH
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     0 {2,S}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.54e+27,"s^-1"),
        n = -5.14,
        Ea = (38320,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 566,
    reactant1 = 
"""
C3H6OOH1-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.31e+33,"s^-1"),
        n = -7.01,
        Ea = (48120,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 567,
    reactant1 = 
"""
C3H6OOH2-2
1     C     1 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product1 = 
"""
CH3COCH3
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+14,"s^-1"),
        n = 0,
        Ea = (1500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 568,
    reactant1 = 
"""
C3H6OOH1-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C3H6OOH1-2O2
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {6,S}
4     O     0 {2,S} {7,S}
5     C     0 {1,S}
6     O     1 {3,S}
7     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 569,
    reactant1 = 
"""
C3H6OOH1-3
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     1 {2,S}
5     O     0 {3,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C3H6OOH1-3O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     O     0 {3,S} {7,S}
6     O     0 {4,S}
7     O     1 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.52e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 570,
    reactant1 = 
"""
C3H6OOH2-1
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     1 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C3H6OOH2-1O2
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {6,S}
4     O     0 {2,S} {7,S}
5     C     0 {1,S}
6     O     0 {3,S}
7     O     1 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.52e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 571,
    reactant1 = 
"""
C3H6OOH1-2O2
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {6,S}
4     O     0 {2,S} {7,S}
5     C     0 {1,S}
6     O     1 {3,S}
7     O     0 {4,S}
""",
    product1 = 
"""
C3KET12
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {6,D}
3     O     0 {1,S} {5,S}
4     C     0 {1,S}
5     O     0 {3,S}
6     O     0 {2,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"s^-1"),
        n = 0,
        Ea = (26400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 572,
    reactant1 = 
"""
C3H6OOH1-3O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     O     0 {3,S} {7,S}
6     O     0 {4,S}
7     O     1 {5,S}
""",
    product1 = 
"""
C3KET13
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     O     0 {2,S} {6,S}
5     O     0 {3,D}
6     O     0 {4,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+10,"s^-1"),
        n = 0,
        Ea = (21400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 573,
    reactant1 = 
"""
C3H6OOH2-1O2
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {6,S}
4     O     0 {2,S} {7,S}
5     C     0 {1,S}
6     O     0 {3,S}
7     O     1 {4,S}
""",
    product1 = 
"""
CH3COCH2O2H
1     C     0 {2,S} {4,D} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     O     0 {1,D}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"s^-1"),
        n = 0,
        Ea = (23850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 574,
    reactant1 = 
"""
C3H6OOH2-1O2
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {6,S}
4     O     0 {2,S} {7,S}
5     C     0 {1,S}
6     O     0 {3,S}
7     O     1 {4,S}
""",
    product1 = 
"""
C3H51-2,3OOH
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {6,S}
4     O     0 {2,S} {7,S}
5     C     1 {1,S}
6     O     0 {3,S}
7     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.125e+11,"s^-1"),
        n = 0,
        Ea = (24400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 575,
    reactant1 = 
"""
C3H6OOH1-2O2
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {6,S}
4     O     0 {2,S} {7,S}
5     C     0 {1,S}
6     O     1 {3,S}
7     O     0 {4,S}
""",
    product1 = 
"""
C3H51-2,3OOH
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {6,S}
4     O     0 {2,S} {7,S}
5     C     1 {1,S}
6     O     0 {3,S}
7     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+11,"s^-1"),
        n = 0,
        Ea = (29400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 576,
    reactant1 = 
"""
C3H51-2,3OOH
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {6,S}
4     O     0 {2,S} {7,S}
5     C     1 {1,S}
6     O     0 {3,S}
7     O     0 {4,S}
""",
    product1 = 
"""
AC3H5OOH
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     O     0 {1,S} {5,S}
4     C     0 {2,D}
5     O     0 {3,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.56e+13,"s^-1"),
        n = -0.49,
        Ea = (17770,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 577,
    reactant1 = 
"""
C3H6OOH1-3O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     O     0 {3,S} {7,S}
6     O     0 {4,S}
7     O     1 {5,S}
""",
    product1 = 
"""
C3H52-1,3OOH
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     O     0 {3,S} {7,S}
6     O     0 {4,S}
7     O     0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"s^-1"),
        n = 0,
        Ea = (26850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 578,
    reactant1 = 
"""
C3H52-1,3OOH
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     O     0 {3,S} {7,S}
6     O     0 {4,S}
7     O     0 {5,S}
""",
    product1 = 
"""
AC3H5OOH
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     O     0 {1,S} {5,S}
4     C     0 {2,D}
5     O     0 {3,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+14,"s^-1"),
        n = -0.63,
        Ea = (17250,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 579,
    reactant1 = 
"""
C3KET12
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {6,D}
3     O     0 {1,S} {5,S}
4     C     0 {1,S}
5     O     0 {3,S}
6     O     0 {2,D}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.45e+15,"s^-1"),
        n = 0,
        Ea = (43000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 580,
    reactant1 = 
"""
C3KET13
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     O     0 {2,S} {6,S}
5     O     0 {3,D}
6     O     0 {4,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (43000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 581,
    reactant1 = 
"""
CH3COCH2O2H
1     C     0 {2,S} {4,D} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     O     0 {1,D}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (43000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 582,
    reactant1 = 
"""
C3H5O
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     1 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
AC3H5OOH
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     O     0 {1,S} {5,S}
4     C     0 {2,D}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 583,
    reactant1 = 
"""
C3H5O
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     1 {2,S}
""",
    product1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (29100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 584,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C3H5O
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 585,
    reactant1 = 
"""
C3H5O
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     1 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 586,
    reactant1 = 
"""
C2H3OOH
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     0 {2,S}
""",
    product1 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e+14,"s^-1"),
        n = 0,
        Ea = (43000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 587,
    reactant1 = 
"""
C3H6O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+14,"s^-1"),
        n = 0,
        Ea = (60000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 588,
    reactant1 = 
"""
C3H6O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 589,
    reactant1 = 
"""
C3H6O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.63e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (5000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 590,
    reactant1 = 
"""
C3H6O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 591,
    reactant1 = 
"""
C3H6O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 592,
    reactant1 = 
"""
C3H6O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 593,
    reactant1 = 
"""
C3H6O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 594,
    reactant1 = 
"""
C3H6O1-3
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+14,"s^-1"),
        n = 0,
        Ea = (60000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 595,
    reactant1 = 
"""
C3H6O1-3
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 596,
    reactant1 = 
"""
C3H6O1-3
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 597,
    reactant1 = 
"""
C3H6O1-3
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.63e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (5000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 598,
    reactant1 = 
"""
C3H6O1-3
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 599,
    reactant1 = 
"""
C3H6O1-3
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 600,
    reactant1 = 
"""
C3H6O1-3
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 601,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.015e+43,"s^-1"),
        n = -9.41,
        Ea = (41490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 602,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.044e+38,"s^-1"),
        n = -8.11,
        Ea = (40490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 603,
    reactant1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 604,
    reactant1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 605,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (52340,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 606,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (49800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 607,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 608,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 609,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (12300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 610,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 611,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (18000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 612,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 613,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.904,"cm^3/(mol*s)"),
        n = 3.65,
        Ea = (7154,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 614,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.02,"cm^3/(mol*s)"),
        n = 3.46,
        Ea = (5481,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 615,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (188000,"cm^3/(mol*s)"),
        n = 2.75,
        Ea = (6280,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 616,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06,"cm^3/(mol*s)"),
        n = 2.4,
        Ea = (4471,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 617,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.054e+10,"cm^3/(mol*s)"),
        n = 0.97,
        Ea = (1586,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 618,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.34e+07,"cm^3/(mol*s)"),
        n = 1.61,
        Ea = (-35,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 619,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 620,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.62e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 621,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (81000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (16690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 622,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (117600,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (14860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 623,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 624,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 625,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 626,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 627,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 628,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 629,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 630,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     1 {2,S}
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
HO2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.68e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 631,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     1 {2,S}
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
HO2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 632,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (81000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (16690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 633,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (117600,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (14860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 634,
    reactant1 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    product2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 635,
    reactant1 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    product2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 636,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 637,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 638,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 639,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 640,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    product2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 641,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    product2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 642,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    product2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 643,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    product2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 644,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 645,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 646,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 647,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 648,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13200,"cm^3/(mol*s)"),
        n = 2.48,
        Ea = (6130,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 649,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17600,"cm^3/(mol*s)"),
        n = 2.48,
        Ea = (6130,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 650,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11,"cm^3/(mol*s)"),
        n = 0.51,
        Ea = (2620,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 651,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11,"cm^3/(mol*s)"),
        n = 0.51,
        Ea = (2620,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 652,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11,"cm^3/(mol*s)"),
        n = 0.51,
        Ea = (1230,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 653,
    reactant1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e-18,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 654,
    reactant1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e-18,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 655,
    reactant1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e-18,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 656,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 657,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 658,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (37190,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 659,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H71-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     1 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (781000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (12290,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 660,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H71-2
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (390000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (5821,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 661,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (337600,"cm^3/(mol*s)"),
        n = 2.36,
        Ea = (207,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 662,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H71-4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     1 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665100,"cm^3/(mol*s)"),
        n = 2.54,
        Ea = (6756,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 663,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H71-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     1 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.14e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (2778,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 664,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H71-2
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.22e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (1451,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 665,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (27640,"cm^3/(mol*s)"),
        n = 2.64,
        Ea = (-1919,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 666,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H71-4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     1 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+09,"cm^3/(mol*s)"),
        n = 0.97,
        Ea = (1586,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 667,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.69,"cm^3/(mol*s)"),
        n = 3.31,
        Ea = (4002,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 668,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C4H71-4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     1 {2,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.452,"cm^3/(mol*s)"),
        n = 3.65,
        Ea = (7154,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 669,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4820,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (10530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 670,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H71-4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     1 {2,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2380,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (16490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 671,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4820,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (10530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 672,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C4H71-4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     1 {2,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2380,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (16490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 673,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40,"cm^3/(mol*s)"),
        n = 2.9,
        Ea = (8609,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 674,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H71-4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     1 {2,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6458,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 675,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 676,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.9e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (12400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 677,
    reactant1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 678,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 679,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 680,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 681,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 682,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 683,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C4H8O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S} {5,S}
5     C     0 {4,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14340,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 684,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 685,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (39390,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 686,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (346000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (2492,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 687,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.24e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-298,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 688,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.42,"cm^3/(mol*s)"),
        n = 3.5,
        Ea = (5675,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 689,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19280,"cm^3/(mol*s)"),
        n = 2.6,
        Ea = (13910,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 690,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19280,"cm^3/(mol*s)"),
        n = 2.6,
        Ea = (13910,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 691,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18,"cm^3/(mol*s)"),
        n = 2.95,
        Ea = (11990,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 692,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 693,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 694,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 695,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 696,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 697,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H8O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S} {5,S}
5     C     0 {4,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14340,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 698,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H8O2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S} {5,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.62e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (12310,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 699,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C4H8O2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S} {5,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.62e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (12310,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 700,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H8OH-1
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S} {4,S}
4     C     0 {3,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.75e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-782,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 701,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H8OH-2
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,S}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.75e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-782,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 702,
    reactant1 = 
"""
C4H8OH-1
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S} {4,S}
4     C     0 {3,S}
5     O     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8OH-1O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {6,S}
3     C     0 {1,S} {5,S}
4     O     0 {1,S} {7,S}
5     C     0 {3,S}
6     O     0 {2,S}
7     O     1 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 703,
    reactant1 = 
"""
C4H8OH-2
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8OH-2O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S} {6,S}
3     O     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {2,S}
7     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 704,
    reactant1 = 
"""
C4H8OH-1O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {6,S}
3     C     0 {1,S} {5,S}
4     O     0 {1,S} {7,S}
5     C     0 {3,S}
6     O     0 {2,S}
7     O     1 {4,S}
""",
    product1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (25000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 705,
    reactant1 = 
"""
C4H8OH-2O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S} {6,S}
3     O     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {2,S}
7     O     1 {3,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product3 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (25000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 706,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
C4H71-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     1 {1,D}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 707,
    reactant1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C4H71-2
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 708,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C4H71-4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 709,
    reactant1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C4H72-2
1     C     0 {2,S}
2     C     1 {1,S} {3,D}
3     C     0 {2,D} {4,S}
4     C     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 710,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 711,
    reactant1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.59e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-131,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 712,
    reactant1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 713,
    reactant1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 714,
    reactant1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,D}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 715,
    reactant1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C4H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,D}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,D}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 716,
    reactant1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    reactant2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 717,
    reactant1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 718,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 719,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 720,
    reactant1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 721,
    reactant1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
C4H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,D}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,D}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 722,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
C4H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,D}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 723,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
C4H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,D}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 724,
    reactant1 = 
"""
C4H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,D}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,D}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+14,"s^-1"),
        n = 0,
        Ea = (19000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 725,
    reactant1 = 
"""
C4H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,D}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,D}
""",
    product1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+14,"s^-1"),
        n = 0,
        Ea = (19000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 726,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+36,"s^-1"),
        n = -6.27,
        Ea = (112353,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 727,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+44,"s^-1"),
        n = -8.62,
        Ea = (123608,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 728,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+15,"s^-1"),
        n = 0,
        Ea = (94700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 729,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+06,"cm^3/(mol*s)"),
        n = 2.53,
        Ea = (12240,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 730,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665000,"cm^3/(mol*s)"),
        n = 2.53,
        Ea = (9240,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 731,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 732,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 733,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+06,"cm^3/(mol*s)"),
        n = 1.9,
        Ea = (3740,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 734,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+06,"cm^3/(mol*s)"),
        n = 1.9,
        Ea = (3740,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 735,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3CHCHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+08,"cm^3/(mol*s)"),
        n = 1.45,
        Ea = (-860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 736,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     1 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+08,"cm^3/(mol*s)"),
        n = 1.45,
        Ea = (-860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 737,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (3430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 738,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 739,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H6O25
1     O     0 {2,S} {5,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     C     0 {3,D} {5,S}
5     C     0 {1,S} {4,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 740,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H3CHOCH2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {3,S}
3     C     0 {1,S} {2,S}
4     C     0 {1,S} {5,D}
5     C     0 {4,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 741,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (22800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 742,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 743,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (22800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 744,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 745,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (22500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 746,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 747,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (22500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 748,
    reactant1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 749,
    reactant1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+67,"s^-1"),
        n = -16.89,
        Ea = (59100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 750,
    reactant1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+26,"cm^3/(mol*s)"),
        n = -3.35,
        Ea = (17423,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 751,
    reactant1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 752,
    reactant1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 753,
    reactant1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 754,
    reactant1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 755,
    reactant1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-596,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 756,
    reactant1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 757,
    reactant1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     1 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
O
1     O     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0.29,
        Ea = (11,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 758,
    reactant1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.2e+16,"cm^3/(mol*s)"),
        n = -1.39,
        Ea = (1010,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 759,
    reactant1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 760,
    reactant1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 761,
    reactant1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 762,
    reactant1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 763,
    reactant1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 764,
    reactant1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 765,
    reactant1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-596,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 766,
    reactant1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 767,
    reactant1 = 
"""
C4H5-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     1 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+67,"s^-1"),
        n = -16.89,
        Ea = (59100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 768,
    reactant1 = 
"""
C4H5-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     1 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+26,"cm^3/(mol*s)"),
        n = -3.35,
        Ea = (17423,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 769,
    reactant1 = 
"""
C4H5-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     1 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product3 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 770,
    reactant1 = 
"""
C4H5-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     1 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 771,
    reactant1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+15,"s^-1"),
        n = 0,
        Ea = (92600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 772,
    reactant1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 773,
    reactant1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (2490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 774,
    reactant1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 775,
    reactant1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 776,
    reactant1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (18500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 777,
    reactant1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+08,"cm^3/(mol*s)"),
        n = 1.65,
        Ea = (327,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 778,
    reactant1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+11,"cm^3/(mol*s)"),
        n = 0.7,
        Ea = (5880,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 779,
    reactant1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-298,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 780,
    reactant1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"s^-1"),
        n = 0,
        Ea = (65000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 781,
    reactant1 = 
"""
C4H6-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"s^-1"),
        n = 0,
        Ea = (65000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 782,
    reactant1 = 
"""
C4H6-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"s^-1"),
        n = 0,
        Ea = (67000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 783,
    reactant1 = 
"""
C4H6-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H612
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 784,
    reactant1 = 
"""
C4H6-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H5-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     1 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (340000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (2490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 785,
    reactant1 = 
"""
C4H6-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (260000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 786,
    reactant1 = 
"""
C4H6-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
C4H5-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     1 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+15,"s^-1"),
        n = 0,
        Ea = (87300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 787,
    reactant1 = 
"""
C4H6-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C4H5-2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     1 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (18500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 788,
    reactant1 = 
"""
C2H3CHOCH2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {3,S}
3     C     0 {1,S} {2,S}
4     C     0 {1,S} {5,D}
5     C     0 {4,D}
""",
    product1 = 
"""
C4H6O23
1     O     0 {2,S} {5,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D} {4,S}
4     C     0 {3,S} {5,S}
5     C     0 {1,S} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14,"s^-1"),
        n = 0,
        Ea = (50600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 789,
    reactant1 = 
"""
C4H6O23
1     O     0 {2,S} {5,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D} {4,S}
4     C     0 {3,S} {5,S}
5     C     0 {1,S} {4,S}
""",
    product1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.95e+13,"s^-1"),
        n = 0,
        Ea = (49400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 790,
    reactant1 = 
"""
C4H6O23
1     O     0 {2,S} {5,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D} {4,S}
4     C     0 {3,S} {5,S}
5     C     0 {1,S} {4,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.75e+15,"s^-1"),
        n = 0,
        Ea = (69300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 791,
    reactant1 = 
"""
C4H6O23
1     O     0 {2,S} {5,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D} {4,S}
4     C     0 {3,S} {5,S}
5     C     0 {1,S} {4,S}
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
C2H4O1-2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (75800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 792,
    reactant1 = 
"""
C4H6O25
1     O     0 {2,S} {5,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     C     0 {3,D} {5,S}
5     C     0 {1,S} {4,S}
""",
    product1 = 
"""
C4H4O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,T}
3     C     0 {1,S} {5,D}
4     C     0 {2,T}
5     O     0 {3,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+12,"s^-1"),
        n = 0,
        Ea = (48500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 793,
    reactant1 = 
"""
C4H4O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,T}
3     C     0 {1,S} {5,D}
4     C     0 {2,T}
5     O     0 {3,D}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H4-P
1     C     0 {2,S} {3,T}
2     C     0 {1,S}
3     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.78e+15,"s^-1"),
        n = 0,
        Ea = (77500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 794,
    reactant1 = 
"""
C4H4O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,T}
3     C     0 {1,S} {5,D}
4     C     0 {2,T}
5     O     0 {3,D}
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+14,"s^-1"),
        n = 0,
        Ea = (77500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 795,
    reactant1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+14,"s^-1"),
        n = 0,
        Ea = (69000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 796,
    reactant1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     1 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (2490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 797,
    reactant1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3CHCHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (2490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 798,
    reactant1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+21,"cm^3/(mol*s)"),
        n = -2.39,
        Ea = (11180,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 799,
    reactant1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+21,"cm^3/(mol*s)"),
        n = -2.39,
        Ea = (11180,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 800,
    reactant1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     1 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1,"cm^3/(mol*s)"),
        n = 3.5,
        Ea = (5675,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 801,
    reactant1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH3CHCHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1,"cm^3/(mol*s)"),
        n = 3.5,
        Ea = (5675,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 802,
    reactant1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
CH2CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     1 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.21,"cm^3/(mol*s)"),
        n = 3.5,
        Ea = (4682,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 803,
    reactant1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
CH3CHCHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.11,"cm^3/(mol*s)"),
        n = 3.5,
        Ea = (4682,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 804,
    reactant1 = 
"""
CH3CHCHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (30000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 805,
    reactant1 = 
"""
CH3CHCHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 806,
    reactant1 = 
"""
CH2CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     1 {2,S}
5     O     0 {3,D}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (25000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 807,
    reactant1 = 
"""
CH2CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     1 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3CHCHCHO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 808,
    reactant1 = 
"""
C6H2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C6H3
1     C     1 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+30,"cm^3/(mol*s)"),
        n = -4.92,
        Ea = (10800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 809,
    reactant1 = 
"""
C6H3
1     C     1 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+23,"cm^3/(mol*s)"),
        n = -2.55,
        Ea = (10780,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 810,
    reactant1 = 
"""
C6H3
1     C     1 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
L-C6H4
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+43,"cm^3/(mol*s)"),
        n = -9.01,
        Ea = (12120,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 811,
    reactant1 = 
"""
C6H3
1     C     1 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C6H2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 812,
    reactant1 = 
"""
C6H3
1     C     1 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C6H2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 813,
    reactant1 = 
"""
C6H3
1     C     1 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    product3 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 814,
    reactant1 = 
"""
L-C6H4
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C-C6H4
1     C     0 {2,S} {6,T}
2     C     0 {1,S} {3,D}
3     C     0 {2,D} {4,S}
4     C     0 {3,S} {5,D}
5     C     0 {4,D} {6,S}
6     C     0 {1,T} {5,S}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+54,"cm^3/(mol*s)"),
        n = -11.7,
        Ea = (34500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 815,
    reactant1 = 
"""
L-C6H4
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C6H3
1     C     1 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+06,"cm^3/(mol*s)"),
        n = 2.53,
        Ea = (9240,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 816,
    reactant1 = 
"""
L-C6H4
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C6H3
1     C     1 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 817,
    reactant1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H5-N
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     1 {1,D}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+51,"cm^3/(mol*s)"),
        n = -11.92,
        Ea = (16500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 818,
    reactant1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H5-I
1     C     1 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+51,"cm^3/(mol*s)"),
        n = -11.92,
        Ea = (17700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 819,
    reactant1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665000,"cm^3/(mol*s)"),
        n = 2.53,
        Ea = (12240,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 820,
    reactant1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (333000,"cm^3/(mol*s)"),
        n = 2.53,
        Ea = (9240,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 821,
    reactant1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (3430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 822,
    reactant1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.55e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 823,
    reactant1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C3H3
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+08,"cm^3/(mol*s)"),
        n = 1.45,
        Ea = (-860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 824,
    reactant1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    reactant2 = 
"""
C2H
1     C     1 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
L-C6H4
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 825,
    reactant1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    product1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+43,"s^-1"),
        n = -9.49,
        Ea = (53000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 826,
    reactant1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+20,"cm^3/(mol*s)"),
        n = -1.67,
        Ea = (10800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 827,
    reactant1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
H2CC
1     C     0 {2,D}
2     C     2S {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+25,"cm^3/(mol*s)"),
        n = -3.34,
        Ea = (10014,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 828,
    reactant1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+47,"cm^3/(mol*s)"),
        n = -10.26,
        Ea = (13070,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 829,
    reactant1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 830,
    reactant1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 831,
    reactant1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
L-C6H4
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14,"cm^3/(mol*s)"),
        n = -0.56,
        Ea = (10600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 832,
    reactant1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
C-C6H4
1     C     0 {2,S} {6,T}
2     C     0 {1,S} {3,D}
3     C     0 {2,D} {4,S}
4     C     0 {3,S} {5,D}
5     C     0 {4,D} {6,S}
6     C     0 {1,T} {5,S}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+46,"cm^3/(mol*s)"),
        n = -10.01,
        Ea = (30100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 833,
    reactant1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
H2CC
1     C     0 {2,D}
2     C     2S {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+23,"cm^3/(mol*s)"),
        n = -2.55,
        Ea = (10780,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 834,
    reactant1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H4
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3     C     0 {1,D}
4     C     0 {2,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+43,"cm^3/(mol*s)"),
        n = -9.01,
        Ea = (12120,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 835,
    reactant1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 836,
    reactant1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 837,
    reactant1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.86e+16,"cm^3/(mol*s)"),
        n = -1.8,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 838,
    reactant1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
C3H4-A
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     C     0 {1,D}
""",
    product2 = 
"""
C2H
1     C     1 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 839,
    reactant1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H3-N
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,D}
3     C     0 {1,T}
4     C     1 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+42,"cm^3/(mol*s)"),
        n = -8.72,
        Ea = (15300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 840,
    reactant1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C4H3-I
1     C     0 {2,S} {3,T}
2     C     1 {1,S} {4,D}
3     C     0 {1,T}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+30,"cm^3/(mol*s)"),
        n = -4.92,
        Ea = (10800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 841,
    reactant1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C3H2
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     C     1 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1720,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 842,
    reactant1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
H2C4O
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,D}
3     C     0 {1,D} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-410,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 843,
    reactant1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    reactant2 = 
"""
C2H
1     C     1 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
C6H2
1     C     0 {2,T} {3,S}
2     C     0 {1,T} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 844,
    reactant1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    reactant2 = 
"""
C2H
1     C     1 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
C6H3
1     C     1 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+37,"cm^3/(mol*s)"),
        n = -7.68,
        Ea = (7100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 845,
    reactant1 = 
"""
H2C4O
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,D}
3     C     0 {1,D} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 846,
    reactant1 = 
"""
H2C4O
1     C     0 {2,D} {3,D}
2     C     0 {1,D} {4,D}
3     C     0 {1,D} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
HCCO
1     C     0 {2,D} {3,D}
2     C     1 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (2000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 847,
    reactant1 = 
"""
H2CC
1     C     0 {2,D}
2     C     2S {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 848,
    reactant1 = 
"""
H2CC
1     C     0 {2,D}
2     C     2S {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 849,
    reactant1 = 
"""
H2CC
1     C     0 {2,D}
2     C     2S {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 850,
    reactant1 = 
"""
H2CC
1     C     0 {2,D}
2     C     2S {1,D}
""",
    reactant2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C4H6
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 851,
    reactant1 = 
"""
C4H8O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S} {5,S}
5     C     0 {4,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 852,
    reactant1 = 
"""
C4H8O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S} {5,S}
5     C     0 {4,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 853,
    reactant1 = 
"""
C4H8O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S} {5,S}
5     C     0 {4,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 854,
    reactant1 = 
"""
C4H8O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S} {5,S}
5     C     0 {4,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 855,
    reactant1 = 
"""
C4H8O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S} {5,S}
5     C     0 {4,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 856,
    reactant1 = 
"""
C4H8O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S} {5,S}
5     C     0 {4,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 857,
    reactant1 = 
"""
C4H8O1-3
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 858,
    reactant1 = 
"""
C4H8O1-3
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 859,
    reactant1 = 
"""
C4H8O1-3
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 860,
    reactant1 = 
"""
C4H8O1-3
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 861,
    reactant1 = 
"""
C4H8O1-3
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 862,
    reactant1 = 
"""
C4H8O1-3
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 863,
    reactant1 = 
"""
C4H8O1-4
1     C     0 {2,S} {5,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     O     0 {1,S} {4,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 864,
    reactant1 = 
"""
C4H8O1-4
1     C     0 {2,S} {5,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     O     0 {1,S} {4,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 865,
    reactant1 = 
"""
C4H8O1-4
1     C     0 {2,S} {5,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     O     0 {1,S} {4,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 866,
    reactant1 = 
"""
C4H8O1-4
1     C     0 {2,S} {5,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     O     0 {1,S} {4,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 867,
    reactant1 = 
"""
C4H8O1-4
1     C     0 {2,S} {5,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     O     0 {1,S} {4,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 868,
    reactant1 = 
"""
C4H8O1-4
1     C     0 {2,S} {5,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     O     0 {1,S} {4,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 869,
    reactant1 = 
"""
C4H8O2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S} {5,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 870,
    reactant1 = 
"""
C4H8O2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S} {5,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 871,
    reactant1 = 
"""
C4H8O2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S} {5,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 872,
    reactant1 = 
"""
C4H8O2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S} {5,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 873,
    reactant1 = 
"""
C4H8O2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S} {5,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 874,
    reactant1 = 
"""
C4H8O2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S} {5,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 875,
    reactant1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.52e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 876,
    reactant1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.54e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 877,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 878,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product1 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 879,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3275,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 880,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 881,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 882,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 883,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 884,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product3 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 885,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 886,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 887,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 888,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 889,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
CH3CO2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S}
3     O     0 {1,D}
4     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 890,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e-14,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 891,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e-14,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 892,
    reactant1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (26030,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 893,
    reactant1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (26030,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 894,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 895,
    reactant1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 896,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product1 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    product2 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 897,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product1 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product2 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 898,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 899,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 900,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 901,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 902,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 903,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 904,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
C3H5O
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 905,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 906,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product1 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 907,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3275,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 908,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 909,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 910,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 911,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 912,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19360,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 913,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19360,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 914,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 915,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 916,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (24640,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 917,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (24640,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 918,
    reactant1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
C4H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,D}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,D}
""",
    product2 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 919,
    reactant1 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C4H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,D}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,D}
""",
    product2 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 920,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 921,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 922,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product3 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 923,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 924,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 925,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 926,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 927,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 928,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
CH3CO2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S}
3     O     0 {1,D}
4     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 929,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 930,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 931,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 932,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 933,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 934,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 935,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
C3H5O
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 936,
    reactant1 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 937,
    reactant1 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 938,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 939,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 940,
    reactant1 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+16,"s^-1"),
        n = 0,
        Ea = (42500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 941,
    reactant1 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.45e+15,"s^-1"),
        n = 0,
        Ea = (41600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 942,
    reactant1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3457,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 943,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9043,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 944,
    reactant1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.33e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6397,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 945,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
C4H8OOH1-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     O     0 {3,S}
6     C     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"s^-1"),
        n = 0,
        Ea = (26850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 946,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
C4H8OOH1-3
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     1 {2,S} {6,S}
5     O     0 {3,S}
6     C     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+10,"s^-1"),
        n = 0,
        Ea = (20850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 947,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
C4H8OOH1-4
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     O     0 {3,S}
6     C     1 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.688e+09,"s^-1"),
        n = 0,
        Ea = (22350,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 948,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C4H8OOH2-1
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     1 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"s^-1"),
        n = 0,
        Ea = (29400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 949,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C4H8OOH2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"s^-1"),
        n = 0,
        Ea = (26850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 950,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C4H8OOH2-4
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     1 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.75e+10,"s^-1"),
        n = 0,
        Ea = (24400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 951,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.044e+38,"s^-1"),
        n = -8.11,
        Ea = (40490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 952,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.075e+42,"s^-1"),
        n = -9.41,
        Ea = (41490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 953,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.044e+38,"s^-1"),
        n = -8.11,
        Ea = (40490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 954,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H8OOH1-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     O     0 {3,S}
6     C     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 955,
    reactant1 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H8OOH2-1
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     1 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11750,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 956,
    reactant1 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C4H8OOH2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11750,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 957,
    reactant1 = 
"""
C4H8OOH1-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     O     0 {3,S}
6     C     0 {4,S}
""",
    product1 = 
"""
C4H8O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S} {5,S}
5     C     0 {4,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"s^-1"),
        n = 0,
        Ea = (22000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 958,
    reactant1 = 
"""
C4H8OOH1-3
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     1 {2,S} {6,S}
5     O     0 {3,S}
6     C     0 {4,S}
""",
    product1 = 
"""
C4H8O1-3
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+10,"s^-1"),
        n = 0,
        Ea = (15250,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 959,
    reactant1 = 
"""
C4H8OOH1-4
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     O     0 {3,S}
6     C     1 {4,S}
""",
    product1 = 
"""
C4H8O1-4
1     C     0 {2,S} {5,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     O     0 {1,S} {4,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.375e+09,"s^-1"),
        n = 0,
        Ea = (6000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 960,
    reactant1 = 
"""
C4H8OOH2-1
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     1 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product1 = 
"""
C4H8O1-2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S} {5,S}
5     C     0 {4,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"s^-1"),
        n = 0,
        Ea = (22000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 961,
    reactant1 = 
"""
C4H8OOH2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product1 = 
"""
C4H8O2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {3,S} {5,S}
3     O     0 {1,S} {2,S}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11,"s^-1"),
        n = 0,
        Ea = (22000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 962,
    reactant1 = 
"""
C4H8OOH2-4
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     1 {2,S}
6     O     0 {3,S}
""",
    product1 = 
"""
C4H8O1-3
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+10,"s^-1"),
        n = 0,
        Ea = (15250,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 963,
    reactant1 = 
"""
C4H8OOH1-1
1     O     0 {2,S}
2     O     0 {1,S} {3,S}
3     C     1 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     C     0 {4,S} {6,S}
6     C     0 {5,S}
""",
    product1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+14,"s^-1"),
        n = 0,
        Ea = (1500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 964,
    reactant1 = 
"""
C4H8OOH2-2
1     C     0 {2,S}
2     C     1 {1,S} {3,S} {5,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S}
5     O     0 {2,S} {6,S}
6     O     0 {5,S}
""",
    product1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+14,"s^-1"),
        n = 0,
        Ea = (1500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 965,
    reactant1 = 
"""
C4H8OOH1-3
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     1 {2,S} {6,S}
5     O     0 {3,S}
6     C     0 {4,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.635e+13,"s^-1"),
        n = -0.16,
        Ea = (29900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 966,
    reactant1 = 
"""
C4H8OOH2-4
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     1 {2,S}
6     O     0 {3,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product3 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.945e+18,"s^-1"),
        n = -1.63,
        Ea = (26790,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 967,
    reactant1 = 
"""
C4H8OOH1-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     O     0 {3,S}
6     C     0 {4,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8OOH1-2O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S} {6,S}
4     O     0 {1,S} {7,S}
5     O     0 {2,S} {8,S}
6     C     0 {3,S}
7     O     1 {4,S}
8     O     0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.54e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 968,
    reactant1 = 
"""
C4H8OOH1-3
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     1 {2,S} {6,S}
5     O     0 {3,S}
6     C     0 {4,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8OOH1-3O2
1     C     0 {2,S} {4,S} {6,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {5,S}
4     O     0 {1,S} {7,S}
5     O     0 {3,S} {8,S}
6     C     0 {1,S}
7     O     1 {4,S}
8     O     0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.54e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 969,
    reactant1 = 
"""
C4H8OOH1-4
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     O     0 {3,S}
6     C     1 {4,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8OOH1-4O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     O     0 {3,S} {7,S}
6     O     0 {4,S} {8,S}
7     O     0 {5,S}
8     O     1 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.52e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 970,
    reactant1 = 
"""
C4H8OOH2-1
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     1 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8OOH2-1O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S} {6,S}
4     O     0 {1,S} {7,S}
5     O     0 {2,S} {8,S}
6     C     0 {3,S}
7     O     0 {4,S}
8     O     1 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.52e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 971,
    reactant1 = 
"""
C4H8OOH2-3
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8OOH2-3O2
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S} {6,S}
3     O     0 {1,S} {7,S}
4     O     0 {2,S} {8,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     O     0 {3,S}
8     O     1 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.54e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 972,
    reactant1 = 
"""
C4H8OOH2-4
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     1 {2,S}
6     O     0 {3,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H8OOH2-4O2
1     C     0 {2,S} {4,S} {6,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {5,S}
4     O     0 {1,S} {7,S}
5     O     0 {3,S} {8,S}
6     C     0 {1,S}
7     O     0 {4,S}
8     O     1 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.52e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 973,
    reactant1 = 
"""
C4H8OOH1-2O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S} {6,S}
4     O     0 {1,S} {7,S}
5     O     0 {2,S} {8,S}
6     C     0 {3,S}
7     O     1 {4,S}
8     O     0 {5,S}
""",
    product1 = 
"""
NC4KET12
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {6,D}
3     C     0 {1,S} {5,S}
4     O     0 {1,S} {7,S}
5     C     0 {3,S}
6     O     0 {2,D}
7     O     0 {4,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"s^-1"),
        n = 0,
        Ea = (26400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 974,
    reactant1 = 
"""
C4H8OOH1-3O2
1     C     0 {2,S} {4,S} {6,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {5,S}
4     O     0 {1,S} {7,S}
5     O     0 {3,S} {8,S}
6     C     0 {1,S}
7     O     1 {4,S}
8     O     0 {5,S}
""",
    product1 = 
"""
NC4KET13
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {6,S}
4     C     0 {2,S} {7,D}
5     C     0 {1,S}
6     O     0 {3,S}
7     O     0 {4,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+10,"s^-1"),
        n = 0,
        Ea = (21400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 975,
    reactant1 = 
"""
C4H8OOH1-4O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     O     0 {3,S} {7,S}
6     O     0 {4,S} {8,S}
7     O     0 {5,S}
8     O     1 {6,S}
""",
    product1 = 
"""
NC4KET14
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,D}
5     O     0 {3,S} {7,S}
6     O     0 {4,D}
7     O     0 {5,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.125e+09,"s^-1"),
        n = 0,
        Ea = (19350,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 976,
    reactant1 = 
"""
C4H8OOH2-1O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S} {6,S}
4     O     0 {1,S} {7,S}
5     O     0 {2,S} {8,S}
6     C     0 {3,S}
7     O     0 {4,S}
8     O     1 {5,S}
""",
    product1 = 
"""
NC4KET21
1     C     0 {2,S} {3,S} {5,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {6,S}
4     O     0 {2,S} {7,S}
5     O     0 {1,D}
6     C     0 {3,S}
7     O     0 {4,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"s^-1"),
        n = 0,
        Ea = (23850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 977,
    reactant1 = 
"""
C4H8OOH2-3O2
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S} {6,S}
3     O     0 {1,S} {7,S}
4     O     0 {2,S} {8,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     O     0 {3,S}
8     O     1 {4,S}
""",
    product1 = 
"""
NC4KET23
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S} {6,D}
3     O     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {2,D}
7     O     0 {3,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"s^-1"),
        n = 0,
        Ea = (23850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 978,
    reactant1 = 
"""
C4H8OOH2-4O2
1     C     0 {2,S} {4,S} {6,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {5,S}
4     O     0 {1,S} {7,S}
5     O     0 {3,S} {8,S}
6     C     0 {1,S}
7     O     0 {4,S}
8     O     1 {5,S}
""",
    product1 = 
"""
NC4KET24
1     C     0 {2,S} {5,S} {6,D}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S} {7,S}
5     C     0 {1,S}
6     O     0 {1,D}
7     O     0 {4,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25e+10,"s^-1"),
        n = 0,
        Ea = (17850,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 979,
    reactant1 = 
"""
NC4KET12
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {6,D}
3     C     0 {1,S} {5,S}
4     O     0 {1,S} {7,S}
5     C     0 {3,S}
6     O     0 {2,D}
7     O     0 {4,S}
""",
    product1 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+16,"s^-1"),
        n = 0,
        Ea = (41600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 980,
    reactant1 = 
"""
NC4KET13
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {6,S}
4     C     0 {2,S} {7,D}
5     C     0 {1,S}
6     O     0 {3,S}
7     O     0 {4,D}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+16,"s^-1"),
        n = 0,
        Ea = (41600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 981,
    reactant1 = 
"""
NC4KET14
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,D}
5     O     0 {3,S} {7,S}
6     O     0 {4,D}
7     O     0 {5,S}
""",
    product1 = 
"""
CH2CH2CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     1 {1,S}
4     O     0 {2,D}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+16,"s^-1"),
        n = 0,
        Ea = (42000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 982,
    reactant1 = 
"""
NC4KET21
1     C     0 {2,S} {3,S} {5,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {6,S}
4     O     0 {2,S} {7,S}
5     O     0 {1,D}
6     C     0 {3,S}
7     O     0 {4,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+16,"s^-1"),
        n = 0,
        Ea = (42000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 983,
    reactant1 = 
"""
NC4KET23
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S} {6,D}
3     O     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {2,D}
7     O     0 {3,S}
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+16,"s^-1"),
        n = 0,
        Ea = (41600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 984,
    reactant1 = 
"""
NC4KET24
1     C     0 {2,S} {5,S} {6,D}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S} {7,S}
5     C     0 {1,S}
6     O     0 {1,D}
7     O     0 {4,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH3COCH2
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     C     0 {1,S}
4     C     1 {1,S}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+16,"s^-1"),
        n = 0,
        Ea = (42000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 985,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2CH2COCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     1 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.55e+09,"cm^3/(mol*s)"),
        n = 0.97,
        Ea = (1586,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 986,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.45e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-228,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 987,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C2H5COCH2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1192,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 988,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2CH2COCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     1 {2,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23800,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (16490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 989,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8698,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 990,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C2H5COCH2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23800,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (14690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 991,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2CH2COCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     1 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.25e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 992,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.07e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 993,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H5COCH2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5962,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 994,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2CH2COCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     1 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.16e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (7700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 995,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.46e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (3200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 996,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H5COCH2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6357,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 997,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2CH2COCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     1 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (51310,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 998,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.55e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (41970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 999,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H5COCH2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (49150,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1000,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2CH2COCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     1 {2,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31.9,"cm^3/(mol*s)"),
        n = 3.17,
        Ea = (7172,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1001,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74,"cm^3/(mol*s)"),
        n = 3.46,
        Ea = (3680,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1002,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C2H5COCH2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.62e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9630,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1003,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2CH2COCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     1 {2,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1004,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2771,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1005,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C2H5COCH2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4660,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1006,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2CH2COCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     1 {2,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19380,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1007,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15250,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1008,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C2H5COCH2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17580,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1009,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
CH2CH2COCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     1 {2,S}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1010,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1011,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C2H5COCH2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.15e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4278,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1012,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH2CH2COCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     1 {2,S}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1013,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1014,
    reactant1 = 
"""
C2H5COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
C2H5COCH2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1015,
    reactant1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3CHOOCOCH3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S} {6,D}
3     O     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {2,D}
7     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1016,
    reactant1 = 
"""
CH3CHOOCOCH3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S} {6,D}
3     O     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {2,D}
7     O     1 {3,S}
""",
    product1 = 
"""
CH2CHOOHCOCH3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S} {6,D}
3     O     0 {1,S} {7,S}
4     C     1 {1,S}
5     C     0 {2,S}
6     O     0 {2,D}
7     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.9e+12,"s^-1"),
        n = 0,
        Ea = (29700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1017,
    reactant1 = 
"""
C2H3COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,D}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2CHOOHCOCH3
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S} {6,D}
3     O     0 {1,S} {7,S}
4     C     1 {1,S}
5     C     0 {2,S}
6     O     0 {2,D}
7     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1018,
    reactant1 = 
"""
CH2CH2CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     1 {1,S}
4     O     0 {2,D}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.127e+13,"s^-1"),
        n = -0.52,
        Ea = (24590,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1019,
    reactant1 = 
"""
CH2CH2COCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     1 {2,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (18000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1020,
    reactant1 = 
"""
C2H5COCH2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,D}
4     C     1 {1,S}
5     C     0 {2,S}
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (35000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1021,
    reactant1 = 
"""
C2H3COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,D}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1022,
    reactant1 = 
"""
CH3CHCO
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH3CHCOCH3
1     C     0 {2,S} {3,S} {4,D}
2     C     1 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.23e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1023,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
NC3H7CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (37560,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1024,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
NC3H7CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+06,"cm^3/(mol*s)"),
        n = 1.8,
        Ea = (-1300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1025,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
NC3H7CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.14e+09,"cm^3/(mol*s)"),
        n = 1.12,
        Ea = (2320,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1026,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
NC3H7CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.94e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1868,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1027,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
NC3H7CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40900,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (10200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1028,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
NC3H7CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00289,"cm^3/(mol*s)"),
        n = 4.62,
        Ea = (3210,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1029,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
NC3H7CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1030,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
NC3H7CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40900,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (10200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1031,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H6CHO-1
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     1 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.28e+09,"cm^3/(mol*s)"),
        n = 0.97,
        Ea = (1586,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1032,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H6CHO-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.68e+07,"cm^3/(mol*s)"),
        n = 1.61,
        Ea = (-35,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1033,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H6CHO-3
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (552,"cm^3/(mol*s)"),
        n = 3.12,
        Ea = (-1176,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1034,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H6CHO-1
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     1 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23790,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (16490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1035,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H6CHO-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9640,"cm^3/(mol*s)"),
        n = 2.6,
        Ea = (13910,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1036,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
C3H6CHO-3
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.44e+12,"cm^3/(mol*s)"),
        n = 0.05,
        Ea = (17880,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1037,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C3H6CHO-1
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     1 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23790,"cm^3/(mol*s)"),
        n = 2.55,
        Ea = (16490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1038,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C3H6CHO-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9640,"cm^3/(mol*s)"),
        n = 2.6,
        Ea = (13910,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1039,
    reactant1 = 
"""
NC3H7CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
C3H6CHO-3
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.44e+12,"cm^3/(mol*s)"),
        n = 0.05,
        Ea = (17880,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1040,
    reactant1 = 
"""
NC3H7CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     1 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"s^-1"),
        n = 0,
        Ea = (9600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1041,
    reactant1 = 
"""
C3H6CHO-1
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     1 {2,S}
5     O     0 {3,D}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.4e+11,"s^-1"),
        n = 0,
        Ea = (21970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1042,
    reactant1 = 
"""
C2H5CHCO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H6CHO-3
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1043,
    reactant1 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C3H6CHO-3
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.23e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1044,
    reactant1 = 
"""
SC3H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C3H6CHO-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1045,
    reactant1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
C3H6CHO-2
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1046,
    reactant1 = 
"""
C2H5CHCO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.73e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1010,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1047,
    reactant1 = 
"""
C2H5CHCO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1459,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1048,
    reactant1 = 
"""
C2H5CHCO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D} {5,D}
4     C     0 {2,S}
5     O     0 {3,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-437,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1049,
    reactant1 = 
"""
SC3H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
SC3H5CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     1 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10,"cm^3/(mol*s)"),
        n = 0.76,
        Ea = (-340,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1050,
    reactant1 = 
"""
SC3H5CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     1 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    product1 = 
"""
C3H5-S
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     C     1 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.6e+15,"s^-1"),
        n = 0,
        Ea = (23000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1051,
    reactant1 = 
"""
SC3H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
SC3H5CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     1 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1052,
    reactant1 = 
"""
SC3H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
SC3H5CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     1 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1053,
    reactant1 = 
"""
SC3H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
SC3H5CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     1 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.18e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1389,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1054,
    reactant1 = 
"""
SC3H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
SC3H5CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     1 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (37600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1055,
    reactant1 = 
"""
SC3H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
SC3H5CO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     1 {1,S} {5,D}
4     C     0 {2,D}
5     O     0 {3,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1056,
    reactant1 = 
"""
C2H3COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,D}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1057,
    reactant1 = 
"""
C2H3COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,D}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1192,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1058,
    reactant1 = 
"""
C2H3COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,D}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7949,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1059,
    reactant1 = 
"""
C2H3COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,D}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,D}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1060,
    reactant1 = 
"""
C2H3COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,D}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,D}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2CHO
1     C     0 {2,S} {3,D}
2     C     1 {1,S}
3     O     0 {1,D}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    product3 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.97e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17050,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1061,
    reactant1 = 
"""
C2H3COCH3
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,D}
3     O     0 {1,D}
4     C     0 {1,S}
5     C     0 {2,D}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D} {3,D}
2     C     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product3 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17580,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1062,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+98,"s^-1"),
        n = -23.81,
        Ea = (145300,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1063,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.85e+95,"s^-1"),
        n = -23.11,
        Ea = (147600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1064,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+06,"cm^3/(mol*s)"),
        n = 2.54,
        Ea = (6756,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1065,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (602000,"cm^3/(mol*s)"),
        n = 2.4,
        Ea = (2583,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1066,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.36,"cm^3/(mol*s)"),
        n = 3.65,
        Ea = (7154,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1067,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.904,"cm^3/(mol*s)"),
        n = 3.46,
        Ea = (4598,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1068,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.73e+10,"cm^3/(mol*s)"),
        n = 0.51,
        Ea = (63,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1069,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.29e+08,"cm^3/(mol*s)"),
        n = 1.53,
        Ea = (776,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1070,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1071,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1072,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (121500,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (16690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1073,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (12260,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1074,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (196800,"cm^3/(mol*s)"),
        n = 2.4,
        Ea = (1150,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1075,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.046e+07,"cm^3/(mol*s)"),
        n = 2.03,
        Ea = (5136,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1076,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1077,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1078,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (46000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1079,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.04e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (41350,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1080,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (121500,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (16690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1081,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.55e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1082,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.55e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1083,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.55e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1084,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.55e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1085,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.55e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1086,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.55e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1087,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     1 {2,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
HO2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1088,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     1 {2,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
HO2CHO
1     C     0 {2,S} {3,D}
2     O     0 {1,S} {4,S}
3     O     0 {1,D}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16010,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1089,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.25e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1090,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1091,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.25e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1092,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1093,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (12260,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1094,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
C2H5O2H
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1095,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
CH3CO3H
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1096,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1097,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1098,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1099,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1100,
    reactant1 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
IC4H10
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1101,
    reactant1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1102,
    reactant1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1103,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1104,
    reactant1 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    reactant2 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1105,
    reactant1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
IC4H8
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.98e+32,"s^-1"),
        n = -6.23,
        Ea = (40070,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1106,
    reactant1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.64e+37,"s^-1"),
        n = -7.4,
        Ea = (38670,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1107,
    reactant1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
IC4H8
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.65e+46,"s^-1"),
        n = -9.83,
        Ea = (55080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1108,
    reactant1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
IC4H8
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e-18,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1109,
    reactant1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
IC4H8
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e-18,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1110,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1111,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1112,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
IC4H7
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     1 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product2 = 
"""
IC4H7O
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,D}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1113,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1114,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1115,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1116,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1117,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
IC4H7
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     1 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product2 = 
"""
IC4H7O
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,D}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1118,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
IC4H7
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     1 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product2 = 
"""
IC4H7O
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,D}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1119,
    reactant1 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.26e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1120,
    reactant1 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1121,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1122,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1123,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1124,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1125,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1126,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1127,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
IC4H7
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     1 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product2 = 
"""
IC4H7O
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,D}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1128,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1129,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C3H6
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1130,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
IC4H8
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
IC4H7
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     1 {1,S}
4     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1131,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
IC4H8
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
IC4H7
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     1 {1,S}
4     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1132,
    reactant1 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    reactant2 = 
"""
IC4H8
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
PC4H9O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     0 {4,S}
""",
    product2 = 
"""
IC4H7
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     1 {1,S}
4     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1133,
    reactant1 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
IC4H8
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
SC4H9O2H
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     0 {3,S}
""",
    product2 = 
"""
IC4H7
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     1 {1,S}
4     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1134,
    reactant1 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    reactant2 = 
"""
IC4H8
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
IC3H7O2H
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {2,S}
""",
    product2 = 
"""
IC4H7
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     1 {1,S}
4     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1135,
    reactant1 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    reactant2 = 
"""
IC4H8
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
NC3H7O2H
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     0 {3,S}
""",
    product2 = 
"""
IC4H7
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     1 {1,S}
4     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1136,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1137,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C4H8-1
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1138,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1139,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C4H8-2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1140,
    reactant1 = 
"""
CC4H8O
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     O     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1141,
    reactant1 = 
"""
CC4H8O
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     O     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.51e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (5000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1142,
    reactant1 = 
"""
CC4H8O
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     O     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.124e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1143,
    reactant1 = 
"""
CC4H8O
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     O     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1144,
    reactant1 = 
"""
CC4H8O
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     O     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
CH3O2H
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1145,
    reactant1 = 
"""
CC4H8O
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     O     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product3 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1146,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    product1 = 
"""
C2H3
1     C     1 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17110,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1147,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
CH4
1     C     0
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1148,
    reactant1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    reactant2 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (26030,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1149,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1150,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (17000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1151,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1152,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19360,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1153,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
PC2H4OH
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19360,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1154,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
SC2H4OH
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1155,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1156,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S}
3     O     0 {1,D}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
CH3CO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1157,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1158,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C2H3CHO
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
C2H3CO
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,D}
3     C     0 {1,D}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1159,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1160,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C2H5CHO
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
C2H5CO
1     C     0 {2,S} {3,S}
2     C     1 {1,S} {4,D}
3     C     0 {1,S}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1161,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3275,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1162,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3275,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1163,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1164,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1165,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
IC4H9O2H
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {3,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1166,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
TC4H9O2H
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     0 {2,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1167,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1168,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
CH3O2
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product1 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1169,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1170,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
C2H5O2
1     C     0 {2,S} {3,S}
2     O     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product1 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1171,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
CH3CO2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S}
3     O     0 {1,D}
4     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1172,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
CH3CO3
1     C     0 {2,S} {3,S} {4,D}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     0 {1,D}
5     O     1 {2,S}
""",
    product1 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product2 = 
"""
CH3CO2
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S}
3     O     0 {1,D}
4     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1173,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product3 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1174,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1175,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product3 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1176,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1177,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
PC4H9O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     O     0 {2,S} {6,S}
5     C     0 {3,S}
6     O     1 {4,S}
""",
    product1 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product2 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1178,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1179,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
SC4H9O2
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     O     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     O     1 {3,S}
""",
    product1 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product2 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1180,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1181,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
NC3H7O2
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     O     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    product1 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1182,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1183,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
IC3H7O2
1     C     0 {2,S} {3,S} {4,S}
2     O     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product1 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product2 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1184,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1185,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16,"cm^3/(mol*s)"),
        n = -1.61,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1186,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1187,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
C2H5O
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1188,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
IC3H7
1     C     1 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
IC3H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1189,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
NC3H7
1     C     0 {2,S} {3,S}
2     C     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
NC3H7O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1190,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
PC4H9
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
PC4H9O
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1191,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
SC4H9
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
SC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1192,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
IC4H9
1     C     0 {2,S} {3,S} {4,S}
2     C     1 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1193,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
TC4H9
1     C     1 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1194,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C3H5-A
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     1 {1,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
C3H5O
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,S}
3     C     0 {1,D}
4     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1195,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
C4H71-3
1     C     0 {2,S} {3,D}
2     C     1 {1,S} {4,S}
3     C     0 {1,D}
4     C     0 {2,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
C4H7O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,D}
3     C     0 {1,S}
4     O     1 {1,S}
5     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1196,
    reactant1 = 
"""
IC4H9O2
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {3,S}
""",
    reactant2 = 
"""
IC4H7
1     C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3     C     1 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
IC4H9O
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    product2 = 
"""
IC4H7O
1     C     0 {2,S} {3,D} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,D}
4     C     0 {1,S}
5     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1197,
    reactant1 = 
"""
TC4H9O2
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     O     1 {2,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
TC4H9O
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     1 {1,S}
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
)