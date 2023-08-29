#Descomponer un número
n = int(input())

m = n// 1000
c = n// 100 - m*10
d = n// 10 - m*100 - c*10
u = n// 1 - m*1000 - c*100 - d*10

if m > 0 :
  print(m,"m+",c,"c+",d,"d+",u,"u")
elif c > 0 :
  print(c,"c+",d,"d+",u,"u")
elif d > 0 :
  print(d,"d+",u,"u")
elif u > 0 :
  print(u,"u")