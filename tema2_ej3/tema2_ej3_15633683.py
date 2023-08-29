def numero_perfecto(a):
    suma=1
    if a==1:
        return True
    else:
        for i in range (2,a):
            if a%i==0:
                suma+=i
        if suma==a:
            return True
        else:
            return False
if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))
    suma_perfectos= 0
    for i in range (1,a):
        if numero_perfecto(i)==True:
            suma_perfectos += i
    print(suma_perfectos)
