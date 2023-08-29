#Descomponer un número
numero = int(input("Escriba un numero de hasta 4 digitos: "))



if numero > 9999:
    print('El numero que ingreso supera los 4 digitos')

elif numero > 0:
    m = numero //1000
    c = (numero%1000)//100
    d = ((numero%1000)%100)//10
    u = ((numero%1000)%100)%10
    print(str(m)+"M +"+str(c)+"C +"+str(d)+"D +"+str(u)+"U")
