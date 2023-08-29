#Sistema de Ecuaciones
Num1 = int(input())  
Num2 = int(input()) 
Num3 = int(input()) 
Num4 = int(input()) 
Num5 = int(input()) 
Num6 = int(input())
y2 = Num2*Num4
y3 = Num3*Num4
y5 = Num5*Num1
y6 = Num6*Num1
y7 = y2 - y5
y8 = y3 - y6
y = y8/y7

x1 = Num1*Num5
x3 = Num3*Num5
x4 = Num4*Num2
x6 = Num6*Num2
x7 = x1 - x4
x8 = x3 - x6
x = x8/x7

a = "x="+str(round(x, 1))
b = "y="+str(round(y, 1))
Lista = [a,b]
print(Lista)
