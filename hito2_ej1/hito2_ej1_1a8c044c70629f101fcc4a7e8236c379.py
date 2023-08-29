secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

alineacion = ""
i = 0
j = 0

while i < len(secuencia1):
    if j < len(secuencia2) and secuencia1[i] == secuencia2[j]:
        alineacion += secuencia2[j]
        i += 1
        j += 1
    else:
        alineacion += "_"
        i += 1

while j < len(secuencia2):
    alineacion += secuencia2[j]
    j += 1

print(alineacion)
      