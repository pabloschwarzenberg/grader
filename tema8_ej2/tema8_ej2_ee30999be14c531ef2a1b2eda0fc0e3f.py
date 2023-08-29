def buscarTodas(a,b):
    largo=len(a)
    apariciones=[]
    for indice in range(largo):
      if a[indice]==b:
        apariciones.append(str(indice))
    cadena=" ".join(apariciones)
    return cadena
if __name__ == "__main__":
    pass
           