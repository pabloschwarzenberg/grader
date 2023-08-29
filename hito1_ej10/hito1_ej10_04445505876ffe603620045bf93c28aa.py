#Cajero Automático
usuario = int(input("ingrese el usuario:"))
clave = int(input("ingrese su clave:"))

intentos = 1
saldo_cajero = 1000000
saldo_usuario = 100000
user = 10334151
passw = 1803

while clave != passw:
 intentos += 1
 
 if clave == passw:
  print("clave incorrecta")
 break
  
if intentos > 3:
 clave = int(input("ingrese de nuevo su clave:"))
  
if intentos > 3:
   print("tarjeta bloqueada")
   
if usuario == user:
  
   if clave == passw:
   
    monto = int(input("¿cuanto quiere retirar?:"))
    
if monto > saldo_usuario and monto > saldo_cajero:
    
     print("monto no permitido")

else:
     saldo_usuario -= monto
     saldo_cajero -= monto
     print("saldo cuenta =" +str(saldo_usuario))
     print("saldo cajero =" +str(saldo_cajero))