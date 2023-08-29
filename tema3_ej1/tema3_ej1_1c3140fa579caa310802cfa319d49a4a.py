# completa el código de la función
def suma_divisores(a):
    suma=0
    for i in range(1,a):
        if a % i==0:
            suma +=i
    primo=(suma==1)
    return suma, primo
    
if __name__ == '__main__':
    numero=int(input('Ingrese un numero: '))
    suma,primo=suma_divisores(numero)
    print('La suma de los divisores es:', suma)
    if primo:
        print('El numero es primo')
    else:
        print('El numero no es primo')