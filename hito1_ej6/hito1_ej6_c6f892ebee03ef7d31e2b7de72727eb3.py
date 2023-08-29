#Ordenar tres números
n1 = int(input("ingrese primer numero"))
n2 = int(input("ingrese segundo numero"))
n3 = int(input("ingrese tercer numero"))

v= min(n1,n2,n3)
v2= max(n1,n2,n3)
v3= (n1+n2+n3)-v-v2
         
print("el orden es:{},{},{}". format(v,v3,v2))
