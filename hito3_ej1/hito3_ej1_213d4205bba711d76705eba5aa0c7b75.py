class Taxon:
   def __int__(self, aves_datos):
      A = aves_datos.split(",")
      self.categoria = int(A[0]) 
      self.nombre = int(A[1])

      n = input("nombre del ave:")
      c = input("catecorias del ave:")

      if n == 0:
        print("el nomebre:", n)
      if c == 0:
        print("categorias del ave:", c)
    
pass
      