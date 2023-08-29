def es_vocal(texto):
    return texto in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
def jerigonzo(texto):
    aux=""
    for letra in texto:
        if not es_vocal(letra):
            aux+=letra
        else:
            aux+=letra+"p"+letra
    return aux
if __name__=="__main__":
    a=input("Ingrese a: ")
    print(jerigonzo(a)) 