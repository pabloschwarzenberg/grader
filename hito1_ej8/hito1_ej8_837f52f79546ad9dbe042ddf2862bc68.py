#Descomponer un número
numero = input("Ingrese un número de máximo cuatro dígitos: ")
largo_num=len(numero)
if largo_num == 1:
    unidades = numero[0]
    print("La descomposición del número ",numero," es: ",unidades,"U")
elif largo_num == 2:
    unidades = numero[1]
    decenas = numero[0]
    print("La descomposición del número ",numero," es: ",decenas,"D + ",unidades,"U")
elif largo_num == 3:
    unidades = numero[2]
    decenas = numero[1]
    centenas = numero[0]
    print("La descomposición del número ",numero," es: ",centenas,"C + ",decenas,"D + ",unidades,"U")
elif largo_num == 4:
    unidades = numero[3]
    decenas = numero[2]
    centenas = numero[1]
    miles = numero[0]
    print("La descomposición del número ",numero," es: ",miles,"M + ",centenas,"C + ",decenas,"D + ",unidades,"U")