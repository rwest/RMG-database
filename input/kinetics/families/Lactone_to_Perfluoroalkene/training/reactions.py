#!/usr/bin/env python
# encoding: utf-8

name = "Lactone_to_Perfluoroalkene/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C3F4O2 <=> C2F4 + CO2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.39e+12,'s^-1'), n=0.63, Ea=(32152.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3-c_FCOC(O) <=> CF2CF2+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3-c_FCOC(O) <=> CF2CF2+CO2
""",
)

entry(
    index = 2,
    label = "C4F6O2 <=> C3F6 + CO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.27e+12,'s^-1'), n=0.64, Ea=(32427.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5-c_FCOC(O) <=> CF3CFCF2+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5-c_FCOC(O) <=> CF3CFCF2+CO2
""",
)

