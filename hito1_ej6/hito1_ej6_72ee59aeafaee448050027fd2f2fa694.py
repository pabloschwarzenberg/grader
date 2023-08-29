#Ordenar tres números
print("ingresa 3 numeros")
a=int(input("ingresa el 1º numero: "))
b=int(input("ingresa el 2º numero: "))
c=int(input("ingresa el 3º numero: "))

d=a,b,c
e=b,c,a
f=c,a,b
g=c,b,a
h=a,c,b
i=b,a,c

if a<=b<=c:
  print("el orden creciente de los numeros es: ",d)
else:
    if b<=c<=a:
      print("el orden creciente de los numeros es: ",e)
    else:
        if c<=a<=b:
          print("el orden creciente de los numeros es: ",f)
        else:
            if c<=b<=a:
              print("el orden creciente de los numeros es: ",g)
            else:
                if a<=c<=b:
                  print("el orden creciente de los numeros es: ",h)
                else:
                    if b<=a<=c:
                      print("el orden creciente de los numeros es: ",i) 