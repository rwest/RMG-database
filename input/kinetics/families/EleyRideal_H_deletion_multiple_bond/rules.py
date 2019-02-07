#!/usr/bin/env python
# encoding: utf-8

name = "EleyRideal_H_deletion_multiple_bond/rules"
shortDesc = u""
longDesc = u"""
Dissociation of two single adsorbates to eachother
"""
entry(
    index = 1,
    label = "Adsorbate1",
    kinetics = StickingCoefficientBEP(
        A = 0.1,
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)
#todo:find better placeholder numbers?