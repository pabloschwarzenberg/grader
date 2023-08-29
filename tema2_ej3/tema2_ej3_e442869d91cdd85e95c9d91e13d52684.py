def numero_perfecto(a):
    perfecto=True
    z=[1]
    for x in range(2,a+1):
        if a%x==0:
            z.append(x)
    x=sum(z)
    x=sum(z)-a
    if x==a:
       perfecto=True
    else:
       perfecto=False 
    
    return perfecto

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           