#Ordenar tres números
a=int(input("Ingrese un numero:  "))
b=int(input("Ingrese un segundo numero: "))
c=int(input("Ingrese un tercer numero: "))
if a>=b>=c :
    print("El orden de menor a mayor ", c,",",b,",",a)
elif b>=a>=c:
     print("El orden de menor a mayor ",c,",",a,",",b)
elif b>=c>=a:
     print("El orden de menor a mayor ",a,",",c,",",b)
elif c>=b>=a:
     print("El orden de menor a mayor ",a,",",b,",",c)
elif c>=a>=b:
    print("El orden de mayor a menor ",b,",",a,",",c)
elif a>=c>=b:
    print("El orden de mayor a menor ",b,",",c,",",a)
elif a==b==c:
    print("Sus numeros son igules",a,",",b,",",c)


