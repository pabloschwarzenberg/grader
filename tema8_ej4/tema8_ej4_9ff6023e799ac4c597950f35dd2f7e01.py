def rot13(palabra):
    abc = "abcdefghijklmnopqrstuvwxyz"
    abc_list = list(abc)
    lista_palabra = list(palabra)
    posicion_letra = []
    palabra_rot13 = []
    for i in lista_palabra:
      posicion_letra_abc = abc.index(i)
      if posicion_letra_abc <= 12:
        numero_letra = (posicion_letra_abc + 13)
        posicion_letra.append(numero_letra)
      else:
        numero_letra = (posicion_letra_abc - 13)
        posicion_letra.append(numero_letra)
    for i in posicion_letra:
      letra_rot13 = abc[i]
      palabra_rot13.append(letra_rot13)
      resultado = "".join(palabra_rot13)
    return resultado
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           