#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C3F6O <=> CF2O + C2F4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.7e+09,'s^-1'), n=1.16, Ea=(83135.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OCFCF2 <=> CF2O+CF2CF2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OCFCF2 <=> CF2O+CF2CF2
""",
)

entry(
    index = 2,
    label = "C3F6O-2 <=> CF2O + C2F4-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.43e+08,'s^-1'), n=1.22, Ea=(48702.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OCCF3 <=> CF3CF+CF2O""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OCCF3 <=> CF3CF+CF2O
""",
)

entry(
    index = 3,
    label = "C3HF7O <=> CF2O + C2HF5",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.59e+11,'s^-1'), n=0.77, Ea=(82880,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OCFHCF3 <=> CF2O+CF3CF2H""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OCFHCF3 <=> CF2O+CF3CF2H
""",
)

entry(
    index = 4,
    label = "C3F6O2 <=> CF2O + C2F4O",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.87e+11,'s^-1'), n=0.42, Ea=(49974.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OC(O)CF3 <=> CF2O+CF3CFO""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OC(O)CF3 <=> CF2O+CF3CFO
""",
)

entry(
    index = 5,
    label = "C3HF4O3 <=> CF2O + C2HF2O2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.02e+07,'s^-1'), n=1.62, Ea=(30984.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OCFC(O)OH <=> CF2O+CF2C(O)OH""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OCFC(O)OH <=> CF2O+CF2C(O)OH
""",
)

entry(
    index = 6,
    label = "C4F8O <=> C2F4O-2 + C2F4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.3e+08,'s^-1'), n=1.02, Ea=(81186.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OCFCF2 <=> CF3CFO+CF2CF2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCFCF2 <=> CF3CFO+CF2CF2
""",
)

entry(
    index = 7,
    label = "C4F8O-2 <=> C2F4O-2 + C2F4-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.53e+09,'s^-1'), n=0.9, Ea=(52188.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OCCF3 <=> CF3CFO+CF3CF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCCF3 <=> CF3CFO+CF3CF
""",
)

entry(
    index = 8,
    label = "C4HF9O <=> C2F4O-2 + C2HF5",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.98e+09,'s^-1'), n=0.79, Ea=(79774,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OCFHCF3 <=> CF3CFO+CF3CF2H""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCFHCF3 <=> CF3CFO+CF3CF2H
""",
)

entry(
    index = 9,
    label = "C4F8O2 <=> C2F4O-2 + C2F4O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.16e+12,'s^-1'), n=-0.04, Ea=(50928.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OC(O)CF3 <=> CF3CFO+CF3CFO""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OC(O)CF3 <=> CF3CFO+CF3CFO
""",
)

entry(
    index = 10,
    label = "C4F9O2 <=> CF2O + C3F7O",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(2480,'s^-1'), n=2.51, Ea=(65844.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OC(CF3)OCF3 <=> CF3OCFCF3+CF2O""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OC(CF3)OCF3 <=> CF3OCFCF3+CF2O
""",
)

entry(
    index = 11,
    label = "C4HF6O3 <=> C2F4O-2 + C2HF2O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.85e+07,'s^-1'), n=1.44, Ea=(23859.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OCFC(O)OH <=> CF3CFO+CF2C(O)OH""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCFC(O)OH <=> CF3CFO+CF2C(O)OH
""",
)

entry(
    index = 12,
    label = "C4HF7O3 <=> CF2O + C3HF5O2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.94e+10,'s^-1'), n=0.98, Ea=(81914.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OCF(CF3)C(O)OH <=> CF2O+C2F5C(O)OH""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OCF(CF3)C(O)OH <=> CF2O+C2F5C(O)OH
""",
)

entry(
    index = 13,
    label = "C5F10O <=> C3F6O-3 + C2F4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.54e+08,'s^-1'), n=1.06, Ea=(80760.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OCFCF2 <=> C2F5CFO+CF2CF2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCFCF2 <=> C2F5CFO+CF2CF2
""",
)

entry(
    index = 14,
    label = "C5F10O-2 <=> C3F6O-3 + C2F4-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.26e+08,'s^-1'), n=1.07, Ea=(51125.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OCCF3 <=> C2F5CFO+CF3CF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCCF3 <=> C2F5CFO+CF3CF
""",
)

entry(
    index = 15,
    label = "C5HF11O <=> C3F6O-3 + C2HF5",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.18e+10,'s^-1'), n=0.8, Ea=(79374.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OCFHCF3 <=> C2F5CFO+CF3CF2H""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCFHCF3 <=> C2F5CFO+CF3CF2H
""",
)

entry(
    index = 16,
    label = "C5F10O2 <=> C3F6O-3 + C2F4O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.47e+11,'s^-1'), n=0.12, Ea=(50136.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OC(O)CF3 <=> C2F5CFO+CF3CFO""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OC(O)CF3 <=> C2F5CFO+CF3CFO
""",
)

entry(
    index = 17,
    label = "C5F11O2 <=> CF2O + C4F9O",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(15200,'s^-1'), n=2.17, Ea=(66752.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OC(CF3)OCF3 <=> C2F5OCFCF3+CF2O""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OC(CF3)OCF3 <=> C2F5OCFCF3+CF2O
""",
)

entry(
    index = 18,
    label = "C5HF8O3 <=> C3F6O-3 + C2HF2O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9e+06,'s^-1'), n=1.39, Ea=(21512.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OCFC(O)OH <=> C2F5CFO+CF2C(O)OH""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCFC(O)OH <=> C2F5CFO+CF2C(O)OH
""",
)

entry(
    index = 19,
    label = "C5HF9O3 <=> C2F4O-2 + C3HF5O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.36e+10,'s^-1'), n=0.57, Ea=(77873.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OCF(CF3)C(O)OH <=> CF3CFO+C2F5C(O)OH""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCF(CF3)C(O)OH <=> CF3CFO+C2F5C(O)OH
""",
)

entry(
    index = 20,
    label = "C6HF11O3 <=> C3F6O-3 + C3HF5O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.43e+11,'s^-1'), n=0.16, Ea=(77189.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OCF(CF3)C(O)OH <=> C2F5CFO+C2F5C(O)OH""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCF(CF3)C(O)OH <=> C2F5CFO+C2F5C(O)OH
""",
)

entry(
    index = 21,
    label = "C6HF11O3 <=> C3HF3O3 + C3F8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08e+10,'s^-1'), n=0.39, Ea=(88203.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OCF(CF3)C(O)OH <=> C3F8+CF3C(O)C(O)OH""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCF(CF3)C(O)OH <=> C3F8+CF3C(O)C(O)OH
""",
)

