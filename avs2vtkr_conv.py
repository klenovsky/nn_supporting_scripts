# Converts nextnano++ (not tested for nn3) file into .vtk format in order to view it e.g. in mayavi2 
# (which is included in standard python distribution)
#
# based originally on avs2xyz.py script downloaded from nextnano site 
#
# written for more comfortable data viewing than that in Origin before nextnanomat
# however useful even now e.g. for making isosurface plots of the data or 
# scalar cuts of them in arbitrary plane (both properties of standard python's mayavi2 script)
#
# tested currently only on python 2.x distributions 
# 
# written by Petr Klenovsky, 2010
# command line execution: avs2vtkr.py filename
#
# klenovsky@physics.muni.cz
#
# Department of condensed matter physics, Masaryk university, Brno, Czech republic 


import numpy as np
import sys

def conv(path,stName,VTKoutPath,VTKoutName):
        fname=path+stName
        f_fld=open(fname+'.fld','r')
        size=1
        for line in f_fld:
                if(line.lower().count('ndim') > 0):
                        ndim=int(line.split()[2])
                if(line.lower().count('dim1') > 0):
                        dim1=int(line.split()[2])
                        size=size*dim1
                if(line.lower().count('dim2') > 0):
                        dim2=int(line.split()[2])
                        size=size*dim2
                if(line.lower().count('dim3') > 0):
                                dim3=int(line.split()[2])
                                size=size*dim3
                if(line.lower().count('veclen') > 0):
                        veclen=int(line.split()[2])                                      
                        
        f_fld.close()
        coord=np.loadtxt(fname+'.coord')
        coord_1=coord[0:dim1]
        coord_2=coord[dim1:dim1+dim2]
        if(ndim==3):
                coord_3=coord[dim1+dim2:]
        else:
                coord_3=[0]
                        
# Check whether the file is binary or ascii
#   The chenking is implemented by counting the number of
#   lines is ascii mode. If it is equal to size, the file
#   is an ascii file. 

        count=0
        for line in open(fname+'.dat','r'):
                if (line.strip() != ''): count += 1

        if (count == (size*veclen)):
                # Ascii file
                read_data=np.loadtxt(fname+'.dat')
        else:
                # Binary file
                fd=open(fname+'.dat','rb')
                read_data = fd.read(fd, count, 'd')
                print read_data
                fd.close()

        f_out=open(VTKoutPath+VTKoutName+'.vtk','w')
        f_out.write('# vtk DataFile Version 2.0\n')
        f_out.write(fname+'\n')
        f_out.write('ASCII\n')    
        f_out.write('DATASET RECTILINEAR_GRID\n')
        if(ndim==3):
                f_out.write('DIMENSIONS %6d %6d %6d\n'%(dim1,dim2,dim3))
        else:
                f_out.write('DIMENSIONS %6d %6d\n'%(dim1,dim2))
        f_out.write('X_COORDINATES %8d float\n'%(dim1))
        for x in coord_1:
               f_out.write('%18.10f\n'%(x))
        f_out.write('Y_COORDINATES %8d float\n'%(dim2))
        for y in coord_2:
               f_out.write('%18.10f\n'%(y)) 
        if(ndim==3):                     
               f_out.write('Z_COORDINATES %8d float\n'%(dim3))
               for z in coord_3:                    
                       f_out.write('%18.10f\n'%(z))            
        
        f_out.write('\n')
        f_out.write('POINT_DATA %8d\n'%(size))
        for l in range(0,veclen):
               f_out.write('SCALARS '+fname+repr(l)+' float 1\n') 
               f_out.write('LOOKUP_TABLE default\n')
               i=0
               for z in coord_3:
                       for y in coord_2:
                                for x in coord_1:
                                       val=read_data[i+l*size]                                
                                       f_out.write('%18.12E\n'%(val))                                                                           
                                       i+=1                       
        f_out.close()
