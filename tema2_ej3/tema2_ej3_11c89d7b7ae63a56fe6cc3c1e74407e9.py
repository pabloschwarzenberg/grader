def numero_perfecto(a):
  suma = 0
  for i in range(1,a):
    if (a % i == 0):
      suma += i
 
  if a == suma:
    return True
  else:
    return False

if "_name_" =="main_":
    a=int(input("ingrese a: "))
    print(numero_perfecto(a))