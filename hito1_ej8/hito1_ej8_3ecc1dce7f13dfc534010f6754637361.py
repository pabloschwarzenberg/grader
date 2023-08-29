#Descomponer un número
numero= int(input("Ingrese un número de hasta 4 cifras: "))
miles=int(numero/1000)
centenas=int((numero-miles*1000)/100)
decenas=int((numero-centenas*100-miles*1000)/10)
unidades=int((numero-miles*1000-centenas*100-decenas*10))
if miles!=0:
    print(miles, 'M+', centenas, 'C+', decenas, 'D+', unidades, 'U')
if miles==0 and centenas!=0:
    print(centenas, 'C+', decenas, 'D+', unidades, 'U')
if miles==0 and centenas==0 and decenas!=0:
    print(decenas, 'D+', unidades, 'U')
if miles==0 and centenas==0 and decenas==0 and unidades!=0:
    print(unidades, 'U')
    