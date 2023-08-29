numero = input("Ingrese un número de hasta 4 digitos: ")
num_list = []
contar=0

for a in numero:
    num_list.append(a)
    contar += 1

num_list_int = [int(x) for x in num_list]

if contar ==1:
    print(str(num_list_int[0]) + "U")
if contar == 2:
    print(str(num_list_int[0]) + "D+" + str(num_list_int[1]) + "U")
if contar == 3:
    print(str(num_list_int[0]) + "C+" + str(num_list_int[1]) + "D+" + str(num_list_int[2]) + "U")
if contar == 4:
    print(str(num_list_int[0]) + "M+" + str(num_list_int[1]) + "C+" + str(num_list_int[2]) + "D+" + str(num_list_int[3]) + "U")






