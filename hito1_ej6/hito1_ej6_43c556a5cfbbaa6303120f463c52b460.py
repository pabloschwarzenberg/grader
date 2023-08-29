#Ordenar tres números
print("Ingrese los tres numeros que desea ordenar:")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a <= b and b<=c:
    print("Los numeros ordenados son:")
    print(a,b,c,sep=",")

elif a>=b and b>=c:
    print("Los numeros ordenados son:")
    print(c,b,a,sep=",")

elif a>=c and c>=b:
    print("Los numeros ordenados son:")
    print(b,c,a,sep=",")

elif b>=a and a>=c:
    print("Los numeros ordenados son:")
    print(c,a,b,sep=",")

elif b>=c and c>=a:
    print("Los numeros ordenados son:")
    print(a,c,b,sep=",")

elif c>=a and a>=b:
    print("Los numeros ordenados son:")
    print(b,a,c,sep=",")

print("Muchas gracias!\n")