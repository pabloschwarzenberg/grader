# completa el código de la función
def suma_divisores(a):
    condPrimo = a%2==1
    if(a==1):
        condPrimo = False
    valor = 0
    x = a
    contador = a - 1
    
    while(contador>0):
        if(x%contador == 0):
            valor = valor + contador
        contador = contador - 1
        
    return (valor,condPrimo)

if __name__ == "__main__":
    numero = int(input("-: "))
    resultado = suma_divisores(numero)
    print(resultado)
