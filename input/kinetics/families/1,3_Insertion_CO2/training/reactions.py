#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "H2 + CO2 <=> CH2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.51e+09,'cm^3/(mol*s)'), n=1.23, Ea=(309.198,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: CO2_Cdd;H2
""",
)

entry(
    index = 1,
    label = "CH4 + CO2 <=> C2H4O2",
    degeneracy = 8.0,
    kinetics = Arrhenius(A=(36240,'cm^3/(mol*s)'), n=2.83, Ea=(331.373,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""
Converted to training reaction from rate rule: CO2_Cdd;C_methane
""",
)

entry(
    index = 2,
    label = "C2H6 + CO2 <=> C3H6O2",
    degeneracy = 12.0,
    kinetics = Arrhenius(A=(130800,'cm^3/(mol*s)'), n=2.56, Ea=(320.494,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""
Converted to training reaction from rate rule: CO2_Cdd;C_pri/NonDeC
""",
)

entry(
    index = 3,
    label = "C3H8 + CO2 <=> C4H8O2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(424000,'cm^3/(mol*s)'), n=2.13, Ea=(322.168,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""
Converted to training reaction from rate rule: CO2_Cdd;C/H2/NonDeC
""",
)

entry(
    index = 4,
    label = "C3H8-2 + CO2 <=> C4H8O2-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(292,'cm^3/(mol*s)'), n=3.13, Ea=(493.712,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Aaron Vandeputte calculation for methylpropanate using BMK/CBSB7""",
    longDesc = 
"""
Converted to training reaction from rate rule: CO2_Od;C_methyl_C_pri
""",
)

entry(
    index = 5,
    label = "C2HF3O2 <=> CO2 + CHF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.19e-45,'s^-1'), n=17.11, Ea=(41536.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3C(O)OH <=> CF3H+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3C(O)OH <=> CF3H+CO2
""",
)

entry(
    index = 6,
    label = "C3HF4O2 <=> CO2 + C2HF4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(66.3,'s^-1'), n=2.87, Ea=(24236.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F4C(O)OH <=> CF2CF2H+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F4C(O)OH <=> CF2CF2H+CO2
""",
)

entry(
    index = 7,
    label = "C3HF5O2 <=> CO2 + C2HF5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.54e-42,'s^-1'), n=16.02, Ea=(42280.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5C(O)OH <=> CF3CF2H+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5C(O)OH <=> CF3CF2H+CO2
""",
)

entry(
    index = 8,
    label = "C4HF6O2 <=> CO2 + C3HF6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.44e-44,'s^-1'), n=16.52, Ea=(41072.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F6C(O)OH <=> C2F4CF2H+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F6C(O)OH <=> C2F4CF2H+CO2
""",
)

entry(
    index = 9,
    label = "C4HF7O2 <=> CO2 + C3HF7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.18e-40,'s^-1'), n=15.66, Ea=(42257.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7C(O)OH <=> C2F5CF2H+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7C(O)OH <=> C2F5CF2H+CO2
""",
)

entry(
    index = 10,
    label = "C4HF7O3 <=> CO2 + C3HF7O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.99e-30,'s^-1'), n=12.69, Ea=(46973.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3OCF(CF3)C(O)OH <=> CF3OCFHCF3+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OCF(CF3)C(O)OH <=> CF3OCFHCF3+CO2
""",
)

entry(
    index = 11,
    label = "C5HF9O2 <=> CO2 + C4HF9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.93e-43,'s^-1'), n=16.39, Ea=(41420.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C4F9C(O)OH <=> C3F7CF2H+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C4F9C(O)OH <=> C3F7CF2H+CO2
""",
)

entry(
    index = 12,
    label = "C5HF9O3 <=> CO2 + C4HF9O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.77e-25,'s^-1'), n=11.12, Ea=(47765.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F5OCF(CF3)C(O)OH <=> C2F5OCFHCF3+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCF(CF3)C(O)OH <=> C2F5OCFHCF3+CO2
""",
)

entry(
    index = 13,
    label = "C6HF11O3 <=> CO2 + C5HF11O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.14e-22,'s^-1'), n=10.39, Ea=(48295.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F7OCF(CF3)C(O)OH <=> C3F7OCFHCF3+CO2""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCF(CF3)C(O)OH <=> C3F7OCFHCF3+CO2
""",
)

