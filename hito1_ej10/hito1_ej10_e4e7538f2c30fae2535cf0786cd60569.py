#Cajero Automático
cajero = 1000000
cuenta = 100000
usuario = str(input("Ingrese el usuario: "))
while usuario != "10334151" :
   usuario = str(input("Ingrese nuevamente: "))
clave = str(input("Ingrese clave: "))
if clave != "1803" :
   print("clave invalida")
   clave = str(input("Ingrese clave: "))
   if clave != "1803" :
      print("clave invalida")
      clave = str(input("Ingrese clave: "))
      if clave != "1803" :
         print("Tarjeta bloqueada")
if clave == "1803" and usuario == "10334151" :
   retiro = eval(input("Ingrese monto a retirar: "))
   while retiro < 0 or retiro > cuenta:
      print("monto no permitido")
   if retiro > 0 and retiro <= cuenta:
      cuenta = cuenta-retiro
      cajero = cajero-retiro
      print("saldo cuenta={} \nsaldo cajero={}".format(cuenta,cajero))      