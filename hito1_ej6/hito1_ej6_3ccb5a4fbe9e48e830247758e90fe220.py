#Ordenar tres números
print("Ordenar 3 numeros de menor a mayor")
a = eval(input('ingrese un numero: '))
b = eval(input('ingrese un numero: '))
c = eval(input('ingrese un numero: '))
if(a<b and b<c):
    print("",a, ",",b",",c)
elif(b<c and c<a):
    print("", b,",",c,",",a)
elif(a<c and c<b):
    print("", a,",",c,",",b)
elif(c<b and b<a):
    print("", c,",",b,",",a)
elif(c<a and a<b):
    print("", c,",",a,",",b)
elif(b<a and a<c):
    print("", b,",",a,",",c)