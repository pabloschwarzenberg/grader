#Cajero Automático
import time
cuentau=100000
cajero=1000000
cont=0
x=0
z=0
y=0
print("*************************************")
print("               Cajero")
print("*************************************")
while x == 0:
    usuario=int(input("Ingrese Ususario: "))
    if usuario == 10334151:
        while z== 0:
            clave=int(input("Ingrese su Clave: "))
            if clave == 1803:
                while y ==  0:
                    montor=int(input("Cuanto desea retirar? :"))
                    if montor > cuentau:
                        print("No Tienes Saldo Suficiente, Intentalo Nuevamente")
                    else:
                        cuentau=cuentau-montor
                        cajero=cajero-montor
                        print("Saldo Cliente : ",cuentau)
                        print("Saldo Cajero : ",cajero)
                        
                        if cuentau > 0:
                            opcion=int(input("Desea Retirar mas Dinero? : 1.- Si 2.- No : "))
                            if opcion == 2:
                                y=1
                                x=1
                                z=1
                            else:
                                print("Cargando...")
                                time.sleep(5)
            else:
                print("Dato Invalido, Ingrese su Clave Nuevamente")
                cont=cont+1
                if cont == 3:
                    x=1
                    z=1
                    print("Su Clave ha Sido Bloqueada por superar los Intentos Permitidos")
    else:
        print("Dato Invalido, Ingrese su Usuario Nuevamente")
print("Saliendo...")
time.sleep(5)
