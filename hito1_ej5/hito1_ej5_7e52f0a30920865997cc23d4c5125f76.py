#Cálculo del dígito verificador de un rut
rut=int(input("Indice su rut sin el guion porfavor :"))
d8 = rut%10
d7= (rut%100)//10
d6 = (rut%1000)//100
d5 = (rut%10000)//1000
d4 = (rut%100000)//10000
d3 = (rut%1000000)//100000
d2 = (rut%10000000)//1000000
d1 = (rut%100000000)//10000000
suma = (d8*2)+(d7*3)+(d6*4)+(d5*5)+(d4*6)+(d3*7)+(d2*2)+(d1*3)
resto = int(suma/11)
multi = resto * 11
resta = suma - multi
dv = 11 - resta
if(dv==11):
    print("dv=0")
elif(dv==10):
    print("dv=K")
else:
    print("dv=",dv)      