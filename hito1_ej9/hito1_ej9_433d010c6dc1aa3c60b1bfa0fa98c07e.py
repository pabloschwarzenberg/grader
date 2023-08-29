#Sistema de Ecuaciones
num1 = int(input("Ingrese el número 1:\n"))
num2 = int(input("Ingrese el número 2:\n"))
num3 = int(input("Ingrese el número 3:\n"))
num4 = int(input("Ingrese el número 4:\n"))
num5 = int(input("Ingrese el número 5:\n"))
num6 = int(input("Ingrese el número 6:\n"))

op1 = ((num6*num1)-(num4*num3))/((num1*num5)-(num4*num2))

op2 = (num3-num2*op1)/num1

op1 = round(op1,1)
op2 = round(op2,1)

print("['x=",op1,", 'y=",op2,"']")