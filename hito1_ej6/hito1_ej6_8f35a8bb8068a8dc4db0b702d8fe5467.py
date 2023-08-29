print("Ingrese 3 números enteros")

a = eval(input("Ingrese A:"))
b = eval(input("Ingrese B:"))    
c = eval(input("Ingrese C:"))

if a >= b and b >= c:

 print("\nEl orden de los números de menor a mayor es:\n")
 print(c,b,a,sep=",")

elif b >= c and c >= a:
 print("\nEl orden de los números de menor a mayor es:\n")
 print(a,c,b,sep=",")
    
elif c >= a and a >= b:
 print("\nEl orden de los números de menor a mayor es:\n")
 print(b,a,c,sep=",")

elif c >= b and b >= a:
 print("\nEl orden de los números de menor a mayor es:\n")
 print(a,b,c,sep=",")

elif a >= c and c >= b:
 print("\nEl orden de los números de menor a mayor es:\n")
 print(b,c,a,sep=",")

elif b >= a and a >= c:
 print("\nEl orden de los números de menor a mayor es:\n")
 print(c,a,b,sep=",") 
 