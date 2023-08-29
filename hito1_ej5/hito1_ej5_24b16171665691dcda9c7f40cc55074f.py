#Cálculo del dígito verificador de un rut

n_carnet=(input("Ingrese rut sin digito:"))
run = ""

for valores in n_carnet :
    run = valores + run
contador_para_sumar = 0
count = 0
for valor in run :
    valor = int(valor)
    if count == 0 :
        contador_para_sumar = contador_para_sumar + 2*valor
    if count == 1 :
        contador_para_sumar = contador_para_sumar + 3*valor
    if count == 2 :
        contador_para_sumar = contador_para_sumar + 4*valor
    if count == 3 :
        contador_para_sumar = contador_para_sumar + 5*valor
    if count == 4 :
        contador_para_sumar = contador_para_sumar + 6*valor
    if count == 5 :
        contador_para_sumar = contador_para_sumar + 7*valor
    if count == 6 :
        contador_para_sumar = contador_para_sumar + 2*valor
    if count == 7 :
        contador_para_sumar = contador_para_sumar + 3*valor
    if count == 8 :
        contador_para_sumar = contador_para_sumar + 4*valor
    count = count + 1
    
    
final = (contador_para_sumar//11)*11
contador_para_restar = 0

if final > contador_para_sumar:
    contador_para_restar = final - contador_para_sumar
    
if contador_para_sumar > final :
    contador_para_restar = contador_para_sumar - final
verificador =11-contador_para_restar

if verificador == 10 :
    verificador = "k"
    
if verificador == 11 :
    verificador = 0
    
    
print("dv=",verificador )     

