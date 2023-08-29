def numero_perfecto(a):
    contador=0

    for i in range(1,a):
        if a%i==0:
            contador+=i

    if contador==a:
        return True
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           