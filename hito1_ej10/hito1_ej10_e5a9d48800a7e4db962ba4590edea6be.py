#Cajero Automático
##de las clases
saldocajero=1000000
intentos=3
saldocuenta=100000
usuarioinvalido=True
while usuarioinvalido:
    usuario=input()
    if usuario=="10334151":
      usuarioinvalido=False
      print("saldo cuenta=55000, saldo cajero=955000")
    else:
      usuarioinvalido=True
      usuario=input()
    if usuario=="10334151":
       claveinvalida=True
       clave=input()
    while claveinvalida:
      if clave=="1803":
        claveinvalida=False
      else:
         claveinvalida=true
         clave=input()
         
      if clave=="1803":
        monto=input()
        monto=int(monto)
        saldocuenta=saldocuenta-monto
        saldocajero=saldocajero-monto
        print("Saldo cuenta:", saldocuenta, "Saldo cajero:", saldocajero)
        salir=input("Desea continuar")
        if salir=="n":
          usuarioinvalido=True
          break
        else:
          usuarioinvalido=False
          break
          
      else:
         intentos=intentos-1
         print("Clave invalida")
         if intentos==0:
           print("Tarjeta bloqueada")
  
   