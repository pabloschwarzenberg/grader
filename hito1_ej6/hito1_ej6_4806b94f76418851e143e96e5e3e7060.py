#Ordenar tres números
a = int(input("INTRODUZCA EL PRIMER NUMERO: "))
b = int(input("INTRODUZCA EL SEGUNDO NUMERO: "))
c = int(input("INTRODUZCA EL TERCER NUMERO: "))
if a <= b <= c:
  print(a, ",", b, "," , c)
elif a <=c < b:
  print(a, ",", c, ",", b)
elif b <=a < c:
  print(b, ",", a, ",", c)
  