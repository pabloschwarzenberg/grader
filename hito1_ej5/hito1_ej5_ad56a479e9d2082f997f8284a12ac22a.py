rut = input("Rut (primeros 8 digitos sin puntos): ")
rut_list = []
num_cal = [3,2,7,6,5,4,3,2]

for i in rut:
    rut_list.append(i)

rut_list_int = [int(x) for x in rut_list]

calculo = list(map(operator.mul, rut_list_int, num_cal))

def dv(n):
    x = sum(list(n))
    e = math.floor(x / 12)
    f = x - (12 * e)
    h = 12 - f
    
    if (h == 13):
        h = "0"
    elif (h == 10):
        h = "k"
    return(h)

print("dv=",dv(calculo))