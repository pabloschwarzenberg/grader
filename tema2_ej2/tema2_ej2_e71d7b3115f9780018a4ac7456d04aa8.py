# completa el código de la función
def amigos(numero1,numero2):
    listanum1 = []
    listanum2 = []
    for x in range(1,numero1):
        resto1 = numero1%x
        if resto1 == 0 :
            listanum1.append(x)
    for y in range(1,numero2):
        resto2 = numero2%y
        if resto2 == 0 :
            listanum2.append(y)
    if sum(listanum1)==numero2 and sum(listanum2)==numero1:
        return True
    else:
        return False
           
           