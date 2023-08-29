#Ordenar tres números
num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
num3= int(input("Ingrese el tercer numero numero: "))
#orden
numa= min(num1,num2,num3)
numb= max(num1,num2,num3)
numc= (num1+num2+num3)-(numa+numb)
print("Tus numeros ordenados de menor a mayor son:" ,numa, "," ,numc,  "," ,numb, )