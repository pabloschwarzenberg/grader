a=str(input("ingrese un numero de hasta 4 digitos: "))
if len(a)==4:
   print(a[0],"M+",a[1],"C+",a[2],"D+",a[3],"U")
elif len(a)==3:
   print(a[0],"C+",a[1],"D+",a[2],"U")
elif len(a)==2:
   print(a[0],"D+",a[1],"U")
else:
   print(a[0],"U")
