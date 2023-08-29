#Sistema de Ecuaciones

Valor1=int(input("Ingrese el primer valor:"))
Valor2=int(input("Ingrese el segundo valor:"))
Valor3=int(input("Ingrese el tercer valor:"))
Valor4=int(input("Ingrese el cuarto valor:"))
Valor5=int(input("Ingrese el quinto valor:"))
Valor6=int(input("Ingrese el sexto valor:"))
#Calculo de Sistemas
x = (Valor6-Valor5*Valor3/Valor2)/(Valor4-Valor5*Valor1/Valor2)
y = (Valor3-Valor1*x)/Valor2

print(round(x,1))
print(round(y,1))