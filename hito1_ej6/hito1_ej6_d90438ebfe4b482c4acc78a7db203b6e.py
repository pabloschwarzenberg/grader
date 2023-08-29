#Ordenar tres números
Var_1 = int(input("primer numero :"))
Var_2 = int(input("segundo numero :"))
Var_3 = int(input("tercer numero :"))
print("el orden de sus numeros es")
if Var_1 > Var_2 :
   if Var_2 > Var_3:
    print(Var_3," , ", Var_2 ," , " ,Var_1)
   elif Var_3 > Var_1:
    print(Var_2," , ", Var_1, " , ", Var_3)
   else:
    print(Var_2, " , " ,Var_3 ," , ",Var_1)
else:
   if Var_1 > Var_3:
    print(Var_3 ," , ",Var_1," , ", Var_2)
   elif Var_3 > Var_2:
    print(Var_1," , ", Var_2, " , ", Var_3)
   else:
    print(Var_1 ," , ", Var_3 ," , ", Var_2)