"""
Encriptador ROT13
"""

L1 = "abcdefghijklm"
L2 = "nopqrstuvwxyz"

def rot13(palabra):
    codificado = []
    for i in palabra:
        if i in L1:
            cifra = L1.find(i)
            i = L2[cifra]
            codificado.append(i)
        elif i in L2:
            cifra = L2.find(i)
            i = L1[cifra]
            codificado.append(i)

    mensaje = "".join(codificado)
    return mensaje

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)

           