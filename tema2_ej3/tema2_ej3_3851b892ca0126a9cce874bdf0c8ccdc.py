def numero_perfecto(a):

 suma = 0
 for i in range(1,a):
  if (a % (i) == 0):
   suma += (i)
 if a == suma:
  return True
 else:
  return False
_name=0
if _name=="main_":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))