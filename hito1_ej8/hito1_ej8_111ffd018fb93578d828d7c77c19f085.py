#Descomponer un número
import math
n = eval(input("ingrese un numero de 4 cifras : "))
miles = n/1000
m = math.trunc(miles)
cientos = (n/100)-(m*10)
c = math.trunc(cientos)
decenas = (n/10)-((m*100)+(c*10))
d = math.trunc(decenas)
unidades = (n-((m*1000)+(c*100)+(d*10)))
U = math.trunc(unidades)
if n > 1000:
    print(m,"M+", c,"C+", d,"D+", U,"U")
else:
    if 100 < n <= 999:
        print(c,"C+", d,"D+", U,"U")
    else:
        if 10 < n <= 99:
            print(d,"D+", U,"U")
        else:
            print(U,"U")
    

