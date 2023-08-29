def rot13(palabra):
   abc = "abcdefghijklmnopqrstuvwxyz"
   out_palabra = ""
   for char in palabra:
       out_palabra += abc[(abc.find(char)+13)%26]
   return out_palabra
   pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           