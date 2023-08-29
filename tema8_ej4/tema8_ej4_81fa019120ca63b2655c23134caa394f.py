def rot13(palabra):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in range(27):
      descifrado = ""
      for q in palabra:
        if q in abecedario:
          encri_letra = abecedario.index(q)
          nueva_encri = (encri_letra - i) % len(abecedario)
          descifrado += abecedario[nueva_encri]
        else: 
          descifrado += q
        pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           