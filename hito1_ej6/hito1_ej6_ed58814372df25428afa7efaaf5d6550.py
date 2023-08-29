#Ordenar tres números
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese un numero: "))
num3=int(input("Ingrese un numero: "))

#ok
if num1< num2 and num1< num3 and num2<3:
    print(str(num1)+","+str(num2)+","+str(num3))
#ok
elif num1< num2 and num1< num3 and num3<2:
    print(str(num1)+","+str(num3)+","+str(num2))
#ok
elif num2< num1 and num2< num3 and num1<3:
    print(str(num2)+","+str(num1)+","+str(num3))
#ok
elif num2< num1 and num2< num3 and num3<1:
    print(str(num2)+","+str(num3)+","+str(num1))
#ok
elif num3< num1 and num3< num2 and num1<2:
    print(str(num3)+","+str(num1)+","+str(num2))
else:
    print(str(num3)+","+str(num2)+","+str(num1))