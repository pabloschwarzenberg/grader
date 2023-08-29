print("ingresar el primer numero: ")
num1 = int(input())
print("ingresar el segundo numero: ")
num2 = int(input())
print("ingresar el tercer numero: ")
num3 = int(input())
if(num1<num2 and num2<num3):
    print(num1,num2,num3)
elif(num2<num1 and num1<num3):
    print(num2,num1,num3)
elif(num3<num1 and num1<num2):
    print(num3,num1,num2)
elif(num3<num2 and num2<num1):
    print(num3,num2,num1)
elif(num1<num3 and num3<num2):
    print(num1,num3,num2)
elif(num2<num3 and num3<num1):
    print(num2,num3,num1)
elif(num1==num2 and num2==num3):
    print(num1,num2,num3)
elif(num2==num1 and num1==num3):
    print(num2,num1,num3)
elif(num3==num1 and num1==num2):
    print(num3,num1,num2)
elif(num3==num2 and num2==num1):
    print(num3,num2,num1)
elif(num1==num3 and num3==num2):
    print(num1,num3,num2)
elif(num2==num3 and num3==num1):
    print(num2,num3,num1)
elif(num1<num2 and num2==num3):
    print(num1,num2,num3)
elif(num2<num1 and num1==num3):
    print(num2,num1,num3)
elif(num3<num1 and num1==num2):
    print(num3,num1,num2)
elif(num3<num2 and num2==num1):
    print(num3,num2,num1)
elif(num1<num3 and num3==num2):
    print(num1,num3,num2)
elif(num2<num3 and num3==num1):
    print(num2,num3,num1)
elif(num1==num2 and num2<num3):
    print(num1,num2,num3)
elif(num2==num1 and num1<num3):
    print(num2,num1,num3)
elif(num3==num1 and num1<num2):
    print(num3,num1,num2)
elif(num3==num2 and num2<num1):
    print(num3,num2,num1)
elif(num1==num3 and num3<num2):
    print(num1,num3,num2)
elif(num2==num3 and num3<num1):
    print(num2,num3,num1)
else:
    print("se ingresaron numeros iguales:")