print("ingrese 3 numeros diferentes")
a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
if (a>=b>=c):
    print("el resultado final es", (c,b,a))
elif (a>=c>=b):
    print ("el resultado final es", (b,c,a))
elif (b>=c>=a):
    print("el resultado final es", (a,c,b))
elif (c>=a>=b):
    print("el resultado final es", (b,a,c))
elif (b>=a>=c):
    print("el resultado final es", (c,a,b))
elif (b>=c>=a):
    print("el resultado final es", (a,c,b))
elif (c>=b>=a):
    print ("el resultado final es", (a,b,c))