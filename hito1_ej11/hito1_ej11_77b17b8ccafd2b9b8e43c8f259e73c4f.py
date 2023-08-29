user = '10334151'
password = '1803'

saldo_cajero = 1000000
saldo_cuenta = 100000

cant_20 = 20
cant_10 = 40
cant_5 = 40


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
    monto = int(input("Cuando desea retirar: "))
    if(monto <= saldo_cajero and monto <= saldo_cuenta):
        if(monto % 5000 == 0):
            saldo_cuenta = saldo_cuenta - monto
            saldo_cajero = saldo_cajero - monto
            
            cant_20_m = monto // 20000
            
            resto = monto % 20000
            
            cant_10_m = resto // 10000
            
            resto = monto % 10000
            
            cant_5_m = resto // 5000
            
            print("saldo cuenta="+str(saldo_cuenta))
            print("saldo cajero="+str(saldo_cajero))
            
            if(cant_20_m > 0):
                print("billetes 20000="+str(cant_20_m))
                cant_20 = cant_20 - cant_20_m
            if(cant_10_m > 0):
                print("billetes 10000="+str(cant_10_m))
                cant_10 = cant_10 - cant_10_m
            if(cant_5_m > 0):
                print("billetes 5000="+str(cant_5_m))
                cant_5 = cant_5 - cant_5_m
        else:
            print("monto no permitido")
    else:
        print("monto no permitido")