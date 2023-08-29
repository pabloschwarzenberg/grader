#Cajero Automático
      ##6_Cajero Automático nivel1:
saldo=1000
print("\t.:menu:")
print("1.-Ingresar dinero en la cuenta")
print("2.-Retirar dinero de la cuenta")
print("1.-Mostrar dinero disponible")
print("1.-salir")
opcion=int(input("digite una opcion del menu"))

print()
if opcion==1:
    extra=float(input("¿Cuanto dinero desea ingresar? ->"))
    saldo += extra
    print(f"Su dinero en la cuenta es de:${saldo}")
elif opcion==2:
    retirar=float(input("¿Cuanto dinero desea retirar? ->"))
    if retirar>saldo:
        print("saldo insuficiente:")
    else:
        saldo -=retirar
        print(f"\n dinero en la cuenta:{saldo}\n")
elif opcion==3:
    print(f"dinero en la cuenta:{saldo}")
elif opcion==4:
    print("Gracias por utilizar su cajero automatico")
else:
    print("Error,se equivoco de opcion de menu")