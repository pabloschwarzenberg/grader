def rot13(palabra):
    resultado=""
    abecedario="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for i in palabra:
        a=abecedario.find(i)
        b=a+13
        c=abecedario[b]
        resultado+=c
    return(resultado)

    pass

if __name__=="__main__":
  palabra=input("Ingresa la palabra que quieras encriptar: ")
  palabra=palabra.lower()
  resultado=rot13(palabra)
  print("El resultado es: ",resultado)
