print("Introduzca 3 numeros enteros:")

n1=int(input("n1="))
n2=int(input("n2="))
n3=int(input("n3="))

print("Los numeros escogidos, ordenados de menor a mayor son:")

if n3<=n2<=n1:
    print(n3,",",n2,",",n1)
else:
    if n2<=n3<=n1:
        print(n2,",",n3,",",n1)
    else:
        if n3<=n1<=n2:
            print(n3,",",n1,",",n2)
        else:
            if n1<=n3<=n2:
                print(n1,",",n3,",",n2)
            else:
                if n1<=n2<=n3:
                    print(n1,",",n2,",",n3)
                else:
                    if n2<=n1<=n3:
                        print(n2,",",n1,",",n3)
    
     




    
     
