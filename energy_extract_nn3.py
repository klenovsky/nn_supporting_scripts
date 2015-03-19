import numpy as na
import scipy as sp
import sys, os
import directory_names as dn
from sets import Set
from operator import itemgetter, attrgetter
#import matplotlib.pyplot as plt

class energy ():
   def __init__( self , prefix='', NNmode='8x8'):
       #NNmode: 1x1, 1x6, 8x8     only 1x6 currently working  
       print 'extract_energy for nn3 initialized'
       self.prefix=prefix 
       self.mode=NNmode

   def loadDat( self ):
       if self.mode=='1x6':
          filename_e = self.prefix+'\\Schroedinger_1band\\ev3D_cb001_qc001_sg001_deg001_dir.dat'
          if not os.path.isfile(filename_e):
            print 'ERROR: file %s not found\n' % (filename_e)
            sys.exit(1)        
          filename_h = self.prefix+'\\Schroedinger_kpband\\kp_6x6eigenvalues_qc001_hl_3D_dir.dat'
          if not os.path.isfile(filename_h):
            print 'ERROR: file %s not found\n' % (filename_h)
            sys.exit(1)
          e_enSt=na.loadtxt(filename_e,skiprows=1,unpack=True)
          h_enSt=na.loadtxt(filename_h,skiprows=1,unpack=True)
          state_e=e_enSt[0]     
          state_h=h_enSt[0]
          E_e=e_enSt[1]
          E_h=h_enSt[1]
          #print state_e, state_h, E_e , E_h
       elif self.mode=='8x8': 
          filename_e = self.prefix+'\\Schroedinger_kpband\\kp_8x8eigenvalues_qc001_el_3D_dir.dat'
          if not os.path.isfile(filename_e):
            print 'ERROR: file %s not found\n' % (filename_e)
            sys.exit(1)        
          filename_h = self.prefix+'\\Schroedinger_kpband\\kp_8x8eigenvalues_qc001_hl_3D_dir.dat'
          if not os.path.isfile(filename_h):
            print 'ERROR: file %s not found\n' % (filename_h)
            sys.exit(1)
          e_enSt=na.loadtxt(filename_e,skiprows=1,unpack=True)
          h_enSt=na.loadtxt(filename_h,skiprows=1,unpack=True)
          state_e=e_enSt[0]     
          state_h=h_enSt[0]
          E_e=e_enSt[1]
          E_h=h_enSt[1]
          #print state_e, state_h, E_e , E_h
       return [ state_e, state_h, E_e , E_h ] 

   def calc_E( self ):
       load=self.loadDat()
       state_e=load[0]
       state_h=load[1]
       E_e=load[2]
       E_h=load[3]
       diff_E = []   
       diff_st = []
       #we are considering e-h transitions only
       for i1 in range(len(E_e)):
            for i2 in range(len(E_h)):
                 #diff=item2-item1
                 diff=abs( E_h[i2]-E_e[i1] )
                 #if diff > 0 and diff > abs(E[i1]) and diff > abs(E[i2]):
                 a=Set([diff])
                 b=Set(diff_E)
                 if not a.intersection(b):
                    diff_E.append(diff)
                    diff_st.append([state_e[i1],state_h[i2]])
       diff_E=sp.multiply(diff_E,1000.0*na.ones(len(diff_E)))
       #print len(diff_E),len(diff_st)
       #print diff_E,diff_st
       #diff_E[0]=sp.true_divide(1240.0*na.ones(len(diff_E[0])),diff_E)
       out_E=list([diff_E,diff_st])
       out_E_T=zip(*out_E)
       out_E_sort=sorted(out_E_T, key=itemgetter(0))
       #out_E.sort()
       #print out_E_sort#, diff_st[0]
       #print '\n\n\n'
       print out_E_sort[0][0]
       #print '\n\n\n'
       return out_E_sort 
    