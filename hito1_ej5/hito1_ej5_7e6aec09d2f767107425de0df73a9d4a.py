#Cálculo del dígito verificador de un rut
rut=int(input())
a_8=rut//10000000
a_7=rut%10000000
a_7a=a_7//1000000
a_6=rut%1000000
a_6a=a_6//100000
a_5=rut%100000
a_5a=a_5//10000
a_4=rut%10000
a_4a=a_4//1000
a_3=rut%1000
a_3a=a_3//100
a_2=rut%100
a_2a=a_2//10
a_1=rut%10

producto1=a_1*2
producto2=a_2a*3
producto3=a_3a*4
producto4=a_4a*5
producto5=a_5a*6
producto6=a_6a*7
producto7=a_7a*2
producto8=a_8*3

sumaproductos=(producto1+producto2+producto3+producto4+producto5+producto6+producto7+producto8)
parteentera=sumaproductos//11
resto=sumaproductos-(11*parteentera)
resta=11-resto

if(resta==11):
   print("dv=","0")
if(resta==10):
   print("dv=","K")
else:
   print("dv=",resta)




