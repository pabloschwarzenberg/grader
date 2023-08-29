#Descomponer un número
num = input("Ingrese número de 4 digitos: \n")
if len(num) == 4:
 u = num[3]
 d = num[2]
 c = num [1]
 um = num [0]
 print("{}M + {}C + {}D + {}U".format(um,c,d,u))
elif len(num)== 3:
 u = num[2]
 d = num[1]
 c = num[0]
 print("{}C + {}D + {}U".format(c,d,u))
elif len(num)==2:
 u = num[1]
 d = num[0]
 print("{}D + {}U".format(d,u))
elif len(num)==1:
 u = num[0]
 print("{}U".format(u))
else:
    print("Ingrese un número de hasta 4 digitos")