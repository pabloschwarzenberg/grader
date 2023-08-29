#Descomponer un número
x = int(input("Introduce un numero de 4 digitos: "))



# Para 1 numero
k= str(x)

f= k[0]

if((x>=0) and (x <=9)):
    print(f,"U")


# Para 2 numeros
else:
    j= k[0]
    k= k[1]
    if((x>=10) and (x <=99)):
     print(j+"D"" + "+k+"U")

# Para 3 numeros
    else:
        k= str(x)
        z= k[0]
        c= k[1]
        v= k[2]
        if((x>=100) and (x <=999)):
         print(z+"C"" + "+c+"D"" + "+v+"U")


# Para 4 numeros
        else:
            k= str(x)
            a= k[0]
            b= k[1]
            m= k[2]
            d= k[3]
            if((x>=1000) and (x <=9999)):
             print(a+"M"" + "+b+"C"" + "+m+"D"" + "+d+"U")

            else:
             print("Numero invalido")

      