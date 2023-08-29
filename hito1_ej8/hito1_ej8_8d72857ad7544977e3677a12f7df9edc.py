#Descomponer un número
n = eval(input("Ingrese un numero de 4 digitito: "))
n1= n%10
n2 = (n%100)//10
n3 = (n%1000)//100
n4 = (n%10000)//1000

x1 = str(n4)
x2 = str(n3)
x3 = str(n2)
x4 = str(n1)

y1 = x4
y2 = x3 + x4
y3 = x2 + x3 + x4
y4 = x1 + x2 + x3 + x4


if str(n) == y4:
  print(x1+"M","+",x2+"C","+",x3+"D","+",x4+"U")
elif str(n)== y3:
  print(x2+"C","+",x3+"D","+",x4+"U")
elif str(n) == y2:
  print(x3+"D","+",x4+"U")
elif str(n)== y1:
  print(x4+"U")

else:
  print("no es valido")


