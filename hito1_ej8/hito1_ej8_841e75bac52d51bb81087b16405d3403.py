#Descomponer un número
numero = input("Ingrese número: ")
if len(numero) == 4:
    m = int(numero)//1000
    c = (int(numero)//100)%10
    d = (int(numero)//10)%10
    u = int(numero)%10
    print(m,"M + ",c,"C + ",d,"D + ",u,"U")
elif len(numero) == 3:
    c = int(numero)//100
    d = (int(numero)//10)%10
    u = int(numero)%10
    print(c,"C + ",d,"D + ",u,"U")
elif len(numero) == 2:
    d = int(numero)//10
    u = int(numero)%10
    print(d,"D + ",u,"U")
elif len(numero) == 1:
    u = int(numero)%10
    print(u,"U")