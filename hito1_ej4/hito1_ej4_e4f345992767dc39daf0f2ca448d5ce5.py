#Conversión de Decimal a Binario
def d_a_b(d):
    if d <=0:
       return "0"
    b = ""
    while d > 0:
            residuo = int(d % 2)
            d = int(d / 2)
            b = str(residuo) + b
    return b

d = float(input("Holi bb ingresa un número decimal: "))
b = d_a_b(d)
print("resultado=",b)      