num_1 = int(input("ingrese un numero "))
num_2 = int(input("ingrese un numero "))
num_3 = int(input("ingrese un numero "))
num_maximo = max(num_1 , num_2 , num_3) 
num_minimo = min(num_1 , num_2 , num_3)
num_medio= num_1 + num_2 + num_3 - num_maximo - num_minimo
print(num_minimo , ","  ,  num_medio , "," , num_maximo)