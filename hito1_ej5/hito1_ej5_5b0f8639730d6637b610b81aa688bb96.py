from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11
def imprimir_rut(rut_1):
    if rut_1==10:
        rut_1="10"
        rut_1= rut_1.replace('10','K',1)
        print("dv=" + str(rut_1))
    elif rut_1<=9:
        print("dv="+str(rut_1))

rut_1=(input("Ingrese el rut:"))
rut_1=digito_verificador(rut_1)
imprimir_rut(rut_1)

