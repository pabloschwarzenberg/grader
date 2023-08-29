hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

def estadisticas_frase(palabra):
  #Contador de palabras
  contador_palabras = 0 #RETORNAR
  for i in range(0,len(palabra)):
    if palabra[i] in " \n": 
      contador_palabras += 1
  for j in range(0,len(palabra)):
    if palabra[j] == "\n" and palabra[j+1] == "\n": 
      contador_palabras -= 1
  #Numero de Caracteres
  numero_de_caracteres = 0 #RETORNAR
  for k in range(0,len(palabra)):
    numero_de_caracteres += 1
  #Promedio de letras
  sumatoria = 0
  lista = palabra.split()
  #This wil remove the dots from the final element of the list
  last = lista[len(lista)-1]
  lista_last = []
  for n in range(0,len(last)):
    lista_last.append(last[n])
  o = 0
  while o <= len(lista_last):
    if lista_last[o] == ".":
      lista_last.pop(-1)
    o += 1
  lista_last.remove(".")
  lista[len(lista)-1] = "".join(lista_last)
  #Ready
  for l in range(0,len(lista)):
    contador = 0
    for m in range(0,len(lista[l])):
      contador += 1
    sumatoria += contador
  promedio = sumatoria/contador_palabras #RETORNAR
  #Numero de espacios
  spaces = 0 #RETORNAR
  for p in range(0,len(palabra)):
    if palabra[p] == " ":
      spaces += 1
  #Signos de puntuacion
  signos = 0
  for q in range(0,len(palabra)):
    if palabra[q] in "¿?{}[]!¡.,-_:;/*'''":
      signos += 1
  
  return contador_palabras,numero_de_caracteres,promedio,spaces,signos

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         