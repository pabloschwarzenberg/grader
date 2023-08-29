#Cálculo del dígito verificador de un rut
def contar_caracteres(cadena):
    contador = 0
    while cadena[contador:]:
        contador += 1
    return contador
rut = input("Ingrese su rut sin puntos y sin el digito verificador:")
digitos = (len(rut))
if digitos == 8:
    num8 = eval(rut[0])
    num7 = eval(rut[1])
    num6 = eval(rut[2])
    num5 = eval(rut[3])
    num4 = eval(rut[4])
    num3 = eval(rut[5])
    num2 = eval(rut[6])
    num1 = eval(rut[7])
    suma = (num1*2)+(num2*3)+(num3*4)+(num4*5)+(num5*6)+(num6*7)+(num7*2)+(num8*3)
    resto = (suma % 11)
    resta = (11 - resto)
    if (resta == 11):
        print("dv=0")
    if (resta == 10):
        print("dv=k")
    if (resta < 10):
        print("dv=",resta)
if digitos == 7:
    num7 = eval(rut[0])
    num6 = eval(rut[1])
    num5 = eval(rut[2])
    num4 = eval(rut[3])
    num3 = eval(rut[4])
    num2 = eval(rut[5])
    num1 = eval(rut[6])
    suma = (num1*2)+(num2*3)+(num3*4)+(num4*5)+(num5*6)+(num6*7)+(num7*2)
    resto = (suma % 11)
    resta = (11 - resto)
    if (resta == 11):
        print("dv=0")
    if (resta == 10):
        print("dv=k")
    if (resta < 10):
        print("dv=",resta)