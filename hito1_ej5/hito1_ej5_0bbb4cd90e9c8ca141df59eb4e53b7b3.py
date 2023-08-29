import operator


rut=input("Ingrese el rut: ")
rut_list = []
contar = 0

for a in rut:
    rut_list.append(a)
    contar = contar + 1

if contar == 8:
    mult_list = [3,2,7,6,5,4,3,2]
if contar == 7:
    mult_list = [2,7,6,5,4,3,2]

rut_list_int = [int(x) for x in rut_list]
multiplicacion = list(map(operator.mul, rut_list_int, mult_list))

suma = sum(list(multiplicacion))
division = int(suma/11)
resta = suma - (11*division)
valor_final = 11 - resta

if valor_final == 11:
    dv=0
elif valor_final == 10:
    dv="k"
else:
    dv=valor_final

print(suma)

print("dv=" + str(dv))