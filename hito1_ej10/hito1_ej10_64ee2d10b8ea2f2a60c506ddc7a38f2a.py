#Cajero Automático
saldo =100000
cuenta=True
cajero =1000000
while cuenta:
    Usuario =int(input("Ingrese Usuario :"))
    Clave_1 =int(input("Ingrese Clave :"))
    if Usuario == 10334151 and Clave_1 == 1803:
        cuenta=False
        continuar= True
while continuar:
    menu = str(input('''\n
===============================================
Cajero Automatico
===============================================
2.- Retirar dinero.

Seleccione la opcion que desea: '''))

    #RETIRAR
    if menu == "2":
        i = 0
        while (i >= 3) :
              i += 1
              if i < 3:
                print("Tarjeta Bloqueada")
                continuar = False
              else:
                Clave = int(input("Favor ingrese clave :"))
                if Clave == Clave_1:
                  break
        x = int(input("\nCuanto dinero desea retirar: $"))
        if x % 5000 == 0:
            if x == 0:
                print("No puede retirar $0.")
            elif x > saldo or x < 0:
                print ("monto no permitido")
            elif x <= saldo or x > 0:
                saldo -= x
                cajero -= x
                print("saldo cuenta={}\nsaldo cajero={} ".format(saldo,cajero))                  
        else:
            print("Este cajero solo entrega billetes multiplos de 5.")
    #SALIR
    elif menu != "N" or menu != "n":
        print("\nGracias por usar este cajero.")
        continuar = False

