def rot13(palabra):
    inicio = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final = "NOPQRSTUVWXYZABCDEFGHIJKLM"
    palabra_if = dict(zip(inicio + final, final + inicio))
    x = "".join(palabra_if.get(x.upper(), x) for x in palabra)
    return x.lower()
    pass

if __name__ == "__main__":
    palabra= input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("Tu palabra es: ", resultado) 