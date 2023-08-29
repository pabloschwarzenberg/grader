# completa el código de la función
def amigos(x,y):
    suma_x = 0
    suma_y = 0
    for i in range(1,x):
        if x % i==0:
            suma_x +=i
    for i in range(1,y):
        if y % i==0:
            suma_y +=i
    return suma_x==y and suma_y==x