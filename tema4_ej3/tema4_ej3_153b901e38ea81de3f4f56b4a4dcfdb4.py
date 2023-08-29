vocales=["a","e","i","o","u"]
def jerigonzo(string): 
    lista=list(string)
    for v in vocales:
        for i in range(0,len(lista)):
            if lista[i]==v:
                lista[i]=str(v)+"p"+str(v)
    snuevo="".join(lista)
    return snuevo  


if __name__ == "__main__": 
  s=input("Ingrese texto")   
  print(jerigonzo(s))
  

         