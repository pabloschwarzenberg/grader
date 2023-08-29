#Cálculo del dígito verificador de un rut
n = int(input("Ingrese su numero de rut para obtener su codigo rutificador:  "))
suma = ((n[1]) * (n[8]) + (n[2]) * (n[7]) + (n[3]) * (n[6]) + (n[4]) * (n[5]))
resto = (suma / 11)
total = suma - (11 * resto)
db = (total - 11)

while n == 8:
    if db == 11:
        print("dv = 0")
        break
    elif db == 10:
        print("dv = k")
        break
    else:
        print("dv =  " , db)
