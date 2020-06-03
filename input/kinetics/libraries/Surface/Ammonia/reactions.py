#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia"
shortDesc = u"Things related to Ammonia (oxidation on Pt and other studies)"
longDesc = u"""
Based on "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014
and some other studies as noted.
"""

entry(
    index = 1,
    label = "N_Pt + N_Pt <=> N2 + Pt + Pt",
    kinetics = SurfaceArrhenius(
        A=(7.449e+16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (85.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Modeling ammonia oxidation over a Pt (533) surface""",
    longDesc = u"""
"Kinetics of ammonia oxidation on stepped platinum surfacesII. Simulation results"

A factor from paper / surface site density of Pt
3e11 1/s / 2.483e-05 mol/m^2 = 7.449e+16 m^2/(mol*s)
Surface Science 576 (2005) 131–144
""",
    metal = "Pt",
)

entry(
    index = 2,
    label = "N_Pt + O_Pt <=> NO_Pt + Pt",
    kinetics = SurfaceArrhenius(
        A=(4.966e+20, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (85.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Modeling ammonia oxidation over a Pt (533) surface""",
    longDesc = u"""
Reaction 11 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
2e15 1/s / 2.483e-05 mol/m^2 = 4.966e+16 m^2/(mol*s)
""",
    metal = "Pt",
)

entry(
    index = 3,
    label = "NO_Pt + N_Pt <=> N2O + Pt + Pt",
    kinetics = SurfaceArrhenius(
        A=(2.7313e+19, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (101.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Modeling ammonia oxidation over a Pt (533) surface""",
    longDesc = u"""
A factor from Reaction 13a in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
1.1e14 1/s / 2.483e-05 mol/m^2 = 2.7313e+19 m^2/(mol*s)

Ea from "N2O formation and dissociation during ammonia combustion: A combined DFT and experimental study"
https://doi.org/10.1016/j.proci.2016.05.004
""",
    metal = "Pt",
)

entry(
    index = 4,
    label = "N2O + Pt <=> N2 + O_Pt",
    kinetics = SurfaceArrhenius(
        A=(1.0e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(147.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""N2O formation and dissociation during ammonia combustion Pt(111)""",
    longDesc = u"""
Ea from "N2O formation and dissociation during ammonia combustion: A combined DFT and experimental study"
https://doi.org/10.1016/j.proci.2016.05.004

A factor made up
Metal surface: Pt(111)
""",
    metal = "Pt",
)

entry(
    index = 5,
    label = "NO_Pt + NO_Pt <=> N2O + O_Pt + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.0e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (241.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""NO pairing and transformation to N2O on ... Pt (111)""",
    longDesc = u"""
Ea from "NO pairing and transformation to N2O on Cu (111) and Pt (111) from first principles"
A. Bogicevic, K.C. Hass, Surf. Sci. 506 (2002) L237-L242.

A factor made up.
Metal surface: Pt(111)
""",
    metal = "Pt",
)

# entry(
#     index = 6,
#     label = "NO_Pt + N_Pt <=> N2O + Pt + Pt",
#     kinetics = SurfaceArrhenius(
#         A=(1.0e18, 'm^2/(mol*s)'),
#         n = 0.,
#         Ea = (48.0, 'kJ/mol'),
#         Tmin = (298, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Ea from "N2O formation and dissociation during ammonia combustion: A combined DFT and experimental study"
# https://doi.org/10.1016/j.proci.2016.05.004

# A factor made up.
# Metal Pt(100)
# """,
#     metal = "Pt",
# )

## This is called N2O dissociation, but it's in fact N2O desorption,
## Which I'd expect to be taken care of by an adsorption sticking coefficient and eqm.
## Also, the provided adjacency list for N2O_Pt didn't have a surface atom and was gas phase.
## So I'm commenting it out (Richard West)
# entry(
#     index = 7,
#     label = "N2O_Pt <=> N2O + Pt",
#     degeneracy = 1,
#     kinetics = SurfaceArrhenius(
#         A=(1e13, '1/s'),
#         n = 0.,
#         Ea = (29.0, 'kJ/mol'),
#         Tmin = (298, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""N2O Dissociation""",
#     longDesc = u"""
#     Ea from
#     "N2O formation and dissociation during ammonia combustion: A combined DFT and experimental study"
#     https://doi.org/10.1016/j.proci.2016.05.004

#     A made up by David.
#     Metal: Pt(100)
#     """,
#     metal = "Pt",
# )
