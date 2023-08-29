rut = int(input("Ingrese RUT sin digito verificador: "))
dv = 0
i = 0
a = 2
b = 1
valor_guard = ""
#-------------------
rut = str(rut) #el rut se convierte a caracteres
rut1 = ((rut)[::-1]) #rut 1 es el rut invertido
rut2 = rut1[i] #rut2 es rut invertido en la posicion i
tamaño = len(rut)
print(tamaño)
print(rut2)

while(not(rut2 == "")):
    rut3 = eval(rut2)
    valor = rut3 * a
    valor = str(valor)+"+"
    valor_guard = valor_guard + valor
    if(a == 7):
        a = b
        a = a + 1
        i = i + 1
        if(not(tamaño == i)):
            rut2 = rut1[i]

    else:
        a = a + 1
        i = i + 1
        print("i",i)
        print("a",a)
        if(not(tamaño == i)):
            rut2 = rut1[i]
        else:
            rut2 = ""
            valor_guard = valor_guard + "0"

suma_producto = eval(valor_guard)
print("valorguard",valor_guard)
print("suma de productos",suma_producto)

valor2 = int(suma_producto / 11)
print(valor2)
valor3 = suma_producto - (11 * valor2)
print(valor3)
resultado = 11 - valor3

if(resultado == 11):
    dv = 0
    print("dv =",dv)

else:
    if(resultado == 10):
        dv = "k"
        print("dv =",dv)

    else:
        if(resultado == resultado):
            dv = resultado
            print("dv =",dv)
      