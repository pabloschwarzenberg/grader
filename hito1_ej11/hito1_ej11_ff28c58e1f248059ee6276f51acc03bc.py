#Cajero Automático
def bills(c,x):
  billetes = c // x
  resto = c % x
  return billetes,resto

usr = int(input("Ingrese el usuario: "))
cla = int(input("Ingrese su clave: "))

iten = 1
scro = 1000000
susr = 100000
user = 10334151
passw = 1803

billetes_20 = 20000
billetes_10 = 10000
billetes_5 = 5000

while cla != passw:
  intentos += 1
   
  if cla == passw:
    print("clave incorrecta")
    break

  if iten > 3:

    break

  print("clave invalida")
  cla = int(input("Ingrese de nuevo su clave: "))

if iten > 3:
  print("tarjeta bloqueada")
if usr == user :

   
  if cla == passw:
    mon = int(input("¿Cuanto quiere retirar?: "))

     
    if mon > susr and mon > scro:
      print("monto no perimitido")
      
    else:

      susr -= mon
      scro -= mon
      b, r = bills(mon,billetes_20)
      c , r = bills(r , billetes_10)
      j , r = bills(r, billetes_5)

      print("saldo cuenta="+str(susr))
      print("saldo cajero="+str(scro))
      print("billetes20000="+str(b))
      print("billetes10000="+str(c))
      print("billetes5000="+str(j))
