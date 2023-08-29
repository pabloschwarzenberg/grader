#Cajero Automático
dinero_cajero=1000000
cuenta_corriente=100000
usuario_valido= 10334151
clave_valida= 1803
bloqueo=0

usuario= int(input("Ingrese usuario: "))
clave=int(input("Ingrese clave: "))

while usuario!=usuario_valido:
        usuario=int(input("Ingrese el usuario valido: "))
while clave!=clave_valida:
        print("Clave invalida")
        clave=int(input("Ingrese clave: "))
        bloqueo=bloqueo+1
        if bloqueo>3:
            print("Tarjeta bloqueada")
            exit()
        else:
            bloqueo=bloqueo

if usuario==usuario_valido and clave==clave_valida:
    print("Saldo cuenta: " + str(cuenta_corriente))
    retirar=int(input("Digite el dinero a retirar: "))
    while retirar>cuenta_corriente:
        print("Monto no permitido")
        retirar=int(input("Digite dinero a retirar:"))
    saldo_cuenta= cuenta_corriente - retirar
    cuenta_corriente=saldo_cuenta
    dinero_cajero= dinero_cajero - retirar
  

print("saldo cuenta=" + str(cuenta_corriente))
print("Saldo cajero=" + str(dinero_cajero))