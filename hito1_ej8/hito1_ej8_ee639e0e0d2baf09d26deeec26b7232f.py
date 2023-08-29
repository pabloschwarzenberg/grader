#Descomponer un número
#Entradas
N =int(input("Ingrese 4 digitos: "))
#Ejecucion
#primer digito
if  N > 999 :
      M_1 = (N//1000)
      R_1 = (N%1000)
else:
      M_1 = 0 
      R_1 = N
#segundo digito
if R_1 >99 and R_1<1000  :

    C_1 = (R_1//100)
    R_2 = (R_1%100)

else :
    C_1 = 0
    R_2 = 0
#Tercer digito
if R_2 > 9 and R_2 < 100:
      R_3 = (R_2//10)
      D_1 = (R_2%10)
else :
      D_1 = 0
      R_3 = 0
#Ultimo digito
if D_1 >= 1 and D_1 < 9:
      R_4 = (D_1//1)

else :
      R_4 = 0

#Salida
print(str(M_1)+ "M" + "+" + str(C_1) +"C" + "+" + str(R_3) + "D" + "+" + str(R_4) + "U")      