rut= int(input("ingrese numero de rut sin puntos y sin digito verificador:",))

n1= (rut%100000000)
n2= (rut%10000000//10**7)
n3= (rut%1000000//10**6)
n4= (rut%100000//10**5)
n5= (rut%10000//10**4)
n6= (rut%1000//10**3)
n7= (rut%100//10**2)
n8= (rut%10//10)

#calculo numero verificador
suma= (n1*2 + n2*3 + n3*4 + n4*5 + n5*6 + n6*7 + n7*2 + n8*3)
calculo= suma//11
r_s= suma - (11*calculo)
calculo= (11 - r_s)
if(r_s== 11):
  print(0)
if(r_s== 10):
  print(k)
print("el digito verificadores:", r_s)  