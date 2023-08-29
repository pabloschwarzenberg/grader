#Cajero Automático
saldo_cajero=1000000
saldo_cuenta=100000
usuario="Numero de 8 digitos"
clave="Numero de 4 digitos"
print("Bienvenido")
usuario=(int(input("Ingrese su usuario: ")))
if usuario==10334151:
    clave=(int(input("Ingrese  clave: ")))
    if clave!=1803:
        print("Clave incorrecta")
    else:
        print("El saldo de su cuenta es:", saldo_cuenta)
        Monto=int(input("Ingrese monto a retirar: "))
        print("El saldo de su cuenta es: ", saldo_cuenta-Monto)