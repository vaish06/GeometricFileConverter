# Mesh.py
# Vaishnave Iyengar
# vaichu42@gmail.com
# CSC 220, Fall 2016

# Mesh is an independent, stand alone class composed of other classes.
# It stores the vertex coordinates. The vertex coordinates are always x,y,z triples. We don't know how many, but they're always triples. 
# Mesh also contains the faces. We not only don't know how many faces a given OBJ file has.

from positional_list import *

class Mesh:
	'''Mesh is an independent, stand alone class composed of other classes.'''
	def __init__(self, filename):
	    print("In Mesh, creating mesh1.")
	    self.vertices = []
	    self.faces = PositionalList()
	    self.faceCount = []
	    self.min_bounds = [0,0,0]
	    self.max_bounds = [0,0,0]
	    self.objFile = filename
	
	def loadOBJ(self):
	    """Loads a Wavefront OBJ file."""
        print("In the loadOBJ method\n")
		for line in open(self.objFile, "r"):
			if line.startswith('#'): continue
			values = line.split()
			if not values: continue
			if values[0] == 'v':
				v = map(float, values[1:4])
				self.vertices.append(v)
			elif values[0] == 'f':
				f = map (int, values[1:])
				self.faces.add_last(f)
				
	def findBounds(self):
		i = 0
		for v in self.vertices and i < 3:
			if v < min_bounds[i]:
				min_bounds[i] = v
			elif v > max.bounds[i]:
				max_bounds[i] = v
			i += 1
		
	def findFaceCount(self):
		unsortedCount = []
		for f in self.faces:
			unsortedCount.append(len(f))
		unsortedCount.sort()
		count = 0
		for i in range (0, len(unsortedCount)):
			if ( i < len(unsortedCount)):
				if(unsortedCount[i] == unsortedCount[i+1]):
					count += 1
				else:
					faceCount.append((unsortedCount[i], count+1))
					count = 0	
			else:
				if(unsortedCount[i-1] == unsortedCount[i]):
					faceCount.append((unsortedCount[i], count+1))
				else:
					faceCount.append((unsortedCount[i-1], count))
					faceCount.append((unsortedCount[i], 1))
	
	def writeVTK(self):
		# split the filename from '.'
		name = self.filename.spilt('.')
		# append .vtk to the new filename
		vtkFile = name[0] + '.vtk'
		file = open(vtkFile, "w")
        file.write("# vtk DataFile Version 3.0 \n")
        file.write(str(vtkFile))
        file.write("\n")
        file.write("ASCII \n")
        file.write("DATASET POLYDATA \n")
        file.write("POINTS ")
		# print the total count of vertices
        file.write(str(len(vertices)))
        file.write(" float \n")
		# print each vertex as a float of x y z
        for v in vertices and i in range (0,3):
            file.write(str(v[i]))
            file.write(" ")
            if i == 2:
                file.write("\n")
        file.write("\n")
        file.write("POLYGONS ")
		# print I the number of polygons in the object
        file.write(str(len(faces)))
        file.write(" ")
		# print J the total count of numbers in the data section
        file.write(str(count_numbers))
        file.write("\n")
		# loop through the below section for every face
		# print the total nodes of face
        for f in faces:
            file.write(str(len(f)))
            file.write(" ")
			# print the face
            i = 0
            while i < len(f):
                file.write(str(f[i] -1))
                i += 1
        file.write(" ")
        file.close()
        return vtkFile
		
    #def triangularize(self):
		# triangularizes the obj file
		
    #def writeTriVTK(self):
		# split the filename from '.'
		#name = self.filename.spilt('.')
		# append .vtk to the new filename
		#triVtkFilename = name[0] + '_Tri.vtk'
		#triVtkFile = vtk(triVtkFilename, self.vertices, self.faces)
		#return triVtkFile
		
	def printStats(self):
		print("*************************************\n")
		print("--------------Stats Table------------\n")
		print("Number of vertices: ")
		print(len(vertices))
		print("\n")
		print("Number of faces: ")
		print(len(faces))
		print("\n")
		print("Minimum bounds [x,y,z]: ")
		print(min_bounds)
		print("Maximum bounds [x,y,z]: ")
		print(max_bounds)
		print("----------------Faces----------------\n")
		for c in faceCount:
			print(c[0])
			print(" vertices = ")
			print(c[1])
			print(" faces\n")
		print("*************************************\n")
	