#Aprobación de créditos
print("----------------Ingrese su rut----------------")
rut = input()
print("----------------Ingrese la clave----------------")
clave = input()
print("----------------SELECCIONE TIPO DE CUENTA----------------")
print("1: Cuenta corriente")
print("2: Cuenta vista")
print("3: Cuenta ahorro")
print("4: Cuenta CHQ")
#escojer variable del saldo actual
escogido=int(input("Ingrese el numero de la opcion\n"))
if escogido==1:
    print("----------------Tu Saldo es de $50.000CLP----------------")
    print("----------------Eliga las Opciones----------------")
    print("1: Retiro")
    print("2: Pago")
    print("3: Transferencia")
    print("4: Depositos")
    escogido=int(input("Ingrese el numero de la opcion\n"))
    if escogido==1:
        print("----------------ingrese el monto que quieres retirar----------------")
        print("""
1:$10.000          2:$20.000

3:$40.000          4:$50.000""")
        escogido=int(input("Ingrese el numero de la opcion\n"))
        if escogido==1:
            print("----------------Elegiste la suma de $10.000CLP----------------")
            print("----------------Quieres continuar----------------")
            print("si")
            print("no")
            if escogido=="si":
                print("----------------Desea boleta----------------")
                print("si")
                print("no")
                if escogido=="si":
                    print("Gracias por elegir BANCO_TE_ROBAMOS")      