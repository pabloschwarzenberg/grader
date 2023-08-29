#Ordenar tres números
def orden_num(n1,n2,n3):
    numero=[n1,n2,n3]
    numero.sort()
    numero_str=",".join(str(num) for num in numero)
    return numero_str
    
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("Ingrese el tercer numero: "))

n_orden=orden_num(n1,n2,n3)
print(n_orden)
