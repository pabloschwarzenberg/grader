rut = input("Rut (primeros 8 digitos sin puntos): ")
rut_list = []
num_cal = [2,7,6,5,4,3,2]

for i in rut:
    rut_list.append(i)

rut_list_int = [int(x) for x in rut_list]
def calculo(lis1, list2):
    suma = 0
    y = 0
    for x in lis1:
        multi = x * list2[y]
        suma += multi
        y +=1
    return suma

calculo = calculo(num_cal, rut_list_int)
def dv(n):
    x = n/11
    y = n-(11*x)
    z = 11-y
    if (z == 11):
        return 0
    elif (z == 10):
        return "k"
    return(z)

print(dv(calculo))