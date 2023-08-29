x=10334151
clave=1803
cajero=1000000
intento=0
while intento<3:
  usuario=int(input("Ingrese el usuario: "))
  cl=int(input("Ingrese la clave: "))
  if usuario == x and cl == clave:
    while intento <3:
       retiro = int(input("Ingrese el retiro de dinero: "))
       saldoi=100000
       resta= saldoi-retiro
       cj= cajero-retiro
       if(retiro>saldoi>0):
        print("Monto no permitido")
       else:
          print('saldo cuenta=' + str(resta))
          print('saldo cajero=' + str(cj))
          break
    break
  else:
    if(usuario != x or cl != clave):
      print("Clave invalida")
      intento+=1
    if intento == 3:
      print("Tarjeta Bloqueada")
      break
  