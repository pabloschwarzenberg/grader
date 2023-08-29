def numero_perfecto(a):
    numero_perfecto=False
    suma_divisores_a=0
    for i in range(1,a):
        if a%i==0:
            suma_divisores_a=suma_divisores_a+i
    if suma_divisores_a==a:
        numero_perfecto=True
    return numero_perfecto

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    suma_perfectos=0
    for f in range (a+1):
        if numero_perfecto(f)==True:
            suma_perfectos=suma_perfectos+f
    print(suma_perfectos)


