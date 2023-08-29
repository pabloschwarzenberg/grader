def rot13(palabra):
    abecedario="abcdefghijklmnopqrstuvwxyz"
    palabra_arreglada=""
    for i in range(len(palabra)):
      for j in range(len(abecedario)):
        k=j+13
        if palabra[i]==abecedario[j]:
          if k>25:
            palabra_arreglada+=abecedario[k-26]
          else:
            palabra_arreglada+=abecedario[k]
    return palabra_arreglada

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           