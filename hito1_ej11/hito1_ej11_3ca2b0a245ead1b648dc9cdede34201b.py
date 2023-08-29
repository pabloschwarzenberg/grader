#Cajero Automatico
#Entrada
clave=int(input("Introdzca su clave: "))
saldoCajero=1000000
saldoCuenta=100000
billetesDe20= 20
billetesDe10= 40
billetesDe5= 40

i=1
while clave!= 1803 and i<3:
    clave=int(input("Clave incorrecta, intente nuevamente: "))
    i=i+1
    if clave != 1803 and i==3:
        print("Tarjeta Bloqueada")
i=3
retiro= int(input("Introduzca el monto que desea retirar: "))
if retiro <= saldoCuenta:
    saldoCuenta= saldoCuenta - retiro
    print("Saldo cuenta=", saldoCuenta)
    
    saldoCajero= saldoCajero - retiro
    print("Saldo cajero=", saldoCajero)
    

    if retiro % 20000==0:
        billetesDe20= retiro // 20000
        resto= retiro % 20000
        billetesDe10= (resto % 20000)//10000
        billetesDe5= (resto % 20000)//5000
        print("billetes 20000=" + str(billetesDe20))
        print("billetes 10000=" + str(billetesDe10))
        print("billetes 5000=" + str(billetesDe5))

    else:
        billetesDe20= retiro // 20000
        resto= retiro % 20000
        if resto % 10000==0:
            billetesDe10= resto // 10000
            billetesDe5= (resto %  10000) // 5000
            print("billetes 20000=" + str(billetesDe20))
            print("billetes 10000=" + str(billetesDe10))
            print("billetes 5000=" + str(billetesDe5))
            
        else:
            billetesDe10= resto // 10000
            resto= resto % 10000
            billetesDe5= resto // 5000
            print("billetes 20000=" + str(billetesDe20))
            print("billetes 10000=" + str(billetesDe10))
            print("billetes 5000=" + str(billetesDe5))       
        
else:
    print("Monto no permitido")