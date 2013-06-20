#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
recommended = True

entry(
	index = 1,
	reactant1 = 
"""
1    C 0 {2,S}
2 *3 O 0 {1,S} {3,S}
3 *1 C 0 {2,S} {4,D} {5,S}
4    O 0 {3,D}
5 *2 O 0 {3,S} {6,S}
6 *4 C 0 {5,S}
""",
	product1 = 
"""
1 *4 C 0 {2,S}
2 *3 O 0 {1,S} {3,S}
3    C 0 {2,S}
""",
	product2 = 
"""
1 *2 O 0 {2,D}
2 *1 C 0 {1,D} {3,D}
3    O 0 {2,D}
""",
	degeneracy = 1,
	kinetics = Arrhenius(
		A=(6.79e+19,'s^-1'),
		n=-0.766,
		Ea=(79.04,'kcal/mol'),
		T0=(1,'K'),
		Tmin = (1000,"K"),
		Tmax = (2000,"K"),
	),
	reference = None,
	referenceType = "",
	rank = 3, # MEANING UNKNOWN!
	shortDesc = u"""Peukert et al. (2013) doi:10.1021/jp312643k""",
	longDesc = 
u"""
This is the high pressure limit rate taken from table S1 in the supplementary material of:
[1] Peukert, S. L.; Sivaramakrishnan, R.; Michael, J. V. "High Temperature Shock Tube and Theoretical
 Studies on the Thermal Decomposition of Dimethyl Carbonate and Its Bimolecular Reactions with H and
 D-Atoms." J. Phys. Chem. A 2013, 117, 3718–3728 [doi:10.1021/jp312643k].
 
 Valid temperature range is probably 1000-2000 (where the paper focuses) but it's not
 explicitly stated. May be a bit wider.
""",
	history = [
		("Thu Jun 19 14:05:30 2012","Fariba Seyedzadeh <seyedzadehkhanshan.fn@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> created this entry."""),
	],
)
