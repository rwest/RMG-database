#!/usr/bin/env python
# encoding: utf-8

name = "OF_Radical_Formation/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "CF3O2 <=> FO + CF2O",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.57e+12,'s^-1'), n=0.68, Ea=(97093.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OO <=> CF2O+OF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OO <=> CF2O+OF
""",
)

entry(
    index = 2,
    label = "C2F5O2 <=> FO + C2F4O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.43e+12,'s^-1'), n=0.48, Ea=(94172.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OO <=> CF3CFO+OF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OO <=> CF3CFO+OF
""",
)

entry(
    index = 3,
    label = "C3F7O2 <=> FO + C3F6O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.3e+11,'s^-1'), n=0.67, Ea=(92427.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OO <=> C2F5CFO+OF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OO <=> C2F5CFO+OF
""",
)

