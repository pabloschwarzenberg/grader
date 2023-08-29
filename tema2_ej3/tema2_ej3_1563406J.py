def numero_perfecto(a):
    x=0
    for i in range(1,a):
        if a%i==0:
            x=x+i
    if x==a:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("ingrese numero: "))
    print(numero_perfecto(a))
    w=1
    z=0
    while w<a:
        if numero_perfecto(w)==True:
            z=z+w
        w=w+1
    print("La suma de los numeros perfectos menores que ",a,":",z)