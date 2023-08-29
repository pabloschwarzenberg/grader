def amigos(a,b):
    divdenumero_1=1
    divdenumero_2=1
    sumadivnumero_1=0
    sumadivnumero_2=0
    while divdenumero_1<a:
        if a%divdenumero_1==0:
            sumadivnumero_1+=divdenumero_1
        divdenumero_1+=1
    while divdenumero_2<b:
        if b%divdenumero_2==0:
            sumadivnumero_2+=divdenumero_2
        divdenumero_2 += 1
    if sumadivnumero_1==b and sumadivnumero_2==a:
        return True
    else:
        return False
try:
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    print(amigos(numero1,numero2))
except:
    print("Por favor Ingrese un Número")