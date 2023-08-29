def rot13(palabra):
 abc = "abcdefghijklmnopqrstuvwxyz"
 cifrado=""
 n = 13
 for l in palabra:
   if l in abc:
     pos_letra = abc.index(l)
     nueva_pos = (pos_letra + n) % len(abc)
     cifrado+= abc[nueva_pos]
   else:
     cifrado+= l
 return cifrado
if __name__ == "__main__":
 palabra=input("Ingresa la palabra que quieras encriptar: ")
 palabra.lower()
 resultado= rot13(palabra)
 print("El resultado es: ", resultado)