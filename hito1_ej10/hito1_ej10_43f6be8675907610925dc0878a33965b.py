#Cajero Automático
def ValidarClave(clave):
  if clave=="1803":
    return True
  else:
    return False

saldo_cajero=1000000
usuario=input("Ingresar usuario:")
clave=input("Ingresar clave:")
intentos=0
ValidarClave(clave)
while intentos==3 or ValidarClave(clave)==True:
    intentos=intentos+1
    if ValidarClave(clave)==False:
        clave=input("Por favor vuelve a intentarlo")
    if intentos==3:
        print("tarjeta bloqueda")
if ValidarClave(clave)==True:
    if usuario=="1033411":
        monto=100000
        retiro=int(input("Cuanto deseas retirar:"))
        if retiro<monto:
            a=monto-retiro
            b=saldo_cajero-retiro
            print("saldo cuenta:",a)
            print("saldo cajero:",b)

