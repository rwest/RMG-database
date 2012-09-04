#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_CO/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')
"""
recommended = True

entry(
    index = 588,
    label = "CH2CHO;mb_CO_2H",
    group1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 O 0 {1,D}
3    H 0 {1,S}
4    C 1 {1,S} {5,S} {6,S}
5    H 0 {4,S}
6    H 0 {4,S}
""",
    group2 = 
"""
1 *3 CO 0 {2,D} {3,S} {4,S}
2 *4 Od 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.2319,"cm^3/(mol*s)","*|/",5),
        n = 3.416,
        alpha = 0,
        E0 = (77.107,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""MRH CBS-QB3 calculations with 1d h.r. corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations for the reverse of the reaction sequence *CH2-cycle(CH-CH2-O-O) => *CH2-O-O-CH=CH2 ==> CH2O + CH2CHO

Previous RMG estimate for this reaction was an "Average of average" estimate, in addition to RMG needing
to increase the estimated Ea by ~20 kcal/mol because the barrier was not greater than the endothermicity.
This reaction was of interest to MRH/MHS because the butanol model was sensitive to allyl+O2 => CH2O+CH2CHO.
The high-p limit kinetics were necessary to estimate a k(T,P) for this PES.

The kinetics correspond to the reaction CH2O+CH2CHO => *CH2-cycle(CH-CH2-O-O)

Reactant: 0 hindered rotors
TS: 0 hindered rotors were considered (the only low-frequency torisonal mode corresponded to
	a hindered rotation within the cycle; MRH did not think treating this as a 1-d separable
	hindered rotor was accurate)
Product: 1 hindered rotor was considered (the *CH2 torsion)

All external symmetry numbers were set equal to one, except for CH2O which was set to two.
MRH could not find a stable geometry for *CH2-O-O-CH=CH2 at the B3LYP/6-31G(d) level (the method/basis
used in the CBS-QB3 method), it would always optimize to CH2O + CH2CHO.  Furthermore, MRH did not run an
IRC for the TS, to confirm the TS would fall apart to CH2O + CH2CHO (instead of CH2-OO-CH=CH2), hence the lowest
ranking of "5" assigned to this rate coefficient.

The k(T) was calculated from 600 - 2000 K, in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 2.319e-01 * (T/1K)^3.416 * exp(-77.107 kcal/mol / RT) cm3/mol/s.
""",
    history = [
        ("Mon Aug 27 14:48:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from the old RMG database."""),
    ],
)

