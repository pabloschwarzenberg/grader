#Descomponer un número
num=list(input("ingrese numero: "))
num.reverse()
n1,n2,n3,n4="U","D","C","M"
if len(num)==4:
    suma=num[0]+n1,num[1]+n2,num[2]+n3,num[3]+n4
elif len(num)==3:
    suma=num[0]+n1,num[1]+n2,num[2]+n3
elif len(num)==2:
    suma=num[0]+n1,num[1]+n2
elif len(num)==1:
    suma=num[0]+n1
l1=list(suma)
l1.reverse()
junta="+".join(l1)
print(junta)