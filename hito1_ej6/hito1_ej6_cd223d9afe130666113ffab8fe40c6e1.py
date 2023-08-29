#Ordenar tres números
a= int(input("ingrese el primer numero entero "))
b= int(input("ingrese el sugundo numero entero "))
c= int(input("ingrese el tercer numero entero "))

if(a<=b<=c):
  print(a,",",b,",",c)
elif(a<=c<=b):
  print(a,",",c,",",b) 
elif(b<=a<=c):
  print(b,",",a,",",c)
elif(b<=c<=a):
  print(b,",",c,",",a)
elif(c<=b<=a):
  print(c,",",b,",",a)
elif(a<=c<=b):
  print(a,",",c,",",b)