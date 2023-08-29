#Ordenar tres números
a=eval(input("ingrese un primer numero:"))
b=eval(input("ingrese un segundo numero:"))
c=eval(input("ingrese un tercer numero:"))
d=max(a,b,c)
print("el numero mayor es :", d)
e=min(a,b,c)
print("el numero menor es :", e)
h=(a+b+c)-d-e
print("ordena de menor a mayor",e,",",h,",",d)