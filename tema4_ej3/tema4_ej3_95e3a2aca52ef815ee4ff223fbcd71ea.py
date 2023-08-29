def jerigonzo(palabra):
    palabra = list(palabra)
    longitud=len(palabra)

    vocal = ["a","e","i","o","u"]

    for i in range(0,longitud):
        if palabra[i] in vocal:
            lista = list(palabra[i])
            lista.append("p")
            lista.append(palabra[i])
            palabra[i] = "".join(lista) 
            
    palabra_final = ''.join(palabra)

    return palabra_final

if __name__ == "__main__":
    palabra=str(input("Ingrese una palabra"))
    resultado = jerigonzo(palabra)
    print(resultado)
