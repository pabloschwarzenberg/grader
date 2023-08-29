user = '10334151'
password = '1803'

saldo_cajero = 1000000
saldo_cuenta = 100000

n_intento = 1
max_intento = False
pass_valida = False
n = "A"

user_input = str(input("ingrese su usuario: "))
while not user_input == user:
  user_input = str(input("ingrese su usuario: "))

pass_input = input("ingrese password del usuario: ")
n_intento = 1
while not pass_input == password:
  if(n_intento < 3):
    pass_input = input("clave invalida intento"+str(n_intento)+" de 3: ")
    n_intento +=1
  else:
    max_intento = True
    print("clave bloqueada")
    break

if(not max_intento):
    monto = int(input("Cuando desea retirar"))
    if(monto < saldo_cajero and monto < saldo_cuenta):
        saldo_cuenta = saldo_cuenta - monto
        saldo_cajero = saldo_cajero - monto
        print("saldo cuenta="+str(saldo_cuenta))
        print("saldo cajero="+str(saldo_cajero))
    else:
        print("monto no permitido")