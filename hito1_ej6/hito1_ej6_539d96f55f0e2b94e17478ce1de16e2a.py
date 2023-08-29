#Ordenar tres números
entero1= int(input("coloque el primer numero entero: "))
entero2= int(input("coloque el segudo numero entero: "))
entero3= int(input("coloque el tercer numero entero: "))
#enteros diferentes
if entero1>entero2>entero3:
    print("el orden de los numeros de menor a mayor seria: ",entero3,",",entero2,",", entero1)
else:
        if entero1>entero3>entero2:
            print("el orden de los numeros de menor a mayor seria: ",entero2,",",entero3,",",entero1)
        else:
                if entero2>entero1>entero3:
                    print("el orden de los numeros de menor a mayor seria: ",entero3,",",entero1,",",entero2)
                else:
                    if entero2>entero3>entero1:
                        print("el orden de los numeros de menor a mayor seria: ",entero1,",",entero3,",",entero2)
                    else:
                        if entero3>entero2>entero1:
                            print("el orden de los numeros de menor a mayor seria: ",entero1,",",entero2,",",entero3)
                        else:
                            if entero3>entero1>entero2:
                                print("el orden de los numeros de menor a mayor seria: ",entero2,",",entero1,",",entero3)
#enteros iguales
if entero1==entero2==entero3:
    print("el orden de los numeros de menor a mayor seria: ",entero1,",",entero2,",",entero3)
else:
        if entero1==entero2>entero3:
            print("el orden de los numeros de menor a mayor seria: ",entero3,",",entero2,",",entero1)
        else:
            if entero1==entero2<entero3:
                print("el orden de los numeros de menor a mayor seria: ",entero1,",",entero2,",",entero3)
            else:
                if entero1==entero3<entero2:
                    print("el orden de los numeros de menor a mayor seria: ",entero1,",",entero3,",",entero2)
                else:
                    if entero1==entero3>entero2:
                        print("el orden de los numeros de menor a mayor seria: ",entero2,",",entero1,",",entero3)
                    else:
                        if entero3==entero2<entero1:
                            print("el orden de los numeros de menor a mayor seria: ",entero3,",",entero2,",",entero1)
                        else:
                            if entero3==entero2>entero1:
                                print("el orden de los numeros de menor a mayor seria: ",entero1,",",entero2,",",entero3)