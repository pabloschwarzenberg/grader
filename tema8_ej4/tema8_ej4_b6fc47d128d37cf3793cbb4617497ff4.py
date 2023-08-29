def rot13(palabra):
  abc1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  abc13=["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
  lista=[]
  for i in range(len(palabra)):
    letra=palabra[i]
    numero=abc1.index(letra)
    n_letra=abc13[numero]
    lista.append(n_letra)
  alfa="".join(lista)
  return alfa
    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           