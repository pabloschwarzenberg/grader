def rot13(palabra):
    codigo = "nopqrstuvwxyzabcdefghijklm"
    abc =    "abcdefghijklmnopqrstuvwxyz"
    resultado=""
    for i in palabra:
      count=0
      for c in abc:
        if i == c:
          resultado = resultado + codigo[count]
        count+=1
    return resultado      

    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)