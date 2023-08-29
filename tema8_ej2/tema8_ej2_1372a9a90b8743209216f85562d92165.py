def buscarTodas(a,b):

  contador = 0

  salida = ""

  for letra in a:

   if letra == b:

    salida = salida + str(contador) + " "

   contador = contador + 1

  salida = salida.rstrip()

  return salida



if __name__ == "__main__":

  p = input("Ingrese la palabra a buscar")

  l = input("Ingrese la letra a buscar")

  salida = buscarTodas(p,l)

  print("Las posiciones encontradas fueron : ", salida)
 
           