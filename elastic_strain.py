import sys,os#,states2transition as st
import numpy as na
import scipy as sp

class elast_strain():
  def __init__(self , prefix='' ):
    print 'strain calculation initialized'
    self.prefix=prefix
    self.readSizesFromFld()
    
  #Funkce pro nacitani dat z nextnano souboru 'filename', stejne jako v strain_from_nextnano_to_csi.py
  def read_data_from_NN( self , filename ):
    buffer=na.fromfile( filename,  sep='\n' )	
    return buffer
    
  #Funkce pro nacteni rozmeru 8kp wf s poradovym cislem 'state', stejne jako v strain_from_nextnano_to_csi.py
  def readSizesFromFld( self ):
    #print state
    fldname=self.prefix+'strain_crystal.fld'
    print fldname
    f=open(fldname,'r')
    lines=[ f.readline() for i in xrange(8) ]
    self.nx=int(lines[3].split()[2])
    self.ny=int(lines[4].split()[2])
    self.nz=int(lines[5].split()[2])
    self.n=self.nx*self.ny*self.nz
    #self.d=int(lines[7].split()[2]) # NUMBER OF WINDOWS, NOT GRID_STEP
    #print 'Sizes %d, %d, %d readed from fld file (%d in total)' % \
    #  (self.nx, self.ny, self.nz, self.n)

  def readCoord( self ):
    1
    self.coordname=self.prefix+'strain_crystal.coord'
    #print self.coordname
    buffer=self.read_data_from_NN( self.coordname )
            
    nx=self.nx
    ny=self.ny
    nz=self.nz
    
    self.coordx=buffer[0:nx]
    self.coordy=buffer[nx:nx+ny]
    self.coordz=buffer[nx+ny:nx+ny+nz]

    #print nx,ny,nz,len(self.coordx),len(self.coordy),len(self.coordz),len(buffer)
    #print self.coordx,self.coordy,self.coordz



  def discriminateSRL( self ):
    #print
    #n=self.readDimensions()
    
    alloyname = self.prefix+'alloy_composition.dat'
    data=self.read_data_from_NN( alloyname )[:self.n]
    
    
    #Inline funkce, ktera provadi cele pretypovani, mezi QD a SRL rozlisuje typickou limitou koncentrace slitiny (<0.35 SRL, >0.35 QD)
    #Ep=[(x*27.0+(1.0-x)*28.8) if x>0.35 else (x*21.5+(1.0-x)*28.8) for x in (data)]    
    temp=na.array([(x*1.0) if (x<0.35 and x>0.001) else (x*0.0) for x in (data)])
    #temp=na.array([(x*1.0) if (x>0.001) else (x*0.0) for x in (data)])
    #print type(data), type(temp)
    #print self.nx, self.ny, self.nz, self.nx*self.ny*self.nz, len(temp) 
    self.SRL=temp.reshape((self.nx, self.ny, self.nz), order='FORTRAN')
    #InAs Ep=21.5 eV
    #GaAs Ep=28.8 eV
    #GaSb Ep=27.0 eV
    
    #print len(Ep)
    return self.SRL

    

  def readStrain( self ):
    self.datname=self.prefix+'strain_crystal.dat'
    buffer=self.read_data_from_NN( self.datname )
    n=self.n
    nx=self.nx
    ny=self.ny
    nz=self.nz
    self.exx=buffer[0:n].reshape((nx, ny, nz), order='FORTRAN')/100.0
    self.exy=buffer[n:2*n].reshape((nx, ny, nz), order='FORTRAN')/100.0
    self.eyy=buffer[2*n:3*n].reshape((nx, ny, nz), order='FORTRAN')/100.0
    self.exz=buffer[3*n:4*n].reshape((nx, ny, nz), order='FORTRAN')/100.0
    self.eyz=buffer[4*n:5*n].reshape((nx, ny, nz), order='FORTRAN')/100.0
    self.ezz=buffer[5*n:6*n].reshape((nx, ny, nz), order='FORTRAN')/100.0

    return list([ self.exx, self.eyy, self.ezz, self.exy, self.exz, self.eyz])
   


  def calcDerivedParam( self, direct='z' ):
    1
    self.readStrain()

    hydrostatSt = self.exx+self.eyy+self.ezz
    #IMPORTANT:
    #biaxial strain B calculated including u_b=-2 and shift of the hh bandedge: DeltaE=-u_bB, thus the more negative value the
    #more lower potential for holes (i.e. bandedge for holes is more positive), holes prefer these areas
    delEbiaxSt = self.exx+self.eyy-2.0*self.ezz
    
    self.discriminateSRL()
    delEbiaxStSRL = self.SRL*delEbiaxSt*1e3
 
    #print delEbiaxStSRL
        
    #print len(na.sum(na.sum( hydrostatSt, axis=0 ) ,axis=0 )), self.nx,self.ny,self.nz
    #print na.sum(na.sum( hydrostatSt, axis=0 ) ,axis=0 )/self.n
    #print na.sum(na.sum(biaxSt, axis=0 ) ,axis=0 )/self.n

    self.readCoord()
    #simVol=(self.coordx[-1]-self.coordx[0])*(self.coordy[-1]-self.coordy[0])*(self.coordz[-1]-self.coordz[0])
    #print simVol

    #print direct
    if direct=='z':
        hydroStCum=na.sum(na.sum( hydrostatSt, axis=0 ) ,axis=0 )/(self.nx*self.ny)
        biaxStCum=na.sum(na.sum(delEbiaxStSRL, axis=0 ) ,axis=0 )/(self.nx*self.ny)
        axis=self.coordz
    elif direct=='x':
        hydroStCum=na.sum(na.sum( hydrostatSt, axis=2 ) ,axis=1 )/(self.nz*self.ny)
        biaxStCum=na.sum(na.sum(delEbiaxStSRL, axis=2 ) ,axis=1 )/(self.nz*self.ny)
        axis=self.coordx
    elif direct=='y':
        hydroStCum=na.sum(na.sum( hydrostatSt, axis=2 ) ,axis=0 )/(self.nz*self.nx)
        biaxStCum=na.sum(na.sum(delEbiaxStSRL, axis=2 ) ,axis=0 )/(self.nz*self.nx)
        axis=self.coordy
    cumsumAx=list([axis,hydroStCum,biaxStCum])
    #print cumsumAx
    #print len(axis),len(hydroStCum),len(biaxStCum)
    #print len(hydrostatSt)
    #dummy=list([[[1,1,1],[2,2,2]],[[3,3,3],[4,5,4]]])
    #print na.sum(na.sum(dummy, axis=0 ) ,axis=0 )
    #hydroZ=[(x*27.0+(1.0-x)*28.8) if x>0.35 else (x*21.5+(1.0-x)*28.8) for x in (hydrostatSt) for y in (hydrostatSt[])]
    #Ep=[(x*27.0+(1.0-x)*28.8) if x>0.35 else (x*21.5+(1.0-x)*28.8) for x in (data)]

    

    #return list([ hydrostatSt, biaxSt ])
    return cumsumAx

