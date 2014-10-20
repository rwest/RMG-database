#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Insertion/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')

"""
entry(
	index = 1,
	label = "Si2S_R_H;Si_H",
	kinetics = ArrheniusEP(
		A = (3.1E-10 , 'cm^3/(mol*s)'),
		n = 0,
		alpha = 0,
		E0 = (-1.9, 'kJ/mol'),
		Tmin = (295, 'K'),
		Tmax = (595, 'K'),
	),
	rank = 1,
	shortDesc = u"""Any silylene insertion into an Si-H bond""",
	longDesc =
u"""
Rate is from the reaction SiH2 + Si2H6 <-> Si3H8, from laser flash photolysis studies of Becerra et al., J. Organometal. Chem., 333-349, 1996.
""",
)