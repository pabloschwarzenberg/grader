#Ordenar tres números
a=int(input("el valor de a es:"))
b=int(input("el valor de b es:"))
c=int(input("el valor de c es:"))
if a<b<c:
 print("el orden de menor a mayor es:",a,",",b,",",c)
else: 
  if a<=c<=b:
   print("el orden de menor a mayor es:",a,",",c,",",b)
  else:
    if b<=a<=c:
     print("el orden de menor a mayor es:",b,",",a,",",c)
    else: 
      if b<=c<=a:
       print("el orden de menor a mayor es:",b,",",c,",",a)
      else: 
        if c<=a<=b:
         print("el orden de menor a mayor es:",c,",",a,",",b)
        else:
          if c<=b<=a:
           print("el orden de menor a mayor es:",c,",",b,",",a)
