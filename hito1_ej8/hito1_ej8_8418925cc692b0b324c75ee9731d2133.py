#Descomponer un número
n=int(input("Ingrese un número de hasta 4 dígistos:")) #número
a = str(n)
if len(a)==4:
    x=a[0]+"M"+"+"+a[1]+"C"+"+"+a[2]+"D"+"+"+a[3]+"U"
    print(x)
elif len(a)==3:
    y=a[0]+"C"+"+"+a[1]+"D"+"+"+a[2]+"U"
    print(y)
elif len(a)==2:
    z=a[0]+"D"+"+",a[1]+"U"
    print(z)
elif len(a)==1:
    w=a[0]+"U"
    print(w)   
else:
    print("El número fue mal ingresado")
 