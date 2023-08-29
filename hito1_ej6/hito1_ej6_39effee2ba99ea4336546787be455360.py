#Ordenar tres números
num1=int(input("ingresa un numero: \n") )
num2=int(input("ingresa otro numero: \n") )
num3=int(input("ingresa un tercer numero: \n")) 

if num1>=num2 and num2>=num3:
    menor=num3
    medio=num2
    mayor=num1
elif num1>=num3 and num3>=num2:
    menor=num2
    medio=num3
    mayor=num1
elif num2>=num1 and num1>=num3:
    menor=num3
    medio=num1
    mayor=num2
elif num2>=num3 and num3>=num1:
    menor=num1
    medio=num3
    mayor=num2
elif num3>=num1 and num1>=num2:
    menor=num2
    medio=num1
    mayor=num3
elif num3>=num2 and num2>=num1:
    menor=num1
    medio=num2
    mayor=num3
     
print(str(menor),",", str(medio),",", str(mayor))
    