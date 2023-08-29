#Ordenar tres números
print("Programa para calcular mayores entre 3 números")
Num_1=int(input("Numero 1: "))
Num_2=int(input("Numero 2: "))
Num_3=int(input("Numero 3: "))
if Num_1<Num_2 :
   if Num_1<Num_3 :
      Menor_1=Num_1
      if Num_2<Num_3 :
            Menor_2=Num_2
            Menor_3=Num_3
      else :
           Menor_2=Num_3
           Menor_3=Num_2
else :
    if Num_2<Num_3 :
      Menor_1=Num_2
      if Num_1<Num_3 :
            Menor_2=Num_1
            Menor_3=Num_3
      else :
            Menor_2=Num_3
            Menor_3=Num_1
    else :
      Menor_1=Num_3
      Menor_2=Num_2
      Menor_3=Num_1

print(Menor_1,",",Menor_2,",",Menor_3)     