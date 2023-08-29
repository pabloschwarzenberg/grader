#Ordenar tres números
first = int(input("ingrese el primer numero: ") or "0")  
second = int(input("ingrese el segundo numero: ") or "0")   
third = int(input("ingrese el tercero numero: ") or "0") 
numbers = [first, second, third]
print(sorted(numbers))