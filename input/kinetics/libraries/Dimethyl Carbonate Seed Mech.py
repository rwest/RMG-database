#!/usr/bin/env python
# encoding: utf-8

name = "Dimethyl Carbonate"
shortDesc = u""
longDesc = u"""

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
		A = (4.29e83, 's^-1'),
		n = -19.437,
		Ea = (55.7, 'kcal/mol'),
		T0 = (1, 'K'),
	),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""

""",
	history = [
			("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
		],
	)
