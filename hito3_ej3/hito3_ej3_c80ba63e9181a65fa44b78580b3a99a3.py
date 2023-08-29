class Taxon:
      def _init_(self,c,n):
        self.categoria = c
        self.nombre = n
        self.subcategorias = []
    def incluir(self,t):
        self.subcategorias.append(t)
	pass
      