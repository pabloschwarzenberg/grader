# completa el código de la función
def amigos(num1,num2):
    lista1=[]
    lista2=[]
    suma1=0
    suma2=0
    for x in range(1,num1):
        if num1 % x == 0:
            lista1.append(x)
    for x in lista1:
        suma1 +=x
    for x in range(1,num2):
        if num2 % x ==0:
            lista2.append(x)
    for x in lista2:
        suma2 +=x
    if suma1 == num2 and suma2 == num1:
        print("Son números amigos")
        return 1
    else:
        print("No son números amigos")
        return 0