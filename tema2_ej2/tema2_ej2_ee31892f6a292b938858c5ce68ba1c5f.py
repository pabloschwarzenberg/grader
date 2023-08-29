# completa el código de la función
def amigos(a,b):
    lista_1 = []
    lista_2 = []
    for i in range(1,a):
        if a % i == 0:               
            lista_1.append(i)
         
    for j in range(1,b):
        if b % j == 0:           
            lista_2.append(j)
         
    if sum(lista_1) == b and sum(lista_2) == a:
        return True

    else:
        return False