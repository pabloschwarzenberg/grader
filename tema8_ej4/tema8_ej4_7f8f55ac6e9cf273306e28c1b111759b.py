def rot13(palabra):
  palabra1=list(palabra)
  primeras_letras=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
  segundas_letras=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
  cambio=[]
  largo=len(palabra1)
  i=0
  k=0
  while i<largo:
    if palabra1[i]==primeras_letras[k]:
        cambio.append(segundas_letras[k])
        i+=1
        k=0
    elif palabra1[i]==segundas_letras[k]:
        cambio.append(primeras_letras[k])
        i+=1
        k=0
    else:
        k+=1
  cambio="".join(cambio)
  return cambio
  pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print(a)
                      