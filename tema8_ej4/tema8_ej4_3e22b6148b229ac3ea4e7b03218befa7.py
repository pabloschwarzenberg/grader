abc = "abcdefghijklmnopqrstuvwxyz"
def rot13(Palabra):
     rotu13 = 13
     clave = ""
     for letra in Palabra:
         suma = abc.find(letra) + rotu13
         modulo = int(suma)% len (abc)
         clave = clave + str(abc[modulo])
     return clave 

if name=="main":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print(resultado)  