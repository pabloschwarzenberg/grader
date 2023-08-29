#Contestador de celular
NT = input("Ingrese un numero telefonico de 8 cifras: ")

H = int(input("Ingrese la hira de la llamada entre las 0 y 23 horas: "))

j = NT[5]
i = NT[6]
k = NT[7]
a ="9"
b = "0"
c = "9"
l = NT[0]
n = NT[1]
m = NT[2]
d = "8"
e = "7"

if H >= 0 and H <= 7 :
    print("Numero telefonico :  ",NT)
    print("Horario de su llamada : ",H)
    print("Resultado: Contestar")
elif H > 7 and H <= 14 :
    if (j==a and i==b and k==c) :
        print("Numero telefonico :  ",NT)
        print("Horario de su llamada : ",H)
        print("Resultado: Contestar")
    else:
        print("Numero telefonico :  ",NT)
        print("Horario de su llamada : ",H)
        print("Resultado: No Contestar")
elif (H >= 17 and H <= 19) : 
    if (l==d and n==e and m==n) :
        print("Numero telefonico :  ",NT)
        print("Horario de su llamada : ",H)
        print("Resultado: No Contestar")
    else :
        print("Numero telefonico :  ",NT)
        print("Horario de su llamada : ",H)
        print("Resultado: Contestar")
else: 
    print("Numero telefonico :  ",NT)
    print("Horario de su llamada : ",H)
    print("Resultado: No Contestar")
