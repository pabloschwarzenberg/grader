#Escribe un programa que le pida al usuario un número de hasta 4 dígitos y que te entregue la descomposición en
#Unidades, Decenas, Centenas y Miles. Ejemplos
#Para 1230 debe imprimir: 1M + 2C + 3D + 0U
#Para 36 debe imprimir: 3D + 6U

#Descomponer un número
num = int(input("Ingrese un número: "))
mil=(num%10000-num%1000)//1000
cen=(num%1000-num%100)//100
dec=(num%100-num%10)//10
uni=(num%10-num%1)//1
if mil == 0 and cen == 0 and dec == 0:
    print(str(uni) + "U")
elif mil == 0 and cen == 0:
    print(str(dec) + "D + " + str(uni) + "U")
elif mil == 0 :
    print(str(cen) + "C + " + str (dec) + "D + " + str(uni) + "U")
else:
    print( str(mil) + "M + " + str(cen) + "C + " + str(dec) + "D + " + str(uni) + "U ")

      