saldo_i=1000000 
while True:
    i=0
    while i<3:
      u=input()
        if u=="N":
            break
        if u=="10334151":
            cuenta=1000000
            clave=input()
            if clave=="1803":
                m=int(input("¿Cuanto desea retirar?: "))
                if m>saldo_i or m>cuenta:
                    print("monto no permitido")
                else:
                    saldo_i=saldo_i-m
                    cuenta=cuenta-m
                    print("saldo cuenta="+str(cuenta))
                    print("saldo cajero="+str(saldo_i))
            else:
                print("clave ivalida")
                i+=1
    if usuario=="N":
        break
    if i==3:
        print("tarjeta bloqueada")
        break 







