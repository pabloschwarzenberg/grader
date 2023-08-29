

class Vector:
	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z
	def norma(self):
		return ((self.x**2+self.y**2+self.z**2))**(1/2)

	def __add__(vector1,vector2):
		x1=vector1.x+vector2.x
		y1=vector1.y+vector2.y
		z1=vector1.z+vector2.z
		vector_suma=Vector(x1,y1,z1)
		return vector_suma

def suma_vectores(vector1,vector2):
	x1=vector1.x+vector2.x
	y1=vector1.y+vector2.y
	z1=vector1.z+vector2.z
	vector_suma=Vector(x1,y1,z1)
	return vector_suma