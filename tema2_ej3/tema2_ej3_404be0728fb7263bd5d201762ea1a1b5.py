def numero_perfecto(a):
    suma1 = 0
    for i in range(1,a):
        if a % i == 0:
            suma1+=i
    if suma1 == a:
    
        return True
    else:
        return False

if __name__=="__main__":
    n1=int(input("Ingrese el primer numero: "))
    print(numero_perfecto(n1))
           