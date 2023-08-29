# completa el código de la función
def amigos(numero,numero2):
    lista1=[]
    lista2=[]
    adicion=0
    adicion2=0
    for x in range(1,numero):
        if numero % x == 0:
            lista1.append(x)
    for x in lista1:
        adicion +=x
    for x in range(1,numero2):
        if numero2 % x ==0:
            lista2.append(x)
    for x in lista2:
        adicion2 +=x
    if adicion == numero2 and adicion2 == numero:
        print("Estos numeros son amigos")
        return 1
    else:
        print("Estos numeros no son amigos")
        return 0
        
        
