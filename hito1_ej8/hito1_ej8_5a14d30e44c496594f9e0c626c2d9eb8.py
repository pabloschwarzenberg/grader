#Descomponer un número
n1 = input("Ingrese un numero de hasta 4 digitos: ")
 
if len(n1) ==4:
    print("{}M + {}C +{}D + {}U".format(n1[0], n1[1], n1[2], n1[3]))
elif len(n1) ==3:
    print("{}C + {}D + {}U".format(n1[0], n1[1], n1[2]))
elif len(n1) ==2:
    print("{}D + {}U".format(n1[0], n1[1]))
elif len(numero) ==1:
    print("{}U".format(n1[0]))         