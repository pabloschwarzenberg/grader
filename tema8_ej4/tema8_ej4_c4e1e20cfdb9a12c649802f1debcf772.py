def rot13(palabra):
    lista=[]
    for i in palabra:
      x=letra_rotada(i)
      lista.append(x)
    return "".join(lista)

def letra_rotada(l):  
    a=ord(l)
    numero_final=((a-97+13)%26)+97
    letra_final=chr(numero_final)
    return letra_final

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           