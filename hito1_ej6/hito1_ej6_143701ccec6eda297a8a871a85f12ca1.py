#Ordenar tres números
primer_num = eval(input("Ingrese el primer numero: "))
segundo_num = eval(input("Ingrese el segundo numero: "))
tercer_num = eval(input("Ingrese el segundo numero: "))

Max = max(primer_num,segundo_num,tercer_num)
Min = min(primer_num,segundo_num,tercer_num)

X = (primer_num + segundo_num + tercer_num) - Max - Min

print("Así quedarian los numeros ordenados de menor a mayor: ", Min ,", ", X ,", ", Max ,".")