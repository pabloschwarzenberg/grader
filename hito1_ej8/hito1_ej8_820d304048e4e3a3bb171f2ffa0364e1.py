#Descomponer un número

n = int(input("Numero: "))

#m unidad de mil
#c centena
#d decena
#u unidad

m = n // 1000
c = (n // 100) % 10
d = (n // 10 ) % 10
u = n % 10


if d == 0 and c == 0 and m == 0:
  print(str(u)+"U")
elif c == 0 and m == 0:
  print(str(d)+"D +",str(u)+"U")
elif m == 0:
  print(str(c)+"C +",str(d)+"D +",str(u)+"U")
else:
  print(str(m)+"M +",str(c)+"C +",str(d)+"D +",str(u)+"U")