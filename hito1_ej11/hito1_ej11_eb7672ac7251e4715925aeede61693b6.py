usuario="10334151"
clave="1803"

def validar_clave(usuario,clave_ingresada):
    if clave_ingresada==clave:
        return True
    else:
        print("clave invalida")
        return False
intentos=3
while intentos>0:
    usuario_ingresado=input("ingresa tu usuario: ")
    clave_ingresada=input("Ingresa tu clave: ")
    if not validar_clave(usuario_ingresado,clave_ingresada):
        intentos=intentos-1
    else:
        break
if intentos==0:
    print("tarjeta bloqueada")
monto=int(input("ingresa tu monto: "))
saldo_cuenta=100000-monto
saldo_cajero=1000000-monto
if 0<monto<100000:
    print("saldo cuenta",saldo_cuenta)
    print("saldo cajero",saldo_cajero)
else:
    print("monto no permitido")
a=monto//20000
b=monto//10000
c=monto//5000
while 0<a<20:
    if monto%20000==0:
        a=a+1
        print(a)
while 0<b<40:
    if monto%10000==0:
        b=b+1
        print(b)
while 0<c<40:
    if monto%5000==0:
        c=c+1
        print(c)
    

