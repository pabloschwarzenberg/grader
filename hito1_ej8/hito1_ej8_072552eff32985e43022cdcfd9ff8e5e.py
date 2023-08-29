#Descomponer un número
a=int(input("Introduzca un número: "))
b=a//1000
bb=b%10
c=a//100
cc=c%10
d=a//10
dd=d%10
e=a//1
ee=e%10
print(str(bb)+"M"+"+"+str(cc)+"C"+"+"+str(dd)+"D"+"+"+str(ee)+"U")