numero=int(input("inserte su rut sin su dato verificador:"))
n1= (numero//10000000) * 3 
n2= ((numero%10000000)//1000000) * 2
n3= (((numero%10000000)%1000000)//100000) * 7
n4= ((((numero%10000000)%1000000)%100000)//10000) * 6
n5= (((((numero%10000000)%1000000)%100000)%10000)//1000) * 5
n6= ((((((numero%10000000)%1000000)%100000)%10000)%1000)//100) * 4
n7= (((((((numero%10000000)%1000000)%100000)%10000)%1000)%100)//10) * 3
n8= (((((((numero%10000000)%1000000)%100000)%10000)%1000)%100)%10) * 2
sn= ((n1) + (n2) + (n3) + (n4) + (n5) + (n6) + (n7) + (n8))
re= (sn) / 11
re2= (sn) - (11 * (re))
re3= 11 - (re2)
if (re)==11:
    print("dv=0")
elif (re)==10:
    print("dv=K")
else:
    print("dv=",re3)