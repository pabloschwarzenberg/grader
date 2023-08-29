#Descomponer un número
numero=int(input("introdusca numero:"))
largo=len(str(numero))
if largo==1:
    print(str(numero)+"U")
elif largo==2:
    print(str(numero)[0]+"D+"+str(numero)[1]+"U")
elif largo==3:
    print(str(numero)[0]+"C+"+str(numero)[1] + "D+" + str(numero)[2] + "U")
else:
    print(str(numero)[0]+"M+"+str(numero)[1]+"C+"+str(numero)[2]+"D+"+str(numero)[3]+"U")