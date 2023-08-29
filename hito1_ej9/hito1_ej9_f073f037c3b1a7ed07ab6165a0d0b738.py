#Sistema de Ecuaciones
n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese un numero: "))
n3 = int(input("ingrese un numero: "))
n4 = int(input("ingrese un numero: "))
n5 = int(input("ingrese un numero: "))
n6 = int(input("ingrese un numero: "))

 

formula = ((n6*n1)-(n4*n3))/((n1*n5)-(n4*n2))
op = (n3-n2*formula)/n1
formula = round(formula,1)
op = round(op,1)
print("['x=",op,", 'y=",formula,"']")