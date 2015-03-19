import os
import getpass

tag_name = 'polPap_eli_In0.6_Sb0.24_highDoping_OIqns0_SRLTdep'
if getpass.getuser() == 'dominique':
    prefix = os.path.join(os.path.abspath('../data/.'),
                          tag_name)
else:
    prefix = ('e:\\Simulace\\QD\\ellipsoid_QD_3D_GaAsSb_SRL'
              + '\\GaAsSbNew120622\\polPap_eli_In0.6_Sb0.24_'
              + 'highDoping_OIqns0_SRLTdep\\')

directory_pref = ('141012_semiellipsoid_asPyr_Sb0.24_80K_'
                  + 'dotIn0.6_2x2st_OI_noSC_d10e19_qns0_perXYZ_TERTHICK_')


sliceName = 'wf_probability_dot_kp8_0000_0002'  # .dat data
matName = 'material'  # .dat data

diryz = [[0, 1, 0], [0, 0, 1]]
dirxz = [[1, 0, 0], [0, 0, 1]]
directions = [diryz, dirxz]
slicePoints = [0, 0, 0]
dir_n = [directory_pref + '1']
