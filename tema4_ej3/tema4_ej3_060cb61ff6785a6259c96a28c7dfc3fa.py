def jerigonzo(string):  # Despues de cada vocal, se repite la p y la vocal
    resultado = ''
    for char in string:
        if char.lower() == 'a':
            resultado += 'apa'
        elif char.lower() == 'e':
            resultado += 'epe'
        elif char.lower() == 'i':
            resultado += 'ipi'
        elif char.lower() == 'o':
            resultado += 'opo'
        elif char.lower() == 'u':
            resultado += 'upu'
        else:
            resultado += char
    return resultado


if __name__ == "__main__":
    palabra = input('Ingrese una palabra: ')
    print(jerigonzo(palabra))

         