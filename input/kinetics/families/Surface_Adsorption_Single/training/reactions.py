#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Single/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "NO + Pt <=> NO_X",
    degeneracy = 1,
    kinetics = StickingCoefficient(
        A = 0.85,
        n = 0,
        Ea = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""NO Adsorption""",
    longDesc = u"""
    Detailed surface reaction mechanism in a three-way catalyst
    Chatterjee, Deutschmann, Warnatz et al.
    doi: 10.1039/b101968f
    Pt(111)
    This is R48
""",
    metal = "Pt",
)

entry(
    index = 2,
    label = "NO_X <=> NO + Pt",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.9864e+20, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (163.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 9,
    shortDesc = u"""NO desorption""",
    longDesc = u"""
    Reaction 12 in "Modeling ammonia oxidation over a Pt (533) surface"
    https://doi.org/10.1016/j.susc.2011.08.014

    A factor from paper / surface site density of Pt
    8e14 1/s / 2.483e05 mol/m^2 = 1.9864e+20 m^2/(mol*s)

    Metal surface: Pt(533)
    """,
    metal = "Pt",
)

