import random

class JuegoDelGato:
	
	def __init__(self):
		
		self.tablero=[[-1, -1, 0],
			[0, 1, 0],
			[1, 1, 0]]

	def __repr__(self):
		
		return str(self.mostrar_tablero())

	def jugarGato(self, fila, columna):
		
		if self.tablero[fila][columna]==0:
			
			self.tablero[fila][columna]=1
			return True
			
		else:
			
			return False

	def jugarRaton(self):
		
		posiciones_vacias=[]
		
		for i in range(3):
			
			for j in range(3):
				
				if self.tablero[i][j]==0:
					
					posiciones_vacias.append((i, j))

		if len(posiciones_vacias)>0:
			
			fila, columna=random.choice(posiciones_vacias)
			self.tablero[fila][columna]=-1
			return True
			
		else:
			
			return False

	def indicarEstado(self):
		
		for i in range(3):
			
			if self.tablero[i][0]==self.tablero[i][1]==self.tablero[i][2]!=0:
				
				return self.tablero[i][0]

			if self.tablero[0][i]==self.tablero[1][i]==self.tablero[2][i]!=0:
				
				return self.tablero[0][i]

		if self.tablero[0][0]==self.tablero[1][1]==self.tablero[2][2]!=0:
			
			return self.tablero[0][0]
			
		if self.tablero[0][2]==self.tablero[1][1]==self.tablero[2][0]!=0:
			
			return self.tablero[0][2]

		if all(self.tablero[i][j]!=0 for i in range(3) for j in range(3)):
			
			return 1

		return 0

	def cargar_tablero(self, tablero):
		
		self.tablero=tablero

	def mostrar_tablero(self):
		
		return self.tablero


if __name__=='__main__':
	
	juego=JuegoDelGato()
	
	while juego.indicarEstado()==0:
		
		print(juego)
		x, y=tuple(input("Ingresa tu jugada: ").split(","))
		juego.jugarGato(int(x), int(y))
		juego.jugarRaton()
		
	print(juego)