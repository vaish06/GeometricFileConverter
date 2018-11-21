# Mesh.py
# Vaishnave Iyengar
# vaichu42@gmail.com
# CSC 220, Fall 2016

# Mesh is an independent, stand alone class composed of other classes.
# It stores the vertex coordinates. The vertex coordinates are always x,y,z triples. We don't know how many, but they're always triples. 
# Mesh also contains the faces. We not only don't know how many faces a given OBJ file has.

class Mesh:
	'''Mesh is an independent, stand alone class composed of other classes.'''
	numVertices = 0
	vertex = () 
	numFaces = 0 
	face = ()
	minBound = ()
	maxBound = ()
	numTriangles = 0
	numQuads = 0
	numPentagons = 0 
	numHexagons = 0
	numSeptagons = 0
	numOctagons = 0 
	
	def loadOBJ(objFile):
	    pass
		
	def writeVTK(objFile):
		pass
	
	def findBounds(objFile):
		pass
		
	def findFaceCount(objFile):
		pass
	
	def triangularize(objFile):
		pass 
	
	