#!/usr/bin/env python
# encoding: utf-8

name = "CF_Radical_Formation_3/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C2F3O <=> CF + CF2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43e+12,'s^-1'), n=0.46, Ea=(30062.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is F2COCF <=> CF2O+CF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: F2COCF <=> CF2O+CF
""",
)

