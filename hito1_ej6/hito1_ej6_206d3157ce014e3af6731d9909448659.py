#Ordenar tres números
     
print ("ingrese numeros para ser ordenados de menor a mayor")

primer_numero = int(input("ingrese un numero 1/3: "))
segundo_numero = int(input("ingrese un numero 2/3: "))
tercer_numero = int(input("ingrese un numero 3/3: "))
     
a = min(primer_numero, segundo_numero, tercer_numero)
b = max(primer_numero, segundo_numero, tercer_numero)
c = primer_numero + segundo_numero + tercer_numero - a - b

#print(f"El orden de menor a mayor es:{a}, {c}, {b} ")

print ("El orden de menor a mayor es: {}, {}, {}" .format(a,c,b))