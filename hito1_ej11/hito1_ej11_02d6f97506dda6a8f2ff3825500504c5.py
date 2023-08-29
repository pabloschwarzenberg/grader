#Cajero Automático

billetes_20= 20
billetes_10= 40
billetes_5= 40

fondo_inicial= 1000000
saldo_incial_cliente= 100000
usuario= input ("Ingrese usuario:")

while usuario != "10334151":
    usuario= input ("Ingrese usuario correcto:")

intentos=1
clave =  input ("Ingrese clave:")

while clave != "1803":
    if intentos <3:
        print ("clave invalida")
        clave =  input ("Ingrese clave correcta:")
        intentos+=1
    elif intentos == 3:
        print ("tarjeta bloqueada")
        break


monto_retiro= int(input("Ingrese monto a retirar:"))
while (monto_retiro) > (saldo_incial_cliente):
    print ("monto no permitido")
    monto_retiro= int(input("Ingrese monto a retirar:"))  
saldo_cuenta= (saldo_incial_cliente) - (monto_retiro)
saldo_cajero= (fondo_inicial) - (monto_retiro)

cantidad_20= int (monto_retiro/20000)
cantidad_10 = int ((monto_retiro - (cantidad_20*20000))/ 10000)
cantidad_5 = int ((monto_retiro - (cantidad_20*20000)- (cantidad_10*10000))/ 5000)


print ("billetes 20000=",cantidad_20)
print ("billetes 10000=",cantidad_10)
print ("billetes 5000=",cantidad_5)
print ("saldo cuenta=",saldo_cuenta)
print ("saldo cajero=",saldo_cajero)