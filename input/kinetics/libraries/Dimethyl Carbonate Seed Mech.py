#!/usr/bin/env python
# encoding: utf-8

name = "Dimethyl Carbonate"
shortDesc = u"Peukert 2013 doi:10.1021/jp312643k"
longDesc = u"""
Peukert, S. L.; Sivaramakrishnan, R.; Michael, J. V. “High Temperature Shock Tube and Theoretical
Studies on the Thermal Decomposition of Dimethyl Carbonate and Its Bimolecular Reactions with H and
D-Atoms.” J. Phys. Chem. A 2013, 117, 3718–3728 [doi:10.1021/jp312643k].
"""
recommended = False

entry(
	index = 1,
	reactant1 = 
"""
DMC
1 C 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}

""",
	product1 = 
"""
Methoxymethane
1 C 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S}
""",
	product2 = 
"""
CO2
1 O 0 {2,D}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
""",
	degeneracy = 1,
	kinetics = Arrhenius(
		A = (6.79e19, 's^-1'),
		n = -0.766,
		Ea = (79.04, 'kcal/mol'), # the molar gas constant * 39 776 kelvin = 79.0430317 kcal / mol
		T0 = (1, 'K'),
	),
	reference = None,
	referenceType = "",
	shortDesc = u"Peukert 2013 doi:10.1021/jp312643k"
    longDesc = u"""Reaction 1 in the following paper.
High pressure limit rate taken from table S1 in the supplementary material.
[1] Peukert, S. L.; Sivaramakrishnan, R.; Michael, J. V. "High Temperature Shock Tube and Theoretical
Studies on the Thermal Decomposition of Dimethyl Carbonate and Its Bimolecular Reactions with H and
D-Atoms." J. Phys. Chem. A 2013, 117, 3718–3728 [doi:10.1021/jp312643k].
    """,
	history = [
			("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Peukert model."""),
            ("Wed June 19 2013","Richard West <r.west@neu.edu>","action","""Richard West corrected this entry from doi:10.1021/jp312643k."""),
		],
	)
