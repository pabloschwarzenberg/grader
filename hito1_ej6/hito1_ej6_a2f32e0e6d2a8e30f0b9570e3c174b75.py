#Ordenar tres números
num1=(int(input("seleccione el primer numero: " )))
num2=(int(input("seleccione el segundo numero: ")))
num3=(int(input("seleccione el tercer numero: ")))
num_ent=(num1, num2, num3)
num_ord=sorted(num_ent)
print("los numeros ordenados son", num_ord)      