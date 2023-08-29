#Ordenar tres números
print("Ingrese valor entero")

a = int(input("valor para a: "))
b = int(input("valor para b: "))
c = int(input("valor para c: "))

if a <= b <= c:
    print(a,",",b,",",c)
elif b <= a <= c:
        print(b,",",a,",",c)
elif c <= a <= b:
        print(c,",",a,",",b)
elif a <= c <= b:
        print(a,",",c,",",b)
print()
print("Fin del programa")