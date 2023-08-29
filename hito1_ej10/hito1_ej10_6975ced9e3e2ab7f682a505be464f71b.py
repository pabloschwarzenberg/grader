

sc=1000000 #saldo cajero
su=100000 #saldo usuario
intentos=3
while  intentos>0:
    a=int(input("ingrese usuario: "))
    b=int(input("ingrese clave: "))
    if a==10334151 and b==1803 and intentos>1: #si la clave es correcta
        m=int(input("ingrese monto a retirar: "))
        if m<=100000:                        #si el monto es correcto
            sc=sc-m                        #saldo cajedo
            su=su-m                        #saldo usuario
            print("saldo cuenta=",su, "saldo cajero=",sc)
            break
        elif m>100000:                      #si el monto no es correcto                   
            print ("monto no permitido") 
    elif not (a==10334151 and b==1803):
        intentos=intentos-1 
        print ("clave invalido")
    if intentos==0:
        print("tarjeta bloqueada.")
