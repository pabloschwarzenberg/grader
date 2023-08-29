def jerigonzo(string):
    jer=""
    for letra in string:
        if letra not in "AEIOUaeiou":
            jer+=letra
        else:
            jer+=letra+"p"+letra
    return jer
if __name__ == "__main__":
    palabra=input("Ingrese la palabra a tranformar: ")
    jerigonzo(palabra)
         