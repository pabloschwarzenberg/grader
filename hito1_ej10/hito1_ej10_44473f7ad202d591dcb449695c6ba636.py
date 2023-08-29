#Cajero Automático
midinero = 100000
cajero = 1000000
i = 1
user = int(input("Número de usuario: "))
clave = int(input("Clave: "))

while (user != 10334151 and clave != 1803):
    if(i < 3):
        i = i + 1
        print("Datos incorrectos \n intente nuevamente")
        user = int(input("Ingrese su número de usuario nuevamente:\n"))
        clave = int(input("Ingrese su clave nuevamente:\n"))
    else:
        print("tarjeta bloqueada")
       
if(user == 10334151 and clave == 1803):
        r = int(input("¿Cuánto dinero desea retirar? \n El saldo en su cuenta ha disposición es de $100000\n"))
        if(1000000 >= r):
            print("saldo cuenta=",midinero - r)
            print("saldo cajero=",cajero - r)