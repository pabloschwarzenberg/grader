#Ordenar tres números
numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
numero3 = int(input("ingrese el tercer numero: "))
Ma = max(numero1,numero2,numero3)
Mi = min(numero1,numero2,numero3)
D = (numero1 + numero2 + numero3) - Ma - Mi
print(Mi,",",D,",",Ma)