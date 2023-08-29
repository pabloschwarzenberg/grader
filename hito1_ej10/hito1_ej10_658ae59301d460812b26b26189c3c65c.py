usuario = int(input("Ingrese su usuario: "))
usuario_correcto = int(10334151)
clave_correcto = int(1803)
saldo_cajero = int(1000000)
saldo_persona = int(100000)
contador_clave = 0
clave = 0
while clave != clave_correcto and contador_clave < 3:
    clave = int(input("Ingresa su clave: "))
    contador_clave = (contador_clave + 1)
    if clave != clave_correcto:
        print("clave invalida")
    if contador_clave == 3:
        print("tarjeta bloqueada")
else:
    if clave == clave_correcto and usuario == usuario_correcto:
        monto = int(input("Ingrese monto a retirar: "))
        while monto > saldo_persona:
            print("monto no permitido")
            monto = int(input("Ingrese monto a retirar: "))
        else:
            saldo_nuevo_persona = (saldo_persona - monto)
            saldo_nuevo_cajero = (saldo_cajero - monto)
            print("saldo cuenta=", saldo_nuevo_persona)
            print("saldo cajero=", saldo_nuevo_cajero)
            
