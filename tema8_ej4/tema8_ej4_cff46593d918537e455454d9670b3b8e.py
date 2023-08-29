def rot13(palabra):
  lista_abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  lista_palabra = list(palabra)
  for i in range(0,len(palabra)):
    a=lista_palabra[i]
    if lista_abc.index(a)<=12:
        b=lista_abc.index(a)+13
    else:
       b=lista_abc.index(a)-13
    lista_palabra[i]=lista_abc[b]
    palabra_nueva="".join(lista_palabra)
  return palabra_nueva
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           