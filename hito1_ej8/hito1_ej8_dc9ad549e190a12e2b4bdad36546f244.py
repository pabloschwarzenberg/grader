#Descomponer un número
num= input("ingrese un numero de hasta 4 digitos: ")

if(len(num) == 4) :
    print(" {}M + {}C + {}D + {}U ".format( num[0], num[1], num[2], num[3]))
elif(len(num) == 3) :
   print(" {}C + {}D + {}U ".format( num[0], num[1], num[2]))
elif(len(num) == 2) :
   print(" {}D + {}U ".format( num[0], num[1]))
elif(len(num) == 1) :
   print(" {}U ".format( num[0]))      