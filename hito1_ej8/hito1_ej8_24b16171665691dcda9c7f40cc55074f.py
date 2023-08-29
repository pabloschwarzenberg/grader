#Descomponer un número
n = int(input("ingrese numero"))

m = n// 1000
c = n// 100 - m*10
d = n// 10 - m*100 - c*10 
u = n// 1 - m*1000 - c*100 - d*10 

if 999 < n < 10000:
  print(m,"M +", c, "C +", d ,"D +", u , "U")
elif 99 < n < 1000 :
  print(c, "C +", d ,"D +", u ,"U")
elif 9 < n < 100:
  print(d,"D +", u ,"U")
elif 0 < n < 10:
  print(u,"U")