#Ordenar tres números
A = eval(input("ingrese valor 1 : "))
B = eval(input("ingrese valor 2 : "))
C = eval(input("ingrese valor 3 : "))
Max = max (A,B,C)
Min = min (A,B,C)
Me = (A + B + C) - Max - Min
print("de menor a mayor es:" , Min ," , ", Me ,"," ,Max)