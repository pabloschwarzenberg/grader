#Descomponer un número
Rut=int(input())
number_string = str(Rut)
if Rut<10:
  d=number_string[0]
  print(d,"U")
elif Rut<100:
  c=number_string[0]
  d=number_string[1]
  print(c,"D + ",d,"U")
elif Rut<1000:
  b=number_string[0]
  c=number_string[1]
  d=number_string[2]
  print(b,"C + ",c,"D + ",d,"U")
else:
  a=number_string[0]
  b=number_string[1]
  c=number_string[2]
  d=number_string[3]
  print(a,"M + ",b,"C + ",c,"D + ",d,"U")