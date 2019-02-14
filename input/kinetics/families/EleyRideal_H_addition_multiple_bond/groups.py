#!/usr/bin/env python
# encoding: utf-8

name = "EleyRideal_H_addition_multiple_bond/groups"
shortDesc = u""
longDesc = u"""
Eeley Rideal reaction with a gas phase double or triple bonded species.

 *2    *4=*3         *3-*4-*2
  |          ---->    |      
~*1~ +              ~*1~    

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s). We will use sticking coefficients.

This is from Theoretical Investigation of the Mechanisms for Olefinic Hydrogenation on
Pt(110) and Pt(111) Surfaces
Vincent Maurice & Christian Minot, J. Phys. Chem. 1990, 94, 8579-8588
"""

template(reactants=["Adsorbate1", "Gas"], products=["Adsorbate2"], ownReverse=False)

reverse = "EleyRideal_H_deletion_multiple_bond"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*3', -1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "Adsorbate1",
    group =
"""
1 *1 Xo u0 p0 {2,S}
2 *2 R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Gas",
    group =
"""
1 *3 R!H ux {2,[D,T,Q]}
2 *4 R!H ux {1,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label="*H",
    group =
"""
1 *1 Xo u0 {2,S}
2 *2 H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label="R=R",
    group =
"""
1 *3 R!H ux {2,D}
2 *4 R!H ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label="R#R",
    group =
"""
1 *3 R!H ux {2,T}
2 *4 R!H ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 6,
    label="C=C",
    group =
"""
1 *3 C u0 {2,D}
2 *4 C u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label="C#C",
    group =
"""
1 *3 C u0 {2,T}
2 *4 C u0 {1,T}
""",
    kinetics = None,
)


tree(
"""
L1: Adsorbate1
    L2: *H
L1: Gas
    L2: R=R
        L3: C=C
    L2: R#R
        L3: C#C
"""
)

