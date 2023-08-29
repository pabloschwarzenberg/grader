#Cálculo del dígito verificador de un rut
mirut = input("Ingrese su rut sin digito verificador: ")
n1 = int(mirut[-1]) * 2
n2 = int(mirut[-2]) * 3
n3 = int(mirut[-3]) * 4
n4 = int(mirut[-4]) * 5
n5 = int(mirut[-5]) * 6
n6 = int(mirut[-6]) * 7
n7 = int(mirut[-7]) * 2
if len(mirut) == 8:
    n8 = int(mirut[-8]) * 3
    total = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
else :
    total = n1 + n2 + n3 + n4 + n5 + n6 + n7
division = total / 11
mult = int(division) * 11
totaln = int(total) - mult
fin = abs(totaln - 11)
if fin == 10 :
    fin = "K"
if fin == 11 :
    fin = 0
print("dv=",fin)