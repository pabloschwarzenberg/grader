a=int(input("ingrese primer entero: "))
b=int(input("ingrese segundo entero: "))
c=int(input("ingrese tercer entero: "))
if a>=b and b>=c:
  print("el orden es:",c,",",b,",",a)
elif a>=c and c>=b:
  print("el orden es:",b,",",c,",",a)
elif b>=a and a>=c:
  print("el orden es:",c,",",a,",",b)
elif b>=c and c>=a:
  print("el orden es:",a,",",c,",",b)
elif c>=a and a>=b:
  print("el orden es:",b,",",a,",",c)
elif c>=b and b>=a:
  print("el orden es:",a,",",b,",",c)