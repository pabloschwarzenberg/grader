n1 = int(input("ingrese numero entero Nº1="))
n2 = int(input("ingrese numero entero Nº2="))
n3 = int(input("ingrese numero entero Nº3="))
if (n1>=n2 and n2>=n3):
    print (n3,",", n2,",",n1)
elif (n2>=n1 and n1>=n3):
    print (n3,",",n1,",",n2)
elif (n3>=n1 and n1>=n2):
    print (n2,",",n1,",",n3)
elif (n3>=n1 and n1>=n2):
    print (n1,",",n2,",",n3)
elif (n1>=n3 and n3>=n2):
    print (n2,",",n3,",",n1)
elif (n2>=n3 and n3>=n1):
    print (n1,",",n3,",",n2)

