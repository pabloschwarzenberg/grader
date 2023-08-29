#Cálculo del dígito verificador de un rut
rut=int(input())
x_8=rut//10000000
x_7=rut%10000000
x_7a=x_7//1000000
x_6=x_7%1000000
x_6a=x_6//100000
x_5=rut%100000
x_5a=x_5//10000
x_4=rut%10000
x_4a=x_4//1000
x_3=rut%1000
x_3a=x_3//100
x_2=rut%100
x_2a=x_2//10
x_1a=rut%10

prod1=x_1a*2
prod2=x_2a*3
prod3=x_3a*4
prod4=x_4a*5
prod5=x_5a*6
prod6=x_6a*7
prod7=x_7a*2
prod8=x_8*3

suma=(prod1+prod2+prod3+prod4+prod5+prod6+prod7+prod8)
parte_entera=suma//11
resto=suma-(11*parte_entera)
resultado=11-resto

if(resultado==10):
    print("dv=","K")
if(resultado==11):
    print("dv=",0)
if(1<=resultado<=9):
    print("dv=",resultado)
    