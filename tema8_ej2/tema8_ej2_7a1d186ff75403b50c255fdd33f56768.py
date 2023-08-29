def buscarTodas(a,b):
  Posicion_Letra = ""
  for x in range(len(a)):
    if b==a[x]:
      Posicion_Letra = Posicion_Letra + str(x) + " "
      Posicion_Letra = Posicion_Letra.rstrip(" ") #Para eliminar espaciados finales
      return Posicion_Letra