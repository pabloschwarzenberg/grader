cajero = 1000000
cuenta = 100000
billetes20 = 20
billetes10 = 40
billetes5 = 40
valorb20= 20000
valorb10 = 10000
valorb5 = 5000
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
       cantidad = retiro
       cantidad20 = cantidad // valorb20
       resto20 = cantidad % valorb20
       cantidad10 = resto20 // valorb10
       resto10 = resto20 % valorb10
       cantidad5 = resto10 // valorb5
       resto5 = resto10 % valorb5
       cuenta = cuenta-retiro
       cajero = cajero-retiro
       suma_billetes = cantidad20 * 20000 + cantidad5 * 5000 + cantidad10 * 10000
       print("saldo cuenta={} \nsaldo cajero={}".format(cuenta,cajero))
       print("", suma_billetes)
       print("billetes 20000={} \nbilletes 10000={} \nbilletes 5000={}".format(cantidad20,cantidad10,cantidad5))
