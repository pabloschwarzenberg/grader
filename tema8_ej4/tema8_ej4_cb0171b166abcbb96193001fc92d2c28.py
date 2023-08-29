abc = "abcdefghijklmnopqrstuvwxyz"
def rot13(Palabra):
     rot13 = 13
     clave = ""
     for letra in Palabra:
         suma = abc.find(letra) + rot13
         modulo = int(suma)% len (abc)
         clave = clave + str(abc[modulo])
     return clave 

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print(resultado)

