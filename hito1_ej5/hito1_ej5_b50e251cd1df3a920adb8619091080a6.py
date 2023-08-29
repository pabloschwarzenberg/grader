#Cálculo del dígito verificador de un rut
d1 = int(input("Ingrese digito 1 del rut: "))
d2 = int(input("Ingrese digito 2 del rut: "))
d3 = int(input("Ingrese digito 3 del rut: "))
d4 = int(input("Ingrese digito 4 del rut: "))
d5 = int(input("Ingrese digito 5 del rut: "))
d6 = int(input("Ingrese digito 6 del rut: "))
d7 = int(input("Ingrese digito 7 del rut: "))
d8 = int(input("Ingrese digito 8 del rut: "))

suma = (d8*2)+(d7*3)+(d6*4)+(d5*5)+(d4*6)+(d3*7)+(d2*2)+(d1*3)
resto = int(suma/11)
multi = resto*11
resta = suma - multi
dv = 11 - resta