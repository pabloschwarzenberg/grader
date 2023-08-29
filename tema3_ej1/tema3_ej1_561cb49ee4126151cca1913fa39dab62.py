# completa el código de la función
def suma_divisores(a):
    if a==1 or a==0:
       return a-1,False 
    elif a == 2:
       return 1,True
    elif a > 2:
        for divisor in range(2,a):
          if a % divisor == 0:
             return a-1,False
          elif a % divisor != 0 and divisor == a-1:
             return 1,True
def numero_perfecto(a):

 suma = 0
 for i in range(1,a):
  if (a % (i) == 0):
   suma += (i)
 if a == suma:
  return True
 else:
  return False
name = 0 
if name=="main":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
