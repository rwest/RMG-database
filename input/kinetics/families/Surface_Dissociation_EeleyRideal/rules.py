#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_EeleyRideal/rules"
shortDesc = u""
longDesc = u"""
Dissociation of two single adsorbates to eachother
"""
entry(
    index = 1,
    label = "Adsorbed1;Adsorbed2",
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