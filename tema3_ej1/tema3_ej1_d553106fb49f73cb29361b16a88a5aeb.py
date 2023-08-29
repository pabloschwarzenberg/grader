def suma_divisores(a):
    divisores=[1]
    if a==1:
        print(1) 
    for i in range(2,a+1):
        if a%i==0:
            divisores.append(i)
    return divisores
if __name__ == "__main__":
    a = int(input("ingrese numero: "))
    print(suma_divisores(a))
