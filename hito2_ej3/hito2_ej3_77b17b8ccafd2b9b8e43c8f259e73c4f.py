secuencia=input("Ingrese la secuencia: ")
n = int(input("Ingrese un numero entero: "))

palabras_unicas = []
palabras_repetidas = []

for i in range(0, len(secuencia)):
  palabra = secuencia[i:i+n]
  if (len(palabra) == n):
    if not(palabra in palabras_unicas):
      if not(palabras_repetidas):
        palabras_unicas.append(palabra)
    else:
      palabras_unicas.remove(palabra)
      palabras_repetidas.append(palabra)

if(len(palabras_unicas) > 0):
  for n in palabras_unicas:
    print(n)
else:
  print('ninguna')

