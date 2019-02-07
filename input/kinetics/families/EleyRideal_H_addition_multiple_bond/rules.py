#!/usr/bin/env python
# encoding: utf-8

name = "EleyRideal_H_addition_multiple_bond/rules"
shortDesc = u""
longDesc = u"""
Eley Rideal mechanism for a gas phase double or triple bonded species.
"""
entry(
    index = 1,
    label = "Adsorbate1;Gas",
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