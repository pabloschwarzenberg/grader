class Vector:
	def __init__(self, x, y, z):
		self.x=x
		self.y=y
		self.z=z
	def norma(self):
		x1=float((self.x)**2)
		y1=(self.y)**2
		z1=(self.z)**2
		modulo=float((x1+y1+z1)**(1/2))
		return modulo
	def __add__(self, other):
		newX=self.x+ other.x
		newY=self.y+ other.y
		newZ=self.z+ other.z
		newVector=Vector(newX, newY, newZ)
		return newVector

def suma_vectores(v1, v2):
	x=v1.x +v2.x
	y=v1.y+v2.y
	z=v1.z+v2.z
	return Vector(x, y, z)
