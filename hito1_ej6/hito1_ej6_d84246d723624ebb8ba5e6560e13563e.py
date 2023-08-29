#Ordenar tres números
num1=int(input('Ingrese el primer numero: '))
num2=int(input('Ingrese el segundo numero: ')) 
num3=int(input('Ingrese el tercer numero: '))

num_menor= min(num1,num2,num3)
num_mayor= max(num1,num2,num3)
num_medio= (num1+num2+num3) - num_menor - num_mayor

print('El orden de menor a mayor es: ' +str(num_menor)+ ',' +str(num_medio)+ ',' +str(num_mayor))