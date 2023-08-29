#Cálculo del dígito verificador de un rut
n = input("Rut (primeros 8 digitos sin puntos): ")
def dv(n):
    x = sum(list(n))
    e = math.floor(x / 11)
    f = x - (11 * e)
    h = 11 - f
    
    if (h == 11):
        h = "0"
    elif (h == 10):
        h = "k"
    return(h)

print("dv=",dv(h))