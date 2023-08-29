#Descomponer un número
num= int(input("Ingrese un número: "))

m= num//1000
c= (num%1000)//100
d= ((num%1000)%100)//10
u= ((num%1000)%100)%10

print("{}M + {}C + {}D + {}U".format(m,c,d,u))
