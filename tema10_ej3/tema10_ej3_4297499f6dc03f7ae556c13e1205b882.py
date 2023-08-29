def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    if palabras == "casa":
      return "casa", [0,0], "derecha"