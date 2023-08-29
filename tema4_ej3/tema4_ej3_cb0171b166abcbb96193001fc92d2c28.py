def es_vocal(texto):
    return texto in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def jerigonzo(texto):
    string =""
    for letra in texto:
        if not es_vocal(letra):
            string+=letra
        else:
            string+=letra+"p"+letra
    return string

if __name__ == "__main__":
    texto = input ("Ingresa el texto que quieres traducir a jerigonzo:")
    res = jerigonzo(texto)
    print(res)