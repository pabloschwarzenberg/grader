
a=input("ingrese un número de 4 dígitos: ")
if len(a)==4:
  print(a[0],"M","+",a[1],"C + ",a[2],"D + ",a[3],"U")
elif len(a)==3:
       print(a[0],"C + ",a[1],"D + ",a[2],"U")
elif len(a)==2:
       print(a[0],"C + ",a[1],"D ")
elif len(a)==1:
       print(a[0],"U")
else:
       print("0")