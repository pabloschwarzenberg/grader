#Ordenar tres números de menor a mayor
print("Ingrese numeros enteros")
a = int(input("Ingrese un primer valor: "))
b = int(input("Ingrese un valor2: "))
c = int(input("Ingrese un valor3: "))
if a <= b <= c:
    print("Los  numeros ordenados de menor a mayor son", a, " , ",b, " , ", c)
else:
    if a >= b <= c:
        print("Los  numeros ordenados de menor a mayor son", b, " , ",a, " , ", c)
    else:
        if a >= b >= c:
            print("Los  numeros ordenados de menor a mayor son", c, " , ",b, " , ", a)
        else:
            if a <= c <= b:
                print("Los  numeros ordenados de menor a mayor son", a, " , ",c, " , ", b)
            else:
                if b <= c <= a:
                    print("Los  numeros ordenados de menor a mayor son", b, " , ",c, " , ", a)
                else:
                    if c <= a <= b:
                        print("Los  numeros ordenados de menor a mayor son", c, " , ",a, " , ", b)
                    else:
                        print("Ingrese numeros distintos a los ingresados")