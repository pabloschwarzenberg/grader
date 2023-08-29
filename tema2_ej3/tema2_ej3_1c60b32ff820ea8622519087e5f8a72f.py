def numero_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    numero_p = False
    if suma == numero:
        numero_p = True
    return numero_p
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           