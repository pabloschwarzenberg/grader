("ingrese distintos numeros con distintos valores")
n1 = eval(input("ingrese un primer numero: "))
n2 = eval(input("ingrese un segundo numero: "))
n3 = eval(input("ingrese un tercer numero: "))
if n1 <= n2 <= n3:
    print("los numeros de menor a mayor son", n1, " , " ,n2, " , " , n3)
else:
    if n1 >= n2 <= n3:
        print("los numeros de menor a mayor son", n2, " , ",  n1, " , ", n3)
    else:
        if n1 >= n2 >= n3:
            print("los numeros de menor a mayor son", n3, " , ", n2, " , ", n1)
        else:
            if n1 <= n3 <= n2:
                print("los numeros de menor a mayor son", n1, " , ", n3, " , ", n2)
            else:
                if n2 <= n3 <= n1:
                    print("los numeros de menor a mayor son", n2, " , ", n3, " , ", n1)
                else:
                    if n3 <= n1 <= n2:
                        print("los numeros de menor a mayor son", n3, " , ", n1, " , ", n2)
                    else :
                        print("ingrese numeros de DISTINTO valor")
