#Ordenar tres números
a = int(input("Ingrese el 1° número: "))
b = int(input("Ingrese el 2° número: "))
c = int(input("Ingrese el 3° número: "))

if a >= b >= c :
 print(c, b, a) 

elif a > b <= c : 
 print(b, c, a)


#---------
elif b >= a >= c :
 print(c, a, b)

elif b > a <= c : 
 print(a, c, b)

#-----------

elif c >= a >= b :
 print(b, a, c)

elif c > a <= b : 
 print(a, b, c)