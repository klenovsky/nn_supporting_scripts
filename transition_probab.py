import sys,os,states2transition
import numpy as na
import scipy as sp

class trans_probab():
  def __init__(self , prefix='' , Ep=21.5 ):
    print 'transition_probab initialized'
    self.prefix=prefix

    #Nacteni Ep bud jako konstanta pro celou strukturu nebo jakozto funkce prostrove souradnice
    #self.Ep=Ep
    self.Ep=self.makeEp()
    
  #Funkce pro nacitani dat z nextnano souboru 'filename', stejne jako v strain_from_nextnano_to_csi.py
  def read_data_from_NN( self , filename ):
    buffer=na.fromfile( filename,  sep='\n' )	
    return buffer

  #Funkce pro nacitani poctu datovych bodu, asi stejne jako v strain_from_nextnano_to_csi.py, nadbytecna funkce
  def readDimensions ( self ):
    self.readSizesFromFld( 1 )
    return self.nx*self.ny*self.nz
    
  #Funkce pro nacteni energie stavu s cislem 'state', stejne jako v strain_from_nextnano_to_csi.py
  def retrieveWFEnergy( self, state ):
    f=open(self.prefix+'wf_spectrum_dot_kp8.dat', 'r')
    lines=f.readlines()
    return float( lines[state].split()[1] )

  #Funkce pro nacteni rozmeru 8kp wf s poradovym cislem 'state', stejne jako v strain_from_nextnano_to_csi.py
  def readSizesFromFld( self, state ):
    #print state
    fldname=self.prefix+'wf_amplitude_real_dot_kp8_1_0000_00%02i.fld'%(state)
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

  #STUB, presently not used
  '''
  def makeEp( self ):
    material = self.prefix+'material.dat'
    buffer=self.read_data_from_NN( material )
    n=self.readDimensions ()

    data=na.array(map( self.mapping, buffer[0:n] ),  na.float32 )
    # LOWER STEP IN z COMPARED TO X, Y - DO NOT FORGET TO MODIFY nz
    #data=na.array(map( self.mapping, buffer[0:n] ),  na.float32 )[:, :, ::2]
    #nz=(nz+1)/2   
    return data 
  '''
  #STUB, presently not used
  def mapping( self,  x ):		
    if x==5.0:
      return 28.8
    elif x==8.0:
      return 21.5
    elif x==34.0:
      return 28.4
    else:
      print 'ERROR: nextnano material %d not known, add to self.mapping, exiting\n' % (x)
      sys.exit(1)

  #STUB, presently not used  
  ''' 
  def mappingAlloy( self,  x ):
    if x<0.3:
      return 0
    else:
      return 1
    #return round(100*x)
  '''
   
  #Funkce generujici Ep jako funkci prostorove souradnice, pouzita je linearni interpolace mezi prislusnymi konstituenty 
  def makeEp( self ):
    #print
    n=self.readDimensions()
    alloyname = self.prefix+'alloy_composition.dat'
    data=self.read_data_from_NN( alloyname )[0:n]
    
    #Inline funkce, ktera provadi cele pretypovani, mezi QD a SRL rozlisuje typickou limitou koncentrace slitiny (<0.35 SRL, >0.35 QD)
    Ep=[(x*27.0+(1.0-x)*28.8) if x>0.35 else (x*21.5+(1.0-x)*28.8) for x in (data)]    
    #InAs Ep=21.5 eV
    #GaAs Ep=28.8 eV
    #GaSb Ep=27.0 eV
    
    #print len(Ep)
    return Ep
  
  #Funkce generujici jmena 8kp wf souboru, stejne jako v strain_from_nextnano_to_csi.py
  def generateWFNames( self , state ):
    #expected project name: wf_amplitude_real_dot_kp8_7_0000_0004.dat
    #real=[ 'wf_amplitude_real_dot_kp8_'+str(i)+'_'+'_'.join(str(state))+'.dat' for i in xrange(1,9)]
    real=[ self.prefix+'wf_amplitude_real_dot_kp8_'+str(i)+'_0000_00%02i.dat'%(state) for i in xrange(1,9)]
    imag=[ self.prefix+'wf_amplitude_imag_dot_kp8_'+str(i)+'_0000_00%02i.dat'%(state) for i in xrange(1,9)]
    #print real
    self.allDatnames=real+imag
    #return allDatnames
    
  #Funkce vytvarejici 8kp wf z nextnana do formatu 8kpTUB, stejne jako v strain_from_nextnano_to_csi.py
  def makeWFkp8state ( self ):
    #print self.allDatnames
    buffers=[ self.read_data_from_NN( self.datname ) for self.datname in self.allDatnames ]
    
    # ordering in this wf: real amplitudes + imag amplitudes + total density; ordering in nn++ wf: s up, s down, x, y, z up, z, y, z down
    data=list([ buffers[0], buffers[2], buffers[3], buffers[4], \
      buffers[1], buffers[5], buffers[6], buffers[7], \
      buffers[8], buffers[10], buffers[11], buffers[12], \
      buffers[9], buffers[13], buffers[14], buffers[15] ])
    dens=list([ data[i]**2+data[i+8]**2 for i in xrange(8) ])
    totaldens=0
    for i in xrange(8):
      totaldens+=dens[i]

    norm=na.sum(totaldens)
    data/=norm**0.5
    totaldens/=norm

    data=list(data)
    data.append(totaldens)
    return data                                 

  #Hlavni funkce pocitajici prechodovy integral, jako vstup ocekava cisla dvou 8kp wf z nn ('st1 , st2') a vektor polarizace ('ex , ey , ez')
  def makeOverlap ( self , st1 , st2 , ex , ey , ez ):
    #Nacteni obou wf:

    #state 1
    self.readSizesFromFld( st1 )
    nx1=self.nx
    ny1=self.ny
    nz1=self.nz
    self.generateWFNames ( st1 )
    kp8_1 = self.makeWFkp8state()
    #print kp8_1

    #state 2
    self.readSizesFromFld( st2 )
    nx2=self.nx
    ny2=self.ny
    nz2=self.nz
    self.generateWFNames ( st2 )
    kp8_2 = self.makeWFkp8state()
    
    #print len(kp8_1[0])
    #print len(kp8_2[1])

    # < psi1 | e.p | psi2 > ; psi = envelope * periodic:
    #Tady se pocita prekryvovy integral, je to hranata zavorka ve Stierove diss str. 53, rov. (4.19)    
    real = float(ex) * ( kp8_1[0]*kp8_2[1] - kp8_1[1]*kp8_2[0] + kp8_1[8]*kp8_2[9] - kp8_1[9]*kp8_2[8] + \
                         kp8_1[4]*kp8_2[5] - kp8_1[5]*kp8_2[4] + kp8_1[12]*kp8_2[13] - kp8_1[13]*kp8_2[12] ) + \
           float(ey) * ( kp8_1[0]*kp8_2[2] - kp8_1[2]*kp8_2[0] + kp8_1[8]*kp8_2[10] - kp8_1[10]*kp8_2[8] + \
                         kp8_1[4]*kp8_2[6] - kp8_1[6]*kp8_2[4] + kp8_1[12]*kp8_2[14] - kp8_1[14]*kp8_2[12] ) + \
           float(ez) * ( kp8_1[0]*kp8_2[3] - kp8_1[3]*kp8_2[0] + kp8_1[8]*kp8_2[11] - kp8_1[11]*kp8_2[8] + \
                         kp8_1[4]*kp8_2[7] - kp8_1[7]*kp8_2[4] + kp8_1[12]*kp8_2[15] - kp8_1[15]*kp8_2[12] )

    imag = float(ex) * ( kp8_1[0]*kp8_2[9] - kp8_1[1]*kp8_2[8] - kp8_1[8]*kp8_2[1] + kp8_1[9]*kp8_2[0] + \
                         kp8_1[4]*kp8_2[13] - kp8_1[5]*kp8_2[12] - kp8_1[12]*kp8_2[5] + kp8_1[13]*kp8_2[4] ) + \
           float(ey) * ( kp8_1[0]*kp8_2[10] - kp8_1[2]*kp8_2[8] - kp8_1[8]*kp8_2[2] + kp8_1[10]*kp8_2[0] + \
                         kp8_1[4]*kp8_2[14] - kp8_1[6]*kp8_2[12] - kp8_1[12]*kp8_2[6] + kp8_1[14]*kp8_2[4] ) + \
           float(ez) * ( kp8_1[0]*kp8_2[11] - kp8_1[3]*kp8_2[8] - kp8_1[8]*kp8_2[3] + kp8_1[11]*kp8_2[0] + \
                         kp8_1[4]*kp8_2[15] - kp8_1[7]*kp8_2[12] - kp8_1[12]*kp8_2[7] + kp8_1[15]*kp8_2[4] )      
                                                             
    #real_s = na.sum(real)
    #imag_s = na.sum(imag)  
    #print len(real)

    #attempt on proper treatment of Ep
    Ep=self.Ep
    #Prepocet Ep na P
    P=sp.sqrt(Ep)
    #print 'LEN EP',len(Ep)

    #CURRENTLY NOT USED: instead vale for InAs is used on the momentum element M (not p) elsewhere matrix expecting the recombination will happen in InAs because of electron wf

    #p dokoncuje ten skalarni soucin ve velke rovnici vyse (tam je jen soucin vektoru) a provadi tedy integral pres simulacni prostor    
    p = list ( [ na.sum(real) , na.sum(imag) ] )

    #predsly krok neni proveden primo ve vyse uvedene velke rovnici, aby se dalo lepe zapocitat Ep (prostorova zavislost) a postup tak zcasti zapocte dusledky Stierovych rovnic (4.20) a (4.21), to stane pri vypoctu f:
    f= list ( [ na.sum(real*P) , na.sum(imag*P) ] )

    #Vypocet rozdilu energii mezi stavy 'st1' a 'st2', dela se to kvuli vypoctu osc. sily
    Eab=abs(self.retrieveWFEnergy( st1 )-self.retrieveWFEnergy( st2 ))
    #print 'Ep/Eab',self.Ep/Eab
    
    #Vypocet maticoveho prvku M=|p|^2
    M=(p[0]**2+p[1]**2)    
    print 'M',M

    #Vypocet osc. sily (normovane) dle diss Stier str. 55, horni odstavec, if je tam jen kvuli tomu, ze jsem si pocital o.s. pro <st1|e.p|st1>, tedy sam na sebe, tak aby se nedelilo 0
    if Eab!=0:
        F=(f[0]**2+f[1]**2)/Eab
    else:
        F=(f[0]**2+f[1]**2)/1e-10
    print 'F',F

    #Vraci vektor, kde prvni element je maticovy prvek M a druhy osc. sila F
    return [M,F]

    #STUB PRESENTLY NOT USED
    '''
    if Eab!=0:
        return [M,self.Ep/Eab]
    else:
        return [M,self.Ep/1e-10]
    '''
    #momentum_el = list ( [ real , imag ] )
    #return momentum_el

  #Vypocet hustoty pravdepodobnosti 8kp wf z nextnana, stare, ted se uz k nicemu nepouziva
  def prob_dens ( self, wf8 ):
    dens=list([ wf8[i]**2+wf8[i+8]**2 for i in xrange(8) ])
    totaldens=na.sum(dens)
    #for i in xrange(8):
    #  totaldens+=dens[i]
    return totaldens

#Stary main, uz se nepouziva
'''
if __name__=='__main__':
  # autodetection of activities
  print sys.argv
  if len(sys.argv) == 4:
     print sys.argv
     f_name = 'trans_dipole_moment_' + sys.argv[1] + '_' + sys.argv[2] + '_' + sys.argv[3] + '.dat'     
     print f_name
     f = open ( f_name , 'w')
     f.write ('polarization direction vector\n')
     f.write ('ex ey ez\n')
     f.write ('%s %s %s\n' %(sys.argv[1], sys.argv[2], sys.argv[3]))     
     f.write ('<st1|st2> | p real | p imag | matrix. el. | osc. strength (*0.5*hbar*m0/e = (2.998*10^{-46}) )\n')
     trans=trans_probab()
     n = trans.readDimensions ()
     #Ep = trans.read_data_from_NN( 'EpMatrix.dat' )[0:n]
     Ep = trans.makeEp()     
     dipole_Ep_sum = []
     print len(Ep)
     for iter in range( 0 , len(states2transition.states) , 2 ):
        st1 = int( states2transition.states[iter] )
        st2 = int( states2transition.states[iter+1] )
        E12 = abs( trans.retrieveWFEnergy( st1 ) - trans.retrieveWFEnergy( st2 ) )
        dipole_el = trans.makeOverlap ( st1 , st2 , sys.argv[1] , sys.argv[2] , sys.argv[3] )        
        dipole_Ep_real = Ep * dipole_el[0]
        dipole_Ep_imag = Ep * dipole_el[1]
        dipole_Ep_real_s = na.sum(dipole_Ep_real)
        dipole_Ep_imag_s = na.sum(dipole_Ep_imag)
        dipole_Ep_sum = dipole_Ep_real_s*dipole_Ep_real_s + dipole_Ep_imag_s*dipole_Ep_imag_s  
        dipole_el_s= list ([ na.sum(dipole_el[0]) , na.sum(dipole_el[1]) ])
        f.write('%02i %02i %f %f %f %f\n' %(st1, st2, dipole_el_s[0], dipole_el_s[1], dipole_el_s[0]*dipole_el_s[0] + dipole_el_s[1]*dipole_el_s[1], dipole_Ep_sum/E12))
        print dipole_el_s
        print dipole_el_s[0]*dipole_el_s[0] + dipole_el_s[1]*dipole_el_s[1]
     
        
     f.write('Oscillator strengths\n')        
     for iter in range( 0 , len(states2transition.states) , 2 ):
        st1 = int( states2transition.states[iter] )
        st2 = int( states2transition.states[iter+1] )
        f.write('%02i %02i %f\n' %(st1, st2, dipole_Ep_sum[iter]))
        print dipole_Ep_sum
     
     
     f.close()
  else:
     print ('This is transition_probab.py, calculates transition between two NN kp8 states listed in states2transition.py\n')
     print ('Usage: transition_probab.py pol_x pol_y pol_z\n')
'''






