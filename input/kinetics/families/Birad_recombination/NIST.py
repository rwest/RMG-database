#!/usr/bin/env python
# encoding: utf-8

name = "Birad_recombination/NIST"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "1967BEN4920-4926:2",
    reactant1 = 
"""
1    C 0 {2,S} {8,S}
2    C 0 {1,S} {6,D}
3    C 0 {4,D} {7,S}
4    C 0 {3,D}
5 *2 C 1 {6,S}
6 *4 C 0 {2,D} {5,S}
7 *1 C 1 {3,S} {8,S}
8 *3 C 0 {1,S} {7,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {6,S}
2 *3 C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {7,S}
4    C 0 {2,S} {5,S}
5    C 0 {4,S} {7,D}
6    C 0 {1,S} {8,D}
7 *4 C 0 {3,S} {5,D}
8    C 0 {6,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"s^-1"),
        n = 0,
        Ea = (7.525,"kJ/mol"),
        T0 = 1,
        Tmin = (550,"K"),
        Tmax = (650,"K"),
    ),
    reference = Article(
        authors = ["Benson, S.W."],
        title = u'Mechanism of the Diels-Alder reactions of butadiene',
        journal = "J. Chem. Phys.",
        volume = "46",
        pages = """4920-4926""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967BEN4920-4926:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
G. Magoon:

***this only considers cis-cis isomer reaction*** cis-trans A prefactor is 50% of the value used here; also, on p. 4923, it is stated that cis trans rate is 5/6 of the overall rate, so maybe the k that should be used is 0.6 of the value currently in place?

Rxn. -d. also looks to be of interest here; whether the rate is high-pressure limit was not investigated, but p. 4922 says that pressures involved were low; DE0 uncertainty added; regarding temperature range, I considered dropping lower temperature limit from 550 K to 400 K (based on p. 4923), but it seems that experiments were performed at or around 600 K, so I will leave it at 550-650 K

Note: after some preliminary confusion on my part, it looks like the existing groups are correct (the correct resonance form for the CH2 radical is taken into account with the Ypri_rad_out (i.e. Cpri_rad_out_H2)), but arguably, another, a more-specific group (C_rad_out_H2/OneDe and Cpri_rad_out_H2/OneDe) should be specified to account for delocalizing group at this site
""",
    history = [
        ("Tue Aug 28 11:45:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1967BEN4920-4926:2"""),
    ],
)

entry(
    index = 2,
    label = "2006SIR/GLA12693-12704:2",
    reactant1 = 
"""
1 *2 C 1 {2,S}
2 *4 C 0 {1,S} {4,S}
3 *1 C 1 {4,S}
4 *3 C 0 {2,S} {3,S}
""",
    product1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *4 C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {4,S}
4 *2 C 0 {2,S} {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.62e+12,"s^-1"),
        n = -0.31,
        Ea = (8.284,"kJ/mol"),
        T0 = 1,
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = Article(
        authors = ["Sirjean, B.", "Glaude, P.A.", "Ruiz-Lopez, M.F.", "Fournet, R."],
        title = u'Detailed kinetic study of the ring opening of cycloalkanes by CBS-QB3 calculations',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """12693-12704""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006SIR/GLA12693-12704:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
Pressure dependence: None reported

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using transition state theory.

===

G. Magoon: Stated pressure is 1 atm, but I believe they are actually calculating the high-pressure limit rate constant
""",
    history = [
        ("Tue Aug 28 11:57:17 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2006SIR/GLA12693-12704:2"""),
    ],
)

entry(
    index = 3,
    label = "2006SIR/GLA12693-12704:12",
    reactant1 = 
"""
1    C 0 {2,S} {6,S}
2    C 0 {1,S} {4,S}
3 *2 C 1 {4,S}
4 *4 C 0 {2,S} {3,S}
5 *1 C 1 {6,S}
6 *3 C 0 {1,S} {5,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3 *4 C 0 {2,S} {5,S}
4 *3 C 0 {1,S} {6,S}
5 *2 C 0 {3,S} {6,S}
6 *1 C 0 {4,S} {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.13e+09,"s^-1"),
        n = 0.14,
        Ea = (8.745,"kJ/mol"),
        T0 = 1,
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
        Pmin = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Sirjean, B.", "Glaude, P.A.", "Ruiz-Lopez, M.F.", "Fournet, R."],
        title = u'Detailed kinetic study of the ring opening of cycloalkanes by CBS-QB3 calculations',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """12693-12704""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006SIR/GLA12693-12704:12",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
Pressure dependence: None reported

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using transition state theory.

===

G. Magoon:

Stated pressure is 1 atm, but I believe they are actually calculating the high-pressure limit rate constant; the rate constant added here was found my performing least squares fit for log(ktot) from 600-2000 K (where ktot is the sum of k5-1 and k5-2)

Note: Recent experimental/RRKM study by Kiefer, Gupte, Harding, and Klippenstein (http://www.combustion.org.uk/ECM_2009/P810069.pdf) (stated uncertainty is +/- 30%) appears to agree with Sirjean et al. results, but they only report forward rate constant
""",
    history = [
        ("Tue Aug 28 12:06:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2006SIR/GLA12693-12704:12"""),
    ],
)

