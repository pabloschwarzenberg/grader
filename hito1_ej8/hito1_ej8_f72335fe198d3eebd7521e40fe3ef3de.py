#Descomponer un número

num=(input("ingrese un número entero de hasta 4 cifras: "))

num_list=[x for x in num]

if len(num_list)==4:
    print(num_list[0], "M +" , num_list[1] , "C +", num_list[2] , "D +", num_list[3] , "U ")

elif len(num_list)==3:
    print(num_list[0] , "C +", num_list[1] , "D +", num_list[2] , "U ")

elif len(num_list)==2:
    print(num_list[0] , "D +", num_list[1] , "U ")

elif len(num_list)==1:
    print(num_list[0] , "U ")