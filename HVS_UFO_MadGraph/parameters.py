# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Mon 17 Mar 2025 11:54:21



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cpsi = Parameter(name = 'cpsi',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{cpsi}',
                 lhablock = 'CHINPUTS',
                 lhacode = [ 1 ])

aa = Parameter(name = 'aa',
               nature = 'external',
               type = 'real',
               value = 1.,
               texname = 'a',
               lhablock = 'CHINPUTS',
               lhacode = [ 2 ])

bb = Parameter(name = 'bb',
               nature = 'external',
               type = 'real',
               value = 1.,
               texname = 'b',
               lhablock = 'CHINPUTS',
               lhacode = [ 3 ])

d3 = Parameter(name = 'd3',
               nature = 'external',
               type = 'real',
               value = 1.,
               texname = '\\text{d3}',
               lhablock = 'CHINPUTS',
               lhacode = [ 4 ])

d4 = Parameter(name = 'd4',
               nature = 'external',
               type = 'real',
               value = 1.,
               texname = '\\text{d4}',
               lhablock = 'CHINPUTS',
               lhacode = [ 5 ])

cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.22759,
                 texname = '\\theta _{\\text{cab}}',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

gv = Parameter(name = 'gv',
               nature = 'external',
               type = 'real',
               value = 2,
               texname = 'g_V',
               lhablock = 'SINGLETINPUTS',
               lhacode = [ 1 ])

MVz = Parameter(name = 'MVz',
                nature = 'external',
                type = 'real',
                value = 2000,
                texname = 'M_{V^0}',
                lhablock = 'SINGLETINPUTS',
                lhacode = [ 2 ])

MVc = Parameter(name = 'MVc',
                nature = 'external',
                type = 'real',
                value = 2000,
                texname = 'M_{V^+}',
                lhablock = 'SINGLETINPUTS',
                lhacode = [ 3 ])

cvvbC = Parameter(name = 'cvvbC',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{cvvbC}',
                  lhablock = 'SINGLETINPUTS',
                  lhacode = [ 4 ])

cqLN = Parameter(name = 'cqLN',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cqLN}',
                 lhablock = 'SINGLETINPUTS',
                 lhacode = [ 5 ])

cqL3N = Parameter(name = 'cqL3N',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{cqL3N}',
                  lhablock = 'SINGLETINPUTS',
                  lhacode = [ 6 ])

clN = Parameter(name = 'clN',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{clN}',
                lhablock = 'SINGLETINPUTS',
                lhacode = [ 7 ])

cuRN = Parameter(name = 'cuRN',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cuRN}',
                 lhablock = 'SINGLETINPUTS',
                 lhacode = [ 8 ])

cuR3N = Parameter(name = 'cuR3N',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{cuR3N}',
                  lhablock = 'SINGLETINPUTS',
                  lhacode = [ 9 ])

cdRN = Parameter(name = 'cdRN',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cdRN}',
                 lhablock = 'SINGLETINPUTS',
                 lhacode = [ 10 ])

cdR3N = Parameter(name = 'cdR3N',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{cdR3N}',
                  lhablock = 'SINGLETINPUTS',
                  lhacode = [ 11 ])

ceRN = Parameter(name = 'ceRN',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{ceRN}',
                 lhablock = 'SINGLETINPUTS',
                 lhacode = [ 12 ])

cuRC = Parameter(name = 'cuRC',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{cuRC}',
                 lhablock = 'SINGLETINPUTS',
                 lhacode = [ 13 ])

cuR3C = Parameter(name = 'cuR3C',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{cuR3C}',
                  lhablock = 'SINGLETINPUTS',
                  lhacode = [ 14 ])

chN = Parameter(name = 'chN',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{chN}',
                lhablock = 'SINGLETINPUTS',
                lhacode = [ 15 ])

chC = Parameter(name = 'chC',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{chC}',
                lhablock = 'SINGLETINPUTS',
                lhacode = [ 16 ])

cvvhhN = Parameter(name = 'cvvhhN',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{cvvhhN}',
                   lhablock = 'SINGLETINPUTS',
                   lhacode = [ 17 ])

cvvhhC = Parameter(name = 'cvvhhC',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{cvvhhC}',
                   lhablock = 'SINGLETINPUTS',
                   lhacode = [ 18 ])

cvvvN = Parameter(name = 'cvvvN',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{cvvvN}',
                  lhablock = 'SINGLETINPUTS',
                  lhacode = [ 19 ])

cvvvC = Parameter(name = 'cvvvC',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{cvvvC}',
                  lhablock = 'SINGLETINPUTS',
                  lhacode = [ 20 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\alpha _{\\text{EW}}{}^{-1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.118,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.42,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.9,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.42,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172.9,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.25,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.0032,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.44140351,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.04759951,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM2x2}')

mmVct = Parameter(name = 'mmVct',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sqrt(MVc**2/2. + cmath.sqrt(MVc**4 - (4*chC**2*(((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))*(MVz**2 - (chN**2*gv**2*MZ**4*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2))))/(MVz**2*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2) - (2*chN**4*gv**4*MZ**6*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2)/(MVz**4*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**4)) - cmath.sqrt((MVz**2 - (chN**2*gv**2*MZ**4*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2))))/(MVz**2*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2) - (2*chN**4*gv**4*MZ**6*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2)/(MVz**4*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**4))*(16*aEW*chN**2*cmath.pi*gv**2*MZ**2 - 4*chN**2*gv**2*MZ**2*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2))) + ((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2*(MVz**2 - (chN**2*gv**2*MZ**4*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2))))/(MVz**2*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2) - (2*chN**4*gv**4*MZ**6*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2)/(MVz**4*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**4)))))**2)/(chN**4*gv**2*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))))/2.)',
                  texname = '\\tilde{m}_{\\text{VC}}')

mmVzt = Parameter(name = 'mmVzt',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sqrt(MVz**2 - (chN**2*gv**2*MZ**4*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2))))/(MVz**2*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2) - (2*chN**4*gv**4*MZ**6*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2)/(MVz**4*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**4))',
                  texname = '\\tilde{m}_{\\text{VN}}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))',
               texname = 'g_w')

vv = Parameter(name = 'vv',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(2)*cmath.sqrt((((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))*(MVz**2 - (chN**2*gv**2*MZ**4*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2))))/(MVz**2*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2) - (2*chN**4*gv**4*MZ**6*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2)/(MVz**4*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**4)) - cmath.sqrt((MVz**2 - (chN**2*gv**2*MZ**4*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2))))/(MVz**2*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2) - (2*chN**4*gv**4*MZ**6*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2)/(MVz**4*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**4))*(16*aEW*chN**2*cmath.pi*gv**2*MZ**2 - 4*chN**2*gv**2*MZ**2*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2))) + ((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2*(MVz**2 - (chN**2*gv**2*MZ**4*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2))))/(MVz**2*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2) - (2*chN**4*gv**4*MZ**6*(-4*aEW*cmath.pi + (8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**2)/(MVz**4*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))**4)))))/(chN**2*gv**2*((8*Gf*MVc**2*MVz**2*MZ**2 + chN**2*gv**2*MVc**2*MZ**2*cmath.sqrt(2) - 4*chC**2*gv**2*MVz**2*MZ**2*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)) + cmath.sqrt(-32*aEW*chN**2*cmath.pi*gv**2*MVc**4*MVz**2*MZ**2 + 128*aEW*chC**2*cmath.pi*gv**2*MVc**2*MVz**4*MZ**2 + 2*chN**4*gv**4*MVc**4*MZ**4 - 16*chC**2*chN**2*gv**4*MVc**2*MVz**2*MZ**4 + 32*chC**4*gv**4*MVz**4*MZ**4 + 64*Gf**2*MVc**4*MVz**4*MZ**4 - 128*aEW*cmath.pi*Gf*MVc**4*MVz**4*MZ**2*cmath.sqrt(2) + 16*chN**2*Gf*gv**2*MVc**4*MVz**2*MZ**4*cmath.sqrt(2) - 64*chC**2*Gf*gv**2*MVc**2*MVz**4*MZ**4*cmath.sqrt(2))/(2.*MVc**2*MVz**2*cmath.sqrt(2)))))',
               texname = '\\tilde{v}')

mmVc = Parameter(name = 'mmVc',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(mmVct**2 - cvvhhC*gv**2*vv**2)',
                 texname = 'm_{\\text{VC}}')

mmVz = Parameter(name = 'mmVz',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(mmVzt**2 - cvvhhN*gv**2*vv**2)',
                 texname = 'm_{\\text{VN}}')

mWt = Parameter(name = 'mWt',
                nature = 'internal',
                type = 'real',
                value = '(gw*vv)/2.',
                texname = '\\tilde{m}_W')

swt = Parameter(name = 'swt',
                nature = 'internal',
                type = 'real',
                value = 'ee/gw',
                texname = '\\tilde{s}_w')

zetaC = Parameter(name = 'zetaC',
                  nature = 'internal',
                  type = 'real',
                  value = '(gv*vv)/mmVct',
                  texname = '\\zeta _C')

zetaN = Parameter(name = 'zetaN',
                  nature = 'internal',
                  type = 'real',
                  value = '(gv*vv)/(2.*mmVzt)',
                  texname = '\\zeta _N')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vv',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vv',
               texname = '\\text{yc}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vv',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vv',
                 texname = '\\text{ytau}')

cwt = Parameter(name = 'cwt',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - swt**2)',
                texname = '\\tilde{c}_w')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(mmVct**2 + mWt**2 - cmath.sqrt((mmVct**2 - mWt**2)**2 + chC**2*gv**2*gw**2*vv**4))/cmath.sqrt(2)',
               texname = 'M_W')

thC = Parameter(name = 'thC',
                nature = 'internal',
                type = 'real',
                value = '-0.5*cmath.atan((2*chC*mmVct*mWt*zetaC)/(mmVct**2 - mWt**2))',
                texname = '\\theta _C')

cC = Parameter(name = 'cC',
               nature = 'internal',
               type = 'real',
               value = 'cmath.cos(thC)',
               texname = 'c_C')

mZt = Parameter(name = 'mZt',
                nature = 'internal',
                type = 'real',
                value = 'mWt/cwt',
                texname = '\\tilde{m}_Z')

sC = Parameter(name = 'sC',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sin(thC)',
               texname = 's_C')

twt = Parameter(name = 'twt',
                nature = 'internal',
                type = 'real',
                value = 'swt/cwt',
                texname = '\\tilde{t}_w')

gz = Parameter(name = 'gz',
               nature = 'internal',
               type = 'real',
               value = 'gw/cwt',
               texname = 'g_z')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'gw*twt',
               texname = 'g_1')

thN = Parameter(name = 'thN',
                nature = 'internal',
                type = 'real',
                value = '-0.5*cmath.atan((2*chN*mmVzt*mZt*zetaN)/(mmVzt**2 - mZt**2))',
                texname = '\\theta _N')

cN = Parameter(name = 'cN',
               nature = 'internal',
               type = 'real',
               value = 'cmath.cos(thN)',
               texname = 'c_N')

sN = Parameter(name = 'sN',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sin(thN)',
               texname = 's_N')

WVc = Parameter(name = 'WVc',
                nature = 'internal',
                type = 'real',
                value = '(ee**2*MVc*sC**2)/(16.*cmath.pi*swt**2) + (cC**2*(MVc - MW)*(MVc + MW)*(MVc**2 + MW**2)*sC**2*(cwt**2*g1**2*((1 + 3*cvvbC + cvvbC**2)*MVc**4 - 2*(7 + 3*cvvbC + cvvbC**2)*MVc**2*MW**2 + (1 + 3*cvvbC + cvvbC**2)*MW**4) - cwt*g1*gw*(5*(1 + cvvbC)*MVc**4 - 2*(17 + 5*cvvbC)*MVc**2*MW**2 + 5*(1 + cvvbC)*MW**4)*swt + gw**2*(5*MVc**4 - 22*MVc**2*MW**2 + 5*MW**4)*swt**2))/(96.*cmath.pi*MVc**5*MW**2) + (cC**2*(MVc**4 + (MW**2 - MZ**2)**2 - 2*MVc**2*(MW**2 + MZ**2))**1.5*sC**2*(gv**2*(6*cvvvC*cvvvN*(MVc**2 + MW**2)*MZ**2 + cvvvN**2*MZ**2*(2*MVc**2 + 2*MW**2 + MZ**2) + cvvvC**2*(MVc**4 + MW**4 + 2*MW**2*MZ**2 + 2*MVc**2*(5*MW**2 + MZ**2)))*sN**2 + cN**2*(cwt**2*gw**2*(MVc**4 + MW**4 + 10*MW**2*MZ**2 + MZ**4 + 10*MVc**2*(MW**2 + MZ**2)) + 2*cwt*g1*gw*(MVc**4 + MW**4 + 5*(1 + cvvbC)*MW**2*MZ**2 + cvvbC*MZ**4 + 5*MVc**2*(2*MW**2 + (1 + cvvbC)*MZ**2))*swt + g1**2*(MVc**4 + MW**4 + 2*(1 + 3*cvvbC + cvvbC**2)*MW**2*MZ**2 + cvvbC**2*MZ**4 + 2*MVc**2*(5*MW**2 + (1 + 3*cvvbC + cvvbC**2)*MZ**2))*swt**2) + 2*cN*gv*sN*(cvvvN*MZ**2*(cwt*gw*(5*MVc**2 + 5*MW**2 + MZ**2) + g1*((3 + 2*cvvbC)*MVc**2 + (3 + 2*cvvbC)*MW**2 + cvvbC*MZ**2)*swt) + cvvvC*(cwt*gw*(MVc**4 + MW**4 + 5*MW**2*MZ**2 + 5*MVc**2*(2*MW**2 + MZ**2)) + g1*(MVc**4 + MW**4 + (2 + 3*cvvbC)*MW**2*MZ**2 + MVc**2*(10*MW**2 + (2 + 3*cvvbC)*MZ**2))*swt))))/(192.*cmath.pi*MVc**5*MW**2*MZ**2) + (CKM1x1*MVc*(ee**2*sC**2 + cC**2*cuRC**2*gv**2*swt**2)*complexconjugate(CKM1x1))/(8.*cmath.pi*swt**2) + (CKM1x2*MVc*(ee**2*sC**2 + cC**2*cuRC**2*gv**2*swt**2)*complexconjugate(CKM1x2))/(8.*cmath.pi*swt**2) - ((ee**2*(MB**4 + MT**4 + MT**2*MVc**2 - 2*MVc**4 + MB**2*(-2*MT**2 + MVc**2))*sC**2 - 12*cC*cuR3C*ee*gv*MB*MT*MVc**2*sC*swt + cC**2*cuR3C**2*gv**2*(MB**4 + MT**4 + MT**2*MVc**2 - 2*MVc**4 + MB**2*(-2*MT**2 + MVc**2))*swt**2)*cmath.sqrt(MB**4 + (MT**2 - MVc**2)**2 - 2*MB**2*(MT**2 + MVc**2)))/(32.*cmath.pi*MVc**5*swt**2) + ((MH**4 + MVc**4 + 10*MVc**2*MW**2 + MW**4 - 2*MH**2*(MVc**2 + MW**2))*(2*aa*cC*mWt**2*sC + gv*(-(cC**2*chC*gw) - 2*cC*cvvhhC*gv*sC + chC*gw*sC**2)*vv**2)**2*cmath.sqrt(MH**4 + (MVc**2 - MW**2)**2 - 2*MH**2*(MVc**2 + MW**2)))/(192.*cmath.pi*MVc**5*MW**2*vv**2)',
                texname = '\\gamma _{V^+}')

WVz = Parameter(name = 'WVz',
                nature = 'internal',
                type = 'real',
                value = '(MVz*(cwt**2*ee*sN + clN*cN*cwt*gv*swt + ee*sN*swt**2)**2)/(32.*cwt**2*cmath.pi*swt**2) + (MVz*(cwt**4*ee**2*sN**2 - 2*clN*cN*cwt**3*ee*gv*sN*swt + cwt**2*(ceRN**2*cN**2*gv**2 + clN**2*cN**2*gv**2 - 2*ee**2*sN**2)*swt**2 + 2*(2*ceRN + clN)*cN*cwt*ee*gv*sN*swt**3 + 5*ee**2*sN**2*swt**4))/(32.*cwt**2*cmath.pi*swt**2) + (MVz*(9*cwt**4*ee**2*sN**2 - 18*cN*cqLN*cwt**3*ee*gv*sN*swt + 3*cwt**2*(3*cdRN**2*cN**2*gv**2 + 3*cN**2*cqLN**2*gv**2 + 2*ee**2*sN**2)*swt**2 + 6*cN*(2*cdRN - cqLN)*cwt*ee*gv*sN*swt**3 + 5*ee**2*sN**2*swt**4))/(144.*cwt**2*cmath.pi*swt**2) + (MVz*(9*cwt**4*ee**2*sN**2 + 18*cN*cqLN*cwt**3*ee*gv*sN*swt + 3*cwt**2*(3*cN**2*(cqLN**2 + cuRN**2)*gv**2 - 2*ee**2*sN**2)*swt**2 - 6*cN*(cqLN + 4*cuRN)*cwt*ee*gv*sN*swt**3 + 17*ee**2*sN**2*swt**4))/(144.*cwt**2*cmath.pi*swt**2) + ((9*cwt**4*ee**2*(-MB**2 + MVz**2)*sN**2 - 18*cN*cwt**3*ee*gv*(3*cdR3N*MB**2 + cqL3N*(-MB**2 + MVz**2))*sN*swt + 3*cwt**2*(18*cdR3N*cN**2*cqL3N*gv**2*MB**2 + 3*cdR3N**2*cN**2*gv**2*(-MB**2 + MVz**2) + 3*cN**2*cqL3N**2*gv**2*(-MB**2 + MVz**2) + 2*ee**2*(-7*MB**2 + MVz**2)*sN**2)*swt**2 - 6*cN*cwt*ee*gv*(5*cdR3N*MB**2 - 7*cqL3N*MB**2 - 2*cdR3N*MVz**2 + cqL3N*MVz**2)*sN*swt**3 + ee**2*(-17*MB**2 + 5*MVz**2)*sN**2*swt**4)*cmath.sqrt(-4*MB**2*MVz**2 + MVz**4))/(288.*cwt**2*cmath.pi*MVz**3*swt**2) + ((9*cwt**4*ee**2*(-MT**2 + MVz**2)*sN**2 + 18*cN*cwt**3*ee*gv*(3*cuR3N*MT**2 + cqL3N*(-MT**2 + MVz**2))*sN*swt - 3*cwt**2*(3*cN**2*gv**2*(-6*cqL3N*cuR3N*MT**2 + cqL3N**2*(MT**2 - MVz**2) + cuR3N**2*(MT**2 - MVz**2)) + 2*ee**2*(11*MT**2 + MVz**2)*sN**2)*swt**2 - 6*cN*cwt*ee*gv*(11*cqL3N*MT**2 - cuR3N*MT**2 + cqL3N*MVz**2 + 4*cuR3N*MVz**2)*sN*swt**3 + ee**2*(7*MT**2 + 17*MVz**2)*sN**2*swt**4)*cmath.sqrt(-4*MT**2*MVz**2 + MVz**4))/(288.*cwt**2*cmath.pi*MVz**3*swt**2) + ((MVz - 2*MW)*(MVz + 2*MW)*(cN**2*gv**2*(12*cvvvC*cvvvN*MVz**2*MW**2 + 4*cvvvC**2*MW**2*(MVz**2 + 3*MW**2) + cvvvN**2*(MVz**4 + 4*MVz**2*MW**2))*sC**4 + 2*cN*gv*sC**2*sN*(cC**2*cwt*gw*(2*cvvvC*MW**2*(5*MVz**2 + 6*MW**2) + cvvvN*(MVz**4 + 10*MVz**2*MW**2)) - g1*(2*MW**2*(2*cvvvC*MVz**2 + 3*cvvvN*MVz**2 + 6*cvvvC*MW**2) + cvvbC*MVz**2*(cvvvN*MVz**2 + 6*cvvvC*MW**2 + 4*cvvvN*MW**2))*sC**2*swt) + sN**2*(cC**4*cwt**2*gw**2*(MVz**4 + 20*MVz**2*MW**2 + 12*MW**4) - 2*cC**2*cwt*g1*gw*(cvvbC*MVz**4 + 10*MVz**2*MW**2 + 10*cvvbC*MVz**2*MW**2 + 12*MW**4)*sC**2*swt + g1**2*(12*cvvbC*MVz**2*MW**2 + 4*MW**2*(MVz**2 + 3*MW**2) + cvvbC**2*(MVz**4 + 4*MVz**2*MW**2))*sC**4*swt**2))*cmath.sqrt(MVz**4 - 4*MVz**2*MW**2))/(192.*cmath.pi*MVz**3*MW**4) + ((MH**4 + MVz**4 + 10*MVz**2*MZ**2 + MZ**4 - 2*MH**2*(MVz**2 + MZ**2))*(4*aa*cN*cwt*mZt**2*sN + gv*(-4*cN*cvvhhN*cwt*gv*sN + chN*gw*(-cN**2 + sN**2))*vv**2)**2*cmath.sqrt(MH**4 + (MVz**2 - MZ**2)**2 - 2*MH**2*(MVz**2 + MZ**2)))/(768.*cwt**2*cmath.pi*MVz**5*MZ**2*vv**2)',
                texname = '\\gamma _{V^0}')

