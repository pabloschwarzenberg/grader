def numero_perfecto(n):
    divisores=[]
    k=1
    for k in range(1,(n+1)):
        if n%k==0:
            divisores.append(k)
        else:
            divisores=divisores
    divisores.pop()
    suma=0
    for i in range(len(divisores)):
        suma=suma+int(divisores[i])
    if suma==n:
        return True
    else:
        return False
        
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           