# completa el código de la función
def amigos(a,b):
    lista_1 = []
    for i in range(1,a):
        if a % i == 0:
            lista_1.append(i)
    lista_2 = []
    for x in range(1,b):
        if b % x == 0:
            lista_2.append(x)
    suma_1 = sum(lista_1)
    suma_2 = sum(lista_2)
    if (a == 1 or a == 2) or (b == 1 or b == 2):
       return False 
    if suma_1 == a or suma_2 == a:
        return True
    if suma_1 == b or suma_2 == b:
        return True
    else:
        return False
            
           