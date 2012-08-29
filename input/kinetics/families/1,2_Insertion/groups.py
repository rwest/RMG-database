#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["CO_birad", "RR'"], products=["R_CO_R'"], ownReverse=False)

reverse = "1,1_Elimination"

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['LOSE_RADICAL', '*1', '2'],
])

entry(
    index = 1,
    label = "CO_birad",
    group = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    kinetics = Arrhenius(
        A = (0.081856,"m^3/(mol*s)"),
        n = 2.39,
        Ea = (341916,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "RR'",
    group = "OR{R_H, R_R'}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "R_H",
    group = 
"""
1 *2 {H,Cs,Cd,Cb,O,Sis,Sid} 0 {2,S}
2 *3 H                      0 {1,S}
""",
    kinetics = Arrhenius(
        A = (2.2347,"m^3/(mol*s)"),
        n = -0.085,
        Ea = (-14685.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "H2",
    group = 
"""
1 *2 H 0 {2,S}
2 *3 H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (35305.9,"m^3/(mol*s)"),
        n = -1.23,
        Ea = (1589.92,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "RO_H",
    group = 
"""
1 *2 O 0 {2,S} {3,S}
2 *3 H 0 {1,S}
3    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.5515e-06,"m^3/(mol*s)"),
        n = 1.31,
        Ea = (-118658,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "CsO_H",
    group = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 H  0 {1,S}
3    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.5515e-06,"m^3/(mol*s)"),
        n = 1.31,
        Ea = (-118658,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "Cd_H",
    group = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 H 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "Cd_pri",
    group = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "Cd_sec",
    group = 
"""
1 *2 C   0 {2,D} {3,S} {4,S}
2    C   0 {1,D}
3 *3 H   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "Cd/H/NonDeC",
    group = 
"""
1 *2 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *3 H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "Cd/H/NonDeO",
    group = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 H 0 {1,S}
4    O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "Cd/H/OneDe",
    group = 
"""
1 *2 C             0 {2,D} {3,S} {4,S}
2    C             0 {1,D}
3 *3 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "Cb_H",
    group = 
"""
1 *2 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *3 H        0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "Cs_H",
    group = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 H 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
5    R 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (6.90525,"m^3/(mol*s)"),
        n = -0.1475,
        Ea = (7238.32,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 15,
    label = "C_methane",
    group = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.200352,"m^3/(mol*s)"),
        n = 0.47,
        Ea = (21673.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 16,
    label = "C_pri",
    group = 
"""
1 *2 C   0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   0 {1,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.11659,"m^3/(mol*s)"),
        n = 0.14,
        Ea = (15815.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 17,
    label = "C_pri/NonDeC",
    group = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1.11659,"m^3/(mol*s)"),
        n = 0.14,
        Ea = (15815.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 18,
    label = "C_pri/NonDeO",
    group = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "C_pri/De",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "C_sec",
    group = 
"""
1 *2 C   0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (9.3579,"m^3/(mol*s)"),
        n = -0.32,
        Ea = (2008.32,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 21,
    label = "C/H2/NonDeC",
    group = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (9.3579,"m^3/(mol*s)"),
        n = -0.32,
        Ea = (2008.32,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 22,
    label = "C/H2/NonDeO",
    group = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 H      0 {1,S}
3    H      0 {1,S}
4    O      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "C/H2/CsO",
    group = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  0 {1,S}
3    H  0 {1,S}
4    O  0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "C/H2/O2",
    group = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
5    O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "C/H2/OneDe",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "C/H2/OneDeC",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    Cs            0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "C/H2/OneDeO",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    O             0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "C/H2/TwoDe",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    {Cd,Ct,CO,Cb} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "C_ter",
    group = 
"""
1 *2 C   0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1086.05,"m^3/(mol*s)"),
        n = -0.88,
        Ea = (-10543.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 30,
    label = "C/H/NonDeC",
    group = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 H      0 {1,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1086.05,"m^3/(mol*s)"),
        n = -0.88,
        Ea = (-10543.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "C/H/Cs3",
    group = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = Arrhenius(
        A = (1086.05,"m^3/(mol*s)"),
        n = -0.88,
        Ea = (-10543.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 32,
    label = "C/H/NDMustO",
    group = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 H      0 {1,S}
3    O      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "C/H/OneDe",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "C/H/Cs2",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
5    Cs            0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "C/H/ODMustO",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    O             0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "C/H/TwoDe",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "C/H/Cs",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Cs            0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "C/H/TDMustO",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    O             0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "C/H/ThreeDe",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "R_R'",
    group = 
"""
1 *2 {Cs,Sis}           0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,Cb,Sis,Sid} 0 {1,S}
3    H                  0 {1,S}
4    H                  0 {1,S}
5    H                  0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.00657252,"m^3/(mol*s)"),
        n = 0.9,
        Ea = (95311.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 41,
    label = "Cs_Cs",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = Arrhenius(
        A = (0.00657252,"m^3/(mol*s)"),
        n = 0.9,
        Ea = (95311.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 42,
    label = "C_methyl_C_methyl",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs 0 {1,S} {6,S} {7,S} {8,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    H  0 {2,S}
7    H  0 {2,S}
8    H  0 {2,S}
""",
    kinetics = Arrhenius(
        A = (0.00657252,"m^3/(mol*s)"),
        n = 0.9,
        Ea = (95311.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
        ("Wed Aug 29 13:42:10 2012","Sean Troiano <stroiano7@gmail.com>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 43,
    label = "C_methyl_C_pri",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs 0 {1,S} {6,S} {7,S} {8,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    H  0 {2,S}
7    H  0 {2,S}
8    C  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "C_methyl_C_sec",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs 0 {1,S} {6,S} {7,S} {8,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    H  0 {2,S}
7    C  0 {2,S}
8    C  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "C_methyl_C_ter",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs 0 {1,S} {6,S} {7,S} {8,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    C  0 {2,S}
7    C  0 {2,S}
8    C  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "Cs_Cd",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "C_methyl_Cd_pri",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd 0 {1,S} {6,S} {7,D}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    H  0 {2,S}
7    C  0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "C_methyl_Cd_sec",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd 0 {1,S} {6,S} {7,D}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    C  0 {2,S}
7    C  0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "Cs_Cb",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cb 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

tree(
"""
L1: CO_birad
L1: RR'
    L2: R_H
        L3: H2
        L3: RO_H
            L4: CsO_H
        L3: Cd_H
            L4: Cd_pri
            L4: Cd_sec
                L5: Cd/H/NonDeC
                L5: Cd/H/NonDeO
                L5: Cd/H/OneDe
        L3: Cb_H
        L3: Cs_H
            L4: C_methane
            L4: C_pri
                L5: C_pri/NonDeC
                L5: C_pri/NonDeO
                L5: C_pri/De
            L4: C_sec
                L5: C/H2/NonDeC
                L5: C/H2/NonDeO
                    L6: C/H2/CsO
                    L6: C/H2/O2
                L5: C/H2/OneDe
                    L6: C/H2/OneDeC
                    L6: C/H2/OneDeO
                L5: C/H2/TwoDe
            L4: C_ter
                L5: C/H/NonDeC
                    L6: C/H/Cs3
                    L6: C/H/NDMustO
                L5: C/H/OneDe
                    L6: C/H/Cs2
                    L6: C/H/ODMustO
                L5: C/H/TwoDe
                    L6: C/H/Cs
                    L6: C/H/TDMustO
                L5: C/H/ThreeDe
    L2: R_R'
        L3: Cs_Cs
            L4: C_methyl_C_methyl
            L4: C_methyl_C_pri
            L4: C_methyl_C_sec
            L4: C_methyl_C_ter
        L3: Cs_Cd
            L4: C_methyl_Cd_pri
            L4: C_methyl_Cd_sec
        L3: Cs_Cb
"""
)

