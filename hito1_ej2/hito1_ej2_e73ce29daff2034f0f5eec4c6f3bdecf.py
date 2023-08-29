#Contestador de celular
n= int(input("ingrese un numero entero de 8 digitos:"))
h= int(input("ingrese hora de llamamda entre 0 y 23: "))

if h>0 and h<7:
    print("CONTESTAR")
elif h<14 :
    if n%1000 == 909 :
        print("CONTESTAR")
    else :
        print("NO CONTESTAR")
elif h<17 :
    print("NO CONTESTAER")
elif h<=19 :   
    if int(n/100000) ==877 :
        print(" NO CONTESTAR")
    else:
        print(" CONTESTAR")

else : 
    print("NO CONTESTAR")
