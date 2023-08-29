def rot13(palabra):
    string = ""
    for i in range(len(palabra)):
        if ord(palabra[i]) >=65 and ord(palabra[i]) <=77 or ord(palabra[i]) >=97 and ord(palabra[i]) <=109:
            string+= chr(ord(palabra[i])+13)
        elif ord(palabra[i]) >=78 and ord(palabra[i]) <=90 or ord(palabra[i]) >=110 and ord(palabra[i]) <=122:
            string+= chr(ord(palabra[i])-13)
    return string

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           