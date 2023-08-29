#Descomponer un número
num = int(input("Ingrese un numero de 4 digitos: "))
m = num // 1000
c = (num % 1000) // 100 
d = ((num % 1000) % 100) // 10
u = ((num % 1000) % 100) % 10




if num > 0 and num <= 9999:

 if m != 0 and c >= 0 and d >= 0 and u >= 0 :
  print(m,"M + ",c,"C + ",d,"D + ",u,"U")

 elif m == 0 :

  if m == 0 and c != 0:
   print(c,"C + ",d,"D + ",u,"U")

  if c == 0 and d != 0:
   print(d,"D + ",u,"U")

  if c == 0 and d == 0 :
    print(u,"U")
