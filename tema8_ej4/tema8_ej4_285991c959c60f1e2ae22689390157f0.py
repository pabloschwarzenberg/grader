def rot13(palabra):
    lista=[]
    for i in palabra:
        x = rotarletra(i)
        lista.append(x)
    
    return "".join(lista)
  


def rotarletra(l):
    numero=ord(l)
    nf=((numero-97+13)%26)+97
    letra_final=chr(nf)
    return letra_final





if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
