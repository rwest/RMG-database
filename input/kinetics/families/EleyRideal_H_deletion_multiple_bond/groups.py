#!/usr/bin/env python
# encoding: utf-8

name = "EleyRideal_H_deletion_multiple_bond/groups"
shortDesc = u""
longDesc = u"""
Eeley Rideal reverse reaction to form a gas phase double or triple bonded species.

 *3-*4-*2            *2*    *4=*3
  |          ---->    |      
~*1~                ~*1~  +     

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2)
so k should be in (1/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbate1"], products=["Adsorbate2", "Gas"], ownReverse=False)

reverse = "EleyRideal_H_addition_multiple_bond"

recipe(actions=[
    ['BREAK_BOND', '*2', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*1', 1, '*3'],
    ['CHANGE_BOND', '*3', 1, '*4'],
])

entry(
    index = 1,
    label = "Adsorbate1",
    group =
"""
1 *1 Xo u0 {3,S}
2 *2 H u0 p0 {4,S}
3 *3 R u0 {1,S} {4,[S,D,T]}
4 *4 R u0 {2,S} {3,[S,D,T]}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate1
"""
)

