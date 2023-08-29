num = str(input("Ingresa un numeor a descomponer: "))
if(4 >= len(num) >= 1):
    if(len(num) == 4):
        n1 = num[0] + "M"
        n2 = num[1] + "C"
        n3 = num[2] + "D"
        n4 = num[3] + "U"
        print(n1,"+",n2,"+",n3,"+",n4)
    elif(len(num) == 3):
        n1 = num[0] + "C"
        n2 = num[1] + "D"
        n3 = num[2] + "U"
        print(n1,"+",n2,"+",n3)
    elif(len(num) == 2):
        n1 = num[0] + "D"
        n2 = num[1] + "U"
        print(n1,"+",n2)
    elif(len(num) == 1):
        n1 = num[0] + "U"
        print(n1)
    else:
        print("Numero in")
else:
    print("Numero ingresado invalido.")