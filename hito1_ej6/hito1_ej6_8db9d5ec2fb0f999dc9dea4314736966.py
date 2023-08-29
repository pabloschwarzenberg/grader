num1=int(input("Ingrese su primer numero: "))
num2=int(input("Ingrese su segundo numero: "))
num3=int(input("Ingrese su tercer numero: "))
lista=[num1,num2,num3]
lista.sort()
lista=",".join(map(str,lista))
print("Sus numeros ordenados de menor a mayor son:",lista)