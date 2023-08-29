def numero_perfecto(x):
    divisores=[0]
    s=0
    for i in range(1,x):
        if x%i==0:
            divisores.append(i)
    for i in range(0,len(divisores)):
        s=divisores[i]+s
    print(s)
    if x==1:
        return True
    if s==x:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           