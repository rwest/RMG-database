#!/usr/bin/env python
# encoding: utf-8

name = "CF_Radical_Formation_1/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "CHF2 <=> FH + CF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.01e+12,'s^-1'), n=0.49, Ea=(72977.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF2H <=> CF+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF2H <=> CF+HF
""",
)

entry(
    index = 1,
    label = "C2F5 <=> CF4 + CF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.44e+10,'s^-1'), n=1.13, Ea=(110322,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3CF2 <=> CF4+CF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3CF2 <=> CF4+CF
""",
)

entry(
    index = 2,
    label = "C2F3O <=> CF2O + CF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.27e+10,'s^-1'), n=0.64, Ea=(78811.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF2CFO <=> CF2O+CF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF2CFO <=> CF2O+CF
""",
)

