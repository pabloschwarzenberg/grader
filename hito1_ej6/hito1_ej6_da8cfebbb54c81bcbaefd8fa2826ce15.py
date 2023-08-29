#Ordenar tres números
n1=int(input("ingresar primer numero:"))
n2=int(input("ingresar segundo numero:"))
n3=int(input("ingresar tercer numero:"))
if n1 >= n2 >= n3 :
     print("de menor a mayor es:",n3,",",n2,",",n1)
if n3 >= n2 >= n1 :
     print("de menor a mayor es:",n1,",",n2,",",n3)
if n2 >= n3 >= n1 :
     print("de menor a mayor es:",n1,",",n3,",",n2)
if n3 >= n1 >= n2 :
     print("de menor a mayor es:",n2,",",n1,",",n3)
if n2 >= n1 >= n3 :
     print("de menor a mayor es:",n3,",",n1,",",n2)
if n1 >= n3 >= n2 :
     print("de menor a mayor es:",n2,",",n3,",",n1)