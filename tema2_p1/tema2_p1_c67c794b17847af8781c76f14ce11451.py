def es_primo(numero):
    for i in range(numero):
        if numero%(i+1) == 0 and (i+1)!=1 and (i+1)!=numero:
            return "False"
    return "True"
        
def main():
    numero = int(input())
    verificacion = es_primo(numero)
    print("el numero", verificacion)
        
main()
def es_primo(n):
    fact = 1
    if n < 0:
        return 0
    elif n == 0:
        return 1
    while (n > 1):
        fact *= n
        n -= 1
    return fact

def main():
    numero = int(input("Escoge un numero: "))
    operacion = es_primo(numero - 1) + 1
    if operacion % numero == 0:
        return True
    else:
        return False

main()