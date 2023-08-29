#Descomponer un número
NUMBER_1 = int(input("Ingrese el numero que desea descomponer : "))
print (NUMBER_1)

NUMBER_2 = list(str(NUMBER_1))
print (NUMBER_2)

if len(NUMBER_2) == 4:
    print (NUMBER_2[0]+'M' , "+" , NUMBER_2[1]+'C' , "+" , NUMBER_2[2] + 'D' , "+" ,  NUMBER_2[3] + 'U')

elif len(NUMBER_2) == 3:
    print (NUMBER_2[0]+'C' , "+" , NUMBER_2[1] + 'D' , "+" ,  NUMBER_2[2] + 'U')

elif len(NUMBER_2) == 2:
    print (NUMBER_2[0] + 'D' , "+" ,  NUMBER_2[1] + 'U')

elif len(NUMBER_2) == 1:
    print (NUMBER_2[0] + 'U')