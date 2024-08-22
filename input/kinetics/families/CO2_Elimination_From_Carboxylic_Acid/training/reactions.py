#!/usr/bin/env python
# encoding: utf-8

name = "CO2_Elimination_From_Carboxylic_Acid/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""entry(
    index = 1,
    label = "C2HF2O2 <=> CHF2 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.85e-12,'s^-1'), n=6.85, Ea=(32530.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF2C(O)OH <=> CF2H+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF2C(O)OH <=> CF2H+CO2
""",
)

entry(
    index = 2,
    label = "C3HF4O2 <=> C2HF4 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.54e-21,'s^-1'), n=9.6, Ea=(27803.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3CFC(O)OH <=> CF3CFH+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3CFC(O)OH <=> CF3CFH+CO2
""",
)

entry(
    index = 3,
    label = "C3HF4O3 <=> C2HF4O + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.14661e-12,'s^-1'), n=7.1, Ea=(32688.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OCFC(O)OH <=> CF3OCFH+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OCFC(O)OH <=> CF3OCFH+CO2
""",
)

entry(
    index = 4,
    label = "C4HF6O3 <=> C3HF6O + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e-13,'s^-1'), n=7.32, Ea=(32895.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OCFC(O)OH <=> C2F5OCFH+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCFC(O)OH <=> C2F5OCFH+CO2
""",
)

