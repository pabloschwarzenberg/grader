# completa el código de la función
def amigos(a,b):
    if a==b:
      return False
    lista=[a,b]
    divisores_a= [x for x in range(1,a+1) if a%x==0]
    divisores_b= [x for x in range(1,b+1) if b%x==0]
    suma_a= 0
    suma_b=0
    for i in divisores_a:
        suma_a+=i
    for i in divisores_b:
        suma_b+=i
    if suma_a == suma_b:
        return True
    else:
        return False
    n = int(input("Ingrese un numero entero: "))

    primos=[2,3,5,7,11,13,17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    divisores=[]
    for i in primos:
        while n%i==0:
            divisores.append(i)
            n= n/i
            print(divisores)
