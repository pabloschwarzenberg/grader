def es_primo(numero):
    if numero % 2 == 0 and numero != 2:
        primo = False
    elif numero % 3 == 0 and numero != 3:
        primo = False
    elif numero % 5 == 0 and numero != 5:
        primo = False
    elif numero % 7 == 0 and numero != 7:
        primo = False
    elif numero % 11 == 0 and numero != 11:
        primo = False
    elif numero == 1:
        primo = False
    else:
        primo = True

    return primo


if __name__ == "__main__":
    valor = int(input("Ingrese un numero: "))
    print(es_primo(valor))

