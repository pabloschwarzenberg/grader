#Descomponer un número
numero = input("Ingrese un numero de hasta 4 digitos: ")
 
if len(numero) ==4:
    print("{}M + {}C +{}D + {}U".format(numero[0], numero[1], numero[2], numero[3]))
elif len(numero) ==3:
    print("{}C + {}D + {}U".format(numero[0], numero[1], numero[2]))
elif len(numero) ==2:
    print("{}D + {}U".format(numero[0], numero[1]))
elif len(numero) ==1:
    print("{}U".format(numero[0])) 