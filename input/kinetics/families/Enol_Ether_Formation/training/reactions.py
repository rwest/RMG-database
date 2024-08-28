#!/usr/bin/env python
# encoding: utf-8

name = "Enol_Ether_Formation/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C3F6O <=> C3F6O-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.91e+09,'s^-1'), n=0.87, Ea=(41067.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OCCF3 <=> CF3OCFCF2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OCCF3 <=> CF3OCFCF2
""",
)

entry(
    index = 1,
    label = "C4F8O <=> C4F8O-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.83e+09,'s^-1'), n=0.88, Ea=(40777.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OCCF3 <=> C2F5OCFCF2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCCF3 <=> C2F5OCFCF2
""",
)

entry(
    index = 2,
    label = "C5F10O <=> C5F10O-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.16e+07,'s^-1'), n=1.56, Ea=(40037.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OCCF3 <=> C3F7OCFCF2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCCF3 <=> C3F7OCFCF2
""",
)

