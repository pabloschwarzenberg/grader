#Contestadora
numero1=True
numero2=False
n=input("Ingrese el número telefónico:")
h=input("Ingrese la hora de llamada:")
n1=n[5::]
n2=n[0:3]
print(n1,n2)
if n1==909:
    numero1=True
    
if n2==877:
    numero2=False

h=int(h)    
if h>=0 and h<=7:
 print('CONTESTAR')

elif h<=14 and numero1:
 print('CONTESTAR')

elif h>=17 and h<=19 and numero2:
 print("CONTESTAR")

else:
    print("NO CONTESTAR")
      