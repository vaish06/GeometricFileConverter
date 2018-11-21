# project2.py
# Vaishnave Iyengar
# vaichu42@gmail.com
# CSC 220, Fall 2016

# Grabs the name of a user supplied OBJ file from the command line using sys.argv.
# Constructs a Mesh object based on that file.
# Prints out the stats after reading in the file.
# Writes out a converted VTK file.
# Triangularizes the mesh.
# Prints out the new stats.
# Writes out a second, independent VTK of the triangularized mesh.

from Mesh import *
import sys

if __name__=='__main__':
    try:
        filename = sys.argv[1]
        filetype = filename[-3:]
        
        if (filetype == 'obj'):
            mesh1 = Mesh(filename)
            print("In main, after creating mesh.") 
        else:
            raise ValueError('Unknown file extension.')
        
        print(filetype) 
        print(filename) 
        mesh1.loadOBJ()
        #mesh1.findBounds
        #mesh1.findFaceCount
        #mesh1.printStats
        #vtkFile = mesh1.writeVTK
        #mesh1.triangularize()
	    #mesh1.printStats()
	    #triVtkFile = mesh1.writeTriVTK()
    except Exception as e:
        print('Exception raised:')
        print(e)

	
