#Cajero Automático
caja=1000000
saldoI=100000
intentos=0
clave=1803
real=int(10334151)
salida="N"

while salida=="N" :
    usuario=int(input("Ingrese su usuario"))
    if real==usuario:
     ingresado=int(input("Ingrese la clave"))
     intentos+=1
     while ingresado!=clave and intentos<3:
        ingresado=int(input("clave invalida"))
        intentos+=1
        if intentos==3 and ingresado!=clave:
            print("tarjeta bloqueada")
            salida="s"
    
     if ingresado==clave:
       monto=int(input("Ingrese el monto a retirar"))
       while monto>100000:
         monto=int(input("monto no permitido"))
       if monto<=100000:
        cajero=1000000-monto
        cuenta=100000-monto
        print("saldo cuenta=",cuenta,sep="")
        print("saldo cajero=",cajero,sep="")
                  
       salida=input("ingrese N si desea continuar")


