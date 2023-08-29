abc = "abcdefghijklmnopqrstuvwxyz"
def rot13(Palabra):
     rot13 = 13
     clav = ""
     for letra in Palabra:
         su = abc.find(letra) + rot13
         modulo = int(su)% len (abc)
         clav = clav + str(abc[modulo])
     return clav 

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    res=rot13(palabra)
    print(res)