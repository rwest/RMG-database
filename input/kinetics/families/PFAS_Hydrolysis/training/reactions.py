#!/usr/bin/env python
# encoding: utf-8

name = "PFAS_Hydrolysis/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""entry(
    index = 1,
    label = "CF4 + H2O <=> FH + CHF3O",
    degeneracy = 8.0,
    kinetics = Arrhenius(A=(48.9,'cm^3/(mol*s)'), n=3.22, Ea=(86268,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF4+H2O <=> CF3OH+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF4+H2O <=> CF3OH+HF
""",
)

entry(
    index = 2,
    label = "CF2O + H2O <=> FH + CHFO2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(0.242,'cm^3/(mol*s)'), n=3.33, Ea=(35135.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF2O+H2O <=> FC(O)OH+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF2O+H2O <=> FC(O)OH+HF
""",
)

entry(
    index = 3,
    label = "C2F6 + H2O <=> FH + C2HF5O",
    degeneracy = 12.0,
    kinetics = Arrhenius(A=(2.98,'cm^3/(mol*s)'), n=3.36, Ea=(80307.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F6+H2O <=> C2F5OH+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F6+H2O <=> C2F5OH+HF
""",
)

entry(
    index = 4,
    label = "C2F4O + H2O <=> FH + C2HF3O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.0257,'cm^3/(mol*s)'), n=3.6, Ea=(30432.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3CFO+H2O <=> CF3C(O)OH+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3CFO+H2O <=> CF3C(O)OH+HF
""",
)

entry(
    index = 5,
    label = "C3F8 + H2O <=> FH + C3HF7O",
    degeneracy = 12.0,
    kinetics = Arrhenius(A=(0.0677,'cm^3/(mol*s)'), n=3.77, Ea=(79908.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F8+H2O <=> C3F7OH+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F8+H2O <=> C3F7OH+HF
""",
)

entry(
    index = 6,
    label = "C3F6O + H2O <=> FH + C3HF5O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.00923,'cm^3/(mol*s)'), n=3.71, Ea=(30829.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5CFO+H2O <=> C2F5C(O)OH+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5CFO+H2O <=> C2F5C(O)OH+HF
""",
)

entry(
    index = 7,
    label = "C4F8O + H2O <=> FH + C4HF7O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.00267,'cm^3/(mol*s)'), n=3.86, Ea=(31139.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7CFO+H2O <=> C3F7C(O)OH+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7CFO+H2O <=> C3F7C(O)OH+HF
""",
)

