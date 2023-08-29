#Contestador de celular
print("hola, contesta o no contestar el telefono:")
nt = input("ingrese el numero telefonico:")
hll = int(input("hora de la llamada:"))
if hll>= 0 and hll<=7:
  print("contestar")
if hll > 7 and hll<= 14:
 if nt[5:] == "874":
   print("no contestar")
 else:
   print("no contestar")
if hll>= 17 and hll<= 19:
 if nt[0:3] == "682":
   print("contestar")
 else:
   print("no contestar")
if hll> 19:
   print("no contestar")