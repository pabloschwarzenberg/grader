#Cálculo del dígito verificador de un rut
rut = int(input("ingrese su rut:"))
n1 = (int(rut)//10000000) *3
n2 = (rut//1000000 - (rut//10000000)*10) *2
n3 = (rut//100000 - (rut//1000000)*10) *7
n4 = (rut//10000 - (rut//100000)*10) *6
n5 = (rut//1000 - (rut//10000)*10) *5
n6 = (rut//100 - (rut//1000)*10) *4
n7 = (rut//10 - (rut//100)*10) *3
n8 = (rut//1 - (rut//10)*10) *2
y = n1 + n2 +n3 + n4 + n5 + n6 + n7 + n8    
z = y // 11 
a = y - (11 * z)
cod = 11 - a
if cod == 10:
  print("dv=K")
elif cod == 11:
  print("dv=0")
else: 
  print("dv=",cod)