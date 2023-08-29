#Descomponer un número
x=int(input("Ingrese su numero"))
m=int(x//1000)
c=int((x-m*1000)/100)
d=int((x-m*1000-c*100)/10)
u=int((x-m*1000-c*100-d*10)/1)
print(m,"M+",c,"C+",d,"D+",u,"U") 