intentos=3

while intentos>=1:
   usuario=int(input("usuario:"))
   clave=int(input("ingrese su clave:"))

   if usuario==10334151 and clave==1803:
      print("tienes 100.000 en tu cuenta")
      
      monto=int(input("ingresar monto a retirar"))
      saldo_cuenta=100000
      saldo_cajero=1000000
      if saldo_cuenta>0 and saldo_cajero>0:
         if saldo_cuenta>monto:
            saldo_cuenta = saldo_cuenta-monto
            saldo_cajero = saldo_cajero-monto
         elif saldo_cuenta==monto:
            saldo_cuenta = saldo_cuenta-monto
            saldo_cajero= saldo_cajero-monto
         else:
            print("no tienes saldo suficiente para retirar dinero")
      
      
else:
      intentos=intentos-1
      print("clave o usuario incorrecto")


      