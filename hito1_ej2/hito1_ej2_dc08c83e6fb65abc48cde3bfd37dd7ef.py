#Contestador de celular
numero=int(input())
numero_final=(numero%10000000)%1000000%100000%10000%1000
hora=int(input())
if 7>=hora>=0:
    print("CONTESTAR")
if 7<hora<14:
    if numero_final==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if 19>=hora>=17:
    if 87600000<numero<87800000:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if 19<hora:
    print("NO CONTESTAR")
     