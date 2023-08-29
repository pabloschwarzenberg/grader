def numero_perfecto(a):
    divisor_de_A=0
    for i in range(1,a):
        if a%i==0:
            divisor_de_A=i+divisor_de_A
    if divisor_de_A==a:
        return True
    else:
        return False

if __name__=="__main__":
    sumatoria=0
    a=int(input("Ingrese variable a: "))
    print(numero_perfecto(a))
    nueva=int(input("Ingrese variable nueva: "))
    for i in range(1,nueva):
        if numero_perfecto(i)==True:
            sumatoria=i+sumatoria
    print(suma)
           