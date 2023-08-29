def buscarTodas(a,b):
    largo=len(a)
    lista_guardar = []
    for i in range(largo):
      if a[i]==b:
        lista_guardar.append(str(i))
    return " ".join(lista_guardar)
        
      

if __name__ == "__main__":
    buscartodas("tres tristes tigres","t")
           