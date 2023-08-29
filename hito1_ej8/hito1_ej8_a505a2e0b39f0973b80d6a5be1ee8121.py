#Descomponer un número
num = input("Ingrese un número: ")
if len(num)==2:
  u = num[1] 
  d = num[0]
  print(d,"D + ", u,"U", sep="")
elif len(num)==3:
  u = num[2] 
  d = num[1]
  c = num[0]
  print(c, "C + ", d,"D + ", u,"U", sep="")
elif len(num)==4:
  u = num[3] 
  d = num[2]
  c = num[1]
  m = num[0]
  print(m, "M + ", c, "C + ", d,"D + ", u,"U", sep="") 