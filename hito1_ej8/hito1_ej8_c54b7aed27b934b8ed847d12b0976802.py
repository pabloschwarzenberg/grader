#Descomponer un número
n1=int(input("ingresar numero: "))
m1=(n1//1000)
c1=((n1-(m1*1000))//100)
d1=((n1-(m1*1000)-(c1*100))//10)    
u1=(n1-(m1*1000)-(c1*100)-(d1*10))
print (m1,"M +",c1,"C +",d1,"D +",u1,"U") 
