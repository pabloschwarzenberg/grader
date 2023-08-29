class Matriz:
	
	def __init__(self, celdas=[]):
		self.celdas=celdas

	def __repr__(self):
		s=""
		for i in range(len(self.celdas)):
			for j in range(len(self.celdas[i])):
				s+="{0: >5} ".format(self.celdas[i][j])
			s+="\n"
		return s

	def __mul__(self, other):
		
		if isinstance(other, Matriz):
			
			if len(self.celdas[0]) != len(other.celdas):
				
				print('Erai')

			Producto=[]
			for i in range(len(self.celdas)):
				
				F=[]
				
				for j in range(len(other.celdas[0])):
					
					x=0
					
					for k in range(len(self.celdas[0])):
						
						x+=self.celdas[i][k] * other.celdas[k][j]
						
					F.append(x)
					
				Producto.append(F)

			return Matriz(Producto)
			
		else:
			print('Erai')


if __name__ == '__main__':
	
	a=Matriz([[1,2],[3,4]])
	b=Matriz([[5,6],[7,8]])
	r=a*b
	print(r)