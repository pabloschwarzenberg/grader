#Sistema de Ecuaciones
num1=input()
numero1=int(num1)
num2=input()
numero2=int(num2)
num3=input()
numero3=int(3)
num4=input()
numero4=int(num4)
num5=input()
numero5=int(num5)
num6=input()
numero6=int(num6)

y=((numero6*numero1)-(numero4*numero3))/((numero1*numero5)-(numero4*numero2))
x=(numero3-numero2*y)/numero1
y=round(y,1)
x=round(x,1)
print("['x=",x,", 'y=",y,"']")