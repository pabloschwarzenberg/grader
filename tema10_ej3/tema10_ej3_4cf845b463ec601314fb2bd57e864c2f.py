def sopaletras(nombre_archivo,palabras):
    with open(nombre_archivo,"r") as sopaletras:
      lines= sopaletras.readlines()
      for l in range(len(lines)):
        lines[1]= lines[1].replace(" ","").replace("\n","").lower() 
    for fila,linea in enumerate(sopaletras):
      if palabra in linea:
        print(fila)
    for fila,linea in enumerate(sopa_letra):
      if palabra in linea:
        for l in range(len(linea)):
          if palabra == linea[l:l+len(palabra)]:
            print(fila,l)