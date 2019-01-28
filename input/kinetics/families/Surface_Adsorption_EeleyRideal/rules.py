#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_EeleyRideal/rules"
shortDesc = u""
longDesc = u"""
Adsorption of a gas-phase species forming two single adsorbates that are bound to two sites
"""
entry(
    index = 1,
    label = "Adsorbate;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.1,
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)
#todo:find better placeholder numbers?