# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Linux x86 (64-bit) (June 16, 2022)
# Date: Mon 17 Mar 2025 11:54:21


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '-G',
                order = {'QCD':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-(complex(0,1)*G**2)',
                order = {'QCD':2})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '(cC*cuR3C*complex(0,1)*gv)/cmath.sqrt(2)',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '(cC*CKM1x1*cuRC*complex(0,1)*gv)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '(cC*CKM1x2*cuRC*complex(0,1)*gv)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '(cC*CKM2x1*cuRC*complex(0,1)*gv)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(cC*CKM2x2*cuRC*complex(0,1)*gv)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = 'cC**2*cN*cwt*complex(0,1)*gw',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(cC**4*complex(0,1)*gw**2)',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-((cuR3C*complex(0,1)*gv*sC)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-((CKM1x1*cuRC*complex(0,1)*gv*sC)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-((CKM1x2*cuRC*complex(0,1)*gv*sC)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-((CKM2x1*cuRC*complex(0,1)*gv*sC)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-((CKM2x2*cuRC*complex(0,1)*gv*sC)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = 'cC*cN*cwt*complex(0,1)*gw*sC',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-(cC**3*complex(0,1)*gw**2*sC)',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '2*cC**3*complex(0,1)*gw**2*sC',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(cC**2*complex(0,1)*gw**2*sC**2)',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(cC*complex(0,1)*gw**2*sC**3)',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '2*cC*complex(0,1)*gw**2*sC**3',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(complex(0,1)*gw**2*sC**4)',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '2*complex(0,1)*gw**2*sC**4',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(cC*ee*complex(0,1))/(swt*cmath.sqrt(2))',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(cC*CKM1x1*ee*complex(0,1))/(swt*cmath.sqrt(2))',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(cC*CKM1x2*ee*complex(0,1))/(swt*cmath.sqrt(2))',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(cC*CKM2x1*ee*complex(0,1))/(swt*cmath.sqrt(2))',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(cC*CKM2x2*ee*complex(0,1))/(swt*cmath.sqrt(2))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(ee*complex(0,1)*sC)/(swt*cmath.sqrt(2))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(CKM1x1*ee*complex(0,1)*sC)/(swt*cmath.sqrt(2))',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(CKM1x2*ee*complex(0,1)*sC)/(swt*cmath.sqrt(2))',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(CKM2x1*ee*complex(0,1)*sC)/(swt*cmath.sqrt(2))',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(CKM2x2*ee*complex(0,1)*sC)/(swt*cmath.sqrt(2))',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-0.5*(cqL3N*complex(0,1)*gv*sN) - (cN*cwt*ee*complex(0,1))/(2.*swt) - (cN*ee*complex(0,1)*swt)/(6.*cwt)',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-0.5*(cqLN*complex(0,1)*gv*sN) - (cN*cwt*ee*complex(0,1))/(2.*swt) - (cN*ee*complex(0,1)*swt)/(6.*cwt)',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-0.5*(cqL3N*complex(0,1)*gv*sN) + (cN*cwt*ee*complex(0,1))/(2.*swt) - (cN*ee*complex(0,1)*swt)/(6.*cwt)',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-0.5*(cqLN*complex(0,1)*gv*sN) + (cN*cwt*ee*complex(0,1))/(2.*swt) - (cN*ee*complex(0,1)*swt)/(6.*cwt)',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-0.5*(cdR3N*complex(0,1)*gv*sN) + (cN*ee*complex(0,1)*swt)/(3.*cwt)',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-0.5*(cdRN*complex(0,1)*gv*sN) + (cN*ee*complex(0,1)*swt)/(3.*cwt)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-0.5*(clN*complex(0,1)*gv*sN) - (cN*cwt*ee*complex(0,1))/(2.*swt) + (cN*ee*complex(0,1)*swt)/(2.*cwt)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-0.5*(clN*complex(0,1)*gv*sN) + (cN*cwt*ee*complex(0,1))/(2.*swt) + (cN*ee*complex(0,1)*swt)/(2.*cwt)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-0.5*(cuR3N*complex(0,1)*gv*sN) - (2*cN*ee*complex(0,1)*swt)/(3.*cwt)',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-0.5*(cuRN*complex(0,1)*gv*sN) - (2*cN*ee*complex(0,1)*swt)/(3.*cwt)',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-0.5*(ceRN*complex(0,1)*gv*sN) + (cN*ee*complex(0,1)*swt)/cwt',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = 'cN*cwt*complex(0,1)*gw*sC**2 - cC**2*cvvvC*complex(0,1)*gv*sN - cC**2*cN*complex(0,1)*g1*swt',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(cN*cwt*complex(0,1)*gw*sC**2) + cC**2*cvvvC*complex(0,1)*gv*sN + cC**2*cN*complex(0,1)*g1*swt',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = 'cN*cwt*complex(0,1)*gw*sC**2 - cC**2*cvvvN*complex(0,1)*gv*sN - cC**2*cN*cvvbC*complex(0,1)*g1*swt',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(cN*cwt*complex(0,1)*gw*sC**2) + cC**2*cvvvN*complex(0,1)*gv*sN + cC**2*cN*cvvbC*complex(0,1)*g1*swt',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(cwt*complex(0,1)*g1*sC**2) - cC**2*complex(0,1)*gw*swt',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-(cvvbC*cwt*complex(0,1)*g1*sC**2) - cC**2*complex(0,1)*gw*swt',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = 'cwt*complex(0,1)*g1*sC**2 + cC**2*complex(0,1)*gw*swt',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = 'cvvbC*cwt*complex(0,1)*g1*sC**2 + cC**2*complex(0,1)*gw*swt',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(cC*cN*cwt*complex(0,1)*gw*sC) - cC*cvvvC*complex(0,1)*gv*sC*sN - cC*cN*complex(0,1)*g1*sC*swt',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = 'cC*cvvvC*complex(0,1)*gv*sC*sN + cC*cN*complex(0,1)*g1*sC*swt',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = 'cC*cN*cwt*complex(0,1)*gw*sC + cC*cvvvC*complex(0,1)*gv*sC*sN + cC*cN*complex(0,1)*g1*sC*swt',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(cC*cN*cwt*complex(0,1)*gw*sC) - cC*cvvvN*complex(0,1)*gv*sC*sN - cC*cN*cvvbC*complex(0,1)*g1*sC*swt',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = 'cC*cvvvN*complex(0,1)*gv*sC*sN + cC*cN*cvvbC*complex(0,1)*g1*sC*swt',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = 'cC*cN*cwt*complex(0,1)*gw*sC + cC*cvvvN*complex(0,1)*gv*sC*sN + cC*cN*cvvbC*complex(0,1)*g1*sC*swt',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = 'cC*cwt*complex(0,1)*g1*sC - cC*complex(0,1)*gw*sC*swt',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = 'cC*cvvbC*cwt*complex(0,1)*g1*sC - cC*complex(0,1)*gw*sC*swt',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-(cC*cwt*complex(0,1)*g1*sC) + cC*complex(0,1)*gw*sC*swt',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(cC*cvvbC*cwt*complex(0,1)*g1*sC) + cC*complex(0,1)*gw*sC*swt',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-2*cC*cvvvC*cwt*complex(0,1)*g1*gv*sC*sN - 2*cC*cN*cwt*complex(0,1)*g1**2*sC*swt - 2*cC*cN*cwt*complex(0,1)*gw**2*sC*swt',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '-(cvvvC*complex(0,1)*gv*sC**2*sN) - cN*complex(0,1)*g1*sC**2*swt',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-(cvvvN*complex(0,1)*gv*sC**2*sN) - cN*cvvbC*complex(0,1)*g1*sC**2*swt',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '2*cvvvC*cwt*complex(0,1)*g1*gv*sC**2*sN - 2*cC**2*cN*cwt*complex(0,1)*gw**2*swt + 2*cN*cwt*complex(0,1)*g1**2*sC**2*swt',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '-(cC**2*cwt*complex(0,1)*g1) - complex(0,1)*gw*sC**2*swt',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-(cC**2*cvvbC*cwt*complex(0,1)*g1) - complex(0,1)*gw*sC**2*swt',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = 'cC**2*cwt*complex(0,1)*g1 + complex(0,1)*gw*sC**2*swt',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = 'cC**2*cvvbC*cwt*complex(0,1)*g1 + complex(0,1)*gw*sC**2*swt',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '2*cC**2*cvvvC*cwt*complex(0,1)*g1*gv*sN + 2*cC**2*cN*cwt*complex(0,1)*g1**2*swt - 2*cN*cwt*complex(0,1)*gw**2*sC**2*swt',
                 order = {'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '(cN*cqL3N*complex(0,1)*gv)/2. - (cwt*ee*complex(0,1)*sN)/(2.*swt) - (ee*complex(0,1)*sN*swt)/(6.*cwt)',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '(cN*cqLN*complex(0,1)*gv)/2. - (cwt*ee*complex(0,1)*sN)/(2.*swt) - (ee*complex(0,1)*sN*swt)/(6.*cwt)',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(cN*cqL3N*complex(0,1)*gv)/2. + (cwt*ee*complex(0,1)*sN)/(2.*swt) - (ee*complex(0,1)*sN*swt)/(6.*cwt)',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '(cN*cqLN*complex(0,1)*gv)/2. + (cwt*ee*complex(0,1)*sN)/(2.*swt) - (ee*complex(0,1)*sN*swt)/(6.*cwt)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(cdR3N*cN*complex(0,1)*gv)/2. + (ee*complex(0,1)*sN*swt)/(3.*cwt)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(cdRN*cN*complex(0,1)*gv)/2. + (ee*complex(0,1)*sN*swt)/(3.*cwt)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(clN*cN*complex(0,1)*gv)/2. - (cwt*ee*complex(0,1)*sN)/(2.*swt) + (ee*complex(0,1)*sN*swt)/(2.*cwt)',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '(clN*cN*complex(0,1)*gv)/2. + (cwt*ee*complex(0,1)*sN)/(2.*swt) + (ee*complex(0,1)*sN*swt)/(2.*cwt)',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(cN*cuR3N*complex(0,1)*gv)/2. - (2*ee*complex(0,1)*sN*swt)/(3.*cwt)',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(cN*cuRN*complex(0,1)*gv)/2. - (2*ee*complex(0,1)*sN*swt)/(3.*cwt)',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(ceRN*cN*complex(0,1)*gv)/2. + (ee*complex(0,1)*sN*swt)/cwt',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = 'cC**2*cN*cvvvC*complex(0,1)*gv + cwt*complex(0,1)*gw*sC**2*sN - cC**2*complex(0,1)*g1*sN*swt',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-(cC**2*cN*cvvvC*complex(0,1)*gv) - cwt*complex(0,1)*gw*sC**2*sN + cC**2*complex(0,1)*g1*sN*swt',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = 'cC**2*cN*cvvvN*complex(0,1)*gv + cwt*complex(0,1)*gw*sC**2*sN - cC**2*cvvbC*complex(0,1)*g1*sN*swt',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-(cC**2*cN*cvvvN*complex(0,1)*gv) - cwt*complex(0,1)*gw*sC**2*sN + cC**2*cvvbC*complex(0,1)*g1*sN*swt',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = 'cC*cN*cvvvC*complex(0,1)*gv*sC - cC*cwt*complex(0,1)*gw*sC*sN - cC*complex(0,1)*g1*sC*sN*swt',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-(cC*cN*cvvvC*complex(0,1)*gv*sC) + cC*cwt*complex(0,1)*gw*sC*sN + cC*complex(0,1)*g1*sC*sN*swt',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = 'cC*cN*cvvvN*complex(0,1)*gv*sC - cC*cwt*complex(0,1)*gw*sC*sN - cC*cvvbC*complex(0,1)*g1*sC*sN*swt',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-(cC*cN*cvvvN*complex(0,1)*gv*sC) + cC*cwt*complex(0,1)*gw*sC*sN + cC*cvvbC*complex(0,1)*g1*sC*sN*swt',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '-(cC*cN*cvvvC*cwt*complex(0,1)*g1*gv*sC) + cC*cwt*complex(0,1)*g1**2*sC*sN*swt + cC*cwt*complex(0,1)*gw**2*sC*sN*swt',
                 order = {'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '2*cC*cN*cvvvC*cwt*complex(0,1)*g1*gv*sC - 2*cC*cwt*complex(0,1)*g1**2*sC*sN*swt - 2*cC*cwt*complex(0,1)*gw**2*sC*sN*swt',
                 order = {'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = 'cN*cvvvC*complex(0,1)*gv*sC**2 + cC**2*cwt*complex(0,1)*gw*sN - complex(0,1)*g1*sC**2*sN*swt',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-(cN*cvvvC*complex(0,1)*gv*sC**2) - cC**2*cwt*complex(0,1)*gw*sN + complex(0,1)*g1*sC**2*sN*swt',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = 'cN*cvvvN*complex(0,1)*gv*sC**2 + cC**2*cwt*complex(0,1)*gw*sN - cvvbC*complex(0,1)*g1*sC**2*sN*swt',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(cN*cvvvN*complex(0,1)*gv*sC**2) - cC**2*cwt*complex(0,1)*gw*sN + cvvbC*complex(0,1)*g1*sC**2*sN*swt',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = 'cN*cvvvC*cwt*complex(0,1)*g1*gv*sC**2 + cC**2*cwt*complex(0,1)*gw**2*sN*swt - cwt*complex(0,1)*g1**2*sC**2*sN*swt',
                  order = {'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = 'cC**2*cN*cvvvC*cwt*complex(0,1)*g1*gv - cC**2*cwt*complex(0,1)*g1**2*sN*swt + cwt*complex(0,1)*gw**2*sC**2*sN*swt',
                  order = {'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '-2*cC**2*cN*cvvvC*cwt*complex(0,1)*g1*gv + 2*cC**2*cwt*complex(0,1)*g1**2*sN*swt - 2*cwt*complex(0,1)*gw**2*sC**2*sN*swt',
                  order = {'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = 'cN**2*cwt**2*complex(0,1)*gw**2*sC**2 + 2*cC**2*cN*cvvvC*complex(0,1)*g1*gv*sN*swt + cC**2*cN**2*complex(0,1)*g1**2*swt**2',
                  order = {'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '-2*cN**2*cwt**2*complex(0,1)*gw**2*sC**2 - 4*cC**2*cN*cvvvC*complex(0,1)*g1*gv*sN*swt - 2*cC**2*cN**2*complex(0,1)*g1**2*swt**2',
                  order = {'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = 'cwt**2*complex(0,1)*g1**2*sC**2 + cC**2*complex(0,1)*gw**2*swt**2',
                  order = {'QED':2})

GC_108 = Coupling(name = 'GC_108',
                  value = 'cC*cN**2*cwt**2*complex(0,1)*gw**2*sC - 2*cC*cN*cvvvC*complex(0,1)*g1*gv*sC*sN*swt - cC*cN**2*complex(0,1)*g1**2*sC*swt**2',
                  order = {'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '-2*cC*cN**2*cwt**2*complex(0,1)*gw**2*sC + 4*cC*cN*cvvvC*complex(0,1)*g1*gv*sC*sN*swt + 2*cC*cN**2*complex(0,1)*g1**2*sC*swt**2',
                  order = {'QED':2})

GC_110 = Coupling(name = 'GC_110',
                  value = '-(cC*cwt**2*complex(0,1)*g1**2*sC) + cC*complex(0,1)*gw**2*sC*swt**2',
                  order = {'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '2*cC*cwt**2*complex(0,1)*g1**2*sC - 2*cC*complex(0,1)*gw**2*sC*swt**2',
                  order = {'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = 'cC**2*cN**2*cwt**2*complex(0,1)*gw**2 + 2*cN*cvvvC*complex(0,1)*g1*gv*sC**2*sN*swt + cN**2*complex(0,1)*g1**2*sC**2*swt**2',
                  order = {'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '-2*cC**2*cN**2*cwt**2*complex(0,1)*gw**2 - 4*cN*cvvvC*complex(0,1)*g1*gv*sC**2*sN*swt - 2*cN**2*complex(0,1)*g1**2*sC**2*swt**2',
                  order = {'QED':2})

GC_114 = Coupling(name = 'GC_114',
                  value = 'cC**2*cwt**2*complex(0,1)*g1**2 + complex(0,1)*gw**2*sC**2*swt**2',
                  order = {'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '-2*cC**2*cwt**2*complex(0,1)*g1**2 - 2*complex(0,1)*gw**2*sC**2*swt**2',
                  order = {'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = 'cN*cwt**2*complex(0,1)*gw**2*sC**2*sN - cC**2*cN**2*cvvvC*complex(0,1)*g1*gv*swt + cC**2*cvvvC*complex(0,1)*g1*gv*sN**2*swt + cC**2*cN*complex(0,1)*g1**2*sN*swt**2',
                  order = {'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = 'cC*cN*cwt**2*complex(0,1)*gw**2*sC*sN + cC*cN**2*cvvvC*complex(0,1)*g1*gv*sC*swt - cC*cvvvC*complex(0,1)*g1*gv*sC*sN**2*swt - cC*cN*complex(0,1)*g1**2*sC*sN*swt**2',
                  order = {'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '-2*cC**2*cN*cwt**2*complex(0,1)*gw**2*sN + 2*cN**2*cvvvC*complex(0,1)*g1*gv*sC**2*swt - 2*cvvvC*complex(0,1)*g1*gv*sC**2*sN**2*swt - 2*cN*complex(0,1)*g1**2*sC**2*sN*swt**2',
                  order = {'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = 'cwt**2*complex(0,1)*gw**2*sC**2*sN**2 - 2*cC**2*cN*cvvvC*complex(0,1)*g1*gv*sN*swt + cC**2*complex(0,1)*g1**2*sN**2*swt**2',
                  order = {'QED':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '-2*cwt**2*complex(0,1)*gw**2*sC**2*sN**2 + 4*cC**2*cN*cvvvC*complex(0,1)*g1*gv*sN*swt - 2*cC**2*complex(0,1)*g1**2*sN**2*swt**2',
                  order = {'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = 'cC*cwt**2*complex(0,1)*gw**2*sC*sN**2 + 2*cC*cN*cvvvC*complex(0,1)*g1*gv*sC*sN*swt - cC*complex(0,1)*g1**2*sC*sN**2*swt**2',
                  order = {'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '-2*cC*cwt**2*complex(0,1)*gw**2*sC*sN**2 - 4*cC*cN*cvvvC*complex(0,1)*g1*gv*sC*sN*swt + 2*cC*complex(0,1)*g1**2*sC*sN**2*swt**2',
                  order = {'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = 'cC**2*cwt**2*complex(0,1)*gw**2*sN**2 - 2*cN*cvvvC*complex(0,1)*g1*gv*sC**2*sN*swt + complex(0,1)*g1**2*sC**2*sN**2*swt**2',
                  order = {'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '2*cC*chC*complex(0,1)*gv*gw*sC + 2*cvvhhC*complex(0,1)*gv**2*sC**2 + (2*bb*cC**2*complex(0,1)*mWt**2)/vv**2',
                  order = {'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '(chN*cN*complex(0,1)*gv*gw*sN)/cwt + 2*cvvhhN*complex(0,1)*gv**2*sN**2 + (2*bb*cN**2*complex(0,1)*mZt**2)/vv**2',
                  order = {'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '-(cC**2*chC*complex(0,1)*gv*gw) - 2*cC*cvvhhC*complex(0,1)*gv**2*sC + chC*complex(0,1)*gv*gw*sC**2 + (2*bb*cC*complex(0,1)*mWt**2*sC)/vv**2',
                  order = {'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '2*cC**2*cvvhhC*complex(0,1)*gv**2 - 2*cC*chC*complex(0,1)*gv*gw*sC + (2*bb*complex(0,1)*mWt**2*sC**2)/vv**2',
                  order = {'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '-0.5*(chN*cN**2*complex(0,1)*gv*gw)/cwt - 2*cN*cvvhhN*complex(0,1)*gv**2*sN + (chN*complex(0,1)*gv*gw*sN**2)/(2.*cwt) + (2*bb*cN*complex(0,1)*mZt**2*sN)/vv**2',
                  order = {'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '2*cN**2*cvvhhN*complex(0,1)*gv**2 - (chN*cN*complex(0,1)*gv*gw*sN)/cwt + (2*bb*complex(0,1)*mZt**2*sN**2)/vv**2',
                  order = {'QED':2})

GC_130 = Coupling(name = 'GC_130',
                  value = '(3*d4*complex(0,1)*MH**2)/vv**2',
                  order = {'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '(3*d3*complex(0,1)*MH**2)/vv',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(2*aa*complex(0,1)*mWt**2*sC**2)/vv + 2*cC**2*cvvhhC*complex(0,1)*gv**2*vv - 2*cC*chC*complex(0,1)*gv*gw*sC*vv',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '(2*aa*cC**2*complex(0,1)*mWt**2)/vv + 2*cC*chC*complex(0,1)*gv*gw*sC*vv + 2*cvvhhC*complex(0,1)*gv**2*sC**2*vv',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '(2*aa*cC*complex(0,1)*mWt**2*sC)/vv - cC**2*chC*complex(0,1)*gv*gw*vv - 2*cC*cvvhhC*complex(0,1)*gv**2*sC*vv + chC*complex(0,1)*gv*gw*sC**2*vv',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(2*aa*complex(0,1)*mZt**2*sN**2)/vv + 2*cN**2*cvvhhN*complex(0,1)*gv**2*vv - (chN*cN*complex(0,1)*gv*gw*sN*vv)/cwt',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(2*aa*cN**2*complex(0,1)*mZt**2)/vv + (chN*cN*complex(0,1)*gv*gw*sN*vv)/cwt + 2*cvvhhN*complex(0,1)*gv**2*sN**2*vv',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(2*aa*cN*complex(0,1)*mZt**2*sN)/vv - (chN*cN**2*complex(0,1)*gv*gw*vv)/(2.*cwt) - 2*cN*cvvhhN*complex(0,1)*gv**2*sN*vv + (chN*complex(0,1)*gv*gw*sN**2*vv)/(2.*cwt)',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-((cpsi*complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '-((cpsi*complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((cpsi*complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-((cpsi*complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(cC*cuRC*complex(0,1)*gv*complexconjugate(CKM1x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((cuRC*complex(0,1)*gv*sC*complexconjugate(CKM1x1))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(cC*ee*complex(0,1)*complexconjugate(CKM1x1))/(swt*cmath.sqrt(2))',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '(ee*complex(0,1)*sC*complexconjugate(CKM1x1))/(swt*cmath.sqrt(2))',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(cC*cuRC*complex(0,1)*gv*complexconjugate(CKM1x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((cuRC*complex(0,1)*gv*sC*complexconjugate(CKM1x2))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(cC*ee*complex(0,1)*complexconjugate(CKM1x2))/(swt*cmath.sqrt(2))',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '(ee*complex(0,1)*sC*complexconjugate(CKM1x2))/(swt*cmath.sqrt(2))',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '(cC*cuRC*complex(0,1)*gv*complexconjugate(CKM2x1))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((cuRC*complex(0,1)*gv*sC*complexconjugate(CKM2x1))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(cC*ee*complex(0,1)*complexconjugate(CKM2x1))/(swt*cmath.sqrt(2))',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '(ee*complex(0,1)*sC*complexconjugate(CKM2x1))/(swt*cmath.sqrt(2))',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(cC*cuRC*complex(0,1)*gv*complexconjugate(CKM2x2))/cmath.sqrt(2)',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '-((cuRC*complex(0,1)*gv*sC*complexconjugate(CKM2x2))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '(cC*ee*complex(0,1)*complexconjugate(CKM2x2))/(swt*cmath.sqrt(2))',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '(ee*complex(0,1)*sC*complexconjugate(CKM2x2))/(swt*cmath.sqrt(2))',
                  order = {'QED':1})

