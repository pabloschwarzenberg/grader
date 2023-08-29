saldoCajero = 1000000
saldoUsuario = 100000
bill20 = 20
bill10 = 40
bill5 = 40
usu = "10334151"
passw = "1803"
intentos = 0
salir = False

while intentos < 3:
 if salir == True:
  break
 usuario = input("Ingrese el usuario")
 clave = input("Ingrese la clave")
 if usuario == usu and passw == clave:
  while True:
    
   monto = eval(input("Ingrese el monto"))
   if monto > saldoUsuario:
    print("monto no permitido")
   else:
    saldoUsuario = saldoUsuario - monto
    retiro = 0
    auxlst = [0,0,0]
    while retiro < monto:
        if retiro+40001 < monto:
            retiro += 20000
            auxlst[0] += 1
        elif retiro +10001< monto:
            retiro += 10000
            auxlst[1] += 1
        elif retiro +5000 <= monto:
            retiro +=5000
            auxlst[2] += 1
        else:
            break
    bill20 -= auxlst[0]
    bill10 -= auxlst[1]
    bill5 -= auxlst[2]
    saldoCajero = saldoCajero - monto
    print("billetes 20000=", auxlst[0])
    print("billetes 10000=", auxlst[1])
    print("billetes 5000=", auxlst[2])
    print("saldo cuenta=", saldoUsuario)
    print("saldo cajero=", saldoCajero)
   opcion = input("Desea Salir Y/N")
   if not(opcion == "N"):
    salir = True
    break
     
 else: 
  print("clave invalida")
  intentos = intentos + 1
if intentos == 3:
 print("tarjeta bloqueada")