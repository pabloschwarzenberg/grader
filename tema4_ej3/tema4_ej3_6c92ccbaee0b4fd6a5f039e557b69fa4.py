def jerigonzo(Palabra):
    Palabra = Palabra.upper()
    Letras = []
    jeri = ""
    for I in range(len(Palabra)):
        if Palabra[I] == "A" or Palabra[I] == "E" or Palabra[I] == "I" or Palabra[I] == "O" or Palabra[I] == "U":
            Letras.append(Palabra[I] + "P" + Palabra[I])
        else:
            Letras.append(Palabra[I])
        jeri = jeri + Letras[I]
    return jeri.lower()
     
if __name__ == "__main__":
    Palabras = input("Ingrese el texto a traducir: ")
    H = jerigonzo(Palabras)
    print(H)