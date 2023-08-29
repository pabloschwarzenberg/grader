#Cálculo del dígito verificador de un rut
rut=int(input("ingrese rut: "))
a=rut%10    #8#2
b=rut%100//10   #7#3
c=rut%1000//100    #6#4
d=rut%10000//1000    #5#5
e=rut%100000//10000   #4#6
f=rut%1000000//100000   #3#7
g=rut%10000000//1000000   #2#2
h=rut%100000000//10000000   #1#3

suma = (a*2)+(b*3)+(c*4)+(d*5)+(e*6)+(f*7)+(g*2)+(h*3)
div = suma//11

resto = suma - (11*div) 
dv = 11 - resto
print(dv)

if (dv==11):
  print("dv=0")

elif(dv==10):
  print("dv=k")

else:
  print("dv=",dv)
