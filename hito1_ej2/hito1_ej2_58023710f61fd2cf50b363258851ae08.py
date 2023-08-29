#Contestador de celular
x=int(input("Ingrese número: "))
y=int(input("Ingrese hora: "))
x_str=str(x)
a=eval(x_str[5:8])
b=eval(x_str[0:3])
if 0<=y<=7:
  print("CONTESTAR")
elif 7<y<14:
  if a==909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif 14<=y<17:
  print("NO CONTESTAR")
elif 17<=y<=19:
  if b==877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
elif y>19:
  print("NO CONTESTAR")
  