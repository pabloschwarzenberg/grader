def sopaletras(nombre_archivo,palabras):
  
  listav = []
  nuevo= ""

  with open(nombre_archivo, "r") as file:
    sopa = file.readlines()
    print(sopa)
    sopahorizontal=[]
  for indice in range(len(sopa)):
    sopa[indice] = sopa[indice].replace(" ", "").replace("\n","").lower()
  
  for creacion in range(len(sopa[0])):
    nuevo=""
    for lista in range(len(sopa)):
      nuevo += sopa[lista][creacion]
    listav.append(nuevo)

  for palabra in range(len(palabras)):
    for indice in range(len(sopa)):#derecha
      if palabras[palabra] in sopa[indice]:
        for columna in range(len(sopa[indice])):
          #print(columna, sopa_de_letras[indice][columna:columna+len(palabra[0])])
          if palabras[palabra] == sopa[indice][columna:columna+len(palabras[palabra])]:
            print(palabras[palabra],[indice, columna],"derecha")

    for columnav in range(len(listav)): #abajo
      if palabras[palabra] in listav[columnav]:
        #print(f"La palabra esta en la columna")
        for filav in range(len(listav[columnav])):
          if palabras[palabra] == listav[columnav][filav:filav+len(palabras[palabra])]:
            print(palabras[palabra],[filav, columnav],"abajo")