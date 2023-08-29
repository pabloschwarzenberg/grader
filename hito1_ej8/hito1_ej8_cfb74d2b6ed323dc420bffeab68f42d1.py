num=input("Escriba un número de hasta 4 dígitos : ")
num1=''
num2=''
num3=''
num4=''
if num==num[0]:
    num1=num[0]
    print( num1, "U")
elif num==num[0]+num[1]:
    num1 = num[0]
    num2 = num[1]
    print(num1, "D +", num2, "U")
elif num==num[0]+num[1]+num[2]:
    num1 = num[0]
    num2 = num[1]
    num3 = num[2]
    print(num1, "C +", num2, "D +", num3, "U")
elif num==num[0]+num[1]+num[2]+num[3]:
    num1=num[0]
    num2=num[1]
    num3=num[2]
    num4=num[3]
    print(num1,"M +",num2,"C +",num3,"D +",num4,"U")
else: print("ingreso un número incorrecto")