#!/usr/bin/env python
# encoding: utf-8

name = "CF_Radical_Formation_2/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C2F4 <=> CF + CF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.54e+21,'s^-1'), n=-1.47, Ea=(70284.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3CF <=> CF3+CF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3CF <=> CF3+CF
""",
)

entry(
    index = 1,
    label = "C3F6 <=> CF + C2F5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.66e+20,'s^-1'), n=-1.26, Ea=(66713.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5CF <=> CF3CF2+CF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5CF <=> CF3CF2+CF
""",
)

