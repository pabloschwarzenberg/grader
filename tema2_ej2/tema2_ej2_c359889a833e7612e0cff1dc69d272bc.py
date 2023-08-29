def amigos(a,b):
    div_a=[]
    for i in range(1,a+1):
        rest_a=a%i
        if rest_a==0:
            div_a.append(i)
    print("Los divisores de",a,"son: ",div_a)
    suma_a=0
    for i in div_a:
        suma_a=suma_a+i
    print("La suma de los divisores de",a,"es: ",suma_a)
    div_b=[]
    for n in range(1,b+1):
        rest_b=b%n
        if rest_b==0:
            div_b.append(n)
    print("Los divisores de",b,"son: ",div_b)
    suma_b=0
    for n in div_b:
        suma_b=suma_b+n
    print("La suma de los divisores de",b,"es: ",suma_b)
    if suma_a==suma_b and a!=b:
        return True
    else:
        return False
    
if __name__=="__main__":
    numero_1=int(input("Ingrese un número: "))
    numero_2=int(input("Ingrese otro número: "))
    print(amigos(numero_1,numero_2))
           