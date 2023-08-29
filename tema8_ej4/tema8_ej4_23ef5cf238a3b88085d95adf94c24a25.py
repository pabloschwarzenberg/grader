def rot13(palabra):
    codigo = ""
    abc= "abcdefghijklmnopqrstuvwxyz"
    abc1 = "nopqrstuvwxyzabcdefghijklm"
    for i in range(len(palabra)):
      p= abc.find(palabra[i])
      codigo = codigo + abc1[p]
    return codigo
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           