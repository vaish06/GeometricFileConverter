# OBJ.py
# Vaishnave Iyengar
# vaichu42@gmail.com
# CSC 220, Fall 2016

# Reads the Wavefront OBJ file. Returns the stats for 
# vertices and faces.

from positional_list import *

class OBJ:
	def __init__(self, filename):
		"""Loads a Wavefront OBJ file."""
		print("In the OBJ class\n")
		self.vertices = []
		self.faces = PositionalList()
	
	def load(self):
		for line in open(filename, "r"):
			if line.startswith('#'): continue
			values = line.split()
			if not values: continue
			if values[0] == 'v':
				v = map(float, values[1:4])
				self.vertices.append(v)
			elif values[0] == 'f':
				f = map (int, values[1:])
				self.faces.add_last(f)
		return self.vertices, self.faces