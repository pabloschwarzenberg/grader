class Taxon:
	def __init__(self, categoria, nombre):
		self.categoria=categoria
		self.nombre=nombre
	subcategorias=[]
	def incluir(self):
		#if self.categoria==