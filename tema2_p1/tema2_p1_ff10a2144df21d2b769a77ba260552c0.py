# por favor escribe aquí tu función
primos=[2,3,5,7,11,13,17,19,23,29,31,37,41,3,47,53]
def es_primo(n):
    for i in primos:
        division=n/i
        if division>i:
            return False
            break
        if division<i:
            return True
            break
if __name__ == "__main__":
    numero = input("Por favor ingrese un número: ")
    numero = eval(numero)
    print (es_primo(numero))