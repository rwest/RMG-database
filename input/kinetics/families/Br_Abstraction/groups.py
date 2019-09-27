#!/usr/bin/env python
# encoding: utf-8

name = "Br_Abstraction/groups"
shortDesc = u""
longDesc = u"""
The reaction site *3 needs a lone pair in order to react. It cannot be 2S or 4S.
"""

template(reactants=["X_Br_or_Xrad_Br_Xbirad_Br_Xtrirad_Br", "Y_rad_birad_trirad_quadrad"], products=["X_Br_or_Xrad_Br_Xbirad_Br_Xtrirad_Br", "Y_rad_birad_trirad_quadrad"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*2', 1, '*3'],
    ['GAIN_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "X_Br_or_Xrad_Br_Xbirad_Br_Xtrirad_Br",
    group = "OR{X_Br, Xrad_Br, Xbirad_Br, Xtrirad_Br}",
    kinetics = None,
)

entry(
    index = 2,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_2centeradjbirad, Y_1centerbirad, Y_rad, Y_1centertrirad, Y_1centerquadrad}",
    kinetics = None,
)

entry(
    index = 3,
    label = "X_Br",
    group =
"""
1 *1 R u0 {2,S}
2 *2 Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Br2",
    group =
"""
1 *1 Br1s u0 {2,S}
2 *2 Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "HBr",
    group =
"""
1 *1 H u0 {2,S}
2 *2 Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Ct_Br",
    group =
"""
1 *1 Ct    u0 {2,S} {3,T}
2 *2 Br1s     u0 {1,S}
3    [C,N] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Ct/Br/NonDeC",
    group =
"""
1 *1 Ct u0 {2,S} {3,T}
2 *2 Br1s  u0 {1,S}
3    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Ct/Br/NonDeN",
    group =
"""
1 *1 Ct  u0 {2,S} {3,T}
2 *2 Br1s   u0 {1,S}
3    N3t u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Cd_Br",
    group =
"""
1 *1 C     u0 {2,D} {3,S} {4,S}
2    C u0 {1,D}
3 *2 Br1s     u0 {1,S}
4    R     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Cd_pri",
    group =
"""
1 *1 C     u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Br1s     u0 {1,S}
4    H     u0 {1,S}
5   R   u0 {2,S}
""",
    kinetics = None,
)


entry(
    index = 30,
    label = "Cd_sec",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    Cd  u0 {1,D} {5,S}
3 *2 Br1s   u0 {1,S}
4    R!H u0 {1,S}
5   R u0 {2,S}
""",
    kinetics = None,
)
entry(
    index = 40,
    label = "Cd_allenic",
    group =
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 Cdd u0 {1,D}
3 *2 Br1s u0 {1,S}
4 R u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 60,
    label = "Cs_Br",
    group =
"""
1 *1 Cs u0 {2,S}
2 *2 Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Cs_Br2",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 610,
    label = "Cs_Br2_H2",
    group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    H u0 {1,S}
5    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 611,
    label = "Cs_Br3",
    group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *2 Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 612,
    label = "Cs_Br4",
    group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

#entry(
#    index = 61,
#    label = "C_methane",
#    group =
#"""
#1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
#2 *2 Br u0 {1,S}
#3    [H,Br] u0 {1,S}
#4    [H,Br] u0 {1,S}
#5    [H,Br] u0 {1,S}
#""",
#    kinetics = None,
#)
#

entry(
   index = 62,
   label = "C_pri_Br3",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    Br1s    u0 {1,S}
5    C     u0  p0 {1,S}
""",
   kinetics = None,
)

entry(
   index = 63,
   label = "C_pri_HBr2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    H    u0 {1,S}
5    C     u0 p0 {1,S}
""",
   kinetics = None,
)

entry(
   index = 64,
   label = "C_pri_H2Br",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    H       u0 {1,S}
4    H       u0 {1,S}
5    C     u0 p0 {1,S}
""",
   kinetics = None,
)

entry(
   index = 65,
   label = "C_pri_Br3/C_sec_H2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    Br1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H       u0 {5,S}
7    H       u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 66,
   label = "C_pri_Br3/C_sec_HBr",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    Br1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    Br1s       u0 {5,S}
7    H       u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 67,
   label = "C_pri_Br3/C_sec_Br2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    Br1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    Br1s    u0 {5,S}
7    Br1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 68,
   label = "C_pri_HBr2/C_sec_H2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H    u0 {5,S}
7    H    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 69,
   label = "C_pri_HBr2/C_sec_HBr",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    H       u0 {1,S}
5    Cs      u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H       u0 {5,S}
7    Br1s    u0 {5,S}
8    C    u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 70,
   label = "C_pri_HBr2/C_sec_Br2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    Br1s    u0 {5,S}
7    Br1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 71,
   label = "C_pri_H2Br/C_sec_H2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    H       u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H       u0 {5,S}
7    H       u0 {5,S}
8    C       u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 72,
   label = "C_pri_H2Br/C_sec_HBr",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H    u0 {5,S}
7    Br1s    u0 {5,S}
8    C      u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 73,
   label = "C_pri_H2Br/C_sec_Br2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    Br1s   u0 {5,S}
7    Br1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)


entry(
    index = 74,
    label = "C_sec_Br2",
    group =
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s   u0 {1,S}
3    Br1s   u0 {1,S}
4    C   u0  p0 {1,S}
5    C   u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "C_sec_HBr",
    group =
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s   u0 {1,S}
3    H   u0 {1,S}
4    C   u0 p0 {1,S}
5    C   u0 p0 {1,S}
""",
    kinetics = None,
)

# entry(
#     index = 76,
#     label = "C_sec_Br2/C_pri_Br3",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    Br1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    Br1s u0 {5,S}
# 7    Br1s u0 {5,S}
# 8    Br1s u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 77,
#     label = "C_sec_HBr/C_pri_Br3",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    Br1s u0 {5,S}
# 7    Br1s u0 {5,S}
# 8    Br1s u0 {5,S}
# """,
#     kinetics = None,
# )
#
# entry(
#     index = 78,
#     label = "C_sec_Br2/C_pri_HBr2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    Br1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    Br1s u0 {5,S}
# 8    Br1s u0 {5,S}
# """,
#     kinetics = None,
# )
#
# entry(
#     index = 79,
#     label = "C_sec_HBr/C_pri_HBr2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    Br1s u0 {5,S}
# 8    Br1s u0 {5,S}
# """,
#     kinetics = None,
# )
#
#
# entry(
#     index = 80,
#     label = "C_sec_Br2/C_pri_H2Br",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    Br1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    H u0 {5,S}
# 8    Br1s u0 {5,S}
# """,
#     kinetics = None,
# )
#
# entry(
#     index = 81,
#     label = "C_sec_HBr/C_pri_H2Br",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    H u0 {5,S}
# 8    Br1s u0 {5,S}
# """,
#     kinetics = None,
# )
#
# entry(
#     index = 82,
#     label = "C_sec_Br2/C_pri_H3",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    Br1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    H u0 {5,S}
# 8    H u0 {5,S}
# """,
#     kinetics = None,
# )
#
# entry(
#     index = 83,
#     label = "C_sec_HBr/C_pri_H3",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    H u0 {5,S}
# 8    H u0 {5,S}
# """,
#     kinetics = None,
# )
#
# entry(
#     index = 84,
#     label = "C_sec_Br2/C_sec_Br2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    Br1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    Br1s u0 {5,S}
# 7    Br1s u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 85,
#     label = "C_sec_HBr/C_sec_Br2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    Br1s u0 {5,S}
# 7    Br1s u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 86,
#     label = "C_sec_Br2/C_sec_HBr",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    Br1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    Br1s u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 87,
#     label = "C_sec_HBr/C_sec_HBr",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    H  u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    Br1s u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )


# entry(
#     index = 88,
#     label = "C_sec_Br2/C_sec_H2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    Br1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    H u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 89,
#     label = "C_sec_HBr/C_sec_H2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    H u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

entry(
   index = 90,
   label = "C_pri_Br3/C_ter_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    Br1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H    u0 {5,S}
7    C    u0 {5,S}
8    C    u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 91,
   label = "C_pri_Br3/C_ter_Br",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    Br1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    Br1s    u0 {5,S}
7    C    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 92,
   label = "C_pri_HBr2/C_ter_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H    u0 {5,S}
7    C     u0 {5,S}
8    C      u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 93,
   label = "C_pri_HBr2/C_ter_Br",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    Br1s    u0 {5,S}
7    C    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 94,
   label = "C_pri_H2Br/C_ter_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H    u0 {5,S}
7    C     u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 95,
   label = "C_pri_H2Br/C_ter_Br",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    H     u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    Br1s    u0 {5,S}
7    C     u0 {5,S}
8    C      u0 {5,S}
""",
   kinetics = None,
)

# entry(
#     index = 96,
#     label = "C_sec_Br2/C_ter_H",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    Br1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    R!H u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 97,
#     label = "C_sec_Br2/C_ter_Br",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    Br1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    Br1s u0 {5,S}
# 7    R!H u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 98,
#     label = "C_sec_HBr/C_ter_Br",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    Br1s u0 {5,S}
# 7    R!H u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 99,
#     label = "C_sec_HBr/C_ter_H",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 Br1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    R!H u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

entry(
   index = 100,
   label = "Cs_Br3_O2s",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    Br1s    u0 {1,S}
5    O2s     u0 {1,S}
""",
   kinetics = None,
)

entry(
   index = 101,
   label = "Cs_Br2_O2s_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    H       u0 {1,S}
5    O2s     u0 {1,S}
""",
   kinetics = None,
)

entry(
   index = 102,
   label = "Cs_Br_H2_O2s",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    H    u0 {1,S}
4    H       u0 {1,S}
5    O2s     u0 {1,S}
""",
   kinetics = None,
)

entry(
    index = 103,
    label = "Cs_Br2_O2s_O2s",
    group =
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s   u0 {1,S}
3    Br1s   u0 {1,S}
4    O2s u0 {1,S}
5    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Cs_Br_H_O2s_C",
    group =
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s   u0 {1,S}
3    H   u0 {1,S}
4    O2s u0 {1,S}
5    C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "C_ter_Br",
    group =
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s   u0 {1,S}
3    C u0 {1,S}
4    C u0 {1,S}
5    C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "O_Br",
    group =
"""
1 *1 O2s u0 {2,S}
2 *2 Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "HO_Br",
    group =
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    H    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "BrO_Br",
    group =
"""
1 *1 O2s  u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "OO_Br",
    group =
"""
1 *1 O2s  u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1350,
    label = "O_rad_O_Br",
    group =
"""
1 *1 O2s  u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    O2s  u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1351,
    label = "C_rad_O_Br",
    group =
"""
1 *1 O2s  u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    C    u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1352,
    label = "CO_Br",
    group =
"""
1 *1 O2s  u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    C    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "CsO_Br",
    group =
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "CdO_Br",
    group =
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    Cd  u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 138,
    label = "CtO_Br",
    group =
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    Ct   u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 140,
    label = "Xrad_Br",
    group =
"""
1 *1 R!H u1 {2,S}
2 *2 Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1400,
    label = "O_rad_Br",
    group =
"""
1 *1 O u1 {2,S}
2 *2 Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "C_rad_Br",
    group =
"""
1 *1 C u1 {2,S}
2 *2 Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "C_rad_Br/Br",
    group =
"""
1 *1 Cs    u1 {2,S} {3,S}
2 *2 Br1s  u0 {1,S}
3    Br1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1420,
    label = "C_rad_Br/BrBr",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    Br1s  u0 {1,S}
4    Br1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1421,
    label = "C_rad_Br/BrH",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    Br1s  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1422,
    label = "C_rad_Br/BrC",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    Br1s  u0 {1,S}
4    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 999,
    label = "C_rad_Br/BrCs",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    Br1s  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 998,
    label = "C_rad_Br/BrCd",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    Br1s  u0 {1,S}
4    Cd  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 997,
    label = "C_rad_Br/BrCt",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    Br1s  u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 996,
    label = "C_rad_Br/BrO",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    Br1s  u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 995,
    label = "C_rad_Br/CC",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    C  u0 {1,S}
4    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 994,
    label = "C_rad_Br/CO",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    C  u0 {1,S}
4    O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 993,
    label = "C_rad_Br/OO",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    O2s  u0 {1,S}
4    O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 992,
    label = "C_rad_Br/HH",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 991,
    label = "C_rad_Br/HO",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    H  u0 {1,S}
4    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 990,
    label = "C_rad_Br/HC",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Br1s  u0 {1,S}
3    H  u0 {1,S}
4    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 989,
    label = "C_rad_Br/Cd",
    group =
"""
1 *1 C u1 {2,S} {3,D}
2 *2 Br1s  u0 {1,S}
3    Cd  u0 {1,D}

""",
    kinetics = None,
)

entry(
    index = 988,
    label = "C_rad_Br/O2d",
    group =
"""
1 *1 C u1 {2,S} {3,D}
2 *2 Br1s  u0 {1,S}
3    O2d  u0 {1,D}

""",
    kinetics = None,
)


entry(
    index = 143,
    label = "Xbirad_Br",
    group = "OR{C_triplet_Br2, C_triplet_HBr, C_triplet_OBr, C_singlet_HBr, C_singlet_Br2, C_singlet_OBr}",
    kinetics = None,
)

entry(
    index = 144,
    label = "C_triplet_Br2",
    group =
"""
1 *1 C  u2 {2,S} {3,S}
2 *2 Br1s  u0 {1,S}
3    Br1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1440,
    label = "C_triplet_HBr",
    group =
"""
1 *1 C  u2 {2,S} {3,S}
2 *2 Br1s  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1441,
    label = "C_triplet_OBr",
    group =
"""
1 *1 C  u2 {2,S} {3,S}
2 *2 Br1s  u0 {1,S}
3    O2s  u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 145,
    label = "C_singlet_Br2",
    group =
"""
1 *1 C u0 p1 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1450,
    label = "C_singlet_HBr",
    group =
"""
1 *1 C u0 p1 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1451,
    label = "C_singlet_OBr",
    group =
"""
1 *1 C u0 p1 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    O2s u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 146,
    label = "Xtrirad_Br",
    group = "OR{C_quartet_Br, C_doublet_Br}",
    kinetics = None,
)

entry(
    index = 147,
    label = "C_quartet_Br",
    group =
"""
1 *1 C u3 p0 {2,S}
2 *2 Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "C_doublet_Br",
    group =
"""
1 *1 C u1 p1 {2,S}
2 *2 Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet}",
    kinetics = None,
)


entry(
    index = 150,
    label = "C_quintet",
    group =
"""
1 *3 C u4 p0
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "C_triplet",
    group =
"""
1 *3 C u2 p1
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "Y_1centertrirad",
    group = "OR{C_H_Br_quartet, C_H_Br_doublet}",
    kinetics = None,
)


entry(
    index = 153,
    label = "C_H_Br_quartet",
    group =
"""
1 *3 C u3 p0 {2,S}
2    [H,Br1s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "C_H_Br_doublet",
    group =
"""
1 *3 C u1 p1 {2,S}
2    [H,Br1s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "Y_1centerbirad",
    group =
"""
1 *3 [Cs,Cd,CO,CS,O,S,N,Br] u2
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "O_atom_triplet",
    group =
"""
1 *3 O u2
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "CH2_triplet",
    group =
"""
1 *3 Cs u2 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "NH_triplet",
    group =
"""
1 *3 N3s u2 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "Y_rad",
    group =
"""
1 *3 R u1
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "H_rad",
    group =
"""
1 *3 H u1
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "Br_rad",
    group =
"""
1 *3 Br u1
""",
    kinetics = None,
)

entry(
    index = 1610,
    label = "Cl_rad",
    group =
"""
1 *3 Cl u1
""",
    kinetics = None,
)

entry(
    index = 1611,
    label = "F_rad",
    group =
"""
1 *3 F u1
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "Y_2centeradjbirad",
    group =
"""
1 *3 [Ct,O2s,S2s] u1 {2,[S,T]}
2    [Ct,O2s,S2s] u1 {1,[S,T]}
""",
    kinetics = None,
)


entry(
    index = 163,
    label = "O_rad",
    group =
"""
1 *3 O u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1630,
    label = "OO_birad",
    group =
"""
1 *3 O u1 {2,S}
2    O u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1631,
    label = "ROO_rad",
    group =
"""
1 *3 O u1 {2,S}
2    O2s u0 {1,S} {3,S}
3    R u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1632,
    label = "OOH_rad",
    group =
"""
1 *3 O u1 {2,S}
2    O2s u0 {1,S} {3,S}
3    H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "OH_rad",
    group =
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1640,
    label = "OBr_rad",
    group =
"""
1 *3 O u1 {2,S}
2    Br u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "O_sec_rad",
    group =
"""
1 *3 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 166,
    label = "Cd_rad",
    group =
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 167,
    label = "Cs_rad",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

#entry(
#    index = 261,
#    label = "C_methyl",
#    group =
#"""
#1 *3 C u1 {2,S} {3,S} {4,S}
#2    H u0 {1,S}
#3    H u0 {1,S}
#4    H u0 {1,S}
#""",
#    kinetics = None,
#)
#
#entry(
#    index = 26100,
#    label = "C_Chloro",
#    group =
#"""
#1 *3 C u1 {2,S} {3,S} {4,S}
#2    Br u0 {1,S}
#3    Br u0 {1,S}
#4    Br u0 {1,S}
#""",
#    kinetics = None,
#)
#
#entry(
#    index = 262,
#    label = "C_pri_rad",
#    group =
#"""
#1 *3 C   u1 {2,S} {3,S} {4,S}
#2    [H,Br]   u0 {1,S}
#3    [H,Br]   u0 {1,S}
#4    R!H u0 {1,S}
#""",
#    kinetics = None,
#)
#
#
#
#entry(
#    index = 279,
#    label = "C_sec_rad",
#    group =
#"""
#1 *3 C   u1 {2,S} {3,S} {4,S}
#2    [H,Br]   u0 {1,S}
#3    R!H u0 {1,S}
#4    R!H u0 {1,S}
#""",
#    kinetics = None,
#)
#
#
#entry(
#    index = 328,
#    label = "C_ter_rad",
#    group =
#"""
#1 *3 C   u1 {2,S} {3,S} {4,S}
#2    R!H u0 {1,S}
#3    R!H u0 {1,S}
#4    R!H u0 {1,S}
#""",
#    kinetics = None,
#)
#
#entry(
#    index = 329,
#    label = "C_rad/NonDe",
#    group =
#"""
#1 *3 C        u1 {2,S} {3,S} {4,S}
#2    [Cs,O,S] u0 {1,S}
#3    [Cs,O,S] u0 {1,S}
#4    [Cs,O,S] u0 {1,S}
#""",
#    kinetics = None,
#)
#
#entry(
#    index = 344,
#    label = "C_rad/OneDe",
#    group =
#"""
#1 *3 C             u1 {2,S} {3,S} {4,S}
#2    [Cd,Ct,Cb,CO] u0 {1,S}
#3    [Cs,O,S]      u0 {1,S}
#4    [Cs,O,S]      u0 {1,S}
#""",
#    kinetics = None,
#)
#
#
#entry(
#    index = 360,
#    label = "C_rad/TwoDe",
#    group =
#"""
#1 *3 C             u1 {2,S} {3,S} {4,S}
#2    [Cd,Ct,Cb,CO] u0 {1,S}
#3    [Cd,Ct,Cb,CO] u0 {1,S}
#4    [Cs,O,S]      u0 {1,S}
#""",
#    kinetics = None,
#)
#
#entry(
#    index = 379,
#    label = "C_rad/ThreeDe",
#    group =
#"""
#1 *3 C             u1 {2,S} {3,S} {4,S}
#2    [Cd,Ct,Cb,CO] u0 {1,S}
#3    [Cd,Ct,Cb,CO] u0 {1,S}
#4    [Cd,Ct,Cb,CO] u0 {1,S}
#""",
#    kinetics = None,
#)
#

entry(
   index = 168,
   label = "C_pri_HBr2/C_sec_O2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    O2s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 169,
   label = "C_pri_HBr2/C_sec_O_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    H    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 170,
   label = "C_pri_HBr2/C_sec_O_Br",
   group =
"""
1 *1 Cs      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    Br1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)



entry(
   index = 173,
   label = "C_pri_Br3/C_sec_O2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    Br1s       u0 {1,S}
5    Cs       u0  p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    O2s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 174,
   label = "C_pri_Br3/C_sec_O_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    Br1s       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    H    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 175,
   label = "C_pri_Br3/C_sec_O_Br",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s    u0 {1,S}
4    Br1s       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    Br1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)


entry(
   index = 177,
   label = "C_pri_H2Br/C_sec_O2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    H       u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    O2s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 178,
   label = "C_pri_H2Br/C_sec_O_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    H       u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    H    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 179,
   label = "C_pri_H2Br/C_sec_O_Br",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    H       u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    Br1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 180,
   label = "C_pri_H2Br/C_ter_O",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    H     u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    C     u0 {5,S}
8    C      u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 181,
   label = "C_pri_HBr2/C_ter_O",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s     u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    C     u0 {5,S}
8    C      u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 182,
   label = "C_pri_Br3/C_ter_O",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s    u0 {1,S}
3    Br1s     u0 {1,S}
4    Br1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    C     u0 {5,S}
8    C      u0 {5,S}
""",
   kinetics = None,
)


entry(
    index = 183,
    label = "Cs_Br/C_rad",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    C u1 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "Cs_Br/C_rad/C_rad",
    group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *2 Br1s u0 {1,S}
3    C u1 p0 {1,S}
4    C u1 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "Cs_Br/C_rad/C_rad/C_rad",
    group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Br1s u0 {1,S}
3    C u1 p0 {1,S}
4    C u1 p0 {1,S}
5    C u1 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "Cs_Br/C_birad",
    group = "OR{Cs_Br/C_singlet, Cs_Br/C_triplet}",
    kinetics = None,
)

entry(
    index = 187,
    label = "Cs_Br/C_singlet",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    C u0 p1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "Cs_Br/C_triplet",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    C u2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "Cs_Br/C_trirad",
    group = "OR{Cs_Br/C_doublet, Cs_Br/C_quartet}",
    kinetics = None,
)

entry(
    index = 190,
    label = "Cs_Br/C_doublet",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    C u1 p1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "Cs_Br/C_quartet",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 Br1s u0 {1,S}
3    C u3  {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: X_Br_or_Xrad_Br_Xbirad_Br_Xtrirad_Br
    L2: Xtrirad_Br
        L3: C_quartet_Br
        L3: C_doublet_Br
    L2: Xbirad_Br
        L3: C_triplet_Br2
        L3: C_triplet_HBr
        L3: C_triplet_OBr
        L3: C_singlet_Br2
        L3: C_singlet_HBr
        L3: C_singlet_OBr
    L2: Xrad_Br
        L3: O_rad_Br
        L3: C_rad_Br
            L4: C_rad_Br/Br
                L5: C_rad_Br/BrBr
                L5: C_rad_Br/BrH
                L5: C_rad_Br/BrC
                    L6: C_rad_Br/BrCt
                    L6: C_rad_Br/BrCd
                    L6: C_rad_Br/BrCs
                L5: C_rad_Br/BrO
            L4: C_rad_Br/CC
            L4: C_rad_Br/CO
            L4: C_rad_Br/OO
            L4: C_rad_Br/HH
            L4: C_rad_Br/HO
            L4: C_rad_Br/HC
            L4: C_rad_Br/Cd
            L4: C_rad_Br/O2d
    L2: X_Br
        L3: O_Br
            L4: HO_Br
            L4: BrO_Br
            L4: OO_Br
            L4: O_rad_O_Br
            L4: C_rad_O_Br
            L4: CO_Br
                L5: CsO_Br
                L5: CdO_Br
                L5: CtO_Br
        L3: Br2
        L3: HBr
        L3: Ct_Br
            L4: Ct/Br/NonDeC
            L4: Ct/Br/NonDeN
        L3: Cd_Br
            L4: Cd_pri
            L4: Cd_sec
            L4: Cd_allenic
        L3: Cs_Br
            L4: Cs_Br2
                L5: Cs_Br2_H2
                L5: Cs_Br2_O2s_O2s
                L5: Cs_Br2_O2s_H
                L5: C_pri_HBr2
                    L6: C_pri_HBr2/C_sec_Br2
                    L6: C_pri_HBr2/C_sec_HBr
                    L6: C_pri_HBr2/C_sec_H2
                    L6: C_pri_HBr2/C_sec_O2
                    L6: C_pri_HBr2/C_sec_O_H
                    L6: C_pri_HBr2/C_sec_O_Br
                    L6: C_pri_HBr2/C_ter_Br
                    L6: C_pri_HBr2/C_ter_H
                    L6: C_pri_HBr2/C_ter_O
                L5: C_sec_Br2
                L5: Cs_Br3
                    L6: Cs_Br4
                    L6: Cs_Br3_O2s
                    L6: C_pri_Br3
                        L7: C_pri_Br3/C_sec_Br2
                        L7: C_pri_Br3/C_sec_HBr
                        L7: C_pri_Br3/C_sec_H2
                        L7: C_pri_Br3/C_sec_O2
                        L7: C_pri_Br3/C_sec_O_H
                        L7: C_pri_Br3/C_sec_O_Br
                        L7: C_pri_Br3/C_ter_Br
                        L7: C_pri_Br3/C_ter_H
                        L7: C_pri_Br3/C_ter_O
            L4: C_pri_H2Br
                L5: C_pri_H2Br/C_sec_H2
                L5: C_pri_H2Br/C_sec_HBr
                L5: C_pri_H2Br/C_sec_Br2
                L5: C_pri_H2Br/C_sec_O2
                L5: C_pri_H2Br/C_sec_O_H
                L5: C_pri_H2Br/C_sec_O_Br
                L5: C_pri_H2Br/C_ter_H
                L5: C_pri_H2Br/C_ter_Br
                L5: C_pri_H2Br/C_ter_O
            L4: C_sec_HBr
            L4: C_ter_Br
            L4: Cs_Br_H2_O2s
            L4: Cs_Br_H_O2s_C
            L4: Cs_Br/C_rad
                L5: Cs_Br/C_rad/C_rad
                    L6: Cs_Br/C_rad/C_rad/C_rad
            L4: Cs_Br/C_birad
                L5: Cs_Br/C_singlet
                L5: Cs_Br/C_triplet
            L4: Cs_Br/C_trirad
                L5: Cs_Br/C_doublet
                L5: Cs_Br/C_quartet


L1: Y_rad_birad_trirad_quadrad
    L2: Y_1centerquadrad
        L3: C_quintet
        L3: C_triplet
    L2: Y_1centertrirad
        L3: C_H_Br_quartet
        L3: C_H_Br_doublet
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: CH2_triplet
        L3: NH_triplet
    L2: Y_rad
        L3: OO_birad
        L3: H_rad
        L3: Br_rad
        L3: F_rad
        L3: Cl_rad
        L3: Y_2centeradjbirad
        L3: O_rad
            L4: ROO_rad
                L5: OOH_rad
            L4: OH_rad
            L4: OBr_rad
            L4: O_sec_rad
        L3: Cs_rad
        L3: Cd_rad

"""
)

forbidden(
    label = "OS_birad_singlet",
    group =
"""
1 *3 [O,S] u0 p3
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "birad_singlet",
    group =
"""
1 *3 [C,N,Si] u0 p1
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "quadrad_singlet",
    group =
"""
1 *3 [C,N,Si] u0 p2
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)


forbidden(
    label = "disprop1",
    group =
"""
1 *1 R u0 {2,S} {3,S}
2    C u1 {1,S}
3 *2 Br u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "disprop2",
    group =
"""
1 *1 R u0 {2,S} {3,S}
2    R u0 {1,S} {4,D}
3 *2 Br u0 {1,S}
4    R u0 {2,D} {5,S}
5    R u1 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "disprop3",
    group =
"""
1 *1 R u0 {2,S} {3,S}
2    R u0 {1,S} {4,T}
3 *2 Br u0 {1,S}
4    R u0 {2,T} {5,S}
5    R u1 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "disprop4",
    group =
"""
1 *1 R u0 {2,S} {3,S}
2    R u0 {1,S} {4,D}
3 *2 Br u0 {1,S}
4    R u0 {2,D} {5,S}
5    R u0 {4,S} {6,D}
6    R u0 {5,D} {7,S}
7    R u1 {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "disprop5",
    group =
"""
1 *1 R u0 {2,S} {3,S}
2    R u0 {1,S} {4,D}
3 *2 Br u0 {1,S}
4    R u0 {2,D} {5,S}
5    R u0 {4,S} {6,D}
6    R u0 {5,D} {7,S}
7    R u1 {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "disprop6",
    group =
"""
1 *2 Br u0 p0 c0 {2,S} {3,S} {4,S} {5,S} {6,S} {7,S} {8,S}
2 *1 C  u3 p0 c0 {1,S}
3    R  u0 p0 c0 {1,S}
4    R  u0 p0 c0 {1,S}
5    R  u0 p0 c0 {1,S}
6    R  u0 p0 c0 {1,S}
7    R  u0 p0 c0 {1,S}
8    R  u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)


forbidden(
    label = "disprop7",
    group =
"""
1 *1 C  u3 p0 c0 {2,S}
2 *2 Br u0 p0 c0 {1,S} {3,S} {4,S} {5,S} {6,S} {7,S} {8,S}
3    R  u0 p0 c0 {2,S}
4    R  u0 p0 c0 {2,S}
5    R  u0 p0 c0 {2,S}
6    R  u0 p0 c0 {2,S}
7    R  u0 p0 c0 {2,S}
8    R  u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)
