def rot13(palabra):
  palabrar=str(palabra)
  letra=palabrar.split()
  for letra in palabrar:
    palabrar.replace(letra,letra+13)
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           