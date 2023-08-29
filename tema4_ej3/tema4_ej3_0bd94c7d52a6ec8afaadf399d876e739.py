vocales = list("aeiouáéíóú")
def jerigonzo(string):
    j = 0
    while j < 1:
        a = list(string)
        for i, c in enumerate(a):
            if string[i] in vocales:
                posicion = i
                caracter = c
                a[posicion] = str(a[posicion] + "p" + caracter)
            j += 1
    palabra = "".join(a)
    return palabra

if __name__ == "__main__":
    string = input("ingrese su palabra: ")
    print(jerigonzo(string))
         