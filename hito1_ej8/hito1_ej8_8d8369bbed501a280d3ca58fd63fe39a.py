#Descomponer un número
x=int(input(">"))
u=x%10
d=int((x-u)/10)%10
c=int((x-d)/100)%10
m=int((x-c)/1000)%10
print(m,"M +",c,"C +",d,"D +",u,"U")      