def numero_perfecto(a):
    suma_a=0
    for i in range(1,a):
        if a%i==0:
            suma_a+=i
    if suma_a==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           