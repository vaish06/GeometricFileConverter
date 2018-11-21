# VTK.py
# Vaishnave Iyengar
# vaichu42@gmail.com
# CSC 220, Fall 2016

# Writes a VTK file from OBJ file.

class VTK:
    '''Writes a VTK file using extracted data from OBJ file'''
    def __init__(self, vtkFile, vertices, faces):
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