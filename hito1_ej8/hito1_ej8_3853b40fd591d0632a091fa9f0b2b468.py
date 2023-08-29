numero = input("ingrece un numero de 4 digitos: ")
largo_numero = len(numero)

if largo_numero == 1:
    parte1 = str(numero[0]) + "U"
    print(parte1)
elif largo_numero == 2:
    parte1 = str(numero[0]) + "D"
    parte2 = str(numero[1]) + "U"
    print(parte1,"+",parte2)
elif largo_numero == 3:
    parte1 = str(numero[0]) + "C"
    parte2 = str(numero[1]) + "D"
    parte3 = str(numero[2]) + "U"
    print(parte1, "+" , parte2 , "+" ,  parte3)
else:
    parte1 = str(numero[0]) + "M"
    parte2 = str(numero[1]) + "C"
    parte3 = str(numero[2]) + "D"
    parte4 = str(numero[3]) + "U"
    print(parte1,"+",parte2,"+",parte3,"+",parte4)