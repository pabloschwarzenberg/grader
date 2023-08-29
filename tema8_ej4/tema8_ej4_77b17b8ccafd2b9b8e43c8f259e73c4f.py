def rot13(palabra):
    abcdario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
    palabra_rot13 = ''
    for i in palabra:
      posicion = abcdario.index(i)+1 #0->1
      if(posicion < 13):
        palabra_rot13 = palabra_rot13+abcdario[posicion+13-1]
      else:
        palabra_rot13 = palabra_rot13+abcdario[posicion-13-1]
    return palabra_rot13
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           