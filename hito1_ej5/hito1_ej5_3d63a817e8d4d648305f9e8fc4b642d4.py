#Cálculo del dígito verificador de un rut
#Entradas
rut = str(input("Ingrese el número de rut a evaluar: "))

i=-1
j=1
n_f=0
while i >= -len(rut):
    pos_n = rut[i]
    if j < 7:
        calc = -i + 1
        n_2 =int(int(pos_n)*int(calc))
    elif j>=7:
        calc = -i-5
        n_2 = int(int(pos_n)*int(calc))

    n_f += n_2
    j+=1
    i-=1

dv = n_f%11
dv = 11 - dv
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "k"
    
print("dv =", dv)