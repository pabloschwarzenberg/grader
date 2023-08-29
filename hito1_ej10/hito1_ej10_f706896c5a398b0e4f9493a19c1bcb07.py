#Cajero Automático
b=1000000
k=100000
i=0
while b>0 and k>0 :
    u=int(input("Ingrese tu usario: "))
    while u!=10334151:
        print("Usario no registrado")
        u=int(input("Ingrese tu usario: "))
    if u==10334151 :
        while i!=3 : 
            c=int(input("Ingrese tu clave: "))
            if c==1803 :
                i=3
            else:
                print("Calve invalida")
                i+=1
                if i==3 and c!=1803 :         
                    print("trajeta bloqueado")
                    break
        m=int(input("Ingrese monto deseado: "))
        while m>k or m>b:
            print("Monto no permitido")
            m=int(input("Ingrese monto deseado: "))
    k=k-m
    b=b-m
    print("Saldo cuenta=",k)
    print("Saldo cajero=",b)
    cont=input("Para salir ingresa algo destinto de N: ")
    if cont!="N" :
        break