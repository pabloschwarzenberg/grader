#Ordenar tres números
print("ingrese un primer numero:")
num1 = int(input())
print("ingrese un segundo numero:")
num2 = int(input())
print("ingrese un tercer numero:")
num3 = int(input())

Ma = max(num1,num2,num3)
Mi = min(num1,num2,num3)
M = (num1 + num2 + num3) - Ma - Mi

print("de menor a mayor, el orden seria:", Mi ," , ", M ," , ", Ma)