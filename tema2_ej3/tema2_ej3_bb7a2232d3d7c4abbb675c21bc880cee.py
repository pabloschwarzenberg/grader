def numero_perfecto(a):
    return False
def numero_perfecto(a):
  suma = 0
  for i in range(1,a):
    if (a % i == 0):
      suma += i
 
  if a == suma:
    return True
  else:
    return False
if _name=="main_":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))

       