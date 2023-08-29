#Ordenar tres números
Numero1 =eval(input("Ingrese el primer Numero :"))
Numero2 =eval(input("Ingrese el segundo Numero :"))
Numero3 =eval(input("Ingrese el cuarto Numero :"))
if(Numero1 < Numero2 and Numero2 < Numero3):
 print(Numero1,Numero2,Numero3 , sep = ",")
elif(Numero1<Numero2 and Numero3< Numero2):
  print(Numero1,Numero3,Numero2 , sep = ",") 
elif(Numero2 < Numero1 and Numero1 < Numero3):
 print(Numero2,Numero1,Numero3 , sep = ",")
elif(Nnumero2 < Numero1 and Numero3 < Numero1):
  print(Nnumero2,Numero3,Nnumero1 , sep = ",") 
elif(Numero3 < Numero1 and Numero1 < Numero2):
 print(Numero3,Numero1,Numero2 , sep = ",")
elif(Numero3 < Numero1 and Numero2 < Numero1):
 print(Numero3,Numero2,Numero1 , sep = ",")   