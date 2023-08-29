#Cajero Automático
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
print ("saldo cuenta=",saldo_cuenta)
print ("saldo cajero=",saldo_cajero)