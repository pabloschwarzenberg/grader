#Ordenar tres números
a = int(input("ingrese primer numero "))
b = int(input("ingrese segundo numero "))
c = int(input("ingrese tercer numero "))
if a<=b<=c:
    print ("los numero son  " +str(a)+" , "+str(b)+" , " +str(c)) 
elif b<=a<=c:
    print ("los numero son  " +str(b)+" , " +str(a)+" , " +str(c)) 
elif c<=b<=a: 
    print ("los numero son " +str(c)+" , " +str(b)+" , " +str(a)) 
elif b<=c<=a:
    print ("los numero son  " +str(b)+" , " +str(c)+" , " +str(a)) 
if a<=c<=b:
    print ("los numero son  " +str(a)+" , " +str(c)+" , " +str(b))
if c<=a<=b:
    print ("los numero son  " +str(c)+" , " +str(a)+" , " +str(b))           