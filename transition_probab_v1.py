import sys,os,states2transition as st
import numpy as na
import scipy as sp
import bisect as bi
from intergrid import Intergrid 
from scipy import ndimage
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

hbar=1.054571726 #*10**(-34)
e=1.602176565 #*10**(-19)

print na.__version__

class trans_probab():

  REAL_ROOT = 'wf_amplitude_real_dot_'
  IMAG_ROOT = 'wf_amplitude_imag_dot_'

      
  def __init__(self , prefix='' , Ep=21.5 , kind='kp8' ):
    print 'transition_probab initialized'
    self.prefix=prefix
      
    
  #Funkce pro nacitani dat z nextnano souboru 'filename', stejne jako v strain_from_nextnano_to_csi.py
  def read_data_from_NN( self , filename):
    buffer=na.fromfile( filename,  sep='\n' )
    return buffer

  #Funkce pro nacitani poctu datovych bodu, asi stejne jako v strain_from_nextnano_to_csi.py, nadbytecna funkce
  def readDimensions ( self , fldname ):
    f=open(fldname,'r')
    lines=[ f.readline() for i in xrange(8) ]
    nx=int(lines[3].split()[2])
    ny=int(lines[4].split()[2])
    nz=int(lines[5].split()[2])
    n=nx*ny*nz

    #self.readSizesFromFld( 1 , st.wftype[0] )
    return [ nx , ny , nz , n ]
    
  #Funkce pro nacteni energie stavu s cislem 'state', stejne jako v strain_from_nextnano_to_csi.py
  def retrieveWFEnergy( self, state, wftype='kp8' ):
    f=open(os.path.join(self.prefix, 'wf_spectrum_dot_'+wftype+'.dat'), 'r')
    lines=f.readlines()
    return float( lines[state].split()[1] )

  #Funkce pro nacteni rozmeru 8kp wf s poradovym cislem 'state', stejne jako v strain_from_nextnano_to_csi.py
  def readSizesFromFld( self, state , wftype ):
    #print state
    fldname= os.path.join(self.prefix, 'wf_amplitude_real_dot_'+wftype+'_1_0000_00%02i.fld'%(state))
    #print fldname
    f=open(fldname,'r')
    lines=[ f.readline() for i in xrange(8) ]
    self.nx=int(lines[3].split()[2])
    self.ny=int(lines[4].split()[2])
    self.nz=int(lines[5].split()[2])
    self.n=self.nx*self.ny*self.nz
    #self.d=int(lines[7].split()[2]) # NUMBER OF WINDOWS, NOT GRID_STEP
    #print 'Sizes %d, %d, %d readed from fld file (%d in total)' % \
    #  (self.nx, self.ny, self.nz, self.n)

  #Funkce generujici Ep jako funkci prostorove souradnice, pouzita je linearni interpolace mezi prislusnymi konstituenty
  def makeEp( self , coordNameToFit , state1=8 , state2=9 , wftype1='kp8' , wftype2='kp8' ):
    #print    
    alloyname = os.path.join(self.prefix, 'alloy_composition.dat')
    fldname=os.path.join(self.prefix, 'alloy_composition.fld')
    coordname=os.path.join(self.prefix, 'alloy_composition.coord')
    dim=self.readDimensions( fldname )
    nx=dim[0]
    ny=dim[1]
    nz=dim[2]
    n=dim[3]
    #print nx,ny,nz,nx*ny*nz
    #print self.nx,self.ny,self.nz,self.nx*self.ny*self.nz
    data=self.read_data_from_NN( alloyname )[0:n]
    coord=self.read_data_from_NN( coordname )[0:n]    
    coordFit=self.read_data_from_NN( coordNameToFit )[0:self.n]
    #Inline funkce, ktera provadi cele pretypovani, mezi QD a SRL rozlisuje typickou limitou koncentrace slitiny (<0.35 SRL, >0.35 QD)
    #PREFFERED FOR III-V
    EpTemp=[(x*27.0+(1.0-x)*28.8) if x>0.35 else (x*21.5+(1.0-x)*28.8) for x in (data)]    
    #InAs Ep=21.5 eV
    #GaAs Ep=28.8 eV
    #GaSb Ep=27.0 eV
    #Si_(1-x)Ge_x QD attempt using method by Cardona (Fundamentals of Semiconductors)
    #Eab=abs(self.retrieveWFEnergy( state1 , wftype1 )-self.retrieveWFEnergy( state2 , wftype2 ))
    #print 'Eab ', Eab
    #EphSi=13.9*hbar/e*10**(-3.0) #in eV, source: Ioffe + Cardona
    #EphGe=8.17*hbar/e*10**(-3.0) #in eV, source: Ioffe + Cardona
    #print 'EphSi EphGe ',EphSi, EphGe
    #EgSi=1.12
    #EgGe=1.2 #for X point source: Ioffe
    #so far phonon energy is subtracted, so phonon is considered as emitted, which should be the case for low temperatures
    #EpTemp=[(Eab - (x*EphGe+(1.0-x)*EphSi) - (x*EgGe+(1.0-x)*EgSi) )**2.0*na.pi/8.0 for x in (data)]
    #Si_(1-x)Ge_x QD attempt using data from Richard
    #EpTemp=[(x*12.23+(1.0-x)*14.81) for x in (data)]
    #Si Ep=14.81 eV   E_PX from Richard PHYSICAL REVIEW B 70, 235204 (2004)
    #Ge Ep=12.23 eV   E_PXd from Richard PHYSICAL REVIEW B 70, 235204 (2004)
    #Si_(1-x)Ge_x QD attempt using method from Cardona and data from Richard <del|p|gam>=sqrt( 2*pi/hbar*10^-4*(|<gam_15|p|gam_25'>|^2*|<gam_15|del_1>|^2)/(Egdel-Etrans)^2 )
    #PREFFERED FOR SIGE
    #EpxSi=14.81 #from Richard 30 band k.p
    #EpxGe=12.23 #from Richard 30 band k.p
    #EgSi=1.12
    #EgGe=1.2 #for X point source: Ioffe
    #Eab=abs(self.retrieveWFEnergy( state1 , wftype1 )-self.retrieveWFEnergy( state2 , wftype2 ))
    #print Eab    
    #EpTemp=[ na.sqrt( 2.0*na.pi/hbar*10**(-4.0)*(x*EpxGe+(1.0-x)*EpxSi)**2.0*(x*0.7+(1.0-x)*0.75)**2.0/( abs((x*EgGe+(1.0-x)*EgSi)-Eab) )**2.0 ) for x in (data)]
    #Si Ep=14.81 eV   E_PX from Richard PHYSICAL REVIEW B 70, 235204 (2004)
    #Ge Ep=12.23 eV   E_PXd from Richard PHYSICAL REVIEW B 70, 235204 (2004)
    #Si_(1-x)Ge_x QD attempt using data from Richard <delta_1|p|gamma_25> = <gamma_15|p|gamma_25>*<gamma_15|delta_1>
    #EpxSi=14.81 #E_PX from Richard PHYSICAL REVIEW B 70, 235204 (2004)
    #EpxGe=12.23 #E_PXd from Richard PHYSICAL REVIEW B 70, 235204 (2004)
    #EpTemp=[(x*EpxGe+(1.0-x)*EpxSi)*(x*0.7+(1.0-x)*0.75) for x in (data)]
    #Si Ep=14.81 eV   E_PX from Richard PHYSICAL REVIEW B 70, 235204 (2004)
    #Ge Ep=12.23 eV   E_PXd from Richard PHYSICAL REVIEW B 70, 235204 (2004)
    EpUncut=na.asarray(EpTemp).reshape((nx, ny, nz), order='FORTRAN')
    UncutCoords=na.asarray([ coord[:nx] , coord[nx:nx+ny] , coord[nx+ny:nx+ny+nz] ])
    UncutFitCoords=na.asarray([ coordFit[:self.nx] , coordFit[self.nx:self.nx+self.ny] , coordFit[self.nx+self.ny:self.nx+self.ny+self.nz] ])
    #Function for interpolating Ep to the grid of wavefunctions 
    lo=na.array([ UncutCoords[0][0], UncutCoords[1][0], UncutCoords[2][0] ])
    hi=na.array([ UncutCoords[0][-1], UncutCoords[1][-1], UncutCoords[2][-1] ])
    #uniforming coordinates
    maps=[UncutCoords[0],UncutCoords[1],UncutCoords[2]]
    #calling spline interpolation
    interfunc = Intergrid( EpUncut, lo=lo, hi=hi, order=0 )
    #performing spline interpolation
    query_points=[([x,y,z]) for x in UncutFitCoords[0] for y in UncutFitCoords[1] for z in UncutFitCoords[2] ]
    Ep=interfunc.at( query_points ).reshape(self.nx,self.ny,self.nz)
    print 'INTERFUNC DIM ',Ep.ndim
    print 'Ep GENERATED'
    return Ep

  def get_wf_names(self, state, wftype='kp8'):
        real_suffixes = [self.REAL_ROOT + wftype + '_' + str(i) +
                         '_0000_00%02i.dat'%(state) for i in xrange(1,9)]
        imag_suffixes = [self.IMAG_ROOT + wftype + '_' + str(i) +
                         '_0000_00%02i.dat'%(state) for i in xrange(1,9)]
        real_names = [os.path.join(self.prefix, elem) for elem in real_suffixes] 
        imag_names = [os.path.join(self.prefix, elem) for elem in imag_suffixes] 
        return (real_names, imag_names)

  #Funkce generujici jmena 8kp wf souboru, stejne jako v strain_from_nextnano_to_csi.py
  def generateWFNames( self , state , wftype='kp8' ):
    #expected project name: wf_amplitude_real_dot_kp8_7_0000_0004.dat
    #real=[ 'wf_amplitude_real_dot_'+wftype+'_'+str(i)+'_'+'_'.join(str(state))+'.dat' for i in xrange(1,9)]
    
    if wftype == 'kp8':
         real=[ os.path.join(self.prefix, 'wf_amplitude_real_dot_'+wftype+'_'+str(i)+'_0000_00%02i.dat'%(state)) for i in xrange(1,9)]
         imag=[os.path.join(self.prefix, 'wf_amplitude_imag_dot_'+wftype+'_'+str(i)+'_0000_00%02i.dat'%(state)) for i in xrange(1,9)]

         #real=[ self.path+'wf_amplitude_real_dot_kp8_'+str(i)+'_'+'_'.join(parts[6:])+'.dat' for i in xrange(1,9)]
         #imag=[ self.path+'wf_amplitude_imag_dot_kp8_'+str(i)+'_'+'_'.join(parts[6:])+'.dat' for i in xrange(1,9)]
         self.allDatnames=real+imag
    if wftype == 'kp6':
         real=[ self.prefix+'wf_amplitude_real_dot_'+wftype+'_'+str(i)+'_0000_00%02i.dat'%(state) for i in xrange(1,7)]
         imag=[ self.prefix+'wf_amplitude_imag_dot_'+wftype+'_'+str(i)+'_0000_00%02i.dat'%(state) for i in xrange(1,7)]
         self.allDatnames=real+imag
    if wftype == 'x1':
         real=[ self.prefix+'wf_amplitude_real_dot_'+wftype+'_1_0000_00%02i.dat'%(state) ]         
         #imag=[ self.path+'wf_amplitude_imag_dot_x1_1_'+'_'.join(parts[6:])+'.dat' ]
         self.allDatnames=real
    if wftype == 'x2':
         real=[ self.prefix+'wf_amplitude_real_dot_'+wftype+'_1_0000_00%02i.dat'%(state) ]
         #imag=[ self.path+'wf_amplitude_imag_dot_x2_1_'+'_'.join(parts[6:])+'.dat' ]
         self.allDatnames=real
    if wftype == 'x3':
         real=[ self.prefix+'wf_amplitude_real_dot_'+wftype+'_1_0000_00%02i.dat'%(state) ]
         #imag=[ self.path+'wf_amplitude_imag_dot_x3_1_'+'_'.join(parts[6:])+'.dat' ]
         self.allDatnames=real

  #Funkce vytvarejici 8kp wf z nextnana do formatu 8kpTUB, stejne jako v strain_from_nextnano_to_csi.py
  def makeWFkp8state ( self , wftype='kp8' , sbSpin=0 ): #, wftype='kp8' 
    #print self.allDatnames
    #buffers=[ self.read_data_from_NN( self.datname ) for self.datname in self.allDatnames ]
    nx=self.nx
    ny=self.ny
    nz=self.nz 
    buffers=[ self.read_data_from_NN( self.datname ).reshape((nx, ny, nz), order='FORTRAN') for self.datname in self.allDatnames ]
    #print buffers[0]
    # ordering in this wf: real amplitudes + imag amplitudes + total density; ordering in nn++ wf: s up, s down, x, y, z up, z, y, z down
    # final ordering: s up, x, y, z up, s down, z, y, z down      real first 8, imag second 8 
    if ( wftype=='kp8' ): 
      data=list([ buffers[0], buffers[2], buffers[3], buffers[4], \
         buffers[1], buffers[5], buffers[6], buffers[7], \
         buffers[8], buffers[10], buffers[11], buffers[12], \
         buffers[9], buffers[13], buffers[14], buffers[15] ])
    elif ( wftype=='kp6' ):
      data=list([ 0*buffers[0], buffers[0], buffers[1], buffers[2], \
         0*buffers[0], buffers[3], buffers[4], buffers[5], \
         0*buffers[0], buffers[6], buffers[7], buffers[8], \
         0*buffers[0], buffers[9], buffers[10], buffers[11] ]) # conversion to list necessary, would be treated as ndarray otherwise
    elif ( wftype=='x1' or wftype=='x2' or wftype=='x3' ):
      state=int( self.allDatnames[0].split('.')[0].split('_')[-1] )
      print sbSpin
      if ( sbSpin == 0 ):
           data=list([ buffers[0], 0*buffers[0], 0*buffers[0], 0*buffers[0], \
              0*buffers[0], 0*buffers[0], 0*buffers[0], 0*buffers[0], \
              0*buffers[0], 0*buffers[0], 0*buffers[0], 0*buffers[0], \
              0*buffers[0], 0*buffers[0], 0*buffers[0], 0*buffers[0] ]) # conversion to list necessary, would be treated as ndarray otherwise
      elif ( sbSpin == 1 ):
           data=list([ 0*buffers[0], 0*buffers[0], 0*buffers[0], 0*buffers[0], \
              buffers[0], 0*buffers[0], 0*buffers[0], 0*buffers[0], \
              0*buffers[0], 0*buffers[0], 0*buffers[0], 0*buffers[0], \
              0*buffers[0], 0*buffers[0], 0*buffers[0], 0*buffers[0] ]) # conversion to list necessary, would be treated as ndarray otherwise  
    dens=list([ data[i]**2+data[i+8]**2 for i in xrange(8) ])
    totaldens=0
    for i in xrange(8):
      totaldens+=dens[i]
    norm=na.sum(totaldens)
    data/=norm**0.5
    totaldens/=norm
    data=list(data)
    #data.append(totaldens)
    return data                                 

  def make_complex_buffer(self, name_real, name_imag):
        out = (na.fromfile(name_real,  sep='\n')
              + na.fromfile(name_imag,  sep='\n') * 1j)
        return out, na.sum(na.absolute(out)**2)

  def get_state_vectors(self, buffer_names):
    norm_squared = 0.0
    sup_values, modulus = self.make_complex_buffer(buffer_names[0], buffer_names[8])
    norm_squared += modulus
    sdown_values, modulus = self.make_complex_buffer(buffer_names[1], buffer_names[9])
    norm_squared += modulus    
    all_x_up, modulus = self.make_complex_buffer(buffer_names[2], buffer_names[10])
    norm_squared += modulus
    all_y_up, modulus = self.make_complex_buffer(buffer_names[3], buffer_names[11])
    norm_squared += modulus    
    all_z_up, modulus = self.make_complex_buffer(buffer_names[4], buffer_names[12])
    norm_squared += modulus
    all_x_down, modulus = self.make_complex_buffer(buffer_names[5], buffer_names[13])
    norm_squared += modulus    
    all_y_down, modulus = self.make_complex_buffer(buffer_names[6], buffer_names[14])
    norm_squared += modulus    
    all_z_down, modulus = self.make_complex_buffer(buffer_names[7], buffer_names[15])
    norm_squared += modulus    
    norm = na.sqrt(norm_squared)
    return (sup_values / norm,
            sdown_values / norm,
            all_x_up / norm,
            all_y_up / norm,
            all_z_up / norm,
            all_x_down / norm,
            all_y_down / norm,
            all_z_down / norm)

    
  def make_intermediate_vector(self, buffer_names):
    # ordering in this wf: real amplitudes + imag amplitudes + total density; ordering in nn++ wf: s up, s down, x, y, z up, z, y, z down
    # final ordering: s up, x, y, z up, s down, z, y, z down      real first 8 
    real_names_1 = buffer_names[0]
    imag_names_1 = buffer_names[1]
    real_names_2 = buffer_names[2]
    imag_names_2 = buffer_names[3]
    # Build the vectors from buffers, coordinate per coordinate.
    sup_values_1, sdown_values_1, all_x_up_1, all_y_up_1, all_z_up_1,\
      all_x_down_1, all_y_down_1, all_z_down_1 = self.get_state_vectors(real_names_1 + imag_names_1)
    sup_values_2, sdown_values_2, all_x_up_2, all_y_up_2, all_z_up_2,\
      all_x_down_2, all_y_down_2, all_z_down_2 = self.get_state_vectors(real_names_2 + imag_names_2)
    # Execute the vector operations leading to the intermediate vector,
    # Row by row, mixing spin and space variables,
    # and initial as final states following Eq. 1.26 from Klenovsky's PhD thesis.
    all_x_up_2 *= sup_values_1
    all_y_up_2 *= sup_values_1
    all_z_up_2 *= sup_values_1
    all_x_down_2 *= sdown_values_1
    all_y_down_2 *= sdown_values_1
    all_z_down_2 *= sdown_values_1
    all_x_up_1 = (sup_values_2 * all_x_up_1).conjugate()
    all_y_up_1 = (sup_values_2 * all_y_up_1).conjugate()    
    all_z_up_1 = (sup_values_2 * all_z_up_1).conjugate()
    all_x_down_1 = (sdown_values_2 * all_x_down_1).conjugate()
    all_y_down_1 = (sdown_values_2 * all_y_down_1).conjugate()    
    all_z_down_1 = (sdown_values_2 * all_z_down_1).conjugate()
    intermediate_vector = na.column_stack((all_x_up_2  + all_x_down_2 - all_x_up_1 - all_x_down_1,
                                           all_y_up_2  + all_y_down_2 - all_y_up_1 - all_y_down_1,
                                           all_z_up_2  + all_z_down_2 - all_z_up_1 - all_z_down_1))
    return intermediate_vector

  def cache_quantities(self):
    pass

  def makeTME (self, kp8_1, kp8_2, pol):
    # print 'makeTME STARTED'
    # < psi1 | p | psi2 > ; psi = envelope * periodic:
    # Tady se pocita prekryvovy integral, je to hranata zavorka
    # ve Stierove diss str. 53, rov. (4.19)
    # ordering: s up, x, y, z up
    # s down, z, y, z down
    # real first 8, imag second 8

    real = list([pol[0] * (kp8_1[0] * kp8_2[1]
                               - kp8_1[1] * kp8_2[0]
                               - kp8_1[8] * kp8_2[9]
                               + kp8_1[9] * kp8_2[8]
                               + kp8_1[4] * kp8_2[5]
                               - kp8_1[5] * kp8_2[4]
                               - kp8_1[12] * kp8_2[13]
                               + kp8_1[13] * kp8_2[12]),
                    pol[1] * (kp8_1[0] * kp8_2[2]
                              - kp8_1[2] * kp8_2[0]
                              - kp8_1[8] * kp8_2[10]
                              + kp8_1[10] * kp8_2[8]
                              + kp8_1[4] * kp8_2[6]
                              - kp8_1[6] * kp8_2[4]
                              - kp8_1[12] * kp8_2[14]
                              + kp8_1[14] * kp8_2[12]),
                    pol[2] * (kp8_1[0] * kp8_2[3]
                              - kp8_1[3] * kp8_2[0]
                              - kp8_1[8] * kp8_2[11]
                              + kp8_1[11] * kp8_2[8]
                              + kp8_1[4] * kp8_2[7]
                              - kp8_1[7] * kp8_2[4]
                              - kp8_1[12] * kp8_2[15]
                              + kp8_1[15] * kp8_2[12])])

    imag = list([pol[0] * (kp8_1[0] * kp8_2[9]
                               - kp8_1[1] * kp8_2[8]
                               + kp8_1[8] * kp8_2[1]
                               - kp8_1[9] * kp8_2[0]
                               + kp8_1[4] * kp8_2[13]
                               - kp8_1[5] * kp8_2[12]
                               + kp8_1[12] * kp8_2[5]
                               - kp8_1[13] * kp8_2[4]),
                    pol[1] * (kp8_1[0] * kp8_2[10]
                              - kp8_1[2] * kp8_2[8]
                              + kp8_1[8] * kp8_2[2]
                              - kp8_1[10] * kp8_2[0]
                              + kp8_1[4] * kp8_2[14]
                              - kp8_1[6] * kp8_2[12] +
                              kp8_1[12] * kp8_2[6] -
                              kp8_1[14] * kp8_2[4]),
                    pol[2] * (kp8_1[0] * kp8_2[11]
                              - kp8_1[3] * kp8_2[8]
                              + kp8_1[8] * kp8_2[3]
                              - kp8_1[11] * kp8_2[0] +
                              kp8_1[4] * kp8_2[15]
                              - kp8_1[7] * kp8_2[12]
                              + kp8_1[12] * kp8_2[7]
                              - kp8_1[15] * kp8_2[4])])
    # return [ sp.multiply(P,real), sp.multiply(P,imag) ]
    return [real, imag]
    
  # pocita transition matrix element (TME)
  def make_alternate_TME (self, pol, intermediate_vector):
    # print 'makeTME STARTED'
    # < psi1 | p | psi2 > ; psi = envelope * periodic:
    # Tady se pocita prekryvovy integral, je to hranata zavorka
    # ve Stierove diss str. 53, rov. (4.19)
    # ordering: s up, x, y, z up
    # s down, z, y, z down
    # real first 8, imag second 8
    out = pol * intermediate_vector
    return [out.real, out.imag]
  
  #Transition matrix element in basis of s,hh,lh,so
  def makeTMEhls (self, kp8_1, kp8_2, pol):
    #print 'makeTME STARTED'
    # < psi1 | p | psi2 > ; psi = envelope * periodic:
    # Tady se pocita prekryvovy integral, v bazi <s,hh>,<s,lh>,<s,so>
    # spin up: 0-3 (real) a 8-11 (imag)   horni radek
    # spin down: 4-7 (real) a 12-15 (imag)    dolni radek
    real = list([ pol[0]*1.0/na.sqrt(2.0)*(kp8_1[0]*kp8_2[1] - kp8_1[1]*kp8_2[0] + kp8_1[8]*kp8_2[9] - kp8_1[9]*kp8_2[8] + \
                    kp8_1[4]*kp8_2[5] - kp8_1[5]*kp8_2[4] + kp8_1[12]*kp8_2[13] - kp8_1[13]*kp8_2[12]) + \
                   pol[1]*1.0/na.sqrt(2.0)*(kp8_1[0]*kp8_2[10] - kp8_1[2]*kp8_2[8] - kp8_1[8]*kp8_2[2] + kp8_1[10]*kp8_2[0] - \
                    kp8_1[4]*kp8_2[14] + kp8_1[6]*kp8_2[12] + kp8_1[12]*kp8_2[6] - kp8_1[14]*kp8_2[4]) ,
                  pol[0]*1.0/na.sqrt(6.0)*(- kp8_1[0]*kp8_2[1] + kp8_1[1]*kp8_2[0] - kp8_1[8]*kp8_2[9] + kp8_1[9]*kp8_2[8] + \
                    kp8_1[4]*kp8_2[5] - kp8_1[5]*kp8_2[4] + kp8_1[12]*kp8_2[13] - kp8_1[13]*kp8_2[12] ) + \
                   pol[1]*1.0/na.sqrt(6.0)*(kp8_1[0]*kp8_2[10] - kp8_1[2]*kp8_2[8] - kp8_1[8]*kp8_2[2] + kp8_1[10]*kp8_2[0] + \
                    kp8_1[4]*kp8_2[14] - kp8_1[6]*kp8_2[12] - kp8_1[12]*kp8_2[6] + kp8_1[14]*kp8_2[4] ) - \
                   0.0*pol[2]*na.sqrt(2.0/3.0)*( kp8_1[0]*kp8_2[3] - kp8_1[3]*kp8_2[0] + kp8_1[8]*kp8_2[11] - kp8_1[11]*kp8_2[8] + \
                    kp8_1[4]*kp8_2[7] - kp8_1[7]*kp8_2[4] + kp8_1[12]*kp8_2[15] - kp8_1[15]*kp8_2[12] ),
                  pol[0]*1.0/na.sqrt(3.0)*(- kp8_1[0]*kp8_2[1] + kp8_1[1]*kp8_2[0] - kp8_1[8]*kp8_2[9] + kp8_1[9]*kp8_2[8] + \
                    kp8_1[4]*kp8_2[5] - kp8_1[5]*kp8_2[4] + kp8_1[12]*kp8_2[13] - kp8_1[13]*kp8_2[12] ) + \
                   pol[1]*1.0/na.sqrt(3.0)*(kp8_1[0]*kp8_2[10] - kp8_1[2]*kp8_2[8] - kp8_1[8]*kp8_2[2] + kp8_1[10]*kp8_2[0] + \
                    kp8_1[4]*kp8_2[14] - kp8_1[6]*kp8_2[12] - kp8_1[12]*kp8_2[6] + kp8_1[14]*kp8_2[4] ) + \
                   0.0*pol[2]*1.0/na.sqrt(3.0)*( kp8_1[0]*kp8_2[3] - kp8_1[3]*kp8_2[0] + kp8_1[8]*kp8_2[11] - kp8_1[11]*kp8_2[8] + \
                    kp8_1[4]*kp8_2[7] - kp8_1[7]*kp8_2[4] + kp8_1[12]*kp8_2[15] - kp8_1[15]*kp8_2[12] ) ])

    imag = list([ pol[0]*1.0/na.sqrt(2.0)*(kp8_1[0]*kp8_2[9] - kp8_1[1]*kp8_2[8] - kp8_1[8]*kp8_2[1] + kp8_1[9]*kp8_2[0] + \
                    kp8_1[4]*kp8_2[13] - kp8_1[5]*kp8_2[12] - kp8_1[12]*kp8_2[5] + kp8_1[13]*kp8_2[4]) + \
                   pol[1]*1.0/na.sqrt(2.0)*(kp8_1[0]*kp8_2[2] - kp8_1[2]*kp8_2[0] + kp8_1[8]*kp8_2[10] - kp8_1[10]*kp8_2[8] - \
                    kp8_1[4]*kp8_2[6] + kp8_1[6]*kp8_2[4] - kp8_1[12]*kp8_2[14] + kp8_1[14]*kp8_2[12]) ,
                  pol[0]*1.0/na.sqrt(6.0)*( - kp8_1[0]*kp8_2[9] + kp8_1[1]*kp8_2[8] + kp8_1[8]*kp8_2[1] - kp8_1[9]*kp8_2[0] + \
                    kp8_1[4]*kp8_2[13] - kp8_1[5]*kp8_2[12] - kp8_1[12]*kp8_2[5] + kp8_1[13]*kp8_2[4] ) + \
                   pol[1]*1.0/na.sqrt(6.0)*( kp8_1[0]*kp8_2[2] - kp8_1[2]*kp8_2[0] + kp8_1[8]*kp8_2[10] - kp8_1[10]*kp8_2[8] + \
                    kp8_1[4]*kp8_2[6] - kp8_1[6]*kp8_2[4] + kp8_1[12]*kp8_2[14] - kp8_1[14]*kp8_2[12] ) - \
                   0.0*pol[2]*na.sqrt(2.0/3.0)*( kp8_1[0]*kp8_2[11] - kp8_1[3]*kp8_2[8] - kp8_1[8]*kp8_2[3] + kp8_1[11]*kp8_2[0] + \
                    kp8_1[4]*kp8_2[15] - kp8_1[7]*kp8_2[12] - kp8_1[12]*kp8_2[7] + kp8_1[15]*kp8_2[4] ) ,
                  pol[0]*1.0/na.sqrt(3.0)*( - kp8_1[0]*kp8_2[9] + kp8_1[1]*kp8_2[8] + kp8_1[8]*kp8_2[1] - kp8_1[9]*kp8_2[0] + \
                    kp8_1[4]*kp8_2[13] - kp8_1[5]*kp8_2[12] - kp8_1[12]*kp8_2[5] + kp8_1[13]*kp8_2[4] ) + \
                   pol[1]*1.0/na.sqrt(3.0)*( kp8_1[0]*kp8_2[2] - kp8_1[2]*kp8_2[0] + kp8_1[8]*kp8_2[10] - kp8_1[10]*kp8_2[8] + \
                    kp8_1[4]*kp8_2[6] - kp8_1[6]*kp8_2[4] + kp8_1[12]*kp8_2[14] - kp8_1[14]*kp8_2[12] ) + \
                   0.0*pol[2]*1.0/na.sqrt(3.0)*( kp8_1[0]*kp8_2[11] - kp8_1[3]*kp8_2[8] - kp8_1[8]*kp8_2[3] + kp8_1[11]*kp8_2[0] + \
                    kp8_1[4]*kp8_2[15] - kp8_1[7]*kp8_2[12] - kp8_1[12]*kp8_2[7] + kp8_1[15]*kp8_2[4] ) ])
    #return [ sp.multiply(P,real), sp.multiply(P,imag) ]
    return [ real , imag ]

  #Transform TME from {s,p_x,p_y,p_z} basis to {s,hh,lh,so} basis     UNFINISHED   !!!!!!!!!!!!!!!!!!!!!!!!! 
  def basisTrans ( real , imag ):
    hh_re=1/na.sqrt(2.0)*real[1]
    hh_im=1/na.sqrt(2.0)*imag[2] 

  def get_transition_weights(self):
        out = na.array([])
        for transition in st.states:
            na.append(out, float(transition[2]))
        return out

  def load_alternate_WFs(self , wft1 , wft2, transition):
        state_1 = transition[0]
        state_2 = transition[1]
        print 'Handling transition', state_1, state_2
        if len(state_1.split('_')) == 1:
              st1 = int(state_1)
        elif len(state_1.split('_')) == 2:
              st1 = int(state_1.split('_')[0])
        st2 = int(state_2)
        # Nacteni obou wf:
        # state 1
        # st1 and st2 have be same sizes, otherwise we will get into trouble later,
        # so only need to read sizes once.
        self.readSizesFromFld(st1 , wft1)
        real_names_1, imag_names_1 = self.get_wf_names(st1, wft1)
        real_names_2, imag_names_2 = self.get_wf_names(st2, wft2)
        transition_names = (real_names_1, imag_names_1,
                            real_names_2, imag_names_2)
        intermediate_vector = self.make_intermediate_vector(transition_names)
        return intermediate_vector
  
  def loadWFs( self , wft1 , wft2):
    wfStates = []
    stWeight = []
    for s in range(len(st.states)):
         print 'STATES', st.states[s][0], st.states[s][1]
         stWeight.append(float(st.states[s][2]))
         if len(st.states[s][0].split('_')) == 1:
            st1=int(st.states[s][0])
            st2=int(st.states[s][1])
            spin=0          
            #TME.append(self.makeTME ( st1 , st2 , wft1 , wft2 ))
         elif len(st.states[s][0].split('_')) == 2:
            st1=int(st.states[s][0].split('_')[0])
            spin=int(st.states[s][0].split('_')[1])
            st2=int(st.states[s][1])
            #TME.append(self.makeTME ( st1 , st2 , wft1 , wft2 , spin=Spin1 ))
         #Nacteni obou wf:
         #state 1
         self.readSizesFromFld( st1 , wft1 )
         self.generateWFNames ( st1 , wft1 )
         kp8_1 = self.makeWFkp8state( wft1 , sbSpin=spin )
         #state 2
         self.readSizesFromFld( st2 , wft2 )
         self.generateWFNames ( st2 , wft2 )
         kp8_2 = self.makeWFkp8state( wft2 )
         wfStates.append([kp8_1, kp8_2])
    return (wfStates, stWeight)

  # material type: matType='IIIdivV' or matType='SiGe'
  #  PRESENTLY DUE TO COMPUTATIONAL TIME DEMAND EXPECTS
  # THE SAME TRANSITION ENERGY BETWEEN STATES FOR CALCULATION OF EP
  # different types of basis: basisType='sppp' or basisType='shls'
  def makePolDep(self, pol=[[1, 1, 0]], basisType='sppp'):
    local_mode = 'alternate'
    print '\nMaking transition matrix elements\n'
    wft1 = st.wftype[0]
    wft2 = st.wftype[1]
    stWeights = self.get_transition_weights()
    WeightNorm = na.sum(stWeights)    
    kp8wf = None
    if local_mode == 'alternate':
      pass
    else:
      kp8wf, stWeight = self.loadWFs(wft1, wft2)
      WeightNorm = na.sum(stWeight)

    # Eab=abs(self.retrieveWFEnergy( st1 , wft1 )
    # -self.retrieveWFEnergy(st2, wft2))
    # attempt on proper treatment of Ep
    # Nacteni Ep jakozto funkce prostrove souradnice
    if len(st.states[0][0].split('_')) == 1:
            st1 = int(st.states[0][0])
    elif len(st.states[0][0].split('_')) == 2:
            st1 = int(st.states[0][0].split('_')[0])
    if len(st.states[0][1].split('_')) == 1:
            st2 = int(st.states[0][1])
    elif len(st.states[0][1].split('_')) == 2:
            st1 = int(st.states[0][1].split('_')[0])
    coordForEp = self.allDatnames[0][:-4] + '.coord'
    print "coordForEp", coordForEp
    Ep = self.makeEp(coordForEp, st1, st2, wft1, wft2)
    # Prepocet Ep na P
    P = sp.sqrt(Ep)
    pol = na.array(pol)
    polNorm = [elem / na.sqrt(na.sum(elem ** 2)) for elem in pol]
    matrixEl = []
    matrixEl1 = []
    matrixEl2 = []
    matrixEl3 = []
    oscSt = []
    oscSt1 = []
    oscSt2 = []
    oscSt3 = []
    print "Polnorm", len(polNorm)
    for iter in polNorm:
        TME = []
        M = []
        M1 = []
        M2 = []
        M3 = []
        F = []
        F1 = []
        F2 = []
        F3 = []
        Mel = []
        Mel1 = []
        Mel2 = []
        Mel3 = []
        Fel = []
        Fel1 = []
        Fel2 = []
        Fel3 = []
        for i in range(len(st.states)):
        #for i in range(len(kp8wf)):
            if basisType == 'sppp':
                if local_mode == 'alternate':
                    intermediate_vector =\
                      self.load_alternate_WFs(st.states[i], wft1, wft2)
                    # TODO: check correct account of direction of scalar product
                    # with conjugation, compared to sign of imaginary part in
                    # classical implementation.
                    TME.append(self.make_alternate_TME(iter, intermediate_vector))
                else:
                    TME.append(self.makeTME(kp8wf[i][0], kp8wf[i][1], iter))
            elif basisType == 'shls':
                    TME.append(self.makeTMEhls(kp8wf[i][0], kp8wf[i][1], iter))
            MEreal = TME[i][0][0] + TME[i][0][1] + TME[i][0][2]
            MEimag = TME[i][1][0] + TME[i][1][1] + TME[i][1][2]
            sumOfME = (na.sum(P*MEreal))**2+(na.sum(P*MEimag))**2
            sumOfME_1 = (na.sum(P*TME[i][0][0]))**2+(na.sum(P*TME[i][1][0]))**2
            sumOfME_2 = (na.sum(P*TME[i][0][1]))**2+(na.sum(P*TME[i][1][1]))**2
            sumOfME_3 = (na.sum(P*TME[i][0][2]))**2+(na.sum(P*TME[i][1][2]))**2
            M.append(sumOfME)
            M1.append(sumOfME_1)
            M2.append(sumOfME_2)
            M3.append(sumOfME_3)
            if len(st.states[i][0].split('_')) == 1:
                st1 = int(st.states[i][0])
            elif len(st.states[i][0].split('_')) == 2:
                st1 = int(st.states[i][0].split('_')[0])
            if len(st.states[i][1].split('_')) == 1:
                st2 = int(st.states[i][1])
            elif len(st.states[i][1].split('_')) == 2:
                st1 = int(st.states[i][1].split('_')[0])
            Eab = abs(self.retrieveWFEnergy(st1, wft1)
                      - self.retrieveWFEnergy(st2, wft2))
            F.append(sp.true_divide(sumOfME, Eab))
            F1.append(sp.true_divide(sumOfME_1, Eab))
            F2.append(sp.true_divide(sumOfME_2, Eab))
            F3.append(sp.true_divide(sumOfME_3, Eab))
            Mel.append([M[i]*stWeight[i] / WeightNorm])
            Mel1.append([M1[i]*stWeight[i]/WeightNorm])
            Mel2.append([M2[i]*stWeight[i]/WeightNorm])
            Mel3.append([M3[i]*stWeight[i]/WeightNorm])
            Fel.append([F[i]*stWeight[i]/WeightNorm])
            Fel1.append([F1[i]*stWeight[i]/WeightNorm])
            Fel2.append([F2[i]*stWeight[i]/WeightNorm])
            Fel3.append([F3[i]*stWeight[i]/WeightNorm])
        matrixEl.append(na.sum(Mel))
        matrixEl1.append(na.sum(Mel1))
        matrixEl2.append(na.sum(Mel2))
        matrixEl3.append(na.sum(Mel3))
        oscSt.append(na.sum(Fel))
        oscSt1.append(na.sum(Fel1))
        oscSt2.append(na.sum(Fel2))
        oscSt3.append(na.sum(Fel3))
    polDep = [matrixEl, oscSt, matrixEl1, oscSt1,
              matrixEl2, oscSt2, matrixEl3, oscSt3]
    print '\nPolarization calculations finished\n'
    return polDep

