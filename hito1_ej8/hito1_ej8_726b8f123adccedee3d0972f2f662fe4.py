#Descomponer un número
print("Descomponedor de numeros a Unidades, Decenas, Centenas y Miles")
num = int (input ('Porfavor ingrese un numero: '))
if num > 9999:
  print("este no es un valor con el que funcione nuestro descomponedor, intente de nuevo...")
else:
  m = (num%10000-num%1000)//1000
  c = (num%1000-num%100)//100
  d = (num%100-num%10)//10
  u = num%10
  print(m, "M" "+", c, "C" "+", d, "D" "+", u, "U")
 