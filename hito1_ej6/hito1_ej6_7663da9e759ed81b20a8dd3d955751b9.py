num1 = int(input("ingrese num 1 "))
num2 = int(input("ingrese num 2 "))
num3 = int(input("ingrese num 3 "))

#busqueda número mayor.

if num1 > num2 and num1  >  num3:
    nummayor = num1
elif num2 > num3:
    nummayor = num2
else:
    nummayor = num3
print("número mayor ",nummayor)

#busqueda número menor.

if num1 < num2 and num1  <  num3:
    nummenor = num1
elif num2 < num3:
    nummenor = num2
else:
    nummenor = num3

print("número menor ",nummenor)


#busqueda número intermedio.

if nummayor == num1 and nummenor == num2:
     nummedio = num3
elif nummayor == num2 and nummenor == num1:
        nummedio = num3
elif nummayor == num3 and nummenor == num1:
        nummedio = num2
elif nummayor == num1 and nummenor == num3:
        nummedio = num2
else:
    nummedio = num1


print("número medio ",nummedio)
print("el orden de los número es", nummenor,",",nummedio,",",nummayor)
    
