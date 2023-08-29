#Cálculo del dígito verificador de un rut
rut = input("Ingrese rut: ")
x = len(rut)
valor = 0
verificadores = "765432"
y = len(verificadores)
while x>0:
  valor = int(rut[x-1])*int(verificadores[y-1]) + valor
  x = x - 1
  y = y - 1
a = (valor//11)
dv = 11 -(valor-(11*a))
if (dv==11):
    print("dv=", 0)
if (dv==10):
  print("dv=","K")
print("dv=",dv)