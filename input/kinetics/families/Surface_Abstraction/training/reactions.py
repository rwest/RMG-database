#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 24,
    label = "CH2X_1 + HOX_3 <=> CH3X_4 + OX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.39E17, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(19000.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Deutschmann Ni""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R24
""",
	metal = "Ni",
)

entry(
    index = 26,
    label = "CHX_1 + HOX_3 <=> CH2X_4 + OX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.40E18, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(42400.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R26
""",
	metal = "Ni",
)

#Delgado has this reaction as exothermic. However, our own thermo has this reaction as endothermic. removing and replacing with reverse direction, R28.
#entry(
#    index = 27,
#    label = "OX_5 + CHX_4 <=> HOX_3 + CX_1 ",
#    degeneracy = 1,
#    kinetics = SurfaceArrhenius(
#        A=(2.47E17, 'm^2/(mol*s)'),
#        n = 0.312,
#        Ea=(57700.0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    #rank = 3,
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#Delgado et al
#Catalysts, 2015, 5, 871-904. Reaction R27
#""",
#)

entry(
    index = 28,
    label = "HOX_3 + CX_1 <=> OX_5 + CHX_4 ",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.43E17, 'm^2/(mol*s)'),
        n = -0.312,
        Ea=(118900.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R28
""",
	metal = "Ni",
)

entry(
    index = 39,
    label = "O* + HCO* <=> OH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.298e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(0., 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 39 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.0e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.298e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 40,
    label = "NH2X_3 + O* <=> NHX_5 + OH*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (1.51463e+18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (87.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 4 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
6.1e12 1/s / 2.483e-05 mol/m^2 = 1.51463e+18 m^2/(mol*s)
Metal surface: Pt(533)
"""
)

entry(
    index = 41,
    label = "NHX_3 + O* <=> NX_5 + OH*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.483e+18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (84.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 5 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
1e13 1/s / 2.483e05 mol/m^2 = 2.483e+18 m^2/(mol*s)
Metal surface: Pt(533)
"""
)
