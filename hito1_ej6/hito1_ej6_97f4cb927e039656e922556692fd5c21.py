a=int(input("ingresa nota: "))
b=int(input("ingresa nota: "))
c=int(input("ingresa nota: "))
d=min(a , b , c)
e=max(a , b , c)
f=(a + b + c)- d - e
print("los numeros ordenados son: {},{},{}",(d,f,e) )