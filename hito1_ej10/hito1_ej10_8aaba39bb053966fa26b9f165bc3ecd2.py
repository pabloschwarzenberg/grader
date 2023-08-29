#Cajero Automático
Usuario=int(input("Ingresa nuemero de usuario: "))
Numerodeusuario="10334151"
Montousuario=100000
Montocajero=1000000
Clave="1803"
intentos=3
clave_valida=False
while intentos!=0 and not clave_valida:
    clave=input("Por favor ingresa tu clave: ")
    if len(clave)!=4:
        print("Ingrese una clave de 4 digitos")
        continue
    if clave!=Clave:
        print("La clave ingresada no es correcta")
        intentos=intentos-1
    else:
        print("Bienvenido")
        clave_valida=True
if intentos==0:
    print("Su tarjeta ha quedado bloqueada")

Montoaretirar=int(input("Ingresa monto a retirar:"))
if Montoaretirar> 100000 or Montoaretirar<0:
    print("Monto no valido",Montoaretirar) 
else:
    print("Monto valido",Montoaretirar) 
Nuevosaldo=0
Nuevosaldo= Montousuario - Montoaretirar
Saldo_cajero=0
Saldo_cajero=Montocajero-Montoaretirar
print("Saldo cuenta=",+Nuevosaldo,",","Saldo cajero= ",+Saldo_cajero)