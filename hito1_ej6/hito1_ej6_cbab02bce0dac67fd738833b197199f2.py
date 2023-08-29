#Ordenar tres números
D= int(input ('Ingrese el primer numero :'))
E= int(input ('Ingrese el segundo numero:'))
F= int(input ('Ingrese el tercer numero:'))
Min= min (D,E,F)
Max= max (D,E,F)
PM= (D + E + F) - Max - Min
print (Min,',', PM ,',',Max)