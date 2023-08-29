#Cajero Automático
monto_cajero=1000000
monto_banco=100000
intentos=3
clave_invalida=True
saldo_correcto=True
usuraio=True
intentos_1=3
print("Bienvenido a Banco Matias")
usuario=input("Ingrese usuario:")
clave=input("Ingrese su clave:")
while clave_invalida and intentos>1 and usuario:
    if clave=="1803" and usuario=="10334151":
        clave_invalida=False
        usuario=False
    else:
        intentos=intentos-1
        clave_invalida=True
        usuario=False
        print("clave invalida")
        clave=input("Reintente:")
            
if clave=="1803":
    monto=input("Ingrese monto:")
    monto=int(monto)
    while saldo_correcto and intentos_1>1:
        print("saldo cajero=",monto_cajero-monto )
        if monto<=monto_banco:
            monto_banco=monto_banco-monto
            print("saldo cuenta=",monto_banco)
            saldo_correcto=False
            
        else:
            intentos_1=intentos_1-1
            saldo_correcto=True
            print("monto no permitido")
            monto=input("Intente con otro monto:")
            monto=int(monto)
            
            
    recibo=input("¿Desea recibo?")
    if recibo.lower()=="si":
            print("Imprimiendo recibo")
    if recibo.lower()=="no":
            print("Muchas gracias")
    
            
else:
    print("tarjeta bloqueada")
