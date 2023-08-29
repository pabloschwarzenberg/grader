def rot13(palabra):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    trans_table = str.maketrans(alfabeto + alfabeto.upper(), alfabeto[13:] + alfabeto[:13] + alfabeto[13:].upper() + alfabeto[:13].upper())
    return palabra.translate(trans_table)

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)

           