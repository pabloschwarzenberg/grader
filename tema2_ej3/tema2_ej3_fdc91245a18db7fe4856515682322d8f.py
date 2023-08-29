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

if __name__ == "__main__":
    numero=eval(input("Ingrese su numero: "))
    if numero_perfecto(numero):
        print("El numero", numero, " es perfecto"(numero))
    else:
        print("El numero", numero, " no es perfecto"(numero))