def rot13(palabra):
    Lista_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    Lista_2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Encriptado = ""
    for Letra in palabra:
      if Letra in Lista_1:
        Posicion = Lista_1.index(Letra)
        Encriptado = Encriptado + Lista_2[Posicion]
      if Letra in Lista_2:
        Posicion = Lista_2.index(Letra)
        Encriptado = Encriptado + Lista_1[Posicion]
    return Encriptado
   


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           