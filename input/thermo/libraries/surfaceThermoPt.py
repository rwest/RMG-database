#!/usr/bin/env python


name = "SurfaceThermoPt"
#Note: "-h" means "horizontal".

entry(
    index = 1,
    label = "vacant",
    molecule =
"""
1 X  u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(1000.0,'K'), Tmax=(3000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (3000.0, 'K'),
    ),
)

entry(
    index = 2,
    label = "H_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -1.967029880E+00,   1.679207140E-02,  -2.503141390E-05,   1.804854550E-08,
             -5.114915440E-12,  -3.203148470E+03,   7.682112580E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             2.719678530E+00,  -1.076956900E-03,   2.001923030E-06,  -1.128655390E-09,
             2.112684300E-13,  -4.237391580E+03,  -1.527930800E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.240 eV.
            Linear scaling parameters: ref_adatom_H = -0.240 eV, psi = 0.00000 eV, gamma_H(X) = 1.000.""",
)

entry(
    index = 3,
    label = "H2_ads",
    molecule =
"""
1 X  u0 p0 c0
2 H  u0 p0 c0 {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             3.789351110E+00,   1.101480210E-03,  -2.313201000E-06,   2.119378260E-09,
             -6.313500070E-13,  -1.867003330E+03,  -1.006164650E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             4.067002080E+00,  -5.017806830E-04,   6.707394750E-07,  -1.791712200E-10,
             8.868912370E-15,  -1.891077100E+03,  -1.126217240E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.054 eV.
            Linear scaling parameters: ref_adatom_H = -0.240 eV, psi = -0.05448 eV, gamma_H(X) = 0.000.
            The two lowest frequencies, 14.0 and 24.4 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 4,
    label = "H2O_ads",
    molecule =
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             2.537772660E+00,   9.453720100E-03,  -1.413256640E-05,   1.167309450E-08,
             -3.676576400E-12,  -3.845514540E+04,  -5.365485620E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.847894650E+00,  -3.315268160E-03,   5.620187850E-06,  -2.758648930E-09,
             4.612790670E-13,  -3.918465990E+04,  -2.156226990E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.189 eV.
            Linear scaling parameters: ref_adatom_O = -1.030 eV, psi = -0.18932 eV, gamma_O(X) = 0.000.
            The two lowest frequencies, 49.5 and 68.6 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 5,
    label = "OH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.073485830E+00,   1.726522060E-02,  -3.177122320E-05,   2.715365680E-08,
             -8.694489570E-12,  -2.529759270E+04,  -5.656223370E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.018710210E+00,  -1.354252630E-03,   2.276873010E-06,  -1.094077420E-09,
             1.793972220E-13,  -2.599528970E+04,  -2.411600310E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.970 eV.
            Linear scaling parameters: ref_adatom_O = -1.030 eV, psi = -1.45958 eV, gamma_O(X) = 0.500.""",
)

entry(
    index = 6,
    label = "HO-OH_ads",
    molecule =
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             2.837241990E+00,   1.403751750E-02,  -1.463804180E-05,   8.154749030E-09,
             -1.742665040E-12,  -3.666070150E+04,  -5.583587160E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.638673050E+00,  -4.649793400E-03,   8.110187690E-06,  -4.178923370E-09,
             7.286577310E-13,  -3.811206670E+04,  -3.485186360E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.286 eV.
            Linear scaling parameters: ref_adatom_O = -1.030 eV, psi = -0.28574 eV, gamma_O(X) = 0.000.
            The two lowest frequencies, 10.6 and 50.4 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 7,
    label = "O2_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             7.443703460E-01,   2.110274680E-02,  -3.612667540E-05,   2.910321110E-08,
             -9.016898340E-12,  -2.592456660E+04,  -4.833568320E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.796391270E+00,  -7.490423320E-04,   1.406801680E-06,  -7.970925650E-10,
             1.496965290E-13,  -2.692009500E+04,  -2.897152270E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.347 eV.
            Linear scaling parameters: ref_adatom_O1 = -1.030 eV, ref_adatom_O2 = -1.030 eV, psi = 0.68107 eV, gamma_O1(X) = 0.500, gamma_O2(X) = 0.500.""",
)

entry(
    index = 8,
    label = "OOH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             2.354362490E+00,   1.561994550E-02,  -2.440448920E-05,   1.899141380E-08,
             -5.723999400E-12,  -2.786958090E+04,  -5.451454320E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             6.828621010E+00,  -2.146900670E-03,   3.733793480E-06,  -1.909236350E-09,
             3.309557410E-13,  -2.882567240E+04,  -2.720768780E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.742 eV.
            Linear scaling parameters: ref_adatom_O = -1.030 eV, psi = -0.22813 eV, gamma_O(X) = 0.500.
            The two lowest frequencies, 35.9 and 60.2 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 9,
    label = "O_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.797223820E-01,   1.254531560E-02,  -2.299245880E-05,   1.941871770E-08,
             -6.224140990E-12,  -2.291484860E+04,  -2.224097280E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             2.920508970E+00,  -2.704555870E-04,   5.156106320E-07,  -2.939112120E-10,
             5.540304640E-14,  -2.341152430E+04,  -1.509405360E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.030 eV.
            Linear scaling parameters: ref_adatom_O = -1.030 eV, psi = 0.00000 eV, gamma_O(X) = 1.000.""",
)

entry(
    index = 10,
    label = "O-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.444985870E+00,   1.600378770E-02,  -1.546581830E-05,   8.193744020E-09,
             -1.734019180E-12,  -1.448774280E+04,  -8.531535870E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.427278950E+00,  -5.740936460E-03,   1.013806970E-05,  -5.324270730E-09,
             9.425386670E-13,  -1.628811100E+04,  -3.630547990E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.698 eV.
            Linear scaling parameters: ref_adatom_O = -1.030 eV, psi = -0.18381 eV, gamma_O(X) = 0.500.
            The two lowest frequencies, 10.3 and 64.1 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 11,
    label = "O-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.966896120E+00,   9.933156690E-03,   6.039548340E-06,  -1.314991490E-08,
             5.516156980E-12,  -2.611317930E+04,  -3.141256370E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.028360810E+01,  -9.416926730E-03,   1.678746060E-05,  -8.951656980E-09,
             1.603358220E-12,  -2.860449180E+04,  -4.703615990E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.370 eV.
            Linear scaling parameters: ref_adatom_O = -1.030 eV, psi = -0.85962 eV, gamma_O(X) = 0.500.
            The two lowest frequencies, 64.2 and 66.3 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 12,
    label = "NH3_ads",
    molecule =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.314967740E+00,   1.469982890E-02,  -1.306790710E-05,   6.993608690E-09,
             -1.529210790E-12,  -1.453057740E+04,  -4.299925920E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.394599160E+00,  -7.226399710E-03,   1.261697690E-05,  -6.509524410E-09,
             1.135635490E-12,  -1.636590850E+04,  -4.028566780E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.673 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -0.67337 eV, gamma_N(X) = 0.000.""",
)

entry(
    index = 13,
    label = "NH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -1.890107590E+00,   2.862179970E-02,  -4.345452370E-05,   3.341432850E-08,
             -9.994997880E-12,  -4.878935280E+03,   6.349976100E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             6.679688400E+00,  -4.642677320E-03,   8.128720250E-06,  -4.204365180E-09,
             7.351328870E-13,  -6.752260130E+03,  -3.551819040E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.030 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -2.20832 eV, gamma_N(X) = 0.333.""",
)

entry(
    index = 14,
    label = "NH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -2.686630980E+00,   2.891974860E-02,  -4.763985660E-05,   3.773680640E-08,
             -1.148951770E-11,  -1.395786670E+03,   9.810767350E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             4.827006990E+00,  -2.463802090E-03,   4.353788540E-06,  -2.278951850E-09,
             4.025081450E-13,  -2.923329960E+03,  -2.633929730E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.440 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -3.79341 eV, gamma_N(X) = 0.667.""",
)

entry(
    index = 15,
    label = "N_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 N  u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -8.621580740E-01,   1.653217230E-02,  -2.951874530E-05,   2.447413870E-08,
             -7.738948370E-12,   4.568728490E+03,   2.272637920E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             2.878127250E+00,  -4.325471470E-04,   8.188684650E-07,  -4.656415630E-10,
             8.765221080E-14,   3.867889910E+03,  -1.541181530E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: 0.525 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = 0.00000 eV, gamma_N(X) = 1.000.""",
)

entry(
    index = 16,
    label = "H2N-OH_ads",
    molecule =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.219300230E+00,   1.830792140E-02,  -1.289817480E-05,   3.119694590E-09,
             5.171384150E-13,  -2.100855500E+04,   5.247642460E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.024887730E+01,  -7.981630470E-03,   1.402522700E-05,  -7.314557790E-09,
             1.287963900E-12,  -2.341342530E+04,  -4.573611540E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.654 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -0.65407 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 17.1 and 68.9 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 17,
    label = "HN-O_ads",
    molecule =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 O  u0 p2 c0 {2,D}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.080958060E+00,   1.292192670E-02,  -1.333745400E-05,   7.751586780E-09,
             -1.926122460E-12,  -1.383218460E+04,   6.085460490E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             6.476718510E+00,  -3.957940290E-03,   7.093004740E-06,  -3.806276690E-09,
             6.853887560E-13,  -1.523100080E+04,  -2.679966580E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.270 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -1.26632 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 36.2 and 74.0 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 18,
    label = "HN-OH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -9.438345260E-02,   2.798013010E-02,  -3.687170920E-05,   2.547971650E-08,
             -7.027465420E-12,  -1.753103530E+04,  -1.144428380E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.447618320E+00,  -5.668797680E-03,   1.002345690E-05,  -5.269974200E-09,
             9.339851720E-13,  -1.978516270E+04,  -4.859736260E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.370 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -1.54570 eV, gamma_N(X) = 0.333.""",
)

entry(
    index = 19,
    label = "NO_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 O  u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.912534520E+00,   1.197429480E-02,  -1.741507400E-05,   1.310501300E-08,
             -3.984403090E-12,  -1.960944880E+04,  -9.509206200E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.582005070E+00,  -1.446986760E-03,   2.668412780E-06,  -1.486679600E-09,
             2.756138510E-13,  -2.046685430E+04,  -2.767857920E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.580 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -1.75991 eV, gamma_N(X) = 0.333.""",
)

entry(
    index = 20,
    label = "NO-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,D} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             2.315668890E+00,   5.677595510E-03,  -6.715038090E-06,   4.784832250E-09,
             -1.503902040E-12,  -1.725234080E+04,  -4.646781770E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             4.550609120E+00,  -1.475553230E-03,   2.701862050E-06,  -1.492600900E-09,
             2.748394820E-13,  -1.783606340E+04,  -1.599271090E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.390 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -1.73967 eV, gamma_N(X) = 0.667.
            The two lowest frequencies, -19.4 and 68.0 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 21,
    label = "NOH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             7.029683490E-01,   2.370249400E-02,  -3.553301940E-05,   2.656233920E-08,
             -7.776626560E-12,  -1.652308840E+04,  -4.533115280E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.645214550E+00,  -2.917207410E-03,   5.163780850E-06,  -2.715266750E-09,
             4.816343880E-13,  -1.805333470E+04,  -3.852251510E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.260 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -3.60529 eV, gamma_N(X) = 0.667.""",
)

entry(
    index = 22,
    label = "H2N-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             7.109377300E-01,   1.858149570E-02,  -5.982437370E-06,  -4.760234540E-09,
             3.311219350E-12,  -2.755797370E+03,   2.411624270E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.183677000E+01,  -1.131777530E-02,   1.993389930E-05,  -1.043422170E-08,
             1.842308550E-12,  -5.858494110E+03,  -5.524324320E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.977 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -0.97746 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 6.9 and 79.2 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 23,
    label = "HN-NH_ads",
    molecule =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 N  u0 p1 c0 {2,D} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             4.624806040E-01,   2.374639300E-02,  -2.791277020E-05,   1.764540480E-08,
             -4.521952260E-12,   1.086899090E+04,  -3.539451840E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.400984060E+00,  -5.986533070E-03,   1.061363220E-05,  -5.605442160E-09,
             9.969149140E-13,   8.663754620E+03,  -4.844415590E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.676 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -0.67607 eV, gamma_N(X) = 0.000.""",
)

entry(
    index = 24,
    label = "NN_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,D}
4 N  u0 p1 c0 {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             4.139939170E+00,  -9.927559100E-04,   1.767040330E-06,  -1.578843420E-10,
             -3.642067120E-13,  -4.380795290E+03,  -7.289846350E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             4.386605170E+00,  -1.506923910E-03,   2.676405940E-06,  -1.415318030E-09,
             2.513633790E-13,  -4.482254750E+03,  -8.669017440E+00], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.109 eV.
            Linear scaling parameters: ref_adatom_N1 = 0.525 eV, ref_adatom_N2 = 0.525 eV, psi = -0.45958 eV, gamma_N1(X) = 0.333, gamma_N2(X) = 0.333.
            The two lowest frequencies, 6.3 and 24.2 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 25,
    label = "HN-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.471200560E-01,   2.683756430E-02,  -2.812550560E-05,   1.595952190E-08,
             -3.617411930E-12,   5.509297690E+03,  -2.023136970E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.117882480E+01,  -8.425909350E-03,   1.486608940E-05,  -7.796527340E-09,
             1.378811320E-12,   2.718565830E+03,  -5.779014990E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.270 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -1.44545 eV, gamma_N(X) = 0.333.""",
)

entry(
    index = 26,
    label = "N-NH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.093239410E+00,   1.853336280E-02,  -2.468376290E-05,   1.771916790E-08,
             -5.170176790E-12,   1.007693290E+04,  -5.676714430E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.475684980E+00,  -3.838773590E-03,   6.871431070E-06,  -3.677285720E-09,
             6.607737430E-13,   8.545080880E+03,  -3.749613350E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.060 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -1.23214 eV, gamma_N(X) = 0.333.""",
)

entry(
    index = 27,
    label = "N-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             5.701297380E-01,   2.468155620E-02,  -3.143570400E-05,   2.151896510E-08,
             -5.940883200E-12,   5.195654020E+03,  -4.186492000E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.375216130E+00,  -5.750585450E-03,   1.015574400E-05,  -5.329412770E-09,
             9.431018670E-13,   3.078119870E+03,  -4.814499340E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.040 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -2.38988 eV, gamma_N(X) = 0.667.""",
)

entry(
    index = 28,
    label = "HN-NH-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             2.334954140E-01,   2.266105500E-02,  -2.362244440E-05,   1.283897650E-08,
             -2.733729910E-12,   9.550373880E+03,  -2.294914280E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.359530680E+00,  -6.295535350E-03,   1.118941990E-05,  -5.935327740E-09,
             1.059265110E-12,   7.233656080E+03,  -4.847482170E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.982 eV.
            Linear scaling parameters: ref_adatom_N1 = 0.525 eV, ref_adatom_N2 = 0.525 eV, psi = -1.33172 eV, gamma_N1(X) = 0.333, gamma_N2(X) = 0.333.""",
)

entry(
    index = 29,
    label = "HN-N-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -9.333668050E-03,   2.284860100E-02,  -3.139310050E-05,   2.251048610E-08,
             -6.485274120E-12,   7.544688910E+03,  -1.632532260E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.454489580E+00,  -3.873082080E-03,   6.936969980E-06,  -3.715192840E-09,
             6.681941440E-13,   5.790743110E+03,  -3.868062300E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.280 eV.
            Linear scaling parameters: ref_adatom_N1 = 0.525 eV, ref_adatom_N2 = 0.525 eV, psi = -1.80538 eV, gamma_N1(X) = 0.333, gamma_N2(X) = 0.667.""",
)

entry(
    index = 30,
    label = "HN-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,S} {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             4.900390160E-01,   2.209325530E-02,  -9.261491620E-06,  -3.139279890E-09,
             2.925697880E-12,  -5.593036760E+03,  -2.833808710E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.307876640E+01,  -1.203119460E-02,   2.139494100E-05,  -1.136363310E-08,
             2.029340940E-12,  -9.102990380E+03,  -6.803188270E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.850 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -2.02766 eV, gamma_N(X) = 0.333.""",
)

entry(
    index = 31,
    label = "N-CH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {1,S} {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             7.251785550E-01,   2.128262430E-02,  -2.340814270E-05,   1.470287460E-08,
             -3.898541210E-12,   2.523923310E+03,  -4.111146940E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.381583770E+00,  -6.590227470E-03,   1.176829060E-05,  -6.281809660E-09,
             1.126156350E-12,   3.196977850E+02,  -4.788412020E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.660 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -1.83916 eV, gamma_N(X) = 0.333.""",
)

entry(
    index = 32,
    label = "N-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,D} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             4.575824640E-01,   2.082278460E-02,  -1.316662000E-05,   2.487779750E-09,
             6.586814430E-13,  -5.313736880E+03,  -3.129385580E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.123346490E+01,  -9.613921010E-03,   1.716616220E-05,  -9.170601990E-09,
             1.645104190E-12,  -8.264883000E+03,  -5.865670810E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.050 eV.
            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -3.39942 eV, gamma_N(X) = 0.667.""",
)

# entry(
#     index = 33,
#     label = "ON-O_ads",
#     molecule =
# """
# 1 X  u0  p0 c0 {2,S}
# 2 N  u0  p0 c+1 {1,S} {3,S} {4,D}
# 3 O  u0  p2 c-1 {2,S}
# 4 O  u0  p2 c0 {2,D}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[
#              1.908949200E+00,   2.036846110E-02,  -3.030122180E-05,   2.191995790E-08,
#              -6.250090720E-12,   9.003214300E+03,  -2.726671970E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
#             NASAPolynomial(coeffs=[
#              7.636130060E+00,  -1.383989810E-03,   2.571362700E-06,  -1.448349250E-09,
#              2.709019330E-13,   7.732608970E+03,  -3.081328960E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
#         ],
#         Tmin = (298.0, 'K'),
#         Tmax = (2000.0, 'K'),
#     ),
#     longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
#            Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -0.688 eV.
#            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -0.86302 eV, gamma_N(X) = 0.333.
#            The two lowest frequencies, -33.2 and 55.1 cm-1, where replaced by the 2D gas model.""",
# )

entry(
    index = 34,
    label = "C_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,Q}
2 C  u0 p0 c0 {1,Q}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -1.734306970E+00,   1.898554710E-02,  -3.235636610E-05,   2.592698900E-08,
             -7.991024510E-12,   6.363859220E+03,   6.254450290E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             2.821925480E+00,  -6.611677530E-04,   1.241794400E-06,  -7.039894500E-10,
             1.322758700E-13,   5.464681900E+03,  -1.552508610E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -6.750 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.00000 eV, gamma_C(X) = 1.000.""",
)

entry(
    index = 35,
    label = "C-C_ads",
    molecule =
"""
1 X  u0  p0 c0 {3,D}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             2.222827940E-01,   1.969086000E-02,  -3.076268160E-05,   2.359374390E-08,
             -7.124384420E-12,   2.428422350E+04,  -3.036351130E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.607597960E+00,  -1.419218560E-03,   2.634098110E-06,  -1.478306560E-09,
             2.756497440E-13,   2.310969350E+04,  -2.931776010E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -5.910 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 0.84219 eV, gamma_C1(X) = 0.500, gamma_C2(X) = 0.500.""",
)

entry(
    index = 36,
    label = "C-CH2_ads",
    molecule =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D} {4,S} {5,S}
4 H  u0  p0 c0 {3,S}
5 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -2.047857060E+00,   3.381486540E-02,  -4.457753000E-05,   3.083182790E-08,
             -8.569006620E-12,  -2.280275200E+03,   6.644690480E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.428317660E+00,  -6.481254180E-03,   1.158799710E-05,  -6.194951640E-09,
             1.112190750E-12,  -5.009777060E+03,  -5.049459950E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.980 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.60024 eV, gamma_C(X) = 0.500.""",
)

entry(
    index = 37,
    label = "C-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,T} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.576031040E-01,   2.342934130E-02,  -1.866836610E-05,   7.292343700E-09,
             -8.790086710E-13,  -1.125115070E+04,  -1.735822780E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.130503360E+01,  -9.406229300E-03,   1.679356780E-05,  -8.969014990E-09,
             1.608556210E-12,  -1.423361380E+04,  -5.883637900E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -5.590 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52567 eV, gamma_C(X) = 0.750.""",
)

entry(
    index = 38,
    label = "CH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -3.009507790E+00,   3.021933410E-02,  -4.995462940E-05,   3.994784640E-08,
             -1.230215580E-11,  -3.133538590E+03,   1.123144640E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             4.884827150E+00,  -2.708470840E-03,   4.846491090E-06,  -2.585140890E-09,
             4.631810530E-13,  -4.750831740E+03,  -2.678711450E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -6.240 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -1.17590 eV, gamma_C(X) = 0.750.""",
)

entry(
    index = 39,
    label = "CH-CH_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,D} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -1.688980570E+00,   3.528312630E-02,  -4.975784930E-05,   3.621761990E-08,
             -1.045886290E-11,   2.158866520E+02,   6.752389050E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.571818320E+00,  -5.980766930E-03,   1.067377820E-05,  -5.688381210E-09,
             1.018604960E-12,  -2.375834770E+03,  -4.888707440E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.010 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 4.74337 eV, gamma_C1(X) = 0.500, gamma_C2(X) = 0.500.""",
)

entry(
    index = 40,
    label = "CH-CH-vdw_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {2,T} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.111802820E+00,   2.490616590E-02,  -3.964044010E-05,   3.239148690E-08,
             -1.019758240E-11,   2.121358700E+04,   4.054766510E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.553285930E+00,  -4.891489680E-03,   8.553175480E-06,  -4.413048920E-09,
             7.695103000E-13,   1.961410850E+04,  -3.212192450E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.200 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.20021 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 8.5 and 8.7 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 41,
    label = "CH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -2.266023670E+00,   2.925177650E-02,  -4.327287970E-05,   3.306557230E-08,
             -9.932426410E-12,  -2.236194450E+02,   8.227512880E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             6.825726350E+00,  -5.171925050E-03,   9.195519380E-06,  -4.871014860E-09,
             8.677130910E-13,  -2.268866210E+03,  -3.644107520E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.640 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.26541 eV, gamma_C(X) = 0.500.""",
)

entry(
    index = 42,
    label = "CH2-CH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -2.397376040E+00,   3.731943530E-02,  -3.731407020E-05,   1.984351090E-08,
             -4.158833000E-12,  -8.089853170E+03,   9.523838100E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.325998030E+01,  -1.178742920E-02,   2.100171070E-05,  -1.118234380E-08,
             2.000748970E-12,  -1.210782360E+04,  -6.988231750E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.950 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 2.42761 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.250.""",
)

entry(
    index = 43,
    label = "CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             5.800998770E-01,   1.663999770E-02,  -1.391648700E-05,   6.706315820E-09,
             -1.310788280E-12,  -6.309266590E+03,  -7.571483820E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.678705730E+00,  -7.842393860E-03,   1.389561760E-05,  -7.336006350E-09,
             1.303215040E-12,  -8.449598310E+03,  -4.209672320E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.770 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.08242 eV, gamma_C(X) = 0.250.""",
)

entry(
    index = 44,
    label = "CH3-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             3.199748510E+00,   7.938417190E-03,   2.694131640E-05,  -3.534537030E-08,
             1.322078210E-11,  -1.457835120E+04,  -1.679527050E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.591696090E+01,  -1.756168600E-02,   3.122554630E-05,  -1.658749690E-08,
             2.961569650E-12,  -1.861121440E+04,  -6.985675090E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.219 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.21852 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 5.6 and 8.8 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 45,
    label = "CH4_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             5.262470020E+00,  -7.427034130E-03,   3.364723360E-05,  -3.294011500E-08,
             1.102592580E-11,  -1.160383200E+04,  -1.009205410E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.549811810E+00,  -1.037194280E-02,   1.831835610E-05,  -9.633330270E-09,
             1.705585500E-12,  -1.327172180E+04,  -3.453745770E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.122 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.12206 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 3.2 and 8.1 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 46,
    label = "CN_ads",
    molecule =
"""
1 X  u0  p0 c0 {3,D}
2 X  u0  p0 c0 {4,S}
3 C  u0  p0 c0 {1,D} {4,D}
4 N  u0  p1 c0 {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             4.117599990E+00,   2.619254580E-03,  -2.385972420E-06,   1.993708990E-09,
             -8.124100350E-13,   7.239716470E+03,  -1.736311380E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.524181070E+00,  -1.468837310E-03,   2.673570050E-06,  -1.464548470E-09,
             2.678157720E-13,   6.839186390E+03,  -2.463841500E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.340 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = -0.13303 eV, gamma_C1(X) = 0.500, gamma_N2(X) = 0.333.""",
)

entry(
    index = 47,
    label = "CNH_ads",
    molecule =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 N  u0  p1 c0 {2,D} {4,S}
4 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             2.594969490E+00,   1.650891770E-02,  -2.539744080E-05,   2.024680050E-08,
             -6.321037440E-12,  -2.382888560E+03,  -1.158838360E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.619047260E+00,  -2.921867970E-03,   5.154785750E-06,  -2.695250540E-09,
             4.754949230E-13,  -3.499442720E+03,  -3.619059370E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.740 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.63638 eV, gamma_C(X) = 0.500.""",
)

entry(
    index = 48,
    label = "CNH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.530875380E+00,   2.162308060E-02,  -2.713296490E-05,   1.849380210E-08,
             -5.093057920E-12,  -1.036861660E+04,  -8.384684160E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.404684800E+00,  -5.413275340E-03,   9.516934000E-06,  -4.959469070E-09,
             8.728609050E-13,  -1.227074700E+04,  -4.773734890E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.060 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.00119 eV, gamma_C(X) = 0.750.""",
)

entry(
    index = 49,
    label = "CO-f_ads",
    molecule =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 O  u0  p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             2.701122720E+00,   8.766501660E-03,  -1.295124180E-05,   1.041945940E-08,
             -3.397003160E-12,  -4.064376250E+04,  -1.287305120E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.528212260E+00,  -1.526317370E-03,   2.797923910E-06,  -1.545503510E-09,
             2.845235910E-13,  -4.131922900E+04,  -2.691571840E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.480 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.89529 eV, gamma_C(X) = 0.500.""",
)

entry(
    index = 50,
    label = "COH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             8.634377440E-01,   2.148060540E-02,  -3.000095250E-05,   2.117290110E-08,
             -5.909234910E-12,  -3.669519900E+04,  -5.107497320E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.594790560E+00,  -3.068473820E-03,   5.435926470E-06,  -2.864635600E-09,
             5.091492240E-13,  -3.823859790E+04,  -3.836747930E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.260 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.80370 eV, gamma_C(X) = 0.750.""",
)

entry(
    index = 51,
    label = "H2C-CH_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,D} {3,S} {7,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -3.717415240E+00,   4.456392320E-02,  -5.866221190E-05,   4.058802560E-08,
             -1.125848030E-11,  -2.986009480E+03,   1.370561240E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.148266010E+01,  -8.876450790E-03,   1.585906870E-05,  -8.470882520E-09,
             1.519445910E-12,  -6.597182870E+03,  -6.195456650E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.770 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 2.29437 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.500.""",
)

entry(
    index = 52,
    label = "H2C-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -3.107042530E-01,   2.316700050E-02,  -5.713979370E-06,  -7.481218870E-09,
             4.466479270E-12,  -1.029405160E+04,   6.880783850E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.409152890E+01,  -1.476228650E-02,   2.628613620E-05,  -1.398947660E-08,
             2.501675250E-12,  -1.437832120E+04,  -6.801646900E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.750 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.06163 eV, gamma_C(X) = 0.250.
            The two lowest frequencies, 18.6 and 76.6 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 53,
    label = "H2C-NH_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -3.225764610E-01,   2.088075190E-02,  -1.296916540E-05,   1.296828000E-09,
             1.405944810E-12,   3.665139400E+03,   6.825006960E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.027049470E+01,  -9.061706980E-03,   1.610744870E-05,  -8.551186370E-09,
             1.526732760E-12,   7.889389920E+02,  -4.769270980E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.228 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.22807 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 46.0 and 79.7 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 54,
    label = "H2C-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -4.505110660E-01,   2.595035850E-02,  -2.005819370E-05,   7.122848120E-09,
             -4.601839740E-13,  -9.978755620E+03,   7.092621040E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.207763590E+01,  -1.109003320E-02,   1.958896350E-05,  -1.029604420E-08,
             1.823795900E-12,  -1.330449870E+04,  -5.699663650E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.980 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.29283 eV, gamma_C(X) = 0.250.
            The two lowest frequencies, 17.2 and 75.9 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 55,
    label = "H2C-O_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 O  u0 p2 c0 {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -7.308579970E-01,   2.294062590E-02,  -2.431842600E-05,   1.392981890E-08,
             -3.269162720E-12,  -2.642065330E+04,   7.872241010E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.531231470E+00,  -6.493436800E-03,   1.163379150E-05,  -6.243796770E-09,
             1.124208670E-12,  -2.878505430E+04,  -3.902385670E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.184 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.18361 eV, gamma_C(X) = 0.000.""",
)

entry(
    index = 56,
    label = "H2C-OH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -2.459939070E-01,   2.289047240E-02,  -1.870793910E-05,   6.934422500E-09,
             -5.294722990E-13,  -3.501905430E+04,   6.342284080E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.032046890E+01,  -8.548569300E-03,   1.514850330E-05,  -8.002387830E-09,
             1.423474530E-12,  -3.780786390E+04,  -4.764673480E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.890 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.19820 eV, gamma_C(X) = 0.250.
            The two lowest frequencies, 44.2 and 70.8 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 57,
    label = "H2CN-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -8.027196090E-01,   2.772321130E-02,  -3.318227800E-05,   2.125961760E-08,
             -5.542573340E-12,   2.082287050E+03,   1.564258850E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.433404420E+00,  -6.492223650E-03,   1.160241250E-05,  -6.201496760E-09,
             1.113161470E-12,  -4.402180300E+02,  -4.983152020E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.710 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = -0.37462 eV, gamma_C1(X) = 0.250, gamma_N2(X) = 0.667.""",
)

entry(
    index = 58,
    label = "H2CNH-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,S} {3,S} {7,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -3.223188660E+00,   4.083795160E-02,  -5.082181840E-05,   3.338936560E-08,
             -8.818806800E-12,  -2.399461220E+03,   1.163075000E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.133478410E+01,  -8.906917800E-03,   1.586267500E-05,  -8.435108140E-09,
             1.508070290E-12,  -5.922420680E+03,  -6.116976830E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.756 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 0.75753 eV, gamma_C1(X) = 0.250, gamma_N2(X) = 0.333.""",
)

entry(
    index = 59,
    label = "H3C-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {2,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             7.905759400E-01,   1.658523240E-02,   6.481844370E-06,  -1.792981560E-08,
             7.876740930E-12,  -1.510000630E+04,   2.425874390E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.377296490E+01,  -1.467982200E-02,   2.600997950E-05,  -1.374255770E-08,
             2.444013230E-12,  -1.891951550E+04,  -6.578987570E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.879 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.87925 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 16.6 and 84.5 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 60,
    label = "H3C-OH_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             2.705067260E+00,   1.009135940E-02,   1.002606800E-05,  -1.809096030E-08,
             7.445396730E-12,  -3.665965680E+04,  -4.481359600E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.215394940E+01,  -1.131734600E-02,   2.003420860E-05,  -1.057240900E-08,
             1.878528130E-12,  -3.950649720E+04,  -5.446175640E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.316 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.31650 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 16.5 and 57.9 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 61,
    label = "HC-C_ads",
    molecule =
"""
1 X  u0  p0 c0 {3,S}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,D} {5,S}
4 C  u0  p0 c0 {2,D} {3,D}
5 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             5.411705530E-02,   2.527009210E-02,  -3.758039330E-05,   2.829108830E-08,
             -8.395763250E-12,   1.424965930E+04,  -1.637663870E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.622943620E+00,  -3.433215320E-03,   6.147708550E-06,  -3.289316720E-09,
             5.910207600E-13,   1.255419690E+04,  -3.880190340E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.100 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 0.96689 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.500.""",
)

entry(
    index = 62,
    label = "HC-CH2_ads",
    molecule =
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 C  u0  p0 c0 {2,D} {5,S} {6,S}
4 H  u0  p0 c0 {2,S}
5 H  u0  p0 c0 {3,S}
6 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -3.761998800E+00,   4.463873830E-02,  -5.865136870E-05,   4.048714140E-08,
             -1.120403080E-11,  -2.545452840E+03,   1.391918370E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.147737520E+01,  -8.889811580E-03,   1.588277200E-05,  -8.483602150E-09,
             1.521747930E-12,  -6.167735370E+03,  -6.194706680E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.790 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -1.09643 eV, gamma_C(X) = 0.250.""",
)

entry(
    index = 63,
    label = "HC-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -2.391951440E-01,   2.719653020E-02,  -1.964795900E-05,   6.179256460E-09,
             -1.846647830E-13,  -5.605760840E+03,   2.672252250E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.327146290E+01,  -1.196496780E-02,   2.134106240E-05,  -1.138274200E-08,
             2.039152210E-12,  -9.252940800E+03,  -6.909606150E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.580 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.20205 eV, gamma_C(X) = 0.500.""",
)

entry(
    index = 64,
    label = "HCN_ads",
    molecule =
"""
1 X  u0  p0 c0
2 C  u0  p0 c0 {3,T} {4,S}
3 N  u0  p1 c0 {2,T}
4 H  u0  p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.178891710E+00,   1.616396900E-02,  -2.316379570E-05,   1.788946610E-08,
             -5.510675250E-12,   1.102181430E+04,   1.945856020E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             6.543195090E+00,  -3.515497520E-03,   6.263834440E-06,  -3.328035220E-09,
             5.943591820E-13,   9.771402650E+03,  -2.634881610E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.010 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.00995 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 51.9 and 72.8 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 65,
    label = "HCN-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             2.459012910E-02,   2.361209760E-02,  -3.372158490E-05,   2.509590790E-08,
             -7.463089170E-12,   3.557101540E+03,  -1.502255220E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.529791770E+00,  -3.890044330E-03,   6.995371940E-06,  -3.767463920E-09,
             6.802660360E-13,   1.817823810E+03,  -3.861740290E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.650 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 2.37733 eV, gamma_C1(X) = 0.500, gamma_N2(X) = 0.667.""",
)

entry(
    index = 66,
    label = "HCNH_ads",
    molecule =
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 N  u0  p1 c0 {2,D} {5,S}
4 H  u0  p0 c0 {2,S}
5 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -1.356007840E-01,   2.098224740E-02,  -2.215982660E-05,   1.265740390E-08,
             -2.926162780E-12,   1.033631440E+02,   5.896116550E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.399838370E+00,  -6.239002210E-03,   1.109274530E-05,  -5.886085600E-09,
             1.050565380E-12,  -2.065115050E+03,  -3.728266340E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.220 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52691 eV, gamma_C(X) = 0.250.
            The two lowest frequencies, 26.9 and 75.8 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 67,
    label = "HCNH-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -1.132399460E+00,   2.984842440E-02,  -3.781457760E-05,   2.536169760E-08,
             -6.863072610E-12,  -3.167158400E+03,   3.301131430E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.378289670E+00,  -6.300488330E-03,   1.122034070E-05,  -5.964280120E-09,
             1.066210440E-12,  -5.702726090E+03,  -4.921301150E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.490 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 0.71054 eV, gamma_C1(X) = 0.500, gamma_N2(X) = 0.333.""",
)

entry(
    index = 68,
    label = "HCNH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -5.135490730E-01,   2.376096790E-02,  -2.137545260E-05,   1.003752310E-08,
             -1.735549200E-12,  -7.292342490E+03,   7.328192300E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             1.015096690E+01,  -8.744972720E-03,   1.546946520E-05,  -8.147180780E-09,
             1.445661600E-12,  -1.007559350E+04,  -4.698992690E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.670 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.70666 eV, gamma_C(X) = 0.500.
            The two lowest frequencies, 23.1 and 87.8 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 69,
    label = "HCO_ads",
    molecule =
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 H  u0  p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             9.927701340E-01,   1.284824150E-02,  -1.297070810E-05,   7.576700380E-09,
             -1.938811960E-12,  -3.368260580E+04,   1.211895310E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             6.492590290E+00,  -4.185694750E-03,   7.538090580E-06,  -4.074419300E-09,
             7.376251320E-13,  -3.512423160E+04,  -2.678538220E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.210 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52049 eV, gamma_C(X) = 0.250.
            The two lowest frequencies, 17.0 and 73.1 cm-1, where replaced by the 2D gas model.""",
)

entry(
    index = 70,
    label = "HCO-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -7.632291900E-02,   2.348181040E-02,  -3.175564410E-05,   2.223475610E-08,
             -6.256505730E-12,  -3.012025100E+04,  -1.423512910E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.611722790E+00,  -3.810521400E-03,   6.869397080E-06,  -3.715857560E-09,
             6.733529070E-13,  -3.193546280E+04,  -3.963310010E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.900 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_O2 = -1.030 eV, psi = 1.99512 eV, gamma_C1(X) = 0.500, gamma_O2(X) = 0.500.""",
)

entry(
    index = 71,
    label = "HCOH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -4.360428400E-01,   2.005075040E-02,  -1.770431820E-05,   7.498273420E-09,
             -9.939896130E-13,  -3.192012940E+04,   7.321894120E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.396770470E+00,  -6.556646770E-03,   1.170042670E-05,  -6.246003570E-09,
             1.120126310E-12,  -3.423757970E+04,  -3.773509730E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.960 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.42191 eV, gamma_C(X) = 0.500.
            The two lowest frequencies, 46.4 and 91.5 cm-1, where replaced by the 2D gas model.""",
)
