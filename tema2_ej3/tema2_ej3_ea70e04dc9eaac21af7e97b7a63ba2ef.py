def numero_perfecto(a):
    
    divisores=[-a]
    
    for i in range(1,a+1):
        if a%i==0:
            divisores.append(i)
    if sum(divisores)==a:
        return True
    else:
        return False
    pass

if __name__ == "__main__":
    
    b=int(input("Seleccion su divisor -> "))
    c=numero_perfecto(b)
    print(c)
    
    pass