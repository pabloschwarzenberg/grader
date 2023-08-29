#Descomponer un número
n = int(input("ingrese numero: "))

if 1000 <= n <= 9999:
  m = n//1000
  c = (n - m*1000)//100
  d = ((n - m*1000)- c*100)//10
  u = ((n - m*1000)- c*100)-d*10
  print(m,"M+",c,"C+",d,"D+",u,"U")

elif 100 <= n <= 999:
  c = n//100
  d = (n - c*100)//10
  u = (n - c*100)-d*10
  print(c,"C+",d,"D+",u,"U")

elif 10 <= n <= 99:
  d = n//10
  u = n - d*10
  print(d,"D+",u,"U")

elif 0 < n <= 9 :

  print(n, "U")

else:
  print("Número no valido")

