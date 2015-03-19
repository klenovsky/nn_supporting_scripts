import sys,os,states2transition as st
import numpy as na
import scipy as sp
import bisect as bi
from intergrid import Intergrid 
from scipy import ndimage
import numpy.polynomial.legendre as L
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import directory_names as dn
#import matplotlib.image as mpimg

hbar=1.054571726*10**(-34)
e=1.602176565*10**(-19)

class makeCut():
  def __init__(self , name ):
      print name
      self.name=name
      #self.v1=na.array(vec1)
      #self.v2=na.array(vec2)
      #self.nx=20
      #self.ny=20
      #self.nz=10





  #Funkce pro nacitani dat z nextnano souboru 'filename', stejne jako v strain_from_nextnano_to_csi.py
  def read_data_from_NN( self , filename ):
    buffer=na.fromfile( filename,  sep='\n' )
    return buffer






  def normProb( self, prob):
    norm=na.sum(prob)
    probOut=prob/norm 
    return probOut







  #Funkce pro nacitani poctu datovych bodu, asi stejne jako v strain_from_nextnano_to_csi.py, nadbytecna funkce
  def readDimensions ( self, fldname ):
    f=open(fldname,'r')
    lines=[ f.readline() for i in xrange(8) ]
    nx=int(lines[3].split()[2])
    ny=int(lines[4].split()[2])
    nz=int(lines[5].split()[2])
    n=nx*ny*nz
    #self.readSizesFromFld( 1 , st.wftype[0] )
    return [ nx , ny , nz , n ] 





  def readCoords (self , dim, coord_name ):
       dim1=dim[0]
       dim2=dim[1]
       dim3=dim[2] 
       coord=self.read_data_from_NN(coord_name)
       coord_1=coord[0:dim1]
       coord_2=coord[dim1:dim1+dim2]        
       coord_3=coord[dim1+dim2:] 
       #return [coord_1, coord_2, coord_3]
       return na.array( [coord_1, coord_2, coord_3] )








  def defineZero (self, coordsNotZero):
       cenVal=[]
       temp=coordsNotZero
       ooutCoords=temp
       for i in range(len(coordsNotZero)):
          cen= len(coordsNotZero[i])/2 
          cenVal.append(coordsNotZero[i][cen])
          ooutCoords[i]=coordsNotZero[i]-coordsNotZero[i][cen]
       outCoords=na.array(ooutCoords)
       #outCoords=na.array(temp)
       #print outCoords,cenVal            
       return outCoords,cenVal













  def im3D( self, isProbab=0 ):
    plt.clf()
    fldname=self.name+'.fld'
    dim=self.readDimensions(fldname)
    print dim
    nx=dim[0]
    ny=dim[1]
    nz=dim[2]

    datname=self.name+'.dat'
    rawdata=self.read_data_from_NN( datname )
    data=rawdata.reshape((nx, ny, nz), order='FORTRAN')
    if isProbab==1:   
       data=self.normProb(data)
    #print data
    coordname=self.name+'.coord'
    coords=self.readCoords ( dim, coordname )
        
    X=coords[0]
    Y=coords[1]
    Z=coords[2]
    coos=[([x,y,z]) for x in X for y in Y for z in Z ]
    coo=na.array(coos).reshape((nx,ny,nz), order='FORTRAN' ) 
    print 'COOS LEN ',len(coo)
    
    fig = plt.figure(figsize=(14,6))

    # `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
    ax = fig.add_subplot(1, 2, 1, projection='3d')

    p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

    # surface_plot with color grading and color bar
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='Spectral_r', linewidth=0, antialiased=False)
    cb = fig.colorbar(p, shrink=0.5)




    coordname=self.name+'.coord'
    coords=self.readCoords ( dim, coordname )
        
    
    #WORKS OK
    x=len(coords[0])/2
    print 'x ',x,len(coords[0])
    new_data=[]
    for z in range(len(coords[2])):
       for y in range(len(coords[1])):
          new_data.append( data[x,y,z] )
          
    new_data=na.array(new_data).reshape(len(coords[2]),len(coords[1]))
    
    fig, ax = plt.subplots()
    im = ax.imshow(new_data, cmap='Spectral_r', vmin=abs(new_data).min(), vmax=abs(new_data).max(), origin='lower', extent=[coords[1][0], coords[1][-1], coords[2][0], coords[2][-1]])
    #plt.imshow(new_data, cmap='Spectral')
    im.set_interpolation('nearest')  #'bilinear'
    cb = fig.colorbar(im, ax=ax)
    #plt.show()
    #WORKS OK








  def sliceEdge( self, isProbab=0 ):
    fldname=self.name+'.fld'
    dim=self.readDimensions(fldname)
    print dim
    nx=dim[0]
    ny=dim[1]
    nz=dim[2]

    datname=self.name+'.dat'
    rawdata=self.read_data_from_NN( datname )
    data=rawdata.reshape((nx, ny, nz), order='FORTRAN')
    if isProbab==1:   
       data=self.normProb(data)
    #print data 
    coordname=self.name+'.coord'
    coords=self.readCoords ( dim, coordname )
     
    #WORKS OK
    x=len(coords[0])/2
    print 'x ',x,len(coords[0])
    new_data=[]
    for z in range(len(coords[2])):
       for y in range(len(coords[1])):
          new_data.append( data[x,y,z] )
          
    new_data=na.array(new_data).reshape(len(coords[2]),len(coords[1]))

    return new_data, [coords[1][0], coords[1][-1], coords[2][0], coords[2][-1]] 
    















  def sliceAnyDirec( self, name, vec1=[0,1,0], vec2=[0,0,1], isProbab=0, ord=1, loadMatCoord=None ):
    t1=na.array(vec1)
    t2=na.array(vec2)
    norm1=na.sqrt(na.sum(t1**2))
    norm2=na.sqrt(na.sum(t2**2))
    #print norm1,norm2 
    v1=t1/norm1
    v2=t2/norm2
    #print 'v1 array ',v1[:, None, None] 
    #print 'v2 array ',v2[None, :, None]    
    pno=40

    fldname=name+'.fld'
    dim=self.readDimensions(fldname)
    nx=dim[0]
    ny=dim[1]
    nz=dim[2]

    datname=name+'.dat'
    rawdata=self.read_data_from_NN( datname )
    data=rawdata.reshape((nx, ny, nz), order='FORTRAN')
    if isProbab==1:   
       data=self.normProb(data)
    dcX=len(data)/2 
    dcY=len(data[dcX])/2
    
    
    coordname=name+'.coord'
    incoords=self.readCoords ( dim, coordname )
    #print 'COORDS TO ZERO'
    coords=na.array( incoords )
    origin=[0,0,0]
        
    lo=na.array([ coords[0][0], coords[1][0], coords[2][0] ])
    hi=na.array([ coords[0][-1], coords[1][-1], coords[2][-1] ])
    maps=[coords[0],coords[1],coords[2]]
    interfunc = Intergrid( data, lo=lo, hi=hi, order=ord, maps=maps )
    
    if loadMatCoord != None:
       coords=loadMatCoord[0]
       origin=loadMatCoord[1]
    nx, ny, nz = (100,100,50)
    X=na.linspace(coords[0][0],coords[0][-1],nx)
    Y=na.linspace(coords[1][0],coords[1][-1],ny)
    Z=na.linspace(coords[2][0],coords[2][-1],nz)
    coos=[([x,y,z]) for x in X for y in Y for z in Z ]
    
    #print 'INTERFUNC'
    dataN=interfunc.at( coos ).reshape(nx,ny,nz)
    dx=na.abs(X[1]-X[0])
    dy=na.abs(Y[1]-Y[0])
    dz=na.abs(Z[1]-Z[0])
        
    for i in range(len(X)):
        if na.abs(X[i]-dn.slicePoints[0])<dx:
             Xpt=i
    for i in range(len(Y)):
        if na.abs(Y[i]-dn.slicePoints[1])<dy:
             Ypt=i
    for i in range(len(Z)):
        if na.abs(Z[i]-dn.slicePoints[2])<dz:
             Zpt=i
    
    scaling = na.array([dx, dy, dz])
    #print 'Scale'
    #print scaling
        
    lf=norm1
    vf=norm2
    #lf=1; vf=1
    #print 'lf, vf ',lf,vf
    
    LatP=lf*na.sqrt( (v1[0]*X[-1])**2 + (v1[1]*Y[-1])**2 + (v1[2]*Z[-1])**2 )
    VerP=vf*na.sqrt( (v2[0]*X[-1])**2 + (v2[1]*Y[-1])**2 + (v2[2]*Z[-1])**2 )
    LatN=-1.0*lf*na.sqrt( (v1[0]*X[0])**2 + (v1[1]*Y[0])**2 + (v1[2]*Z[0])**2 )
    VerN=-1.0*vf*na.sqrt( (v2[0]*X[0])**2 + (v2[1]*Y[0])**2 + (v2[2]*Z[0])**2 )
    
    #print 'LAT ', LatP, LatN, LatP-LatN
    #print 'VER ', VerP, VerN, VerP-VerN
    coo = (v1[:, None, None] * na.linspace(LatN, LatP, pno)[None, :, None] + v2[:, None, None] * na.linspace(VerN, VerP, pno)[None, None, :])
    cooOS = (v1[:, None, None] * -1.0*LatN*na.ones_like(na.linspace(LatN, LatP, pno))[None, :, None] + v2[:, None, None] * -1.0*VerN*na.ones_like(na.linspace(VerN, VerP, pno))[None, None, :])

    X=X+origin[0]
    Y=Y+origin[1]
    Z=Z+origin[2]
    LatP=lf*na.sqrt( (v1[0]*X[-1])**2 + (v1[1]*Y[-1])**2 + (v1[2]*Z[-1])**2 )
    VerP=vf*na.sqrt( (v2[0]*X[-1])**2 + (v2[1]*Y[-1])**2 + (v2[2]*Z[-1])**2 )
    LatN=-1.0*lf*na.sqrt( (v1[0]*X[0])**2 + (v1[1]*Y[0])**2 + (v1[2]*Z[0])**2 )
    VerN=-1.0*vf*na.sqrt( (v2[0]*X[0])**2 + (v2[1]*Y[0])**2 + (v2[2]*Z[0])**2 )
 
    '''
    print 'coo'
    print coo
    print
    print 'cooOS'
    print cooOS
    print
    print 'coo+cooOS'
    print na.abs(coo+cooOS)
    print    
    '''    
    idx=((coo+cooOS))/ ( scaling[(slice(None),) + (None,)*(coo.ndim-1)] )
    for i in range(len(idx)):
       #print item
       if idx[i][-1][-1]<0:
           #print idx[i][-1][-1]
           idx[i]=na.abs(idx[i][-1][-1])+idx[i]
    #print 'idx'
    #print idx
    #print
    if v1[0]==0 and v2[0]==0:
        idx[0]=Xpt
    elif v1[1]==0 and v2[1]==0:
        idx[1]=Ypt
    elif v1[2]==0 and v2[2]==0:
        idx[2]=Zpt
     
    new_data=ndimage.map_coordinates(dataN, idx).T
    
    return new_data, [LatN, LatP, VerN, VerP], [coords, origin]   