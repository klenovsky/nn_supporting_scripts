import sys, os
import numpy as na

#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\self_consistent_kp_t5_typeII_elConcDep_negSRLonly\\'

#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\SiGeQD_optical_transition\\'
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\ARRT_ALGaAs_QD_EDep\\'
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\ARRT_ALGaAs_QD_StrainDep\\'
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\ARRT_ALGaAs_QD_SCStrainDep\\'
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\ARRT_ALGaAs_QD_EStrainDep\\'
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\ARRT_ALGaAs_QD_SCEStrainDep\\'
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\ARRT_ALGaAs_QD_BiaxStrainDep_NoPiezo\\'
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\PolArticle_GaAsSbLayerThickDep_semiellipsoidQD_InTrump\\'
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\ARRT_140925_ALGaAs_QD_EStrainDep\\'
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\'
path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\polPap_eli_In0.6_Sb0.24_highDoping_OIqns0_SRLTdep\\'


#pref='140321_semiellipsoid_kp_QD8x22_0dotAxis_dotIn1_Sb0.2_negSRLonly_ELCONC_'
#pref='140524_cone_SiGe_110x18_5K_Walle_h_Cargill_e_0d13_0d17_0d634_OI_0.5x1_ELCONC_'
#pref='140807_3DARRTInAsQD_1bEl_6bHl_In0.4to0.1_elField_elField_'
#pref='140807_3DARRTInAsQD_1bEl_6bHl_In0.4to0.1_elField_YSTRAIN_'
#pref='140808_3DARRTInAsQD_1bEl_6bHl_In0.4to0.1_'
#pref='140924_3DARRTInAsQD_1bEl_6bHl_InvPyrIn0.6to0.1_'
#pref='141122_3DARRTInAsQD_8bEl_8bHl_In0.4to0.1_biax_1ex1hh_SC_YSTRAIN_'
pref='141012_semiellipsoid_asPyr_Sb0.24_80K_dotIn0.6_2x2st_OI_noSC_d10e19_qns0_perXYZ_TERTHICK_'


sliceName='wf_probability_dot_kp8_0000_0002'    #.dat data
matName='material'    #.dat data

directions=list([
[ [0,1,0], [0,0,1] ],
[ [1,0,0], [0,0,1] ],
#[ [1,1,0], [0,0,1] ],
#[ [1,-1,0], [0,0,1] ],
#[ [0,1,0], [1,0,0] ],
#[ [1,-1,0], [1,1,0] ],
#[ [-1,1,0], [1,1,0] ],
])

slicePoints=[0,0,0]


dir_n = [
#'HFtest',

#ARRT biaxial strain dependence
#pref+'-0.011758',
#pref+'0.0',
#pref+'0.011758',





#ARRT pin diode [110] el field and strain dep
#pref+'elField_-938989_YSTRAIN_-0.00245987',
#pref+'elField_-766158_YSTRAIN_-0.00200710',
#pref+'elField_-586754_YSTRAIN_-0.00153712',
#pref+'elField_-399964_YSTRAIN_-0.00104779',
#pref+'elField_-204793_YSTRAIN_-0.00053650',
#pref+'elField_0_YSTRAIN_0.00000000',
#pref+'elField_215996_YSTRAIN_0.00056584',
#pref+'elField_445264_YSTRAIN_0.00116646',
#pref+'elField_690599_YSTRAIN_0.00180916',
#pref+'elField_955943_YSTRAIN_0.00250428',
#pref+'elField_1247171_YSTRAIN_0.00326721',


#ARRT pin diode [110] strain dep
#pref+'0.00245987',
#pref+'0.00200710',
#pref+'0.00153712',
#pref+'0.00104779',
#pref+'0.00053650',
#pref+'0.00000000',
#pref+'-0.00056584',
#pref+'-0.00116646',
#pref+'-0.00180916',
#pref+'-0.00250428',
#pref+'-0.00326721',


#ARRT pin diode vertical E field dep
#pref+'-938989',
#pref+'-766158',
#pref+'-586754',
#pref+'-399964',
#pref+'-204793',
#pref+'0',
#pref+'215996',
#pref+'445264',
#pref+'690599',
#pref+'955943',
#pref+'1247171',




#SiGe self consistent calc
#pref+'1.0e12',
#pref+'1.0e14',
#pref+'1.0e15',
#pref+'5.0e15',
#pref+'1.0e16',
#pref+'5.0e16',
#pref+'1.0e17',
#pref+'5.0e17',
#pref+'1.0e18',
#pref+'5.0e18',




#SRL Sb dep
#pref+'1.0E-1',
#pref+'1.2E-1',
#pref+'1.4E-1',
#pref+'1.6E-1',
#pref+'1.8E-1',
#pref+'2.0E-1',
#pref+'2.2E-1',




#QD elongation
#pref+'0.5',
#pref+'0.625',
#pref+'0.76923076',
#pref+'0.90909090',
#pref+'1.0',
#pref+'1.1',
#pref+'1.3',
#pref+'1.6',
#pref+'2.0',



#SRL thickness
pref+'1',
#pref+'2',
#pref+'3',
#pref+'4',
#pref+'5',
#pref+'6',
#pref+'7',
#pref+'8',
#pref+'9',
#pref+'10',
#pref+'11',
#pref+'12',
#pref+'13',
#pref+'14',
#pref+'15',
#pref+'16',
#pref+'17',
#pref+'18',
#pref+'19',
#pref+'20',

#
#
#self consistent calc
#pref+'1.0e14',
#pref+'5.0e14',
#pref+'1.0e15',
#pref+'5.0e15',
#pref+'1.0e16',
#pref+'5.0e16',
#pref+'1.0e17',
#pref+'5.0e17',
#pref+'1.0e18',
#pref+'5.0e18',
#
#
#
#
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\self_consistent_kp_t5_typeII_elConcDep\\'
#'140316_semiellipsoid_QD8x22_t10_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_1.0e14',
#'140316_semiellipsoid_QD8x22_t10_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_5.0e14',
#'140316_semiellipsoid_QD8x22_t10_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_1.0e15',
#'140316_semiellipsoid_QD8x22_t10_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_5.0e15',
#'140316_semiellipsoid_QD8x22_t10_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_1.0e16',
#'140316_semiellipsoid_QD8x22_t10_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_5.0e16',
#'140316_semiellipsoid_QD8x22_t10_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_1.0e17',
#'140316_semiellipsoid_QD8x22_t10_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_5.0e17',
##'140316_semiellipsoid_QD8x22_t10_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_1.0e18',
##'140316_semiellipsoid_QD8x22_t10_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_5.0e18',
#
#
#
#
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\self_consistent_kp_t5_typeII_elConcDep\\'
#'140315_semiellipsoid_QD8x22_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_0.0',
#'140315_semiellipsoid_QD8x22_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_1.0e14',
#'140315_semiellipsoid_QD8x22_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_5.0e14',
#'140315_semiellipsoid_QD8x22_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_1.0e15',
#'140315_semiellipsoid_QD8x22_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_5.0e15',
#'140315_semiellipsoid_QD8x22_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_1.0e16',
#'140315_semiellipsoid_QD8x22_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_5.0e16',
#'140315_semiellipsoid_QD8x22_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_1.0e17',
#'140315_semiellipsoid_QD8x22_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_5.0e17',
#'140315_semiellipsoid_QD8x22_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_1.0e18',
##'140315_semiellipsoid_QD8x22_0dotAxis_dotIn1_Sb0.2_kp_ELCONC_5.0e18',
#
#
#
#
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\671C_3xQD_decreaseHeightUpVK\\'
#'140306_semiellipsoid_3xQD671C_QD3x40_0dotAxis_dotIn1_ascendLensVK_ELONG_0.5',
#'140306_semiellipsoid_3xQD671C_QD3x40_0dotAxis_dotIn1_ascendLensVK_ELONG_0.75',
#'140306_semiellipsoid_3xQD671C_QD3x40_0dotAxis_dotIn1_ascendLensVK_ELONG_0.9',
#'140306_semiellipsoid_3xQD671C_QD3x40_0dotAxis_dotIn1_ascendLensVK_ELONG_1.0',
#'140306_semiellipsoid_3xQD671C_QD3x40_0dotAxis_dotIn1_ascendLensVK_ELONG_1.1',
#'140306_semiellipsoid_3xQD671C_QD3x40_0dotAxis_dotIn1_ascendLensVK_ELONG_1.25',
#'140306_semiellipsoid_3xQD671C_QD3x40_0dotAxis_dotIn1_ascendLensVK_ELONG_1.5',
#
#
#
#
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\671C_3xQD_increaseUp\\'
#'140223_semiellipsoid_3xQD671C_QD3x40_0dotAxis_dotIn1_invAscHeightLensVK_ASPECT_0.064',
#
#
#
#
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\671C_3xQD\\'
#'140222_semiellipsoid_3xQD671C_QD3x40_0dotAxis_dotIn1_ascendLensVK_ASPECT_0.064',
#
#
#
#
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\671C_trump\\'
#'140221_semiellipsoid_671C_1xQD3x40_0dotAxis_dotTrumpIn0.4to1_ASPECT_0.064',
#
#
#
#
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\671C_elong\\'
#'140221_semiellipsoid_671C_1xQD3x40_0dotAxis_dotIn1_ELONG_0.8',
#'140221_semiellipsoid_671C_1xQD3x40_0dotAxis_dotIn1_ELONG_1.0',
#'140221_semiellipsoid_671C_1xQD3x40_0dotAxis_dotIn1_ELONG_1.2',
#'140221_semiellipsoid_671C_1xQD3x40_0dotAxis_dotIn1_ELONG_1.4',
#'140221_semiellipsoid_671C_1xQD3x40_0dotAxis_dotIn1_ELONG_1.6',
#
#
#
#
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\671C\\'
#'140220_semiellipsoid_QD3x40_0dotAxis_dotIn1_srlSb0d0_ASPECT_0.032',
#'140220_semiellipsoid_QD3x40_0dotAxis_dotIn1_srlSb0d0_ASPECT_0.064',
#'140220_semiellipsoid_QD3x40_0dotAxis_dotIn1_srlSb0d0_ASPECT_0.128',
#'140220_semiellipsoid_QD3x40_0dotAxis_dotIn1_srlSb0d0_ASPECT_0.256',
#
#
#
#
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.04',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.06',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.08',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.1',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.12',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.14',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.16',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.18',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.2',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.22',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.24',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.26',
#
#
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\vlastik_protazeni_typ-II_korigovany_grid\\'
#'130822_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_ELONG_0.3',
#'130822_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_ELONG_0.5',
#'130822_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_ELONG_0.7',
#'130822_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_ELONG_0.9',
#'130822_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_ELONG_1.0',
#'130822_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_ELONG_1.1',
#'130822_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_ELONG_1.3',
#'130822_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_ELONG_1.5',
#'130822_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_ELONG_1.7',
#'130822_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_ELONG_1.9',
#'130822_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_ELONG_2.0',
#
#
#
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\vlastik_tloustka_SRL_typ-II\\'
#'130820_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_TERTHICK_1',
#'130820_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_TERTHICK_2',
#'130820_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_TERTHICK_3',
#'130820_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_TERTHICK_4',
#'130820_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_TERTHICK_5',
#'130820_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_TERTHICK_6',
#'130820_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_TERTHICK_7',
#'130820_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_TERTHICK_8',
#'130820_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_TERTHICK_9',
#'130820_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_TERTHICK_10',
#'130820_semiellipsoid_QD8x22_0dotAxis_dotIn1_srlSb0d2_TERTHICK_11',
#
#
#
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_0.5',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_0.7',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_0.9',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.1',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.3',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.5',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.7',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.9',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_2',
#
#
#path = 'e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL\\GaAsSbNew120622\\vlastik_protazeni_typ-I\\'
#'130819_semiellipsoid_t5_QD8x22_0dotAxis_dotIn1_srlSb0d02_ELONG_0.3',
#'130819_semiellipsoid_t5_QD8x22_0dotAxis_dotIn1_srlSb0d02_ELONG_0.5',
#'130819_semiellipsoid_t5_QD8x22_0dotAxis_dotIn1_srlSb0d02_ELONG_0.7',
#'130819_semiellipsoid_t5_QD8x22_0dotAxis_dotIn1_srlSb0d02_ELONG_0.9',
#'130819_semiellipsoid_t5_QD8x22_0dotAxis_dotIn1_srlSb0d02_ELONG_1.0',
#'130819_semiellipsoid_t5_QD8x22_0dotAxis_dotIn1_srlSb0d02_ELONG_1.1',
#'130819_semiellipsoid_t5_QD8x22_0dotAxis_dotIn1_srlSb0d02_ELONG_1.3',
#'130819_semiellipsoid_t5_QD8x22_0dotAxis_dotIn1_srlSb0d02_ELONG_1.5',
#'130819_semiellipsoid_t5_QD8x22_0dotAxis_dotIn1_srlSb0d02_ELONG_1.7',
#'130819_semiellipsoid_t5_QD8x22_0dotAxis_dotIn1_srlSb0d02_ELONG_1.9',
#'130819_semiellipsoid_t5_QD8x22_0dotAxis_dotIn1_srlSb0d02_ELONG_2.0',
#
#
#
#Semiellipsoid QD Sb 0.2 [1-10} ELONGATION DEPENDENCE, center axis of QD 0, In=1 composition
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_0.5',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_0.7',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_0.9',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.1',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.3',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.5',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.7',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.9',
#'semiellipsoid_15K_t5_wy22_0dotAxis_In1_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_2',
#
#
#
#Semiellipsoid QD Sb 0.2 [1-10} ELONGATION DEPENDENCE, center axis of QD 0, pyramid In composition
#'semiellipsoid_15K_t5_wy22_0dotAxis_InTrump_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_0.5', 
#'semiellipsoid_15K_t5_wy22_0dotAxis_InTrump_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_0.7',
#'semiellipsoid_15K_t5_wy22_0dotAxis_InTrump_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_0.9',
#'semiellipsoid_15K_t5_wy22_0dotAxis_InTrump_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1',
#'semiellipsoid_15K_t5_wy22_0dotAxis_InTrump_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.1',
#'semiellipsoid_15K_t5_wy22_0dotAxis_InTrump_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.3',
#'semiellipsoid_15K_t5_wy22_0dotAxis_InTrump_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.5',
#'semiellipsoid_15K_t5_wy22_0dotAxis_InTrump_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.7',
#'semiellipsoid_15K_t5_wy22_0dotAxis_InTrump_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_1.9',
#'semiellipsoid_15K_t5_wy22_0dotAxis_InTrump_xy1_z0d5_[1-10]x[110]_elongSameVol_ELONG_2',
#
#
#
#Semiellipsoid QD Sb 0.2 [1-10} ELONGATION DEPENDENCE
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[1-10]x[110]_elongSameVol_ELONG_0.3',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[1-10]x[110]_elongSameVol_ELONG_0.5',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[1-10]x[110]_elongSameVol_ELONG_0.7',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[1-10]x[110]_elongSameVol_ELONG_0.9',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[1-10]x[110]_elongSameVol_ELONG_1',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[1-10]x[110]_elongSameVol_ELONG_1.1',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[1-10]x[110]_elongSameVol_ELONG_1.3',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[1-10]x[110]_elongSameVol_ELONG_1.5',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[1-10]x[110]_elongSameVol_ELONG_1.7',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[1-10]x[110]_elongSameVol_ELONG_1.9',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[1-10]x[110]_elongSameVol_ELONG_2',
#
#
#
#Semiellipsoid QD Sb 0.2 [110] ELONGATION DEPENDENCE
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[-110]x[110]_elongSameVol_ELONG_0.3',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[-110]x[110]_elongSameVol_ELONG_0.5',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[-110]x[110]_elongSameVol_ELONG_0.7',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[-110]x[110]_elongSameVol_ELONG_0.9',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[-110]x[110]_elongSameVol_ELONG_1',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[-110]x[110]_elongSameVol_ELONG_1.1',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[-110]x[110]_elongSameVol_ELONG_1.3',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[-110]x[110]_elongSameVol_ELONG_1.5',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[-110]x[110]_elongSameVol_ELONG_1.7',
#'semiellipsoid_15K_t5_wy22_xy0d5_z1_[-110]x[110]_elongSameVol_ELONG_2',
#
#
#
#APL QD capped by 12 nm SRL Sb dependence
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.04',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.06',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.08',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.1',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.12',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.14',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.145',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.15',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.155',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.16',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.18',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.2',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.22',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.24',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_ALLOY_0.26',
#
#
#
#Angular dependence of the QD apex - pyramid QD with const In 1 12nm GaAsSb capping
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-90',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-75',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-60',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-45',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-30',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-15',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_0',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_15',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_30',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_45',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_60',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_75',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_90',
#
#
#
#Angular dependence of the QD apex - pyramid QD 5nm GaAsSb capping QD volume InAs NO ALLOY IN DOT
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-90',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-75',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-60',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-45',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-30',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_-15',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_0',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_15',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_30',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_45',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_60',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_75',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_constIn1_APEXANGLE_90',
#
#
#
#Position along [1-10] dependence of the QD apex - pyramid QD 5nm GaAsSb capping
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ApexposAlong[1-10]_revInProfile_APEXPOS_-0.5',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ApexposAlong[1-10]_revInProfile_APEXPOS_-0.4',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ApexposAlong[1-10]_revInProfile_APEXPOS_-0.3',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ApexposAlong[1-10]_revInProfile_APEXPOS_-0.2',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ApexposAlong[1-10]_revInProfile_APEXPOS_-0.1',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ApexposAlong[1-10]_revInProfile_APEXPOS_0',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ApexposAlong[1-10]_revInProfile_APEXPOS_0.1',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ApexposAlong[1-10]_revInProfile_APEXPOS_0.2',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ApexposAlong[1-10]_revInProfile_APEXPOS_0.3',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ApexposAlong[1-10]_revInProfile_APEXPOS_0.4',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ApexposAlong[1-10]_revInProfile_APEXPOS_0.5',
#
#
#
#Angular dependence of the QD apex - pyramid QD 12nm GaAsSb capping
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-90',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-75',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-60',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-45',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-30',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-15',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_0',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_15',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_30',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_45',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_60',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_75',
#'pyramid_2_15K_rho16_z16_t12_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_90',
#
#
#
#Angular dependence of the QD apex - pyramid QD 5nm GaAsSb capping
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-90',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-75',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-60',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-45',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-30',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_-15',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_0',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_15',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_30',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_45',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_60',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_75',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_angleApexpos_revInProfile_APEXANGLE_90',
#
#
#
#Different QD aspect by enlarging the base, i.e. towards quantum well
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_0.01',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_0.02',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_0.03',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_0.05',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_0.1',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_0.2',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_0.3',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_0.5',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_1',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_2',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_3',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_5',
#'pyramid_2_Sb0d2_15K_QDconstAlloy1_t5_w22_xy(22pt)_z1_QDandSRLz0d5_QDasp_QDbaseLarger_ASPECT_10',
#
#
#
#QD as cone same volume as APL Sb dep
#'cone_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.04',
#'cone_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.06',
#'cone_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.08',
#'cone_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.1',
#'cone_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.12',
#'cone_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.14',
#'cone_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.16',
#'cone_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.18',
#'cone_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.2',
#'cone_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.22',
#
#
#
#QD as semiellipsoid same volume as APL Sb dep
#'semillipsoid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.04',
#'semillipsoid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.06',
#'semillipsoid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.08',
#'semillipsoid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.1',
#'semillipsoid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.12',
#'semillipsoid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.14',
#'semillipsoid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.16',
#'semillipsoid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.18',
#'semillipsoid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.2',
#'semillipsoid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.22',
#
#
#
#QD as cuboid same volume as APL Sb dep
#'cuboid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.04',
#'cuboid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.06',
#'cuboid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.08',
#'cuboid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.1',
#'cuboid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.12',
#'cuboid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.14',
#'cuboid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.16',
#'cuboid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.18',
#'cuboid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.2',
#'cuboid_2_15K_rho16_z16_t5_sameVolAsPyr22x8_xy0d5_z1_ALLOY_0.22',
#
#
#
#pyramid QD different position of the QD apex along 110 with respect to QD base
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_apexpos_APEXPOS_0',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_apexpos_APEXPOS_0.25',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_apexpos_APEXPOS_0.5',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_apexpos_APEXPOS_0.75',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_apexpos_APEXPOS_1.0',
#
#
#
#Semiellipsoid QD and GaAsSb SRL DIFFERENT ELONGATION OF THE QD ALONG [110]
#'pyramid_2_15K_rho16_z16_t5_wy22_xy0d5_z1_semiellipsoid_[-110]x[110]_ELONGtoY_0.2',
#'pyramid_2_15K_rho16_z16_t5_wy22_xy0d5_z1_semiellipsoid_[-110]x[110]_ELONGtoY_0.4',
#'pyramid_2_15K_rho16_z16_t5_wy22_xy0d5_z1_semiellipsoid_[-110]x[110]_ELONGtoY_0.6',
#'pyramid_2_15K_rho16_z16_t5_wy22_xy0d5_z1_semiellipsoid_[-110]x[110]_ELONGtoY_0.8',
#'pyramid_2_15K_rho16_z16_t5_wy22_xy0d5_z1_semiellipsoid_[-110]x[110]_ELONGtoY_1.0',
#'pyramid_2_15K_rho16_z16_t5_wy22_xy0d5_z1_semiellipsoid_[-110]x[110]_ELONGtoY_1.2',
#'pyramid_2_15K_rho16_z16_t5_wy22_xy0d5_z1_semiellipsoid_[-110]x[110]_ELONGtoY_1.4',
#'pyramid_2_15K_rho16_z16_t5_wy22_xy0d5_z1_semiellipsoid_[-110]x[110]_ELONGtoY_1.6',
#'pyramid_2_15K_rho16_z16_t5_wy22_xy0d5_z1_semiellipsoid_[-110]x[110]_ELONGtoY_1.8',
#'pyramid_2_15K_rho16_z16_t5_wy22_xy0d5_z1_semiellipsoid_[-110]x[110]_ELONGtoY_2.0',
#
#
#
#APL QD Sb dependence
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.04',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.06',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.08',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.1',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.12',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.14',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.16',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.165',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.17',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.175',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.18',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.185',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.19',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.195',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.2',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.22',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.24',
#'pyramid_2_15K_rho16_z16_t5_w22_xy0d5_z1_ALLOY_0.26',
#
#
#Dependence on QD aspect ratio
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d5_QDasp_ASPECT_0.05',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d5_QDasp_ASPECT_0.1',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d5_QDasp_ASPECT_0.3',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d5_QDasp_ASPECT_0.5',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d5_QDasp_ASPECT_1.0',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d5_QDasp_ASPECT_1.5',
#
#
#Sb dependence for QD aspect ratio 0.1
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d25_QDasp0d1_ALLOY_0.1',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d25_QDasp0d1_ALLOY_0.12',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d25_QDasp0d1_ALLOY_0.14',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d25_QDasp0d1_ALLOY_0.16',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d25_QDasp0d1_ALLOY_0.18',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d25_QDasp0d1_ALLOY_0.2',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d25_QDasp0d1_ALLOY_0.22',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDandSRLz0d25_QDasp0d1_ALLOY_0.24',
#
#
#SRL thickness 2nm Sb dependence, small step in z in simulation area
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.1',
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.12',
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.14',
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.16',
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.18',
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.2',
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.22',
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.24',
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.26',
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.28',
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.3',
#'pyramid_2_15K_rho16_z16_t2_w22_xy1_z1_QDandSRLz0d25_ALLOY_0.32',
#
#
#QD volume 0.5 APL Sb dependence
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDvol0d5_QDandSRLz0d25_ALLOY_0.1',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDvol0d5_QDandSRLz0d25_ALLOY_0.12',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDvol0d5_QDandSRLz0d25_ALLOY_0.14',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDvol0d5_QDandSRLz0d25_ALLOY_0.16',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDvol0d5_QDandSRLz0d25_ALLOY_0.18',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDvol0d5_QDandSRLz0d25_ALLOY_0.2',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDvol0d5_QDandSRLz0d25_ALLOY_0.22',
#'pyramid_2_15K_rho16_z16_t5_w22_xy1_z1_QDvol0d5_QDandSRLz0d25_ALLOY_0.24',
#
#
#Dependence on QD volume as ratio to APL
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_QDvol_RATIO_0.5',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_QDvol_RATIO_0.75',
##'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_QDvol',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_QDvol_RATIO_1.25',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_QDvol_RATIO_1.5',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_QDvol_RATIO_2.0',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_QDvol_RATIO_3.0',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_QDvol_RATIO_5.0',
#
#
#Dependence on SRL thickness
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_1',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_2',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_3',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_4',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_5',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_6',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_7',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_8',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_9',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_10',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_11',
#'pyramid_2_Sb_02_15K_rho16_z16_t5_w22_xy1_z1_TERTHICK_12',
#
#
#For Quantum gate calculation
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_-140',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_-120',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_-110',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_-100',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_-95',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_-90',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_-80',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_-60',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_-40',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_-20',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_0',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_20',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_40',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_60',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_80',
#'pyramid_2_Sb_005to022_15K_rho16_z16_t14wholeSamp_w22_xy1_z05_10e_10h_E_100'
#
#
#
#'pyramid_2_Sb_0_15K_rho16_z16_t5_w22_xy1_z05',
#'pyramid_2_Sb_010_15K_rho16_z16_t5_w22_xy1_z05',
#'pyramid_2_Sb_014_15K_rho16_z16_t5_w22_xy1_z05',
#'pyramid_2_Sb_015_15K_rho16_z16_t5_w22_xy1_z05',
#'pyramid_2_Sb_016_15K_rho16_z16_t5_w22_xy1_z05',
#'pyramid_2_Sb_017_15K_rho16_z16_t5_w22_xy1_z05',
#'pyramid_2_Sb_018_15K_rho16_z16_t5_w22_xy1_z05',
#'pyramid_2_Sb_019_15K_rho16_z16_t5_w22_xy1_z05',
#'pyramid_2_Sb_020_15K_rho16_z16_t5_w22_xy1_z05',
#'pyramid_2_Sb_021_15K_rho16_z16_t5_w22_xy1_z05',
#'pyramid_2_Sb_022_15K_rho16_z16_t5_w22_xy1_z05'#,
#
#
#
#'pyramid_2_Sb_0_15K_rho16_z16_t5_w22_xy1_z05_GaAswithGaSbElast',
#'pyramid_2_Sb_010_15K_rho16_z16_t5_w22_xy1_z05_GaAswithGaSbElast',
#'pyramid_2_Sb_014_15K_rho16_z16_t5_w22_xy1_z05_GaAswithGaSbElast',
#'pyramid_2_Sb_015_15K_rho16_z16_t5_w22_xy1_z05_GaAswithGaSbElast',
#'pyramid_2_Sb_016_15K_rho16_z16_t5_w22_xy1_z05_GaAswithGaSbElast',
#'pyramid_2_Sb_017_15K_rho16_z16_t5_w22_xy1_z05_GaAswithGaSbElast',
#'pyramid_2_Sb_018_15K_rho16_z16_t5_w22_xy1_z05_GaAswithGaSbElast',
#'pyramid_2_Sb_019_15K_rho16_z16_t5_w22_xy1_z05_GaAswithGaSbElast',
#'pyramid_2_Sb_020_15K_rho16_z16_t5_w22_xy1_z05_GaAswithGaSbElast',
#'pyramid_2_Sb_021_15K_rho16_z16_t5_w22_xy1_z05_GaAswithGaSbElast',
#'pyramid_2_Sb_022_15K_rho16_z16_t5_w22_xy1_z05_GaAswithGaSbElast',
#'pyramid_2_Sb_0_15K_rho16_z16_t5_w22_xy1_z05_GaSbwithGaAsElast',
#'pyramid_2_Sb_010_15K_rho16_z16_t5_w22_xy1_z05_GaSbwithGaAsElast',
#'pyramid_2_Sb_014_15K_rho16_z16_t5_w22_xy1_z05_GaSbwithGaAsElast',
#'pyramid_2_Sb_015_15K_rho16_z16_t5_w22_xy1_z05_GaSbwithGaAsElast',
#'pyramid_2_Sb_016_15K_rho16_z16_t5_w22_xy1_z05_GaSbwithGaAsElast',
#'pyramid_2_Sb_017_15K_rho16_z16_t5_w22_xy1_z05_GaSbwithGaAsElast',
#'pyramid_2_Sb_018_15K_rho16_z16_t5_w22_xy1_z05_GaSbwithGaAsElast',
#'pyramid_2_Sb_019_15K_rho16_z16_t5_w22_xy1_z05_GaSbwithGaAsElast',
#'pyramid_2_Sb_020_15K_rho16_z16_t5_w22_xy1_z05_GaSbwithGaAsElast',
#'pyramid_2_Sb_021_15K_rho16_z16_t5_w22_xy1_z05_GaSbwithGaAsElast',
#'pyramid_2_Sb_022_15K_rho16_z16_t5_w22_xy1_z05_GaSbwithGaAsElast'#,
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_-110',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_-100',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_-90',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_-80',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_-60',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_-50',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_-40',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_-30',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_-20',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_-10',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_0',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_10',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_20',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_40',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_60',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_80',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_100',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_140',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_180',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_220',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_260',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_300',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_350',
#'ellipsoid_300K_Sb_0d05_trump_atQDheight_0d2_attop_RHO_2_E_400'
] 