#Desconponer un numero.
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
