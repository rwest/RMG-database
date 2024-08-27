#!/usr/bin/env python
# encoding: utf-8

name = "CF_Radical_Formation_3/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(5.43e+12,'s^-1'), n=0.46, w0=(572.5,'kJ/mol'), E0=(65.6686,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 1 training reactions at node Root
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

