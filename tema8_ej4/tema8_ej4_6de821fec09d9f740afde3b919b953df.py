
def rot13(palabra):
    letras1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    letras2 = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    cripto = []
    for i in palabra:
        if i in letras1:
            cripto.append(letras2[letras1.index(i)])
        elif i in letras2:
            cripto.append(letras1[letras2.index(i)])
    res="".join(cripto)        
    return res

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es:",resultado)