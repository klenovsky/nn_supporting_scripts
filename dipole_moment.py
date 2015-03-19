import numpy as na
#from scipy.io.numpyio import fread
#import numpy as na
import scipy as sp
import sys, os

#if __name__ == '__main__':
class dipole ():
   def __init__( self , prefix='', no_e=1, no_h=2, Type='nn++'):  
       print 'dipole_moment initialized'      
       #state_no_h=int(sys.argv[1])
       #state_no_e=int(sys.argv[2])
       self.Type=Type
       self.prefix=prefix
       self.no_h=no_h
       self.no_e=no_e
       #no_h_s=str(no_h)
       #no_e_s=str(no_e)
        

   def read_data_from_NN( self , filename ):
       if not os.path.isfile(filename):
          print 'ERROR: file %s not found\n' % (filename)
          sys.exit(1)
       buffer=na.fromfile( filename,  sep='\n' )	
       return buffer

   def generateWFNames( self , state , particle ):
     if self.Type=='nn++':
       return self.prefix+'wf_probability_dot_kp8_0000_00%02i'%(state)
     elif self.Type=='nn3_1x6':
       if particle=='e':
          return self.prefix+'\\Schroedinger_1band\\3Dcb001_qc001_sg001_deg001_dir_psi_squared_ev0%02i'%(state)
       elif particle=='h':
          return self.prefix+'\\Schroedinger_kpband\\3Dkp6x6_wave_hl_qc001_ev0%02i'%(state)
     elif self.Type=='nn3_8x8': 
       if particle=='e':
          return self.prefix+'\\Schroedinger_kpband\\3Dkp8x8_wave_el_qc001_ev0%02i'%(state)
       elif particle=='h':
          return self.prefix+'\\Schroedinger_kpband\\3Dkp8x8_wave_hl_qc001_ev0%02i'%(state)


   def read_dimensions (self , filename ):
       fld_name=filename[:-4]+'.fld'
       f_fld=open(fld_name, 'r')
       lines=[ f_fld.readline() for i in xrange(8) ]
       dim1=int(lines[3].split()[2])
       dim2=int(lines[4].split()[2])
       dim3=int(lines[5].split()[2])
       '''
       for line in f_fld:
                print line
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
       '''
       coord_name=filename[:-4]+'.coord'
       coord=self.read_data_from_NN(coord_name)
       coord_1=coord[0:dim1]
       coord_2=coord[dim1:dim1+dim2]        
       coord_3=coord[dim1+dim2:] 
       return [coord_1, coord_2, coord_3]

   def calc_moment (self, state, particle):
       filename=self.generateWFNames( state, particle )+'.dat'
       #print 'GENERATED FILENAME ',filename
       dim=self.read_dimensions (filename)
       data = self.read_data_from_NN( filename )
       norm=na.sum(data)
       moment=[0,0,0]
       i=0
       for z in dim[2]:              
                for y in dim[1]:
                       for x in dim[0]:
                            moment[0]+=x*data[i]/norm
                            moment[1]+=y*data[i]/norm
                            moment[2]+=z*data[i]/norm
                            i+=1
       return moment 

   def calc_e_h_dipole ( self ):
       moment_h = self.calc_moment(state=self.no_h, particle='h')
       moment_e = self.calc_moment(state=self.no_e, particle='e')
       moment=[]
       for j in range (3):                    
             moment.append(moment_h[j]-moment_e[j]) 
       return moment
        

        
