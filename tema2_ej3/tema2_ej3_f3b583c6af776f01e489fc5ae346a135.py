def numero_perfecto(a):
  suma = 0
  for i in range(1,a):
    if (a % i == 0):
      suma += i
 
  if a == suma:
    return True
  else:
    return False
if __name__ == "__main__":   
 a = int(input("introduzca un numero:"))
             
 if numero_perfecto(a):
  suma = 0
  for i in range(1,a):
    if (a % i == 0):
      suma += i
 
  if a == suma:
   print("%s es un numero perfecto" % a)
 else:
   print("%s NO es un numero perfecto" % a)


           