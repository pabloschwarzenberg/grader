#Ordenar tres números

print("ingrese distintos numeros con distintos valores")
a = int(input("ingrese un primer numero: "))
b= int(input("ingrese un segundo numero: "))
c= int(input("ingrese un tercer numero: "))
if (a <= b <= c):

    print("los numeros de menor a mayor son",a, ",", b, ",", c)
elif(b <= a <= c):
    print("los numeros de menor a mayor son",b, ",", a, ",", c)
elif(a <= c <= b):
    print("los numeros de menor a mayor son",a, ",", c, ",", b)
elif(c <= b <= a):
    print("los numeros de menor a mayor son",c, ",", b, ",",a)
elif(b <= c <= a):
    print("los numeros de menor a mayor son",b, ",", c, ",", a)
elif(c <= a <= b):
    print("los numeros de menor a mayor son",c, ",", a, ",", b)
                    
