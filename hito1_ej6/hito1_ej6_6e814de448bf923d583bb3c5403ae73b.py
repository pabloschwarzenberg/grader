#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
if a>=b>=c:
  print(c,",",b,",",a)
elif a>=c>=b:
  print(b,",",c,",",a)
elif b>=a>=c:
  print(c,",",a,",",b)
elif b>=c>=a:
  print(a,",",c,",",b)
elif c>=a>=b:
  print(b,",",a,",",c)
elif c>=b>=a:
  print(a,",",b,",",c)
else:
  print("Error.")      
      
      