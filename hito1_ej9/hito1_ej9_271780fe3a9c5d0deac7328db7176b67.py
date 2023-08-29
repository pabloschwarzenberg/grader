#Sistema de Ecuaciones
Lista1=[]
Lista2=[]


Lista1.append((int(input("ingrese el valor x: "))))
Lista1.append((int(input("ingrese el valor y: "))))
Lista1.append((int(input("ingrese el resultado: "))))


Lista2.append((int(input("ingrese el segundo valor x: "))))
Lista2.append((int(input("ingrese el segundo valor y: "))))
Lista2.append((int(input("ingrese el segundo resultado: "))))

print(Lista1)
print(Lista2)


determinante = (Lista1[0]*Lista2[1])-(Lista2[0]*Lista1[1])

if determinante==0:
    print("el sistema no tiene una solucion")
elif determinante !=0:
    x= ((Lista2[1]*Lista1[2])-(Lista1[1]*Lista2[2]))/determinante
    y= ((Lista1[0]*Lista2[2])-(Lista2[0]*Lista1[2]))/determinante

    print(" ")
    print("Sus incognitas son:  ")
    print("x= ",round(x,1))
    print("y= ",round(y,1))
    