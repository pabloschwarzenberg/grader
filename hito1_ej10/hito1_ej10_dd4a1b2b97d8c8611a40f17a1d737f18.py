#Cajero Automático
saldo_cajero=1000000
intentos=3
monto=100000
clave_inválida=True
numero_usuario=True
print("Bienvenido")
numero_usuario=input("Ingrese numero de usuario: ")
clave=input("Ingresa clave: ")
while clave_inválida and intentos>1:
    if clave=="1803":
       clave_inválida=False
    
    else:
        intentos=intentos-1
        clave_inválida=True
        print("Clave inválida")
        clave=input("Reintente: ")
        
if clave=="1803" and numero_usuario=="10334151":
    retiro=input("Ingrese monto a retirar: ")
    retiro=int(retiro)
    nuevo_monto=monto-retiro
    nuevo_saldo=saldo_cajero-retiro
    if nuevo_monto<=saldo_cajero:
        saldo_cajero=saldo_cajero-monto
        print("saldo cuenta=",nuevo_monto)
        print("saldo cajero=",nuevo_saldo)
    else:
        nuevo_monto>saldo_cajero
        print("monto no permitido")
      
 
else :
    print("tarjeta bloqueda")