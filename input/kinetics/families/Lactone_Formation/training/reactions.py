#!/usr/bin/env python
# encoding: utf-8

name = "Lactone_Formation/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C2HF3O2 <=> C2F2O2 + FH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(9.57e+11,'s^-1'), n=0.34, Ea=(53059.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3C(O)OH <=> c_F2COC(O)+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3C(O)OH <=> c_F2COC(O)+HF
""",
)

entry(
    index = 1,
    label = "C3HF5O2 <=> C3F4O2 + FH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.44e+11,'s^-1'), n=0.83, Ea=(67256.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5C(O)OH <=> CF3-c_FCOC(O)+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5C(O)OH <=> CF3-c_FCOC(O)+HF
""",
)

entry(
    index = 2,
    label = "C4HF7O2 <=> C4F6O2 + FH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.06e+10,'s^-1'), n=0.85, Ea=(55739.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7C(O)OH <=> C2F5-c_FCOC(O)+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7C(O)OH <=> C2F5-c_FCOC(O)+HF
""",
)

entry(
    index = 3,
    label = "C4HF7O3 <=> C4F6O3 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+12,'s^-1'), n=0.42, Ea=(48368.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OCF(CF3)C(O)OH <=> CF3OC(CF3)OCO+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OCF(CF3)C(O)OH <=> CF3OC(CF3)OCO+HF
""",
)

entry(
    index = 4,
    label = "C5HF9O2 <=> C5F8O2 + FH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.32e+07,'s^-1'), n=1.61, Ea=(55284,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C4F9C(O)OH <=> C3F7-c_FCOC(O)+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C4F9C(O)OH <=> C3F7-c_FCOC(O)+HF
""",
)

entry(
    index = 5,
    label = "C5HF9O3 <=> C5F8O3 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.51e+14,'s^-1'), n=-0.2, Ea=(56198.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OCF(CF3)C(O)OH <=> C2F5OC(CF3)OCO+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCF(CF3)C(O)OH <=> C2F5OC(CF3)OCO+HF
""",
)

entry(
    index = 6,
    label = "C6HF11O3 <=> C6F10O3 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.78e+15,'s^-1'), n=-0.84, Ea=(49834.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OCF(CF3)C(O)OH <=> C3F7OC(CF3)OCO+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCF(CF3)C(O)OH <=> C3F7OC(CF3)OCO+HF
""",
)

