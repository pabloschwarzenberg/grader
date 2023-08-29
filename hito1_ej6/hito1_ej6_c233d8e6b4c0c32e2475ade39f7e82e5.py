#Ordenar tres números
a=int(input("Ingrese primer numero: "))
b=int(input("Ingrese segundo numero: "))
c=int(input("Ingrese tercer numero: "))
if a<=b and b<=c:
  print(str(a)+","+ str(b)+","+ str(c))
elif b<=a and a<=c:
  print(str(b)+","+ str(a)+","+ str(c))
elif b<=c and c<=a:
  print(str(b)+","+ str(c)+","+ str(a))
elif a<=c and c<=b: 
  print(str(a)+","+ str(c)+","+ str(b))
elif c<=a and a<=b:
  print(str(c)+","+ str(a)+","+ str(b))
else:
  (str(c)+","+ str(b)+","+ str(a))

