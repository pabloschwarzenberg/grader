#Cajero Automático
Usser=10334151
Pass=1803
def login():
sesion= 3
  print("usuario")
  usuario= input()
  print("contraseña")
  contraseña= input()
Saldo = 1000000

print("\t.:MENU:.") 
print("1. Retirar dinero de la cuenta")
print("2. Salir")
opcion = int(input("elija la opción: ")

print()

if opcion==1:
  retirar = float(input("Cuanto dinero desea retirar de la cuenta -> "))
  if retirar>saldo:
    print("usted no tiene esa cantidad de dinero")
  else:
    saldo -= retirar
    print(f"dinero en la cuenta: {saldo}")
elif opcion==2
  print("gracias por utilizar su cajero automatico, que tenga un buen dia")
else:
  print("Error, intente nuevamente")
    