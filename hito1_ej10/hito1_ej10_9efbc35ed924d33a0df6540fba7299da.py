#cajero autom 1
saldoCajero=1000000
claveValida=1803
usuario=10334151
saldoCta=100000
respuesta="S"
errorclave=1
fuera=True


while (respuesta!="N" or respuesta!="n") and fuera:
    print("Saldo:",saldoCajero)
    if int(input("ingrese numero usuario: "))== usuario:
     True

     clave=int(input("Introduza clave:"))
     if clave==claveValida :
         
       montoRetiro = int(input("ingrese monto de retiro"))
       if int(montoRetiro) <= saldoCta:
            saldoCta-=int(montoRetiro)
            saldoCajero-=int(montoRetiro)
            print("saldo cuenta=",saldoCta,  "saldo cajero=",saldoCajero)
       else:
            print("No tiene suficiente dinero para retirar el monto ")
     else:
             print("clave invalida")
             errorclave+=1
             if errorclave > 3 :
              print("tarjeta bloqueada")
              fuera=False
    else:
        print("usuario incorrecto")

    respuesta=input("si deseas seguir preciona algo distinto a N,n :")        
     
