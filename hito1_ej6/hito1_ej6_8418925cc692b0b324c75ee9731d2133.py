#Ordenar tres números
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if(a>=b>=c):
    print(c,",",b,",",a)
elif(a>=c>=b):
    print(b,",",c,",",a)
elif(b>=c>=a):
    print(a,",",c,",",b)
elif(b>=a>=c):
    print(c,",",a,",",b)
elif(c>=b>=a):
    print(a,",",b,",",c)
elif(c>=a>=b):
    print(b,",",a,",",c)
else:
    print("ERROR")