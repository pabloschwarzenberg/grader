def ejecutar(n,palabra):
  p = palabra
  archivo = open(n,"r")
  cantidad_filas = len(archivo.readlines())
  archivo.close()
  with open(n,"r") as file:
    indice = 0
    sublista = []
    for i in range(cantidad_filas):
      fila =  file.readline()
      fila = fila.replace("\n","").lower().split(" ")
      sublista.append(fila)
    for i in range(3):
      for j in range(4):
        if p[0] == sublista[i][j]:
          for c in range(1,len(p)):
            if p[c] == sublista[i][j+1]:
              # print(1)
              salida = (p,[i,j],"derecha")
              return salida
            elif p[c] == sublista[i+1][j]:
              # print(2)
              salida = (p,[i,j],"abajo ")
              return salida
            elif p[c] == sublista[c][c]:
              # print(3)
              salida = (p,[i,j],"diagonal")
              return salida


def sopaletras(nombre_archivo,palabras):
  n = nombre_archivo
  for i in palabras:
    print(ejecutar(n,i))


    
if __name__=="__main__":
    # print(sopaletras("sopa.txt",["cra"]))
    # print(sopaletras("sopa.txt", ["aro"]))
    # print(sopaletras("sopa.txt", ["casa"]))
    sopaletras("sopa.txt",["casa","cra","aro"])