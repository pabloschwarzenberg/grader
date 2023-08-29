#Cajero Automático
billVeinte=20000
billCuarenta=10000
billCuar=5000
caja=billVeinte*20+billCuarenta*40+billCuar*40
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
       if monto<=saldoI:
          darVeinte=monto//20000
          monto2=monto-(darVeinte*20000)
          darCuarenta=0
          darCuatr=0
          darCuarenta=monto2//10000
          monto3=monto2-(darCuarenta*10000)
          darCuatr=monto3//5000
          total=monto3-(darCuatr*5000)

          saldoF=saldoI-monto
          cajero=caja-(monto)
          print("saldo cuenta=",saldoF,sep="")
          print("saldo cajero=",cajero,sep="")
          print("billetes 20000=",darVeinte)
          print("billetes 10000=",darCuarenta)
          print("billetes 5000=",darCuatr)
          salida=input("ingrese N si desea continuar")      