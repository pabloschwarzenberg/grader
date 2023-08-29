nu1 = int(input("Ingrese un numero : "))
nu2 = int(input("Ingrese un 2° numero :"))
nu3 = int(input("Ingrese un 3° numero : "))
Ma = max(nu1,nu2,nu3)
print(" numero mayor es : " , Ma)
Mi = min(nu1,nu2,nu3)
print("numero menor es :" , Mi)
D = (nu1 + nu2 + nu3) - Ma - Mi
print("De menor a mayor el órden es ",Mi,",",D,",", Ma) 
