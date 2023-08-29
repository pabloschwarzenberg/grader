#Cajero Automático
saldo_cajero=1000000
positivo=True
positivo_1=True
positivo_2=True
intentos=3
n=0
r=0
a=0
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
        while positivo:
            if retiro-20000>=0:
                n=n+1
                retiro=retiro-20000
                positivo=True
            else :
                positivo=False
                print("billetes 20000="+str(n))
                
        while positivo_1:
            if retiro-10000>=0:
                r=r+1
                retiro=retiro-10000
                positivo_1=True
            else :
                positivo_1=False
                print("billetes 10000="+str(r))
                
        while positivo_2:
            if retiro-5000>=0:
                a=a+1
                retiro=retiro-5000
                positivo_2=True
            else :
                positivo_2=False
                print("billetes 5000="+str(a))
                
    else:
        nuevo_monto>saldo_cajero
        print("monto no permitido")
      
 
else :
    print("tarjeta bloqueda")