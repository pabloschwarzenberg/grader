#Ordenar tres números
a = int(input("Ingrese A:"))
b = int(input("Ingrese B:"))
c = int(input("Ingrese C:"))

if a >= b >= c:
    print("Los números ordenados de menor a mayor son:", c ,",", b ,",", a)

else:
    if a >= c >= b:
        print("Los números ordenados de menor a mayor son:", b ,",", c ,",", a)

    else:
        if b >= a >= c:
            print("Los números ordenados de menor a mayor son:", c ,",", a ,",", b)

        else:
            if b >= c >= a:
                print("Los números ordenados de menor a mayor son:", a ,",", c ,",", b)

            else:
                if c >= a >= b:
                    print("Los números ordenados de menor a mayor son:", b ,",", a ,",", c)

                else:
                    if c >= b >= a:
                        print("Los números ordenados de menor a mayor son:", a ,",", b ,",", c)