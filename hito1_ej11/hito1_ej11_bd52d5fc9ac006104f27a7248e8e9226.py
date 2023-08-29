saldo_inicial = 1000000
clave = "1803"
usuario = "10334151"
monto = 100000
veinte = 20
diez = 40
cinco = 40



def validar_clave(usuario_ingresado, clave_ingresada):
    if clave_ingresada == clave:
        print("Bienvenido")
        return True
    else:
        print("Clave Incorrecta")
        return False


intentos = 3
while intentos > 0:
    usuario_ingresado = input("Ingrese su usuario:")
    clave_ingresada = input("Ingrese su clave:")
    if not validar_clave(usuario_ingresado, clave_ingresada):
        intentos = intentos - 1
    else:
        break
if intentos == 0:
    print("Clave bloqueada")

else:
    respuesta = "N"
    while respuesta == "N":
        a = int(input("Monto a retirar:"))
        if a <= 100000:
            b = 1000000 - a
            c = 100000 - a
            print("Saldo cajero=", b)
            print("Saldo cuenta=", c)

            billetes = a

            z = billetes // 20000
            veinte-=z
            print("billetes 20000=" + str(z))

            billetes %= 20000

            o= billetes//10000
            diez-=o
            print("billetes 10000=" + str(o))

            billetes%=10000

            q=billetes//5000
            cinco-=q
            print('billetes 5000=' + str(q))

            respuesta = input(
                "Si desea realizar otra transacción ingrese letra N, de lo contrario ingrese letra diferente a N:")
            if respuesta != "N":
                print("Gracias por realizar la transacción")
        else:
            print("Monto no permitido")
