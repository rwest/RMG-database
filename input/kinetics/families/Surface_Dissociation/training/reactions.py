#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 16,
    label = "CH2X_3 + HX_5 <=> CH3X_1 + Ni_4",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A=(3.09E19, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(57200.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R16
"""
)


entry(
    index = 18,
    label = "CHX_3 + HX_5 <=> CH2X_1 + Ni_4",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A=(9.77E20, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(81000.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R18
"""
)


entry(
    index = 19,
    label = "CHX_1 + Ni_4 <=> CX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(9.88E16, 'm^2/(mol*s)'),
        n = 0.5,
        Ea=(21900.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R19
"""
)


entry(
    index = 32,
    label = "HOX_1 + Ni_4 <=> OX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.25E16, 'm^2/(mol*s)'),
        n = 0.188,
        Ea=(29600.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R32
"""
)


entry(
    index = 44,
    label = "HOCXO_1 + Ni_4 <=> OCX_3 + HOX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.46E20, 'm^2/(mol*s)'),
        n = -0.213,
        Ea=(54300.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R4
"""
)


entry(
    index = 48,
    label = "CXHO_1 + Ni_4 <=> OCX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.71E17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(0.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R8
"""
)