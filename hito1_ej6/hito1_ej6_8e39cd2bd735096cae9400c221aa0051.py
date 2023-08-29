#Ordenar tres números
print("a continuacion se le pediran ingresar 3 numeros para poder ordenarlos de menor a mayor")
a = eval(input("ingrese el primer numero entero: "))
b = eval(input("ingrese el segundo numero entero: "))
c = eval(input("ingrese el tercer numero entero: "))
if(a<=b<=c):
    print(a, ",", b, ",", c)
elif(a<=c<=b):
    print(a,",", c,",", b)
elif(b<=c<=a):
    print(b,",", c,",", a)
elif(b<=a<=c):
    print(b,",", a,",", c)
elif(c<=b<=a):
    print(c,",", b,",", a)
else:
    print(c,",", a,",", b)      