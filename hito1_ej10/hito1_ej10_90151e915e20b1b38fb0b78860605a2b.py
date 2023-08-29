#Cajero Automático
c = 100000
ca = 1000000
u = int(input("ingrese su usuario : "))
if u == 10334151:
   x = int(input("ingrese su contraseña : "))
   
if x == 1803:
     m = int(input("ingrese monto a retirar : "))
     print("saldo cuentas =", c-m)
     print("saldo cajero =", ca-m)     