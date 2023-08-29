cajero=1000000
cuenta=100000
passw=1803
contador=0

for x in range (0,4):
     usuario=input("ingrese su usuario: ")
     clave=input("ingrese su clave: ")
     if passw==clave:
        egreso=int(input("ingrese el monto a retirar: "))
        if 100000>=egreso>=0:
            print("saldo cuenta="+str(cuenta-egreso))
            print("saldo cajero="+str(cajero-egreso))
     elif passw!=clave:
         contador=contador+1
         if contador ==3:
             print("tarjeta bloqueada")
             quit()
         print("clave invalida")