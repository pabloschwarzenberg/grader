#Digito verificador del rut
rut = str(input("Ingrese su rut para calcular su digito verificador: "))
largo_rut = len(rut)
i = 0
multiplicador = 2
tope = 7
inicio = 2
sumatoria = 0
#Calculo digito verificador
def invertir(rut):
    invertir_rut = ""
    for numero in rut:
        invertir_rut = numero + invertir_rut
    return invertir_rut

#Procedimiento
while i<largo_rut:
    numero = int(invertir(rut)[i])
    resultado = multiplicador * numero
    sumatoria = sumatoria + resultado
    if(multiplicador == tope):
        multiplicador = inicio
    else:
        multiplicador += 1
    i += 1
resto = sumatoria % 11
dv = 11 - resto
if (dv == 11):
    dv = "0"
elif (dv == 10):
    dv = "k"

print("dv=",dv)