a=int(input("ingrese primer numero "))
b=int(input("ingrese segundo numero "))
c=int(input("ingrese tercer numero "))
if a<=b and a<=c and b<=c :
  print (a,b,c)
elif b<=a and b<=c and a<=c :
  print (b,a,c)
elif c<=a and c<=b and b<=a :
  print (c,b,a)
elif c<=a and c<=b and a<=b :
  print (c,a,b)
elif b<=a and b<=c and c<=a :
  print (b,c,a)
elif a<=b and a<=c and c<=b :
  print (a,c,b)
else :
  print("numeros no enteros")
