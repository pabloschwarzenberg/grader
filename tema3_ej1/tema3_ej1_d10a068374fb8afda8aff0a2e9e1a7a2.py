

def suma_divisores(a):
    suma = 0
    for b in range (1,a):
        if a % b == 0:
            suma +=b
    hey = suma 
    if hey == 1:

     return suma, True 
    else:
        return suma, False