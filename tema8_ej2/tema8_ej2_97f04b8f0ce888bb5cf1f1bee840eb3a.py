def buscarTodas(a,b):
   Posiciones = []
   for Posicion in range(len(a)):
     if a[Posicion] == b:
       Posiciones.append(str(Posicion))
   return " ".join(Posiciones) 

if __name__ == "__main__":
    pass
           