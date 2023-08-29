def numero_perfecto(a):
    divisores = [1]
    
    for i in range(2, a+1):
        if a%i == 0:
            divisores.append(i)
     
    return (sum(divisores)-a==a)

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           