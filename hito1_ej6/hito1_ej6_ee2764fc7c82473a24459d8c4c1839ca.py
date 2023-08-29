#Ordenar tres números
n1= int(input("ingrese numero 1:",))
n2= int(input("ingrese numero 2:",))
n3= int(input("ingrese numero 3:",))
if(n1<=n2<=n3):
    print ("los numeros de menor a mayor son:", n1,',',n2,',',n3)
if(n2<=n3<=n1):
    print ("los numeros de menor a mayor son:", n2,',' ,n3,',' ,n1)
if(n2<=n1<=n3):
    print ("los numeros de menor a mayor son:", n2,',' ,n1,',' ,n3)
if(n3<=n2<=n1):
    print ("los numeros de menor a mayor son:", n3,',' ,n2,',' ,n1)
if(n3<=n1<=n2):
    print ("los numeros de menor a mayor son:", n3,',' ,n1,',' ,n2)
if(n1<=n3<=n2):
    print ("los numeros de menor a mayor son:", n1,',' ,n3,',' ,n2)      