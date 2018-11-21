class WriteVTK:
	'''Writes a VTK file using extracted data from OBJ file'''
    file_name= "polygon"
    num_vertices= 3
    vertices= [(3,2,3), (1,2,3), (3,4,6)]
    num_faces= 5
    count_numbers=3
    
    file = open("polygon.vtk", "w")
    file.write("# vtk DataFile Version 3.0 \n")
    file.write(file_name)
    file.write(".vtk \n")
    file.write("ASCII \n")
    file.write("DATASET POLYDATA \n")
    file.write("POINTS ")
    file.write(str(num_vertices))
    file.write(" float \n")
    for item in vertices:
        for index in item:
                file.write(str(index))
                file.write(" ")
        file.write("\n")
    file.write("\n")
    file.write("POLYGONS ")
    file.write(str(num_faces))
    file.write(" ")
    file.write(str(count_numbers))
    file.write("\n")
    file.write(str(num_vertices))
    file.write(" ")
    for item in vertices:
        file.write(str(item))
        file.write(" ")
    file.close()