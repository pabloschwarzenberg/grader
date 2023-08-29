#
num1= int(input("porfavor, digite el primer numero"))
num2= int(input("porfavor, digite el segundo numero"))
num3= int(input("porfavor, digite el tercer numero"))

#OPERACION
a = min(num1, num2, num3)
c = max(num1, num2, num3)
b = (num1 + num2 + num3) - a - c

#SALIDA
print("sus números ordenados de menor a mayor quedarian de la siguiente forma: {}, {}, {},".format(a,b,c))