Usuario_valido="10334151"
Clave_valida="1803"
Saldo_Cta=100000
Saldo_Cajero=1000000
Error_Clave=1
Respuesta="S"
Tarjeta_Bloqueada=False
Usuario_valido=input("Introduzca Su usuario:")
while (Respuesta=="S" or Respuesta=="s") and not Tarjeta_Bloqueada:
    Error_Clave=1
    while True :
        Clave=input("Introduzca Su Clave:")
        if Clave!=Clave_valida :
            print("clave invalida")
            Error_Clave+=1
        else :
            break
        if Error_Clave > 3 :
              print("tarjeta bloqueada")
              Tarjeta_Bloqueada=True
              break
    if not Tarjeta_Bloqueada :
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
