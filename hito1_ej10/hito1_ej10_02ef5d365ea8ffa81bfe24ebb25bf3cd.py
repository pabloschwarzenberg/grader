import time

saldo_cajero = 1000000
saldo_usuario = 100000

usuario = '10334151'
clave = '1803'

intentos = 0

usuario_input = input("Por favor ingrese su usuario: ")
clave_input = input("Por favor ingrese su clave: ")

while clave_input != clave:
    if intentos >= 2:
        print("Tarjeta bloqueada")
        while True:
            time.sleep(5)



    print("Clave invalida")
    intentos += 1
    clave_input = input("Por favor ingrese su clave: ")


monto_input = int(input("Por favor indique el monto a retirar: "))

if monto_input > saldo_cajero:
    print("Monto no permitido.")

else:
    saldo_usuario -= monto_input
    saldo_cajero -= monto_input

print("saldo cuenta=", saldo_usuario)
print("saldo cajero=", saldo_cajero)