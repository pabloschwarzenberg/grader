#Ordenar tres números

print("ingrese tres números enteros para ordenarlos de meyor a menor")
print("ingrese número: ") ; a=int(input())
print("ingrese número: ") ; b=int(input())
print("ingrese número: ") ; c=int(input())

print("este es el orden de menor a mayor de los números ingresados: ")
if a<=b<=c:
    print(a,",",b,",",c)
else:
    if a<=c<=b:
        print(a,",",c,",",b)
    else:
        if b<=a<=c:
            print(b,",",a,",",c)
        else:
            if b<=c<=a:
                print(b,",",c,",",a)
            else:
                if c<=a<=b:
                    print(c,",",a,",",b)
                else:
                    if c<=b<=a:
                        print(c,",",b,",",a)

      