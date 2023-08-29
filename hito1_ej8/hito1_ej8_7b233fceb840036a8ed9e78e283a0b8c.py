#Descomponer un número
num = int(input("Ingresa un número de hasta 4 dígitos: "))
n = num
Uni = num%10
num = num//10

Dec = num%10
num = num//10

Cen = num%10
num = num//10

Mil = num%10
# Mostrar los resultados

if 0 <= n  <10:
    cadenaderespuesta = str(Uni)+ 'U'
if 10 <= n <100:
    cadenaderespuesta = str(Dec)+ 'D+  ' + str(Uni) + 'U'
if 100 <= n <1000:
    cadenaderespuesta = str(Cen)+'C+ '  + str(Dec) + 'D+ ' + str(Uni)  +'U'
if 1000 <= n <10000:
    cadenaderespuesta = str(Mil)+'M+ ' + str(Cen)+ 'C+ ' + str(Dec)+ 'D+ ' + str(Uni) + 'U'
print(cadenaderespuesta)