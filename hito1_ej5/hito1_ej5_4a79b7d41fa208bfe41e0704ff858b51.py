#Cálculo del dígito verificador de un rut

def _digito_verificador():
    
rut =int(input("Ingrese su RUT sin el digito verificador:"))
num = str(rut)[::-1]
rut_inverso = list(num)
multiplicadores = [2,3,4,5,6,7]
indice = -1
suma = 0
    
for i in range(0,len(rut_inverso)):
        if (i>=len(multiplicadores)):
            indice = i - len(multiplicadores)
        else:
            indice = i        
    
 suma += int(rut_inverso[i]) * multiplicadores[indice]
    
    # paso 3: modulo 11
mod = suma % 11
    
    # paso 4: restar resultado de paso 3 a 11
dif = 11 - mod
    
    # paso 5: convertir resultado en numero o letra de acuerdo a tres condiciones
if (dif == 11):
  digito_verificador = 0
elif (dif == 10):
  digito_verificador = 'K'
else:
  digito_verificador = dif
return digito_verificador

_digito_verificador()
