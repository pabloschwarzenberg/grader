#Descomponer un número
num=int(input("Ingrese un número de hasta 4 dígitos: "))
mil=num%1000 
mil1=num-mil  
n1=mil1/1000   

cen=mil%100   
cen1=mil-cen    
n2=cen1/100    

dec=cen%10   
dec1=cen-dec   
n3=dec1/10

n4=dec

if n1==0 and n2!=0 and n3!=0:
    print(int(n2),"C +",int(n3),"D +",int(n4),"U")

elif n1==0 and n2==0 and n3!=0:
    print(int(n3),"D +",int(n4),"U")

elif n1==0 and n2==0 and n3==0:
    print(int(n4),"U")

else:
    print(int(n1),"M +",int(n2),"C +",int(n3),"D +",int(n4),"U")