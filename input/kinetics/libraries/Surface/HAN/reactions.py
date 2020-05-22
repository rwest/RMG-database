#!/usr/bin/env python
# encoding: utf-8

name = "HAN"
shortDesc = u""
longDesc = u"""
Reactions pertinent to the decomposition of HAN
"""

entry(
    index = 1,
    label = "NH4NO3 + X + X <=> N2O_X + H2O_X + H2O",
    kinetics = StickingCoefficient(
        A = 1.0e-6,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Ammonium Nitrate Adsorption decomposition""",
    longDesc = u"""
Currently modeling this as one step, adsorbs and breaks down immediately.
The pathway is insipred by Inazu et al. 2004.  http://dx.doi.org/10.1016/j.cattod.2004.06.055
Hopefully the reverse is calculated correctly, with there being a gas phase product.
Assume N2O_X is vdw-adsorbed (because "weakly bound", and I can't figure out a Lewis structure with bonds).
For the rate, just copied Deutschmann's dissociative adsorption of N2 from above, i.e.
a fixed sticking coefficient of 1e-6.
    """
)


entry( 
    index = 2,
    label = "HAN_X + X <=> HO_X + NH2O_X + HONO",
    kinetics = SurfaceArrhenius(
        A = (5e20, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(8.07, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""HONO elimination from HAN on Pd""",
    longDesc = u"""
    The "HONO elimaniton" pathway which is fastest on Pd(111) from Banerjee
    """
)

