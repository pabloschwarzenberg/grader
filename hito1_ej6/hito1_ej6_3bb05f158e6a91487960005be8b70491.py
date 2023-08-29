#Ordenar tres números
print ("Ingrese 3 numeros ")
a = eval(input("Ingrese numero 1: "))
b = eval(input("Ingrese numero 2: "))
c = eval(input("Ingrese numero 3: "))

if (a<=b) and (a<=c)and(b<=c) :
    print("Los numeros de menor a mayor son:",a,",",b,",",c)
    
elif (b<=a) and (b<=c) and (a<=c):
    print("Los numeros de menor a mayor son:",b,",",a,",",c)
    
elif (c<=a) and (c<=b)and (b<=a):
    print("Los numeros de menor a mayor son:",c,",",b,",",a)
    
elif(a<=b) and (a<=c) and (c<=b):
    print("Los numeros de menor a mayor son:",a,",",c,",",b)

elif (b<=a) and (b<=c) and (c<=a):
    print("Los numeros de menor a mayor son:",b,",",c,",",a)

elif (c<=a) and (c<=b)and (a<=b):
    print("Los numeros de menor a mayor son:",c,",",a,",",b)     