# Entrada
rut = eval(input("Ingrese su rut sin el digito verificador (numero despues del guion): "))
a = rut % 10
b = (rut%100 - a)//10
c = (rut%1000 - b)//100
d = (rut%10000 - c)//1000
e = (rut%100000 - d)//10000
f = (rut%1000000 - e)//100000
g = (rut%10000000 - f)//1000000
h = ((rut%100000000 - g)//1000000)//10


# Operaciones para sacar el digito
digitos = (a*2) + (b*3) + (c*4) + (d*5) + (e*6) + (f*7) + (g*2) + (h*3)
resto = digitos%11
resultadoFinal = 11 - resto

# Para verificar el digito
if resultadoFinal == 11:
    print("dv=0")
elif resultadoFinal == 10:
    print("dv=k")

else:
    print("dv=",resultadoFinal)
    
