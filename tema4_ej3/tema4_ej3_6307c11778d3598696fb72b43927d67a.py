def jerigonzo(texto):
    aux=""
    vocal= "aeiouAEIOU"
    for letra in texto:
        if letra not in vocal:
            aux+=letra
        else:
            aux+=letra+"p"+letra
    return aux
if __name__ == "__main__":
    tex = input("ingrese texto ")
    jer = jerigonzo(tex)
    print(jer)
