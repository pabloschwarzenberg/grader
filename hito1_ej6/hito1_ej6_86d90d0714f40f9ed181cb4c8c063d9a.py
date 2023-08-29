#Ordenar tres números
#Ingreso de los números
primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))
tercer_numero = int(input("Ingrese el tercer número: "))
#Orden de los números
numero_mayor = max(primer_numero, segundo_numero, tercer_numero)
numero_menor = min(primer_numero, segundo_numero, tercer_numero)
numero_medio = (primer_numero + segundo_numero + tercer_numero) - numero_mayor - numero_menor
#Print
print(str(numero_menor) + "," + str(numero_medio) + "," + str(numero_mayor))
