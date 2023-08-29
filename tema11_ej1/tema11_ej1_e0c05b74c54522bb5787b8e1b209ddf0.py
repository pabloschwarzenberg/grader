def palindromo(palabra):
    str_1=""
    contador = len(palabra) - 1
    while contador >= 0:
        str_1 += palabra[contador]
        contador -= 1
    if palabra == str_1:
        return True
    else:
        return False

if __name__ == "__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))

           