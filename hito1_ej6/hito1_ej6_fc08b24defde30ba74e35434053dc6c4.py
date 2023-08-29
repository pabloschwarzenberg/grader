#Ordenar tres números
num1= int(input("Ingrese el primer numero:" ))
num2= int(input("Ingrese el segundo numero:" ))
num3= int(input("Ingrese el tercer numero:" ))
#_____
mayor= max(num1,num2,num3)
menor=min(num1,num2,num3)
resultado=(num1+num2+num3)- menor- mayor
print(menor,",",resultado,",",mayor)
#__________
