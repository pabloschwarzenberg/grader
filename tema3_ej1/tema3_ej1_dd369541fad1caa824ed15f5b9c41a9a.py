# completa el código de la función
def suma_divisores(n):
    divisores=[1]
    
    for i in range(2,n+1):
        if n%i==0:
            divisores.append(i)
    
    return sum(divisores)

numero=int(input("Ingrese numero: "))
resultado=suma_divisores(numero)
print(resultado)