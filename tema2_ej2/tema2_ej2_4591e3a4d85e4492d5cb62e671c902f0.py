def amigos(nro_1,nro_2):
    a=nro_1
    b=nro_2
    suma_1=0
    suma_2=0
    for p in range(1, nro_1):
        if nro_1 % p == 0:
            suma_1 = suma_1 + p
    for o in range(1, nro_2):
        if nro_2%o==0:
            suma_2=suma_2+o
    if (suma_1==b)and(suma_2==a):
        return True
    else:
        return False
suma_1=0
suma_2=0
try:
    nro_1= int(input("INGRESE EL PRIMER NUMERO: "))
    nro_2= int(input("INGRESE EL SEGUNDO NUMERO: "))
    if (nro_1 <= 0) or (nro_2 <= 0):
        print("INGRESE NUMEROS NATURALES")
    else:
        if amigos(nro_1,nro_2)==True:
            print("True")
        elif amigos(nro_1,nro_2)==False:
            print("False")
except:
    print("INGRESE NUMEROS NATURALES")

