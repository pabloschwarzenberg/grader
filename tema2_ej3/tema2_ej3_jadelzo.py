def numero_perfecto(numero):
    contador=1
    suma=0
    while contador!=numero:
        if numero%contador==0:
            suma=suma+contador
        contador=contador+1
    if suma==numero:
        return True
    else:
        return False
def numeroprimo(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

def sumaprimos(num): 
 
    for i in range(num): 
        m = 2**(i - 1) 
        if (numeroprimo(m)): 
            if (numero_pefecto(i) > num): 
                return perfect 
            perfect = numero_perfecto(i) 
 
    return perfect

if __name__ == "__main__":
    numero=eval(input("Ingrese su numero: "))
    if numero_perfecto(numero):
        print("El numero {0} es perfecto".format(numero))
    else:
        print("El numero {0} no es perfecto".format(numero))

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           