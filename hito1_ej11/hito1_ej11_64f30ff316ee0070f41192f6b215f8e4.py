Rut= 10334151
Clave =1803
Saldo_Cajero=1000000
Saldo_Cliente=100000

Billetes_20=0
Billetes_10=0
Billetes_5=0



Ingreso_Usuario=input("Ingrese Usuario: ")

#Ingreso_Clave=input("Ingrese Clave: ")

Intentos=1

while Intentos <=3:
       Ingreso_Clave = eval(input("Ingrese Clave: "))
       if Ingreso_Clave==Clave:
           break
       else:
           print('Clave Invalidad')
       Intentos=Intentos+1

if Intentos>3:
    print('tarjeta bloqueada')
else:
    Monto_Retiro = eval(input("Ingrese Monto Retiro: "))
    if Monto_Retiro<=Saldo_Cliente:
        Saldo_Cliente=Saldo_Cliente-Monto_Retiro
        Saldo_Cajero=Saldo_Cajero-Monto_Retiro
    else:
        print('monto no permitido')


    if Monto_Retiro>=20000:
        Billetes_20=Monto_Retiro//20000
        Monto_Retiro=Monto_Retiro%20000
    
    if Monto_Retiro>=10000:
        Billetes_10 = Monto_Retiro // 10000
        Monto_Retiro = Monto_Retiro % 10000
    
    if Monto_Retiro >= 5000:
        Billetes_5 = Monto_Retiro // 5000
        Monto_Retiro = Monto_Retiro % 5000
    

print('saldo cuenta=',Saldo_Cliente,' saldo cajero=',Saldo_Cajero)

print('billetes 20000= ',Billetes_20)
print('billetes 10000= ',Billetes_10)
print('billetes  5000= ',Billetes_5)