#Ordenar tres números
print("ingrese 3 numeros para ordednarlos de menor a mayor")
numero_1=int(input("primer numero: "))
numero_2=int(input("segundo numero: "))
numero_3=int(input("tercer numero: "))

a=min(numero_1,numero_2,numero_3)
c=max(numero_1,numero_2,numero_3)
b=(numero_1+numero_2+numero_3)-a-c
print("y el orden seria :{},{},{}".format(a,b,c))