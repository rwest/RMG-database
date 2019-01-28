#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_EeleyRideal/groups"
shortDesc = u""
longDesc = u"""
Eeley Rideal dissociation of two adsorbates into the gas phase.  The single bonds to the surface is broken; the resulting fragments each are single bonded to 2 eachother.

 *1  *2                *1-*2
  |   |        ---->   
~*3~~*4~              ~*3~*4~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2) * (mol/m3)
so k should be in (m5/mol2/s). We will use sticking coefficients.
"""
#todo: find real units

template(reactants=["Adsorbed1", "Adsorbed2"], products=["Adsorbate", "VacantSite1", "VacantSite2"], ownReverse=False)

reverse = "Surface_Adsorption-EeleyRideal"

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*1', 1, '*3'],
    ['BREAK_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "Adsorbed1",
    group =
"""
1 *1 R  u0 {3,S}
3 *3 R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Adsorbed2",
    group =
"""
1 *2 R  u0 {4,S}
2 *4 R  u0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbed1

L1: Adsorbed2
"""
)

