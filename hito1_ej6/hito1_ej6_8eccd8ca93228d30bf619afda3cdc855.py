#Ordenar tres números
numero1 = eval(input("Ingrese primer numero : "))
numero2 = eval(input("Ingrese segundo numero : "))
numero3 = eval(input("Ingrese tercer numero : "))
MAYOR = max(numero1,numero2,numero3)
MENOR = min(numero1,numero2,numero3)
X = (numero1 + numero2 + numero3)- MAYOR - MENOR
print("el orden de menor a mayor es: ", MENOR,",", X ,",",MAYOR)