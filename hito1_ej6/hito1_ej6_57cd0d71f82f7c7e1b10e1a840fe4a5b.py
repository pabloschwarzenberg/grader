print("ingrese los valores de: ")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a>=b>=c:
    print("el orden seria: ",b,",",c,",",a)
elif a>=c>=b:
    print("el orden seria: ",b,",",c,",",a)
elif b>=a>=c:
    print("el orden seria: ",c,",",a,",",b)
elif b>=c>=a:
    print("el orden seria: ",a,",",c,",",b)
elif c>=b>=a:
    print("el orden seria: ",a,",",b,",",c)
elif c>=a>=b:
    print("el orden seria: ",b,",",a,",",c)