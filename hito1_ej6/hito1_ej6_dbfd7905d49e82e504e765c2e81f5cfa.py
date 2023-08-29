Num_1 = eval(input("Ingrese el primer numero"))
Num_2 = eval(input("Ingrese el segundo numero"))
Num_3 = eval(input("Ingrese el tercer numero"))

if(Num_1 <= Num_2 and Num_2 <= Num_3):
    print(Num_1 , Num_2 , Num_3 , sep=",")
if(Num_1 <= Num_2 and Num_2 >= Num_3 and  Num_1 <= Num_3):
    print(Num_1 , Num_3 , Num_2 , sep=",")
if(Num_2 <= Num_1 and Num_1 <= Num_3):
    print(Num_2 , Num_1 , Num_3 , sep=",")
if(Num_2 <= Num_1 and Num_1 >= Num_3 and Num_2 <= Num_3):
    print(Num_2 , Num_3 , Num_1 , sep=",")
if (Num_3 <= Num_1 and Num_1 <= Num_2):
    print(Num_3, Num_1, Num_2, sep=",")
if(Num_3 <= Num_1 and Num_1 >= Num_2 and Num_3 <= Num_2):
    print(Num_3 , Num_2 , Num_1 , sep=",")
