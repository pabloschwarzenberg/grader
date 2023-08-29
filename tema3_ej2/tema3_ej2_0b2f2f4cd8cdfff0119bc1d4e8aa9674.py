# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
	
	def __init__(self, x, y, z):
		
		self.x=x
		self.y=y
		self.z=z

	def __norma__(self):
		
		return ((self.x*2)+(self.y2)+(self.z2))*0.5

	def __add__(self, other):
		
		if isinstance(other, Vector):
			
			return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
			
		else:
			
			print('Error')


def suma_vectores(v1, v2):
	return v1 + v2
           