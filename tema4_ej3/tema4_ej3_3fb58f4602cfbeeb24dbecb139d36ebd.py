def jerigonzo(texto):
    lista=list(texto)
    posicion=0
    for i in lista:
      if i.lower()=="a":
        lista[posicion]=i+'p'+i.lower()
      if i.lower()=="e":
        lista[posicion]=i+'p'+i.lower()
      if i.lower()=="i":
        lista[posicion]=i+'p'+i.lower()
      if i.lower()=="o":
        lista[posicion]=i+'p'+i.lower()
      if i.lower()=="u":
        lista[posicion]=i+'p'+i.lower()
      if i.lower()=="á":
        lista[posicion]=i+'p'+i.lower()
      if i.lower()=="é":
        lista[posicion]=i+'p'+i.lower()
      if i.lower()=="í":
        lista[posicion]=i+'p'+i.lower()
      if i.lower()=="ó":
        lista[posicion]=i+'p'+i.lower()
      if i.lower()=="ú":
        lista[posicion]=i+'p'+i.lower()
      posicion+=1
      final="".join(lista)
    return final
    
    
if __name__ == "__main__":
  texto=str(input())
  pass
 