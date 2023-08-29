# completa el código de la función
def amigos(a,b):
    dv_nmb_1=1
    dv_nmb_2=1
    plus_dv_nmb_1=0
    plus_dv_nmb_2=0
    while dv_nmb_1<a:
        if a%dv_nmb_1==0:
            plus_dv_nmb_1+=dv_nmb_1
            print("Divisor de %d es: %d" % (a,dv_nmb_1),"la suma de los divisores es: ")
        dv_nmb_1+=1
    while dv_nmb_2<b:
        if b%dv_nmb_2==0:
            plus_dv_nmb_2+=dv_nmb_2
            print("Divisor de %d es: %d" % (b,dv_nmb_2),"la suma de los divisores es: ")
        dv_nmb_2+=1
    if plus_dv_nmb_1==b and plus_dv_nmb_2==a:
        return True
    else:
        return False
try:
    nmb_1=int(input("Numero 1: "))
    nmb_2=int(input("Numero 2: "))
    print(amigos(nmb_1,nmb_2))
except:
    print("Ingrese un numero:")