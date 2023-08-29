#Descomponer un número
valor1 = input("Ingresar un número de máximo de 4 dígitos :")
if len(valor1) == 4:
    num1 = int(valor1[-1])
    num2 = int(valor1[-2])
    num3 = int(valor1[-3])
    num4 = int(valor1[-4])
    print(num4,"M +",num3,"C +",num2,"D +",num1,"U")
else:
    if len(valor1) == 3:
        num1 = int(valor1[-1])
        num2 = int(valor1[-2])
        num3 = int(valor1[-3])
        print(num3,"C +",num2,"D +",num1,"U")
    else:
        if len(valor1) == 2:
            num1 = int(valor1[-1])
            num2 = int(valor1[-2])
            print(num2,"D +",num1,"U")
        else:
            if len(valor1) == 1:
                num1 = int(valor1[-1])
                print(num1,"U")
            else:
                print("Ingrese el número de dígitos correctos")      