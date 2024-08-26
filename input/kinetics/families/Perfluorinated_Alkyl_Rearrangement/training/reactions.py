#!/usr/bin/env python
# encoding: utf-8

name = "Perfluorinated_Alkyl_Rearrangement/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C4F8O <=> C4F8O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.83e+08,'s^-1'), n=0.97, Ea=(72710,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OCCF3 <=> CF2OC(CF3)CF3""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCCF3 <=> CF2OC(CF3)CF3
""",
)

entry(
    index = 2,
    label = "C5F10O <=> C5F10O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(302000,'s^-1'), n=1.52, Ea=(74068.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OCCF3 <=> CF2OC(CF3)C2F5""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCCF3 <=> CF2OC(CF3)C2F5
""",
)

