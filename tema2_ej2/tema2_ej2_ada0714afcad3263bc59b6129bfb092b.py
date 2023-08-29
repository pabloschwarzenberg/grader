# completa el código de la función
def amigos(a,b):
    division_del_numero_1=1
    division_del_numero_2=1
    suma_del_divisor_numero_1=0
    suma_del_divisor_numero_2=0
    while division_del_numero_1<a:
        if a%division_del_numero_1==0:
            suma_del_divisor_numero_1+=division_del_numero_1
        division_del_numero_1+=1
    while division_del_numero_2<b:
        if b%division_del_numero_2==0:
            suma_del_divisor_numero_2+=division_del_numero_2  
        division_del_numero_2 += 1
    if suma_del_divisor_numero_1==b and suma_del_divisor_numero_2==a:
        return True
    else:   
        return False
try:
    numero_1 = int(input("Numero 1: "))
    numero_2 = int(input("Numero 2: "))
    print(amigos(numero_1,numero_2))
except:
    print("Tienes que ingresar un numero")