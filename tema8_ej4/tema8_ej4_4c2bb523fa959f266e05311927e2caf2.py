def rot13(palabra):
    encr=len(palabra)
    for i in range (0,encr):
       for pos in range(0,26):
          if palabra [i] == abc[pos]:
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           