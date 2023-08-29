x_1=int(input("ingrese el valor de la primera x:"))
y_1=int(input("ingresa el valor de la primera y:"))
n_1=int(input("ingresa el valor del primer numero:"))
x_2=int(input("ingrese el valor de la segunda x:"))
y_2=int(input("ingresa el valor de la segunda y:"))
n_2=int(input("ingresa el valor del segundo numero:"))
res_d=((y_1)*(-y_2)+(y_1)*(y_2))
res_e=((x_1)*(-y_2)+(x_2)*(y_1))
res_f=((n_1)*(-y_2)+(n_2)*(y_1))
if res_e<0:
    b=(res_f/res_e)
    a=round(b,1)
elif res_e >0:
    b=(res_f/res_e)
    a=round(b,1)
print("x=",b)
res=((x_1)*(-x_2)+(x_1)*(x_2))
res_b=((y_1)*(-x_2)+(y_2)*(x_1))
res_c=((n_1)*(-x_2)+(n_2)*(x_1))
if res_b < 0:
    a=(res_c/res_b)
    a=round(a,1)

elif res_b >0:
    a=(res_c/res_b)
    a=round(a,1)
print("y=",a)

