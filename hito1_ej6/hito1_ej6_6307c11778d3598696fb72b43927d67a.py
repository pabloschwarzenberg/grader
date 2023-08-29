num1=int(input('Digite un número :'))
num2=int(input('Digite un número distinto del primero :'))
num3=int(input('Digite un número distinto del primero y segundo:'))
if (num1<=num2) and (num1<=num3) and (num2<=num3):
    print( num1,num2,num3, sep =",")
elif (num1<=num2) and (num1<=num3) and (num3<=num2):
    print(num1,num3,num2 ,sep ="," )
elif (num2<=num1) and (num2<=num3) and (num1<=num3):
    print(num2,num1,num3 ,sep=",")
elif (num2<=num1) and (num2<=num3) and (num3<=num1):
    print(num2,num3,num1,sep=",")
elif (num3<=num1) and (num3<=num2) and (num1<=num2):
    print(num3,num1,num2,sep=",")
elif (num3<=num1) and (num3<=num2) and (num2<=num1):
    print(num3,num2,num1,sep=",")
