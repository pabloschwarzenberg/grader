def cambiar_letra(letra):
  abcedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  po=abcedario.index(letra)
  if 0<=po<13:
    return (abcedario[po+13])
  if 12<po<26:
    return (abcedario[po-13])

def rot13(palabra):
    lista=list(palabra)
    n=0
    while n<len(lista):
      lista[n]=cambiar_letra(lista[n])
      n=n+1
    pf="".join(lista)
    return pf
  

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           