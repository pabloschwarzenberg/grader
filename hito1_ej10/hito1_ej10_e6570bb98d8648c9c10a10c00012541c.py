#Cajero Automático
Usuario_valido="10334151"
Clave_valida="1803"
Saldo_Cta=100000
Saldo_Cajero=1000000
Usuario_valido=input("Introduzca Su usuario:")
Error_Clave=1
Respuesta="S"
while Respuesta=="S" or Respuesta=="s":
    Clave=input("Introduzca Su Clave:")
    if Clave==Clave_valida :
            Monto=int(input("Ingrese el monto a Retirar:"))
            if Monto <= Saldo_Cta :
                   Saldo_Cajero-=Monto
                   Saldo_Cta-=Monto
                   print("saldo cuenta="+str(Saldo_Cta))
                   print("saldo cajero="+str(Saldo_Cajero))
            else :
                print("monto no permitido")
            Respuesta=input("Deseas Seguir procesando operaciones bancarias (S/N):")
            if Respuesta=="N" or Respuesta=="n" : break
    else :
        print("clave invalida")
        Error_Clave+=1
    if Error_Clave > 3 :
                  print("tarjeta bloqueada")
                  break      