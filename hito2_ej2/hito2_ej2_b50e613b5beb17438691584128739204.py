def analizarpalabra(palabra):
        global analisis
        global pozo
        analisis = True
        for i in palabra1:
            if i in pozo:
                analisis = analisis and True
            else:
                analisis = False

        return analisis

palabra2=input("Ingrese palabra:")
palabra1 = palabra2.upper()

pozo = "ACTG"

analisis = 0
  
palabra = analizarpalabra(palabra1)

if analisis == True:
  print("secuencia correcta")
else:
  print("secuencia incorrecta")