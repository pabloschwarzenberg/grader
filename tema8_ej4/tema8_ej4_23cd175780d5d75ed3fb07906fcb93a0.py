import string

def rot13(palabra):
    A="abcdefghijklmnopqrstuvwxyz"
    B="nopqrstuvwxyzabcdefghijklm"
    cambio=palabra.maketrans(A,B)
    return palabra.translate(cambio)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)