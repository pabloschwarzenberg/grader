def rot13(palabra):
   abc = 'abcdefghijklmnopqrstuvwxyz'
   resultado = ''
   for letra in palabra:
       resultado += abc[(abc.find(letra)+13)%26]
   return resultado

if __name__ == "__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)        