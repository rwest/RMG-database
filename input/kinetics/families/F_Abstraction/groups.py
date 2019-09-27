#!/usr/bin/env python
# encoding: utf-8

name = "F_Abstraction/groups"
shortDesc = u""
longDesc = u"""
The reaction site *3 needs a lone pair in order to react. It cannot be 2S or 4S.
"""

template(reactants=["X_F_or_Xrad_F_Xbirad_F_Xtrirad_F", "Y_rad_birad_trirad_quadrad"], products=["X_F_or_Xrad_F_Xbirad_F_Xtrirad_F", "Y_rad_birad_trirad_quadrad"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*2', 1, '*3'],
    ['GAIN_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "X_F_or_Xrad_F_Xbirad_F_Xtrirad_F",
    group = "OR{X_F, Xrad_F, Xbirad_F, Xtrirad_F}",
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
    label = "X_F",
    group =
"""
1 *1 R u0 {2,S}
2 *2 F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "F2",
    group =
"""
1 *1 F1s u0 {2,S}
2 *2 F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "HF",
    group =
"""
1 *1 H u0 {2,S}
2 *2 F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Ct_F",
    group =
"""
1 *1 Ct    u0 {2,S} {3,T}
2 *2 F1s     u0 {1,S}
3    [C,N] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Ct/F/NonDeC",
    group =
"""
1 *1 Ct u0 {2,S} {3,T}
2 *2 F1s  u0 {1,S}
3    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Ct/F/NonDeN",
    group =
"""
1 *1 Ct  u0 {2,S} {3,T}
2 *2 F1s   u0 {1,S}
3    N3t u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Cd_F",
    group =
"""
1 *1 C     u0 {2,D} {3,S} {4,S}
2    C u0 {1,D}
3 *2 F1s     u0 {1,S}
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
3 *2 F1s     u0 {1,S}
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
3 *2 F1s   u0 {1,S}
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
3 *2 F1s u0 {1,S}
4 R u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 60,
    label = "Cs_F",
    group =
"""
1 *1 Cs u0 {2,S}
2 *2 F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Cs_F2",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 610,
    label = "Cs_F2_H2",
    group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s u0 {1,S}
3    F1s u0 {1,S}
4    H u0 {1,S}
5    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 611,
    label = "Cs_F3",
    group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *2 F1s u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 612,
    label = "Cs_F4",
    group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {1,S}
""",
    kinetics = None,
)

#entry(
#    index = 61,
#    label = "C_methane",
#    group =
#"""
#1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
#2 *2 F u0 {1,S}
#3    [H,F] u0 {1,S}
#4    [H,F] u0 {1,S}
#5    [H,F] u0 {1,S}
#""",
#    kinetics = None,
#)
#

entry(
   index = 62,
   label = "C_pri_F3",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    F1s    u0 {1,S}
5    C     u0  p0 {1,S}
""",
   kinetics = None,
)

entry(
   index = 63,
   label = "C_pri_HF2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    H    u0 {1,S}
5    C     u0 p0 {1,S}
""",
   kinetics = None,
)

entry(
   index = 64,
   label = "C_pri_H2F",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    H       u0 {1,S}
4    H       u0 {1,S}
5    C     u0 p0 {1,S}
""",
   kinetics = None,
)

entry(
   index = 65,
   label = "C_pri_F3/C_sec_H2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    F1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H       u0 {5,S}
7    H       u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 66,
   label = "C_pri_F3/C_sec_HF",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    F1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    F1s       u0 {5,S}
7    H       u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 67,
   label = "C_pri_F3/C_sec_F2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    F1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    F1s    u0 {5,S}
7    F1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 68,
   label = "C_pri_HF2/C_sec_H2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
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
   label = "C_pri_HF2/C_sec_HF",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    H       u0 {1,S}
5    Cs      u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H       u0 {5,S}
7    F1s    u0 {5,S}
8    C    u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 70,
   label = "C_pri_HF2/C_sec_F2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    F1s    u0 {5,S}
7    F1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 71,
   label = "C_pri_H2F/C_sec_H2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
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
   label = "C_pri_H2F/C_sec_HF",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H    u0 {5,S}
7    F1s    u0 {5,S}
8    C      u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 73,
   label = "C_pri_H2F/C_sec_F2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    F1s   u0 {5,S}
7    F1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)


entry(
    index = 74,
    label = "C_sec_F2",
    group =
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s   u0 {1,S}
3    F1s   u0 {1,S}
4    C   u0  p0 {1,S}
5    C   u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "C_sec_HF",
    group =
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s   u0 {1,S}
3    H   u0 {1,S}
4    C   u0 p0 {1,S}
5    C   u0 p0 {1,S}
""",
    kinetics = None,
)

# entry(
#     index = 76,
#     label = "C_sec_F2/C_pri_F3",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    F1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    F1s u0 {5,S}
# 7    F1s u0 {5,S}
# 8    F1s u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 77,
#     label = "C_sec_HF/C_pri_F3",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    F1s u0 {5,S}
# 7    F1s u0 {5,S}
# 8    F1s u0 {5,S}
# """,
#     kinetics = None,
# )
#
# entry(
#     index = 78,
#     label = "C_sec_F2/C_pri_HF2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    F1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    F1s u0 {5,S}
# 8    F1s u0 {5,S}
# """,
#     kinetics = None,
# )
#
# entry(
#     index = 79,
#     label = "C_sec_HF/C_pri_HF2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    F1s u0 {5,S}
# 8    F1s u0 {5,S}
# """,
#     kinetics = None,
# )
#
#
# entry(
#     index = 80,
#     label = "C_sec_F2/C_pri_H2F",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    F1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    H u0 {5,S}
# 8    F1s u0 {5,S}
# """,
#     kinetics = None,
# )
#
# entry(
#     index = 81,
#     label = "C_sec_HF/C_pri_H2F",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    H u0 {5,S}
# 8    F1s u0 {5,S}
# """,
#     kinetics = None,
# )
#
# entry(
#     index = 82,
#     label = "C_sec_F2/C_pri_H3",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    F1s   u0 {1,S}
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
#     label = "C_sec_HF/C_pri_H3",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
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
#     label = "C_sec_F2/C_sec_F2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    F1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    F1s u0 {5,S}
# 7    F1s u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 85,
#     label = "C_sec_HF/C_sec_F2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    F1s u0 {5,S}
# 7    F1s u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 86,
#     label = "C_sec_F2/C_sec_HF",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    F1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    F1s u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 87,
#     label = "C_sec_HF/C_sec_HF",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    H  u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    H u0 {5,S}
# 7    F1s u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )


# entry(
#     index = 88,
#     label = "C_sec_F2/C_sec_H2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    F1s   u0 {1,S}
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
#     label = "C_sec_HF/C_sec_H2",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
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
   label = "C_pri_F3/C_ter_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    F1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    H    u0 {5,S}
7    C    u0 {5,S}
8    C    u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 91,
   label = "C_pri_F3/C_ter_F",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    F1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    F1s    u0 {5,S}
7    C    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 92,
   label = "C_pri_HF2/C_ter_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
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
   label = "C_pri_HF2/C_ter_F",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    F1s    u0 {5,S}
7    C    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 94,
   label = "C_pri_H2F/C_ter_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
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
   label = "C_pri_H2F/C_ter_F",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    H     u0 {1,S}
4    H    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    F1s    u0 {5,S}
7    C     u0 {5,S}
8    C      u0 {5,S}
""",
   kinetics = None,
)

# entry(
#     index = 96,
#     label = "C_sec_F2/C_ter_H",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    F1s   u0 {1,S}
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
#     label = "C_sec_F2/C_ter_F",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    F1s   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    F1s u0 {5,S}
# 7    R!H u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 98,
#     label = "C_sec_HF/C_ter_F",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
# 3    H   u0 {1,S}
# 4    R!H  u0 {1,S}
# 5    C    u0 {1,S} {6,S} {7,S} {8,S}
# 6    F1s u0 {5,S}
# 7    R!H u0 {5,S}
# 8    R!H u0 {5,S}
# """,
#     kinetics = None,
# )

# entry(
#     index = 99,
#     label = "C_sec_HF/C_ter_H",
#     group =
# """
# 1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
# 2 *2 F1s   u0 {1,S}
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
   label = "Cs_F3_O2s",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    F1s    u0 {1,S}
5    O2s     u0 {1,S}
""",
   kinetics = None,
)

entry(
   index = 101,
   label = "Cs_F2_O2s_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    H       u0 {1,S}
5    O2s     u0 {1,S}
""",
   kinetics = None,
)

entry(
   index = 102,
   label = "Cs_F_H2_O2s",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    H    u0 {1,S}
4    H       u0 {1,S}
5    O2s     u0 {1,S}
""",
   kinetics = None,
)

entry(
    index = 103,
    label = "Cs_F2_O2s_O2s",
    group =
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s   u0 {1,S}
3    F1s   u0 {1,S}
4    O2s u0 {1,S}
5    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Cs_F_H_O2s_C",
    group =
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s   u0 {1,S}
3    H   u0 {1,S}
4    O2s u0 {1,S}
5    C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "C_ter_F",
    group =
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s   u0 {1,S}
3    C u0 {1,S}
4    C u0 {1,S}
5    C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "O_F",
    group =
"""
1 *1 O2s u0 {2,S}
2 *2 F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "HO_F",
    group =
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    H    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "FO_F",
    group =
"""
1 *1 O2s  u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "OO_F",
    group =
"""
1 *1 O2s  u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1350,
    label = "O_rad_O_F",
    group =
"""
1 *1 O2s  u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    O2s  u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1351,
    label = "C_rad_O_F",
    group =
"""
1 *1 O2s  u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    C    u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1352,
    label = "CO_F",
    group =
"""
1 *1 O2s  u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    C    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "CsO_F",
    group =
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "CdO_F",
    group =
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    Cd  u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 138,
    label = "CtO_F",
    group =
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    Ct   u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 140,
    label = "Xrad_F",
    group =
"""
1 *1 R!H u1 {2,S}
2 *2 F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1400,
    label = "O_rad_F",
    group =
"""
1 *1 O u1 {2,S}
2 *2 F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "C_rad_F",
    group =
"""
1 *1 C u1 {2,S}
2 *2 F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "C_rad_F/F",
    group =
"""
1 *1 Cs    u1 {2,S} {3,S}
2 *2 F1s  u0 {1,S}
3    F1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1420,
    label = "C_rad_F/FF",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1421,
    label = "C_rad_F/FH",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    F1s  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1422,
    label = "C_rad_F/FC",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    F1s  u0 {1,S}
4    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 999,
    label = "C_rad_F/FCs",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    F1s  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 998,
    label = "C_rad_F/FCd",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    F1s  u0 {1,S}
4    Cd  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 997,
    label = "C_rad_F/FCt",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    F1s  u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 996,
    label = "C_rad_F/FO",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    F1s  u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 995,
    label = "C_rad_F/CC",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    C  u0 {1,S}
4    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 994,
    label = "C_rad_F/CO",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    C  u0 {1,S}
4    O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 993,
    label = "C_rad_F/OO",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    O2s  u0 {1,S}
4    O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 992,
    label = "C_rad_F/HH",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 991,
    label = "C_rad_F/HO",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    H  u0 {1,S}
4    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 990,
    label = "C_rad_F/HC",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 F1s  u0 {1,S}
3    H  u0 {1,S}
4    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 989,
    label = "C_rad_F/Cd",
    group =
"""
1 *1 C u1 {2,S} {3,D}
2 *2 F1s  u0 {1,S}
3    Cd  u0 {1,D}

""",
    kinetics = None,
)

entry(
    index = 988,
    label = "C_rad_F/O2d",
    group =
"""
1 *1 C u1 {2,S} {3,D}
2 *2 F1s  u0 {1,S}
3    O2d  u0 {1,D}

""",
    kinetics = None,
)


entry(
    index = 143,
    label = "Xbirad_F",
    group = "OR{C_triplet_F2, C_triplet_HF, C_triplet_OF, C_singlet_HF, C_singlet_F2, C_singlet_OF}",
    kinetics = None,
)

entry(
    index = 144,
    label = "C_triplet_F2",
    group =
"""
1 *1 C  u2 {2,S} {3,S}
2 *2 F1s  u0 {1,S}
3    F1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1440,
    label = "C_triplet_HF",
    group =
"""
1 *1 C  u2 {2,S} {3,S}
2 *2 F1s  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1441,
    label = "C_triplet_OF",
    group =
"""
1 *1 C  u2 {2,S} {3,S}
2 *2 F1s  u0 {1,S}
3    O2s  u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 145,
    label = "C_singlet_F2",
    group =
"""
1 *1 C u0 p1 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1450,
    label = "C_singlet_HF",
    group =
"""
1 *1 C u0 p1 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1451,
    label = "C_singlet_OF",
    group =
"""
1 *1 C u0 p1 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    O2s u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 146,
    label = "Xtrirad_F",
    group = "OR{C_quartet_F, C_doublet_F}",
    kinetics = None,
)

entry(
    index = 147,
    label = "C_quartet_F",
    group =
"""
1 *1 C u3 p0 {2,S}
2 *2 F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "C_doublet_F",
    group =
"""
1 *1 C u1 p1 {2,S}
2 *2 F1s u0 {1,S}
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
    group = "OR{C_H_F_quartet, C_H_F_doublet}",
    kinetics = None,
)


entry(
    index = 153,
    label = "C_H_F_quartet",
    group =
"""
1 *3 C u3 p0 {2,S}
2    [H,F1s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "C_H_F_doublet",
    group =
"""
1 *3 C u1 p1 {2,S}
2    [H,F1s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "Y_1centerbirad",
    group =
"""
1 *3 [Cs,Cd,CO,CS,O,S,N,F] u2
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
    label = "F_rad",
    group =
"""
1 *3 F u1
""",
    kinetics = None,
)

entry(
    index = 1610,
    label = "Br_rad",
    group =
"""
1 *3 Br u1
""",
    kinetics = None,
)

entry(
    index = 1611,
    label = "Cl_rad",
    group =
"""
1 *3 Cl u1
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
    label = "OF_rad",
    group =
"""
1 *3 O u1 {2,S}
2    F u0 {1,S}
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
#2    F u0 {1,S}
#3    F u0 {1,S}
#4    F u0 {1,S}
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
#2    [H,F]   u0 {1,S}
#3    [H,F]   u0 {1,S}
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
#2    [H,F]   u0 {1,S}
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
   label = "C_pri_HF2/C_sec_O2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
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
   label = "C_pri_HF2/C_sec_O_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
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
   label = "C_pri_HF2/C_sec_O_F",
   group =
"""
1 *1 Cs      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    F1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)



entry(
   index = 173,
   label = "C_pri_F3/C_sec_O2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    F1s       u0 {1,S}
5    Cs       u0  p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    O2s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 174,
   label = "C_pri_F3/C_sec_O_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    F1s       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    H    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 175,
   label = "C_pri_F3/C_sec_O_F",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s    u0 {1,S}
4    F1s       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    F1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)


entry(
   index = 177,
   label = "C_pri_H2F/C_sec_O2",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
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
   label = "C_pri_H2F/C_sec_O_H",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
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
   label = "C_pri_H2F/C_sec_O_F",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    H       u0 {1,S}
4    H       u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    F1s    u0 {5,S}
8    C     u0 {5,S}
""",
   kinetics = None,
)

entry(
   index = 180,
   label = "C_pri_H2F/C_ter_O",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
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
   label = "C_pri_HF2/C_ter_O",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s     u0 {1,S}
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
   label = "C_pri_F3/C_ter_O",
   group =
"""
1 *1 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s    u0 {1,S}
3    F1s     u0 {1,S}
4    F1s    u0 {1,S}
5    Cs       u0 p0 {1,S} {6,S} {7,S} {8,S}
6    O2s    u0 {5,S}
7    C     u0 {5,S}
8    C      u0 {5,S}
""",
   kinetics = None,
)


entry(
    index = 183,
    label = "Cs_F/C_rad",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    C u1 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "Cs_F/C_rad/C_rad",
    group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *2 F1s u0 {1,S}
3    C u1 p0 {1,S}
4    C u1 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "Cs_F/C_rad/C_rad/C_rad",
    group =
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 F1s u0 {1,S}
3    C u1 p0 {1,S}
4    C u1 p0 {1,S}
5    C u1 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "Cs_F/C_birad",
    group = "OR{Cs_F/C_singlet, Cs_F/C_triplet}",
    kinetics = None,
)

entry(
    index = 187,
    label = "Cs_F/C_singlet",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    C u0 p1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "Cs_F/C_triplet",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    C u2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "Cs_F/C_trirad",
    group = "OR{Cs_F/C_doublet, Cs_F/C_quartet}",
    kinetics = None,
)

entry(
    index = 190,
    label = "Cs_F/C_doublet",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    C u1 p1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "Cs_F/C_quartet",
    group =
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 F1s u0 {1,S}
3    C u3  {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: X_F_or_Xrad_F_Xbirad_F_Xtrirad_F
    L2: Xtrirad_F
        L3: C_quartet_F
        L3: C_doublet_F
    L2: Xbirad_F
        L3: C_triplet_F2
        L3: C_triplet_HF
        L3: C_triplet_OF
        L3: C_singlet_F2
        L3: C_singlet_HF
        L3: C_singlet_OF
    L2: Xrad_F
        L3: O_rad_F
        L3: C_rad_F
            L4: C_rad_F/F
                L5: C_rad_F/FF
                L5: C_rad_F/FH
                L5: C_rad_F/FC
                    L6: C_rad_F/FCt
                    L6: C_rad_F/FCd
                    L6: C_rad_F/FCs
                L5: C_rad_F/FO
            L4: C_rad_F/CC
            L4: C_rad_F/CO
            L4: C_rad_F/OO
            L4: C_rad_F/HH
            L4: C_rad_F/HO
            L4: C_rad_F/HC
            L4: C_rad_F/Cd
            L4: C_rad_F/O2d
    L2: X_F
        L3: O_F
            L4: HO_F
            L4: FO_F
            L4: OO_F
            L4: O_rad_O_F
            L4: C_rad_O_F
            L4: CO_F
                L5: CsO_F
                L5: CdO_F
                L5: CtO_F
        L3: F2
        L3: HF
        L3: Ct_F
            L4: Ct/F/NonDeC
            L4: Ct/F/NonDeN
        L3: Cd_F
            L4: Cd_pri
            L4: Cd_sec
            L4: Cd_allenic
        L3: Cs_F
            L4: Cs_F2
                L5: Cs_F2_H2
                L5: Cs_F2_O2s_O2s
                L5: Cs_F2_O2s_H
                L5: C_pri_HF2
                    L6: C_pri_HF2/C_sec_F2
                    L6: C_pri_HF2/C_sec_HF
                    L6: C_pri_HF2/C_sec_H2
                    L6: C_pri_HF2/C_sec_O2
                    L6: C_pri_HF2/C_sec_O_H
                    L6: C_pri_HF2/C_sec_O_F
                    L6: C_pri_HF2/C_ter_F
                    L6: C_pri_HF2/C_ter_H
                    L6: C_pri_HF2/C_ter_O
                L5: C_sec_F2
                L5: Cs_F3
                    L6: Cs_F4
                    L6: Cs_F3_O2s
                    L6: C_pri_F3
                        L7: C_pri_F3/C_sec_F2
                        L7: C_pri_F3/C_sec_HF
                        L7: C_pri_F3/C_sec_H2
                        L7: C_pri_F3/C_sec_O2
                        L7: C_pri_F3/C_sec_O_H
                        L7: C_pri_F3/C_sec_O_F
                        L7: C_pri_F3/C_ter_F
                        L7: C_pri_F3/C_ter_H
                        L7: C_pri_F3/C_ter_O
            L4: C_pri_H2F
                L5: C_pri_H2F/C_sec_H2
                L5: C_pri_H2F/C_sec_HF
                L5: C_pri_H2F/C_sec_F2
                L5: C_pri_H2F/C_sec_O2
                L5: C_pri_H2F/C_sec_O_H
                L5: C_pri_H2F/C_sec_O_F
                L5: C_pri_H2F/C_ter_H
                L5: C_pri_H2F/C_ter_F
                L5: C_pri_H2F/C_ter_O
            L4: C_sec_HF
            L4: C_ter_F
            L4: Cs_F_H2_O2s
            L4: Cs_F_H_O2s_C
            L4: Cs_F/C_rad
                L5: Cs_F/C_rad/C_rad
                    L6: Cs_F/C_rad/C_rad/C_rad
            L4: Cs_F/C_birad
                L5: Cs_F/C_singlet
                L5: Cs_F/C_triplet
            L4: Cs_F/C_trirad
                L5: Cs_F/C_doublet
                L5: Cs_F/C_quartet


L1: Y_rad_birad_trirad_quadrad
    L2: Y_1centerquadrad
        L3: C_quintet
        L3: C_triplet
    L2: Y_1centertrirad
        L3: C_H_F_quartet
        L3: C_H_F_doublet
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: CH2_triplet
        L3: NH_triplet
    L2: Y_rad
        L3: OO_birad
        L3: H_rad
        L3: F_rad
        L3: Cl_rad
        L3: Br_rad
        L3: Y_2centeradjbirad
        L3: O_rad
            L4: ROO_rad
                L5: OOH_rad
            L4: OH_rad
            L4: OF_rad
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
3 *2 F u0 {1,S}
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
3 *2 F u0 {1,S}
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
3 *2 F u0 {1,S}
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
3 *2 F u0 {1,S}
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
3 *2 F u0 {1,S}
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
1 *2 F u0 p0 c0 {2,S} {3,S} {4,S} {5,S} {6,S} {7,S} {8,S}
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
2 *2 F u0 p0 c0 {1,S} {3,S} {4,S} {5,S} {6,S} {7,S} {8,S}
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
