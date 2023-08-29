#Descomponer un número
numero = int(input("Por favor ingrese un número de hasta 4 cifras: "))

#print("centenas", centenas)
u = numero
d = numero//10
c = numero//100
m = numero//1000

#condiciones.

if 0 <= numero <=9:
    u=numero
    print("La descomposición del número da como resultado:", str(u)+'U')
elif 10 < numero <99:
    u%=10
    numero//=10
    d=numero%10
    numero//=10

    print("La descomposición del número da como resultado:", str(d)+'D +'+ "",str(u)+'U')
elif 100 < numero <999:
    u%=10
    numero//=10
    d=numero%10
    numero//=10
    c=numero%10
    numero//=10
    print("La descomposición del número da como resultado:", str(c)+'C +' + "",str(d)+'D +'+ "",str(u)+'U')
elif 1000 < numero <9999:
    u%=10
    numero//=10
    d=numero%10
    numero//=10
    c=numero%10
    numero//=10
    m=numero%10
    numero//=10
    print("La descomposición del número da como resultado:", str(m)+'M +' + "",str(c)+'C +' + "",str(d)+'D +'+ "",str(u)+'U')
else:
    print("Cifra ingresada erróneamente , intentelo nuevamente.")
    
print("Fin.")
    
    
    



  

