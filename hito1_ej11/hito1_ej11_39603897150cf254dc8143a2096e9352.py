#Cajero Automático
monto_cajero=1000000
monto_banco=100000
intentos=3
clave_invalida=True
saldo_correcto=True
usuraio=True
intentos_1=3
positivo=True
positivo_1=True
positivo_2=True
n=0
r=0
q=0
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
            while positivo:
              if monto-20000>=0:
                n=n+1
                monto=monto-20000
                positivo=True
              else:
                positivo=False
                print("billetes 20000="+str(n))
            while positivo_1:
              if monto-10000>=0:
                r=r+1
                monto=monto-10000
                positivo_1=True
              else:
                positivo_1=False
                print("billetes 10000="+str(r))
            while positivo_2:
              if monto-5000>=0:
                q=q+1
                monto=monto-5000
                positivo_2=True
              else:
                positivo_2=False
                print("billetes 5000="+str(q))
            
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

