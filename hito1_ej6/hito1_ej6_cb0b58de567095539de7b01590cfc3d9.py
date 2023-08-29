#Ordenar tres números
NUMS=print("INGRESE 3 NUMEROS PARA ORDENARLOS DE MENOR A MAYOR")
num1=int(input("PRIMER NUMERO:\t"))
num2=int(input("SEGUNDO NUMERO:\t"))
num3=int(input("TERCER NUMERO:\t"))
if num1>=num2 and num2>=num3:
    print(num3,",",num2,",",num1)
elif num2>=num3 and num3>=num1:
    print(num1,",",num3,",",num2)
elif num2>=num1 and num1>=num3:
    print(num3,",",num1,",",num2)
elif num3>=num2 and num2>=num1:
    print(num1,",",num2,",",num3)
elif num1>=num3 and num3>=num2:
    print(num2,",",num3,",",num1)
elif num3>=num1 and num1>=num2:
    print(num2,",",num1,",",num3)