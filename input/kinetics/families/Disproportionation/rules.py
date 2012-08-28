#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 485,
    label = "Y_rad_birad;XH_Rrad",
    group1 = "OR{Y_1centerbirad, Y_rad}",
    group2 = 
"""
1 *2 R!H 0 {2,S} {3,S}
2 *3 R!H 1 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3e+11,"cm^3/(mol*s)"),
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
    index = 487,
    label = "O2_birad;Cmethyl_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.23e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (15.99,"kcal/mol"),
        Tmin = (700,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""[AJ] Miyoshi 2011 (Table 4, Node 'sp') dx.doi.org/10.1021/jp112152n""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review: i-C3H7 + O2 = HO2 + C3H6

pg. 931-932: Discussion on evaluated data

Entry 42,3 (a): Author appears to be skeptical of the only experimentally reported

value.  Author notes that more recent work on C2H5+O2 suggested that the
addition and disproportionation rxns may be coupled through a common intermediate.
For the time being, the author decided to recommend the only experimentally
reported rate coefficient, only for temperatures above 700K, as they note the
addition rxn should be the predominant rxn at lower temperatures.
MRH 30-Aug-2009

Divide the rate constant by 12 to account for symmetry of 2 (O2) and 6 (i-C3H7, carbons #1 and 3).  The final result is 1.05833e+10 cm3/mol/s.
JDM 31-Mar-2010
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 488,
    label = "CH2_triplet;Cmethyl_Csrad",
    group1 = 
"""
1 *1 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    group2 = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.01e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] Literature review.""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review.  CH2(triplet) + i-C3H7 --> C3H6 + CH3

pg. 944: Discussion on evaluated data

Entry 42,26: No data available at the time.  Author suggests this is a minor channel,

stating the main process should be combination, leading to chemically activated
i-butyl radical.  Rate coefficient is estimate.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 501,
    label = "O2_birad;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.5825e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (14.85,"kcal/mol"),
        Tmin = (500,"K"),
        Tmax = (900,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""[AJ] Miyoshi 2011 (Table 4, Node 'ss') dx.doi.org/10.1021/jp112152n""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review: n-C3H7 + O2 = HO2 + C3H6

pg. 914-915: Discussion on evaluated data

Entry 41,3 (a): The author suggests a rate coefficient based on those reported in the

literature.  The author notes that the data reported in the literature suggests
the formation of C3H6 is controlled by the addition rxn.  The author further
notes that it is surprising that p-dependence effects are not observed for
C3H6 formation.
MRH 30-Aug-2009

Divide the rate constant by 4 to account for symmetry of 2 (O2) and 2 (n-C3H7, carbon #2).  The final result is 2.25825e+10 cm3/mol/s.
JDM 31-Mar-2010
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 502,
    label = "CH2_triplet;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.81e+12,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] Literature review.""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review.  CH2_triplet + n-C3H7 --> C3H6 + CH3

pg. 925: Discussion on evaluated data

Entry 41,26: No data available at the time.  Author estimates the rate coefficient

expression of the addition rxn.  The author then recommends that the disproportionation
rate coefficient not exceed 10% of the combination rate.  Thus, the rate coefficient
is an upper limit.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 504,
    label = "C_methyl;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.15e+13,"cm^3/(mol*s)","*|/",1.7),
        n = -0.32,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] Literature review.""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review.  CH3 + n-C3H7 --> C3H6 + CH4

pg. 920: Discussion on evaluated data

Entry 41,16 (b): No direct measurements for either the addition or disproportionation

rxns.  Author recommends a rate coefficient expression for the addition rxn, based
on the geometric mean rule of the rxns CH3+CH3=>adduct and n-C3H7+n-C3H7=>adduct.
Furthermore, author recommends a branching ratio for disproportionation to
addition of 0.06 (which appears to MRH to be consistent with the experimentally
measured branching ratios)
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 505,
    label = "C_rad/H2/Cs;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.45e+12,"cm^3/(mol*s)","*|/",1.4),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] Literature review.""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review.  C2H5 + n-C3H7 --> C3H6 + C2H6

pg. 937-938: Discussion on evaluated data

Entry 42,17 (b): No direct measurements for either the addition or disproportionation

rxns.  Author recommends a rate coefficient expression for the addition rxn, based
on the geometric mean rule of the rxns C2H5+C2H5=>adduct and n-C3H7+n-C3H7=>adduct.
Furthermore, author recommends a branching ratio for disproportionation to
addition of 0.073 (which is an average of the 2 experimentally determined
branching ratios)
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 506,
    label = "C_rad/H2/Cd;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.45e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (-0.13,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: C3H5 + nC3H7 --> C3H6 + C3H6

pg.268: Discussion on evaluated data

Entry 47,41(a): No data available at the time.  Recommended rate coefficient expression

based on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.) and values
for "alkyl radicals" (Gibian M.J. and Corley R.C.); this leads to disproportionation-
to-addition ratio of 0.07.  The addition rate expression was derived using the geometric
mean rule for the rxns C3H5+C3H5-->adduct and nC3H7+nC3H7-->adduct.
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 507,
    label = "C_rad/H2/O;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.82e+11,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] Literature review.""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review.  CH2OH + n-C3H7 --> C3H6 + CH3OH

pg. 926: Discussion on evaluated data

Entry 41,39 (c): No data available at the time.  Author estimates the rate coefficient

for the addition rxn to be similar to the rate for n-C3H7+n-C3H7=>adduct.  Author
also estimates the branching ratio of disproportionation to addition as 0.051
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 508,
    label = "C_rad/H/NonDeC;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.13e+13,"cm^3/(mol*s)","*|/",2),
        n = -0.35,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] Literature review.""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review.  i-C3H7 + n-C3H7 --> C3H6 + C3H8

pg. 945-946: Discussion on evaluated data

Entry 42,41 (b): No data available at the time.  Author estimates the rate coefficient

expression of the addition rxn using the rate for i-C3H7+i-C3H7=>adduct, the rate
for n-C3H7+n-C3H7=>adduct, and the geometric mean rule.  The author recommends
the branching ratio of disproportionation to addition reported by Gibian and
Corley (1973).
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 509,
    label = "C_rad/Cs3;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.16e+14,"cm^3/(mol*s)","*|/",2),
        n = -0.75,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: t-C4H9 + n-C3H7 --> C3H6 + i-C4H10

pg. 45: Discussion on evaluated data

Entry 44,41 (a): No data available at the time.  Author estimates the rate expression

for the combination rxn using the geometric mean rule (of the rxns t-C4H9+t-C4H9-->adduct
and n-C3H7+n-C3H7-->adduct).  The author then estimates the disproportionation
rate expression using the branching ratio; the branching ratio is from "analogous
processes".
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 510,
    label = "Cd_pri_rad;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.21e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] Literature review.""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review.  C2H3 + n-C3H7 --> C3H6 + C2H4

pg. 922: Discussion on evaluated data

Entry 41,19 (a): No data available at the time.  Author estimates the rate coefficient

based on the rxn C2H5+n-C3H7=C3H6=C2H6.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 511,
    label = "Ct_rad;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 C 1 {2,T}
2    C 0 {1,T}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.03e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] Literature review.""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review.  C2H + n-C3H7 --> C3H6 + C2H2

pg. 923: Discussion on evaluated data

Entry 41,21 (a): No data available at the time.  Author notes that the rxn is more exothermic

than the rxn CH3+n-C3H7=C3H6+CH4 and suggests a rate coefficient 3x larger,
namely 1.0x10^-11 cm3/molecule/s.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 512,
    label = "O_pri_rad;C/H2/Nd_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    H 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.41e+13,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] Literature review.""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review.  OH + n-C3H7 --> C3H6 + H2O

pg. 917: Discussion on evaluated data

Entry 41,6 (a): No data available at the time.  Author estimates rate coefficient based

on the rate coefficient for OH+C2H5=C2H4+H2O, namely 4.0x10^-11 cm3/molecule/s.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 513,
    label = "O2_birad;C/H/NdNd_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.2044e+10,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (600,"K"),
        Tmax = (1000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: O2 + iC4H9 --> iC4H8 + HO2

pg. 52-53: Discussion on evaluated data

Entry 45,3 (a): The author recommends a rate coefficient based on the experiments performed

by Baker et al. (yielding a disproportionation-to-decomposition ratio) and the
current (Tsang) study's recommended iC4H9 unimolecular decomposition rate.
MRH 31-Aug-2009

Divide the rate constant by 2 to account for symmetry of 2 (O2) and 1 (i-C4H9, carbon #2).  The final result is 1.2044e+10 cm3/mol/s.
JDM 31-Mar-2010
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 514,
    label = "Ct_rad;C/H/NdNd_Csrad",
    group1 = 
"""
1 *1 C 1 {2,T}
2    C 0 {1,T}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.03e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: C2H + i-C4H9 --> i-C4H8 + C2H2

pg. 61: Discussion on evaluated data

Entry 45,21: No data available at the time.  The author estimates the rate of 

disproportionation to be 1x10^-11 cm3/molecule/s.
*** NOTE: RMG_database previously had CH2_triplet as Y_rad_birad node, not Ct_rad ***

MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 515,
    label = "H_rad;C/H/NdNd_Csrad",
    group1 = 
"""
1 *1 H 1
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.04e+11,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: H + i-C4H9 --> i-C4H8 + H2

pg. 53: Discussion on evaluated data

Entry 45,4 (c): No data available at the time.  The author estimates the disproportionation

rate coefficent as half the rate of H+n-C3H7=C3H6+H2 (due to the presence of 2
H-atoms on the alpha-carbon in n-C3H7 and only 1 on the alpha-carbon of i-C4H9).
The author also states that the branching ratio is pressure-dependent and supplies
fall-off tables and collisional efficiencies.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 516,
    label = "C_methyl;C/H/NdNd_Csrad",
    group1 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.02e+12,"cm^3/(mol*s)","*|/",2),
        n = -0.32,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: CH3 + i-C4H9 --> i-C4H8 + CH4

pg. 58: Discussion on evaluated data

Entry 45,16 (b): No data available at the time.  The author estimates the disproportionation

rate coefficient as half the rate of CH3+n-C3H7=C3H6+H2 (due to half as many H-atoms
on the alpha-carbon).
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 517,
    label = "C_rad/H2/Cs;C/H/NdNd_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.43e+11,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: C2H5 + i-C4H9 --> i-C4H8 + C2H6

pg. 59: Discussion on evaluated data

Entry 45,17 (a): No direct measurements of either the addition or disproportionation rxns.

The combination rate coefficient was computed using the geometric mean rule (of the
rxns C2H5+C2H5-->adduct and i-C4H9+i-C4H9-->adduct).  The disproportionation rate
coefficient was computed using the disproportionation-to-combination ratio reported
by Gibian and Corley (1973).
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 518,
    label = "C_rad/H2/O;C/H/NdNd_Csrad",
    group1 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.41e+11,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: CH2OH + i-C4H9 --> i-C4H8 + CH3OH

pg. 64: Discussion on evaluated data

Entry 45,39 (c): No data available at the time.  Author estimates the disproportionation rate

coefficient as half the rate of CH2OH+n-C3H7=C3H6+CH3OH (due to half as many H-atoms
on the alpha-carbon).
*** NOTE: Although author states the the rate coefficient of CH2OH+i-C4H9=i-C4H8+CH3OH

is half that of CH2OH+n-C3H7=C3H6+CH3OH, MRH finds them to be equal, both in the electronic
references and the online NIST database (kinetics.nist.gov).  I am therefore
cutting the A in the RMG_database in two. ***
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 519,
    label = "C_rad/H2/Cd;C/H/NdNd_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.83e+11,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (-0.13,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: C3H5 + iC4H9 --> iC4H8 + C3H6

pg.270: Discussion on evaluated data

Entry 47,45(a): No data available at the time.  Recommended rate coefficient expression

based on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.); this leads to disproportionation-
to-addition ratio of 0.04.  The addition rate expression was derived using the geometric
mean rule for the rxns C3H5+C3H5-->adduct and iC4H9+iC4H9-->adduct.
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 520,
    label = "C_rad/H/NonDeC;C/H/NdNd_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.56e+13,"cm^3/(mol*s)","*|/",2),
        n = -0.35,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: i-C3H7 + i-C4H9 --> i-C4H8 + C3H8

pg. 65: Discussion on evaluated data

Entry 45,42 (b): No data available at the time.  Author estimates the disproportionation rate

coefficient as half the rate of i-C3H7+n-C3H7=C3H6+C3H8 (due to half as many H-atoms
on the alpha-carbon).
*** NOTE: MRH computes half the rate of i-C3H7+n-C3H7=C3H6+C3H8 as 0.52x10^-11 * (300/T)^0.35,

not 0.58x10^-11 * (300/T)^0.35.  However, there may be a reason for the relatively
small discrepancy between the author's stated and implemented calculation. ***
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 521,
    label = "C_rad/Cs3;C/H/NdNd_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.08e+14,"cm^3/(mol*s)","*|/",2),
        n = -0.75,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: t-C4H9 + i-C4H9 --> i-C4H8 + i-C4H10

pg. 66: Discussion on evaluated data

Entry 45,44 (b): No data available at the time.  Author estimates the disproportionation rate

coefficient as half the rate of t-C4H9+n-C3H7=C3H6+i-C4H10 (due to half as many H-atoms
on the alpha-carbon).
*** NOTE: Although author states the the rate coefficient of t-C4H9+i-C4H9=i-C4H8+i-C4H10

is half that of t-C4H9+n-C3H7=C3H6+i-C4H10, MRH finds them to be equal, both in the electronic
references and the online NIST database (kinetics.nist.gov).  I am therefore
cutting the A in the RMG_database in two. ***
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 522,
    label = "Cd_pri_rad;C/H/NdNd_Csrad",
    group1 = 
"""
1 *1 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.43e+11,"cm^3/(mol*s)","*|/",4),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: C2H3 + i-C4H9 --> i-C4H8 + C2H4

pg. 60: Discussion on evaluated data

Entry 45,19 (b): No data available at the time.  Author estimates the disproportionation rate

coefficient based on the rate of C2H5+i-C4H9=i-C4H8+C2H6.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 523,
    label = "O_pri_rad;C/H/NdNd_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    H 0 {1,S}
""",
    group2 = 
"""
1 *2 C      0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs     1 {1,S}
3 *4 H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.21e+13,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: OH + i-C4H9 --> i-C4H8 + H2O

pg. 55: Discussion on evaluated data

Entry 45,6 (a): No data available at the time.  Author estimates the disproportionation rate

coefficient as half the rate of OH+n-C3H7=C3H6+H2O (due to half as many H-atoms
on the alpha-carbon).
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 524,
    label = "O2_birad;Cdpri_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.022e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (13.55,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: O2 + C3H5 --> H2C=C=CH2 + HO2

pg.251: Discussion on evaluated data

*** UPPER LIMIT ***

Entry 47,3(b): The author states that there is uncertainty whether this rxn is appreciable

at high temperatures.  There were conflicting results published regarding the
significance above 461K (Morgan et al. and Slagle and Gutman).  The author thus
decides to place an upper limit on the rate coefficient of 2x10^-12 * exp(-6820/T)
cm3/molecule/s.  The author further notes that this upper limit assumes no
contribution from a complex rearrangement of the adduct.  Finally, the author
notes that this rxn should not be significant in combustion situations.
MRH 31-Aug-2009

Divide the rate constant by 2 to account for symmetry of 2 (O2) and 1 (allyl, carbon #2). The final result is 6.022e+11 cm3/mol/s, Ea = 13.55 kcal/mol.
JDM 31-Mar-2010
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 525,
    label = "H_rad;Cdpri_Csrad",
    group1 = 
"""
1 *1 H 1
""",
    group2 = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.81e+13,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: H + C3H5 --> H2C=C=CH2 + H2

pg.252: Discussion on evaluated data

Entry 47,4(c): No data available at the time.  Author assigns a rate coefficient of 

3x10^-11 cm3/molecule/s for the disproportionation rxn.
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 526,
    label = "C_methyl;Cdpri_Csrad",
    group1 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.01e+12,"cm^3/(mol*s)","*|/",3),
        n = -0.32,
        alpha = 0,
        E0 = (-0.13,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: CH3 + C3H5 --> H2C=C=CH2 + CH4

pg.257: Discussion on evaluated data

Entry 47,16(a): No data available at the time.  Recommended rate coefficient expression

based on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.); this leads to disproportionation-
to-addition ratio of 0.03.  The addition rate expression was derived using the geometric
mean rule for the rxns C3H5+C3H5-->adduct and CH3+CH3-->adduct.
NOTE: The Ea reported in the discussion is Ea/R=-132 Kelvin.  However, in the table near

the beginning of the review article (summarizing all reported data) and in the NIST
online database (kinetics.nist.gov), the reported Ea/R=-66 Kelvin.  MRH took the
geometric mean of the allyl combination rxn (1.70x10^-11 * exp(132/T)) and methyl
combination rxn (1.68x10^-9 * T^-0.64) to obtain 1.69x10^-11 * T^-0.32 * exp(66/T).
Multiplying by 0.03 results in the recommended rate coefficient expression.
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 527,
    label = "C_rad/H2/Cs;Cdpri_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.64e+11,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (-0.13,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: C2H5 + C3H5 --> H2C=C=CH2 + C2H6

pg.259: Discussion on evaluated data

Entry 47,17(a): The recommended rate expression is derived from the experimentally-

determined disproportionation-to-addition ratio of 0.047 (James and Troughton)
and the addition rate rule (C2H5+C3H5-->adduct) calculated using the geometric
mean rule of the rxns C2H5+C2H5-->adduct and C3H5+C3H5-->adduct.
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 528,
    label = "C_rad/H2/Cd;Cdpri_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.43e+10,"cm^3/(mol*s)","*|/",2.5),
        n = 0,
        alpha = 0,
        E0 = (-0.26,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: C3H5 + C3H5 --> H2C=C=CH2 + C3H6

pg.271-272: Discussion on evaluated data

Entry 47,47(b): The recommended rate expression is derived from the experimentally-

determined disproportionation-to-addition ratio of 0.008 (James and Kambanis)
and the addition rate rule (C3H5+C3H5-->adduct) calculated based on the results
of Tulloch et al.
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 529,
    label = "C_rad/H/NonDeC;Cdpri_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.58e+12,"cm^3/(mol*s)","*|/",3),
        n = -0.35,
        alpha = 0,
        E0 = (-0.13,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: iC3H7 + C3H5 --> H2C=C=CH2 + C3H8

pg.268: Discussion on evaluated data

Entry 47,42(b): No data available at the time.  Recommended rate coefficient expression

based on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.) and values
for "alkyl radicals" (Gibian M.J. and Corley R.C.); this leads to disproportionation-
to-addition ratio of 0.04.  The addition rate expression was derived using the geometric
mean rule for the rxns C3H5+C3H5-->adduct and iC3H7+iC3H7-->adduct.
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 530,
    label = "C_rad/Cs3;Cdpri_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.89e+13,"cm^3/(mol*s)","*|/",3),
        n = -0.75,
        alpha = 0,
        E0 = (-0.13,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: tC4H9 + C3H5 --> H2C=C=CH2 + iC4H10

pg.269: Discussion on evaluated data

Entry 47,44(b): No data available at the time.  Recommended rate coefficient expression

based on "allyl and alkyl radicals behaving in similar fashion" (possibly referencing
Gibian M.J. and Corley R.C.); this leads to disproportionation-
to-addition ratio of 0.04.  The addition rate expression was derived using the geometric
mean rule for the rxns C3H5+C3H5-->adduct and tC4H9+tC4H9-->adduct.
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 531,
    label = "Cd_pri_rad;Cdpri_Csrad",
    group1 = 
"""
1 *1 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.41e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: C2H3 + C3H5 --> H2C=C=CH2 + C2H4

pg.261-262: Discussion on evaluated data

Entry 47,19(d): No data available at the time.  Author recommends a rate coefficient

of 4x10^-12 cm3/molecule/s for the disproportionation rxn.
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 532,
    label = "O_pri_rad;Cdpri_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    H 0 {1,S}
""",
    group2 = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.03e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: OH + C3H5 --> H2C=C=CH2 + H2O

pg.253: Discussion on evaluated data

Entry 47,6(a): No data available at the time.  Author recommends a rate coefficient

of 1x10^-11 cm3/molecule/s, based on "comparable rxns".
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 533,
    label = "O2_birad;O_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.7209e+12,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (298,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Atkinson et al [98] literature review.""",
    longDesc = 
u"""
[98] Atkinson, R.; Baulch, D.L.; Cox, R.A.; Crowley, J.N.; Hampson, R.F., Jr.; Kerr, J.A.; Rossi, M.J.; Troe, J. "Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry,", 2001.
Literature review: CH3CHOH + O2 --> CH3CHO + HO2

Recommended value is k298.  This reference just gives a table of results,

with no discussion on how the preferred numbers were arrived at.
MRH 31-Aug-2009

Divide the rate constant by 2 to account for symmetry of 2 (O2) and 1 (CH3CHOH, oxygen atom). The final result is 5.7209e+12 cm3/mol/s.
JDM 31-Mar-2010
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 534,
    label = "O2_birad;O_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.92067e+12,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (298,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Atkinson et al [98] literature review.""",
    longDesc = 
u"""
[98] Atkinson, R.; Baulch, D.L.; Cox, R.A.; Crowley, J.N.; Hampson, R.F., Jr.; Kerr, J.A.; Rossi, M.J.; Troe, J. "Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry,", 2001.
Literature review: CH2OH + O2 --> CH2O + HO2

Recommended value is k298.  This reference just gives a table of results,

with no discussion on how the preferred numbers were arrived at.
MRH 31-Aug-2009

Divide the rate constant by 2 to account for symmetry of 2 (O2) and 1 (CH2OH, oxygen atom). The final result is 2.92067e+12 cm3/mol/s.
JDM 31-Mar-2010
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 535,
    label = "O2_birad;O_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.74001e+12,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol","+|-",0.4),
        Tmin = (200,"K"),
        Tmax = (300,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""DeMore et al [183] literature review.""",
    longDesc = 
u"""
[183] DeMore, W.B.; Sander, S.P.; Golden, D.M.; Hampson, R.F.; Kurylo, M.J.; Howard, C.J.; Ravishankara, A.R.; Kolb, C.E.; Molina, M.J.; JPL Publication 97-4
Literature review: CH2OH + O2 --> CH2O + HO2

pg.62 D38: Discussion on evaluated data

pg.22: Recommended A-factor and E/R parameter values

MRH 1-Sept-2009

Divide the rate constant by 2 to account for symmetry of 2 (O2) and 1 (CH2OH, oxygen atom). The final result is 2.74001e+12 cm3/mol/s.
JDM 31-Mar-2010
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 536,
    label = "O_atom_triplet;O_Csrad",
    group1 = 
"""
1 *1 O 2T
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.04e+13,"cm^3/(mol*s)","+|-",3.01e+13),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (298,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Grotheer et al [189].""",
    longDesc = 
u"""
[189] Grotheer, H.; Riekert, G.; Walter, D.; Just, T. Symp. Int. Combust. Proc. 1989, 22, 963.
Absolute value measured directly. Excitation: discharge, analysis: mass spectroscopy. Original uncertainty 3.0E+13

O + CH2OC --> OH + CH2O, O + CH3CHOH --> OH + CH3CHO

O+CH2OH --> OH+CH2O && O+CH3CHOH --> OH+CH3CHO

pg.963: Measured rate coefficients mentioned in abstract as k_2M and k_2E.

pg.965-967: Discussion on measured rate coefficients.

MRH 1-Sept-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 537,
    label = "CH2_triplet;O_Csrad",
    group1 = 
"""
1 *1 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.21e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: CH2 + CH2OH --> CH3 + CH2O

pg. 505: Discussion on evaluated data

Entry 39,26 (b): CH2OH + CH2(triplet) --> CH3 + CH2O

Author estimates the rate of disproportionation as 2.0x10^-12 cm3/molecule/s.  No data at the time.

MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 538,
    label = "H_rad;O_Csrad",
    group1 = 
"""
1 *1 H 1
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2e+13,"cm^3/(mol*s)","+|-",1e+13),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (295,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Edelbuttel-Einhaus et al [190].""",
    longDesc = 
u"""
[190] Edelbuttel-Einhaus, J.; Hoyermann, K.; Rohde, G.; Seeba, J. Symp. Int. Combust. Proc. 1992, 22, 661.
Data derived from fitting to a complex mechanism. Excitation: discharge, analysis: mass spectroscopy. Original uncertainty 1.0E+13

H + CH3CHOH --> H2 + CH3CHO

H+CH3CHOH --> H2+CH3CHO

pg.661: Measured rate coefficient mentioned in abstract as k6.

pg.665-666: Discussion on measured rate coefficient.  The reported rate coefficient is

for H+CH3CHOH --> products, making this an UPPER LIMIT.  The rate coefficient
was calculated based on the rate coefficient of the rxn C2H5+H --> CH3+CH3; the
value the authors used was 3.6x10^13 cm3/mol/s.
MRH 1-Sept-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 539,
    label = "H_rad;O_Csrad",
    group1 = 
"""
1 *1 H 1
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.03e+12,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: H + CH2OH --> H2 + CH2O

pg. 496-497: Discussion on evaluated data

Entry 39,4 (a): CH2OH + H --> H2 + CH2O

Author estimates disproportionation rate will be faster than the H+C2H5=H2+C2H4 reaction

and reports rate coefficient as 1.0x10^-11 cm3/molecule/s.  No data at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 540,
    label = "C_methyl;O_Csrad",
    group1 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.49e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (298,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Pagsberg et al [191].""",
    longDesc = 
u"""
[191] Pagsberg, P.; Munk, J.; Sillesen, A.; Anastasi, C. Chem. Phys. Lett. 1988, 146, 375.
Absolute value measured directly. Excitatio: electron beam, analysis: Vis-UV absorption.

CH2OH + CH3 --> CH2O + CH4

pg.378 Table 2: Formation and decay rates of CH2OH, CH3, and OH observed by pulse radiolysis of

gas mixtures of varying composition.  Chemical composition of systems A-E as in Table 1.
The authors note below Table 2 that the reported rate coefficient for CH3+CH2OH is an

"adjustment of model to reproduce the observed decay rates of CH3 and CH2OH".
MRH is skeptical of data, as this specific rxn is not directly referenced in the article,

nor do the authors address whether other channels besides -->CH4+CH2O exist / are significant.
The value of A in the database is consistent with that reported in Table 2.
MRH 1-Sept-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 541,
    label = "C_methyl;O_Csrad",
    group1 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.41e+12,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: CH3 + CH2OH --> CH4 + CH2O

pg. 500-501: Discussion on evaluated data

Entry 39,16 (b): CH2OH + CH3 --> CH4 + CH2O

Author estimates ratio of disproportionation rate to addition rate to be 0.2,

namely 4x10^-12 cm3/molecule/s.  No data at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 542,
    label = "C_rad/H2/Cs;O_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.41e+12,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: C2H5 + CH2OH --> C2H6 + CH2O

pg. 502: Discussion on evaluated data

Entry 39,17 (b): C2H5 + CH2OH --> C2H6 + CH2O

Author estimates the disproportionation rate coefficient as 4x10^-12 cm3/molecule/s.

No data at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 543,
    label = "C_rad/H2/Cd;O_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.81e+13,"cm^3/(mol*s)","*|/",2.5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] Literature review.""",
    longDesc = 
u"""
[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.
Literature review: C3H5 + CH2OH --> CH2O + C3H6

pg.267: Discussion on evaluated data

Entry 47,39: No data available at the time.  Author notes that combination of these two

reactants will form 3-butene-1-ol which should decompose under combustion conditions
to form C3H6 + CH2O (same products).  The author therefore recommends a rate
coefficient of 3x10^-11 cm3/molecule/s.
MRH 31-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 544,
    label = "C_rad/H2/O;O_Csrad",
    group1 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.82e+12,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: CH2OH + CH2OH --> CH3OH + CH2O

pg. 506: Discussion on evaluated data

Entry 39,39 (b): CH2OH + CH2OH --> CH3OH + CH2O

Meier, et al. (1985) measured the rate of addition + disproportionation.  Tsang estimates

a disproportionation to combination ratio of 0.5
NOTE: Rate coefficient given in table at beginning of reference (summarizing all data

presented) gives k_a+b = 2.4x10^-11, leading to k_b = 8x10^-12.  NIST's online
database (kinetics.nist.gov) reports this number as well.  However, the discussion
on pg. 506 suggests k_a+b = 1.5x10^-11, leading to k_b = 5x10^-12.
MRH 30-Aug-2009

*** NEED TO INVESTIGATE ***
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 545,
    label = "C_rad/H/NonDeC;O_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.35e+12,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] Literature review.""",
    longDesc = 
u"""
[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.
Literature review: CH2OH + i-C3H7 = C3H8 + CH2O

pg. 945: Discussion on evaluated data

Entry 42,39 (b): No data available at the time.  Author suggests rate coefficient based

on rxn C2H5+i-C3H7=C3H8+C2H4, namely 3.9x10^-12 cm3/molecule/s
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 546,
    label = "C_rad/Cs3;O_Csrad",
    group1 = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.47e+14,"cm^3/(mol*s)","*|/",3),
        n = -0.75,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] Literature review.""",
    longDesc = 
u"""
[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.
Literature review: t-C4H9 + CH2OH = CH2O + i-C4H10

pg. 44: Discussion on evaluated data

Entry 44,39 (a): No data available at the time.  Author estimates the addition rxn rate

coefficient based on the rate for t-C4H9+C2H5-->adduct.  The author uses a
disproportionation-to-addition ratio of 0.52 to obtain the reported rate coefficient
expression.
*** NOTE: Previous value in RMG was for k_c (the addition rxn).  I have changed it to match

the rate for the disproportionation rxn. ***
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 547,
    label = "Cd_pri_rad;O_Csrad",
    group1 = 
"""
1 *1 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.01e+13,"cm^3/(mol*s)","*|/",2.5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: CH2OH + C2H3 --> C2H4 + CH2O

pg. 503: Discussion on evaluated data

Entry 39,19 (a): CH2OH + C2H3 --> C2H4 + CH2O

Author suggests a disproportionation rate coefficient near the collision limit, due

to rxn's exothermicity.  No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 548,
    label = "Ct_rad;O_Csrad",
    group1 = 
"""
1 *1 C 1 {2,T}
2    C 0 {1,T}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.61e+13,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: C2H + CH2OH --> C2H2 + CH2O

pg. 504: Discussion on evaluated data

Entry 39,21 (a): CH2OH + C2H --> C2H2 + CH2O

Author suggest a disproportionation rate coefficient of 6.0x10^-11 cm3/molecule/s, due

to very exothermic rxn.  No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 549,
    label = "CO_pri_rad;O_Csrad",
    group1 = 
"""
1 *1 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.81e+14,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: HCO + CH2OH --> CH2O + CH2O

pg. 500: Discussion on evaluated data

Entry 39,15 (b): CH2OH + HCO --> 2 CH2O

Author estimates a disproportionation rate coefficient of 3x10^-11 cm3/molecule/s.

No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 550,
    label = "O_pri_rad;O_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    H 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.41e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: OH + CH2OH --> H2O + CH2O

pg. 497: Discussion on evaluated data

Entry 39,6: CH2OH + OH --> H2O + CH2O

Author estimates a disproportionation rate coefficient of 4x10^-11 cm3/molecule/s.

No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 551,
    label = "O_rad/NonDeC;O_Csrad",
    group1 = 
"""
1 *1 O  1 {2,S}
2    Cs 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.41e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: CH3O + CH2OH --> CH3OH + CH2O

pg. 505: Discussion on evaluated data

Entry 39,24: CH2OH + CH3O --> CH3OH + CH2O

Author estimates a disproportionation rate coefficient of 4x10^-11 cm3/molecule/s.

No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 552,
    label = "O_rad/NonDeO;O_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 0 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.21e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: HO2 + CH2OH --> CH3OH + H2O2

pg. 498: Discussion on evaluated data

Entry 39,7: CH2OH + HO2 --> H2O2 + CH2O

Author recommends a disproportionation rate coefficient of 2x10^-11 cm3/molecules/s.

No data available at the time.
MRH 30-Aug-2009
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 600,
    label = "O2_birad;O_Csrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.3413e+11,"cm^3/(mol*s)"),
        n = 0.3321,
        alpha = 0,
        E0 = (-1.0635,"kcal/mol"),
        Tmin = (250,"K"),
        Tmax = (1000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Zador et al.""",
    longDesc = 
u"""
(Essentially) Pressure-independent rate coefficient for CH3CHOH + O2 = HO2 + CH3CHO [Zador2009]_.

Authors computed the following PES:
	Entrance channel: CH3CHOH+O2
	Product channels: CH3CHO+HO2, CH2CHOH+HO2, 2-oxiranol+OH
	Wells: CH3CH(OO)OH, CH3CH(OOH)O, CH2CH(OOH)OH, CH3CHO--HO2 (hydrogen-bonding)
Geometry optimizations and IRC scans were done using B3LYP/6-311++G(d,p).  Single-point energies were computed using
 RQCISD(T)/cc-pV(INF)Z.  For stationary points with large T1 diagnostics, CASPT2 and MRCI with Davidson corrections
 were employed.
The rate coefficients were computed using RRKM/ME techniques developed by Miller and Klippenstein.  Low-frequency
 torsional modes were treated as hindered rotors using Pitzer-Gwinn; the scan was performed at B3LYP/6-311++G(d,p) and fit
 to a Fourier series.  An asymmetric Eckart tunneling correction was employed.  A simple exponential-down model was used,
 where <delta_Ed> = 100 * (T/298) cm-1.  Lennard-Jones parameters for the C2H5O3 isomers were assumed to be sigma = 4.31 Angstroms
 and epsilon/kB = 297 K.
The authors solved the PES using VRC-TST, with the following exceptions, in Variflex:
	- The TS between CH3CH(OO)OH and CH3CHO--HO2 was treated as the product channel CH3CHO+HO2
	- The CH3CHO--HO2 well, and its TS to the product channel CH3CHO+HO2, were not included
	- The CH3CH(OOH)O well, and its TS to the well CH3CH(OO)OH, were not included
The authors calculated k1,zero (collisionless) and k1,inf (high-pressure-limit) over the range 250-1000 K.
 The two rate coefficients were similar over most of the temperature range, suggesting a pressure-independent rate
 coefficient is adequate.  The value reported in RMG is the high-pressure limit.
The authors conclude that the CH3CHO+HO2 product channel dominates at all temperatures and pressures.  Hence, the
 entire computed k1,inf is assigned to the reaction CH3CHOH+O2=HO2+CH3CHO.  Furthermore, the authors detected a strong
 signal from the m/z = 44 PIE scan; they concluded this was due to the CH3CHO and CH2CHOH isomers.
This rate coefficient recommendation is up to 3x slower than the previous RMG-employed recommendation, over the valid
 temperature range.
 
12-OCT-2010 amendement (MRH): Divided pre-exponential A factor by 2 (to account for symmetry of oxygen).

.. [Zador2009] J. Zador, R.X. Fernandes, Y. Georgievskii, G. Meloni, C.A. Taatjes, J.A. Miller
	"The reaction of hydroxyethyl radicals with O2: A theoretical analysis of experimental product study"
	Proc. Combust. Inst. 32 (2009) 271-277
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

entry(
    index = 20001,
    label = "O2_birad;XH_Rrad",
    group1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    group2 = 
"""
1 *2 R!H 0 {2,S} {3,S}
2 *3 R!H 1 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

