#!/usr/bin/env python
# encoding: utf-8

name = "Metal Binding Energies"
shortDesc = u""
longDesc = """
Metal binding energies and surface site densities
"""

entry(
    index = 0,
    label = "Pt",
    bindingEnergies = "Pt111",
    metal = "Pt", 
    shortDesc = u"Pt111 data",
    longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
    """,
)

entry(
    index = 1,
    label = "Pt111",
    bindingEnergies = {
    		           'H':(-2.75367887E+00, 'eV/molecule'),
                       'C':(-7.02515507E+00, 'eV/molecule'),
                       'N':(-4.63224568E+00, 'eV/molecule'),
                       'O':(-3.81153179E+00, 'eV/molecule'),
                       'H2O': (-0.23, 'eV/molecule'),
                       'NH3': (-0.78, 'eV/molecule'),
    },
    surfaceSiteDensity = (2.483E-09, 'mol/cm^2'),
    facet = "111",
    metal = "Pt",
    shortDesc = u"fcc",
    longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
    """,
)

entry(
    index = 2,
    label = "Ru0001",
    bindingEnergies = {
    		           'H':(-2.85191775E+00, 'eV/molecule'),
                       'C':(-7.59790076E+00, 'eV/molecule'),
                       'N':(-5.96899731E+00, 'eV/molecule'),
                       'O':(-5.44919557E+00, 'eV/molecule'),
    },
    surfaceSiteDensity = (2.630E-09, 'mol/cm^2'),
    facet = "0001",
    metal = "Ru",
    shortDesc = u"hcp",
    longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
    """,
)

entry(
    index = 3,
    label = "Rh111",
    bindingEnergies = {
    		           'H':(-2.83000775E+00, 'eV/molecule'),
                       'C':(-7.33483762E+00, 'eV/molecule'),
                       'N':(-5.30055389E+00, 'eV/molecule'),
                       'O':(-4.71419163E+00, 'eV/molecule'),
                       'H2O': (-0.31, 'eV/molecule'),
                       'NH3': (-0.80, 'eV/molecule'),
    },
    surfaceSiteDensity = (2.656E-09, 'mol/cm^2'),
    facet = "111",
    metal = "Rh",
    shortDesc = u"fcc",
    longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
    """,
)

entry(
     index = 4,
     label = "Ir111",
     bindingEnergies = {
     		          'H':(-2.67673532E+00, 'eV/molecule'),
                        'C':(-7.25234155E+00, 'eV/molecule'),
                        'N':(-5.06204488E+00, 'eV/molecule'),
                        'O':(-4.35235655E+00, 'eV/molecule'),
                        'H2O': (-0.28, 'eV/molecule'),
                         'NH3': (-0.88, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.587E-09, 'mol/cm^2'),
     facet = "111",
     metal = "Ir",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 5,
     label = "Au111",
     bindingEnergies = {
     		          'H':(-2.20847988E+00, 'eV/molecule'),
                        'C':(-4.54649977E+00, 'eV/molecule'),
                        'N':(-2.41077552E+00, 'eV/molecule'),
                        'O':(-2.71822397E+00, 'eV/molecule'),
                        'H2O': (-0.16, 'eV/molecule'),
                         'NH3': (-0.34, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.270E-09, 'mol/cm^2'),
     facet = "111",
     metal = "Au",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 6,
     label = "Pd111",
     bindingEnergies = {
     		            'H':(-2.92248796E+00, 'eV/molecule'),
                        'C':(-7.16786381E+00, 'eV/molecule'),
                        'N':(-4.78495869E+00, 'eV/molecule'),
                        'O':(-4.13577325E+00, 'eV/molecule'),
                        'H2O': (-0.25, 'eV/molecule'),
                        'NH3': (-0.65, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.534E-09, 'mol/cm^2'),
     facet = "111",
     metal = "Pd",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 7,
     label = "Cu111",
     bindingEnergies = {
     		            'H':(-2.58383235E+00, 'eV/molecule'),
                        'C':(-4.96033553E+00, 'eV/molecule'),
                        'N':(-3.58446699E+00, 'eV/molecule'),
                        'O':(-4.20763879E+00, 'eV/molecule'),
                        'H2O': (-0.18, 'eV/molecule'),
                         'NH3': (-0.42, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.943E-09, 'mol/cm^2'),
     facet = "111",
     metal = "Cu",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 8,
     label = "Ag111",
     bindingEnergies = {
     		            'H':(-2.10526806E+00, 'eV/molecule'),
                        'C':(-3.50609006E+00, 'eV/molecule'),
                        'N':(-1.97973590E+00, 'eV/molecule'),
                        'O':(-3.11159241E+00, 'eV/molecule'),
                        'H2O': (-0.17, 'eV/molecule'),
                        'NH3': (-0.31, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.292E-09, 'mol/cm^2'),
     facet = "111",
     metal = "Ag",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 9,
     label = "Ni111",
     bindingEnergies = {
     		            'H':(-2.89202876E+00, 'eV/molecule'),
                        'C':(-6.79794124E+00, 'eV/molecule'),
                        'N':(-5.16380660E+00, 'eV/molecule'),
                        'O':(-4.98902184E+00, 'eV/molecule'),
                        'H2O': (-0.24, 'eV/molecule'),
                         'NH3': (-0.63, 'eV/molecule'),
     },
     surfaceSiteDensity = (3.148E-09, 'mol/cm^2'),
     facet = "111",
     metal = "Ni",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 10,
     label = "Co0001",
     bindingEnergies = {
     		            'H':(-3.02058996E+00, 'eV/molecule'),
                        'C':(-7.09132929E+00, 'eV/molecule'),
                        'N':(-5.58560836E+00, 'eV/molecule'),
                        'O':(-5.38367940E+00, 'eV/molecule'),
     },
     surfaceSiteDensity = (3.118E-09, 'mol/cm^2'),
     facet = "0001",
     metal = "Co",
     shortDesc = u"hcp",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
     """,
)

entry(
     index = 11,
     label = "Pt211",
     bindingEnergies = {
     		            'H':(-2.890, 'eV/molecule'),
                        'C':(-7.205, 'eV/molecule'),
                        'N':(-4.635, 'eV/molecule'),
                        'O':(-4.150, 'eV/molecule'),
                        'H2O': (-0.31, 'eV/molecule'),
                         'NH3': (-0.90, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.634E-09, 'mol/cm^2'),
     facet = "211",
     metal = "Pt",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 12,
     label = "Rh211",
     bindingEnergies = {
     		            'H':(-2.828048658, 'eV/molecule'),
                        'C':(-7.805735262, 'eV/molecule'),
                        'N':(-5.491597358, 'eV/molecule'),
                        'O':(-4.776603013, 'eV/molecule'),
                        'H2O': (-0.44, 'eV/molecule'),
                         'NH3': (-0.84, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.817E-09, 'mol/cm^2'),
     facet = "211",
     metal = "Rh",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 13,
     label = "Ag211",
     bindingEnergies = {
     		            'H':(-2.036, 'eV/molecule'),
                        'C':(-4.045, 'eV/molecule'),
                        'N':(-2.051, 'eV/molecule'),
                        'O':(-3.126, 'eV/molecule'),
                        'H2O': (-0.25, 'eV/molecule'),
                         'NH3': (-0.35, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.432E-09, 'mol/cm^2'),
     facet = "211",
     metal = "Ag",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 14,
     label = "Pd211",
     bindingEnergies = {
     		            'H':(-2.785, 'eV/molecule'),
                        'C':(-7.826, 'eV/molecule'),
                        'N':(-4.774, 'eV/molecule'),
                        'O':(-3.980, 'eV/molecule'),
                        'H2O': (-0.35, 'eV/molecule'),
                        'NH3': (-0.67, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.688E-09, 'mol/cm^2'),
     facet = "211",
     metal = "Pd",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 15,
     label = "Au211",
     bindingEnergies = {
     		            'H':(-2.191205055, 'eV/molecule'),
                        'C':(-4.758643121, 'eV/molecule'),
                        'N':(-2.455006241, 'eV/molecule'),
                        'O':(-2.753661561, 'eV/molecule'),
                        'H2O': (-0.22, 'eV/molecule'),
                         'NH3': (-0.40, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.408E-09, 'mol/cm^2'),
     facet = "211",
     metal = "Au",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 16,
     label = "Ir211",
     bindingEnergies = {
     		          'H':(-3.049382381, 'eV/molecule'),
                        'C':(-7.518738006, 'eV/molecule'),
                        'N':(-5.386894619, 'eV/molecule'),
                        'O':(-5.153576364, 'eV/molecule'),
                        'H2O': (-0.44, 'eV/molecule'),
                         'NH3': (-1.02, 'eV/molecule'),
     },
     surfaceSiteDensity = (2.744E-09, 'mol/cm^2'),
     facet = "211",
     metal = "Ir",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 17,
     label = "Ru211",
     bindingEnergies = {
     		            'H':(-2.990208683, 'eV/molecule'),
                        'C':(-7.767055243, 'eV/molecule'),
                        'N':(-6.167927714, 'eV/molecule'),
                        'O':(-5.858408296, 'eV/molecule'),
     },
     surfaceSiteDensity = (3.199E-09, 'mol/cm^2'),
     facet = "211",
     metal = "Ru",
     shortDesc = u"hcp",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
     """,
)

entry(
     index = 18,
     label = "Co211",
     bindingEnergies = {
     		            'H':(-2.958578034, 'eV/molecule'),
                        'C':(-7.517405633, 'eV/molecule'),
                        'N':(-5.693528936, 'eV/molecule'),
                        'O':(-5.739466384, 'eV/molecule'),
     },
     surfaceSiteDensity = (3.711E-09, 'mol/cm^2'),
     facet = "211",
     metal = "Co",
     shortDesc = u"hcp",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
     """,
)

entry(
     index = 19,
     label = "Ni211",
     bindingEnergies = {
     		            'H':(-2.901, 'eV/molecule'),
                        'C':(-7.775, 'eV/molecule'),
                        'N':(-5.310, 'eV/molecule'),
                        'O':(-5.086, 'eV/molecule'),
                        'H2O': (-0.41, 'eV/molecule'),
                         'NH3': (-0.80, 'eV/molecule'),

     },
     surfaceSiteDensity = (3.339E-09, 'mol/cm^2'),
     facet = "211",
     metal = "Ni",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 20,
     label = "Cu211",
     bindingEnergies = {
     		            'H':(-2.582, 'eV/molecule'),
                        'C':(-5.831, 'eV/molecule'),
                        'N':(-3.723, 'eV/molecule'),
                        'O':(-4.307, 'eV/molecule'),
                        'H2O': (-0.33, 'eV/molecule'),
                         'NH3': (-0.60, 'eV/molecule'),
     },
     surfaceSiteDensity = (3.121E-09, 'mol/cm^2'),
     facet = "211",
     metal = "Cu",
     shortDesc = u"fcc",
     longDesc = u"""
Calculated by Katrin Blondal and Bjarne Kreitz at Brown University
H2O and NH3 from https://pubs.acs.org/doi/10.1021/acs.inorgchem.8b00902
     """,
)

entry(
     index = 21,
     label = "Cu",
     bindingEnergies = "Cu211",
     shortDesc = u"",
     longDesc = u"""

     """,
)

entry(
     index = 22,
     label = "Pd",
     bindingEnergies = "Pd111",
     shortDesc = u"",
     longDesc = u"""

     """,
)

entry(
     index = 23,
     label = "Ag",
     bindingEnergies = "Ag111",
     shortDesc = u"",
     longDesc = u"""

     """,
)

entry(
     index = 25,
     label = "Ru",
     bindingEnergies = "Ru0001",
     shortDesc = u"",
     longDesc = u"""

     """,
)

entry(
     index = 26,
     label = "Rh",
     bindingEnergies = "Rh111",
     shortDesc = u"",
     longDesc = u"""

     """,
)

entry(
     index = 27,
     label = "Au",
     bindingEnergies = "Au111",
     shortDesc = u"",
     longDesc = u"""

     """,
)

entry(
     index = 28,
     label = "Ni",
     bindingEnergies = "Ni111",
     shortDesc = u"",
     longDesc = u"""

     """,
)

entry(
     index = 29,
     label = "Co",
     bindingEnergies = "Co211",
     shortDesc = u"",
     longDesc = u"""

     """,
)

entry(
     index = 30,
     label = "Ir",
     bindingEnergies = "Ir111",
     shortDesc = u"",
     longDesc = u"""

     """,
)

