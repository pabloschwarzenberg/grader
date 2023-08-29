def rot13(palabra):
    abecedario="abcdefghijklmnopqrstuvwxyz"
    largo=len(abecedario)
    nueva=[]
    for letras in palabra:
      posicion=abecedario.index(letras) + 13
      if posicion>=largo:
        posicion-=largo
      letra=abecedario[posicion]
      nueva.append(letra)
    cadena="".join(nueva)
    return cadena

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           