def rot13(palabra):
    import codecs
    a = codecs.encode(palabra, "rot_13")
    return a

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           