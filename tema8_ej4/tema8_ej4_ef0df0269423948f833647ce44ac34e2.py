def rot13(palabra):
  
    abc = "abcdefghijklmnopqrstuvwxyz"
    secret = "".join([abc[(abc.find(c) + 13) % 26] for c in palabra])
    pass
    return secret

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           