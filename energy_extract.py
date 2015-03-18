import numpy as na
import scipy as sp
import sys, os
import directory_names as dn
from sets import Set
from operator import itemgetter, attrgetter
#import matplotlib.pyplot as plt

class energy ():
   def __init__( self , prefix=''):  
       print 'extract_energy initialized'
       self.prefix=prefix 

   def calc_E( self ):
       filename = self.prefix+'wf_spectrum_dot_kp8.dat'
       if not os.path.isfile(filename):
          print 'ERROR: file %s not found\n' % (filename)
          sys.exit(1)        
    
       #E=na.genfromtxt(filename,unpack=True)[1][1:]
       E=na.loadtxt(filename,skiprows=1,unpack=True)[1]
       #state=na.genfromtxt(filename,unpack=True)[0][1:]
       state=na.loadtxt(filename,skiprows=1,unpack=True)[0]
       diff_E = []   
       diff_st = []
       for i1 in range(len(E)):
            for i2 in range(len(E)):
                 #diff=item2-item1
                 diff=abs( E[i2]-E[i1] )
                 #if diff > 0 and diff > abs(E[i1]) and diff > abs(E[i2]):
                 a=Set([diff])
                 b=Set(diff_E)
                 if not a.intersection(b):
                    diff_E.append(diff)
                    diff_st.append([state[i1],state[i2]])
       diff_E=sp.multiply(diff_E,1000.0*na.ones(len(diff_E)))
       #print len(diff_E),len(diff_st)
       #print diff_E,diff_st
       #diff_E[0]=sp.true_divide(1240.0*na.ones(len(diff_E[0])),diff_E)
       out_E=list([diff_E,diff_st])
       out_E_T=zip(*out_E)
       out_E_sort=sorted(out_E_T, key=itemgetter(0))
       #out_E.sort()
       #print out_E_sort#, diff_st[0]
       #print diff_E
       return out_E_sort 
    