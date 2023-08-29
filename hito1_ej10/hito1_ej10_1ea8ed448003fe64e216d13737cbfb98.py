#Cajero Automático
dinero_cajero=1000000
sal_do_inicial=100000
sal_do=0
inten_tos=2

cla_ve=int(input("Ingrese su contraseña: "))

while inten_tos != 0:
    if cla_ve != 1803:
        print("CLAVE INVALIDA")
        inten_tos=inten_tos-1
        cla_ve=int(input("Ingrese su contraseña: "))
    else:
        mon_to = int(input("Ingresar monto que desea retirar(sin comas ni puntos): "))
        if mon_to < sal_do_inicial:
            sal_do=sal_do_inicial-mon_to
            dinero_cajero = dinero_cajero-mon_to
            print("Saldo Cuenta=", sal_do)
            print("Saldo Cajero=", dinero_cajero)
            break
        else:
            print("Monto NO Permitido")
if inten_tos==0:
    print("TARJETA BLOQUEADA")   