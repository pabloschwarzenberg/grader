def jerigonzo(string):
    almacenador=""
    vocal=["a","e","i","o","u"]
    string.lower()
    for letra in string:
        if letra in vocal:
            almacenador+=letra
            # añadir la letra "p" despues de la vocal
            almacenador+="p"
        almacenador+=letra

    return almacenador

if __name__ == "__main__":
    ingreso=input("Por favor ingrese una palabra: ")
    print(jerigonzo(ingreso))