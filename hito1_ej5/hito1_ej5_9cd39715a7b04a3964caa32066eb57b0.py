#Cálculo del dígito verificador de un rut
#in
rut =  int(input('Ingrese rut:'))
#Digitos
x1 = rut % 10 #ult digito
x2 = int((rut % 100)/10) #Penult digito
x3 = int((rut % 1000)/100)
x4 = int((rut % 10000)/1000)
x5 = int((rut % 100000)/10000)
x6 = int((rut % 1000000)/100000)
x7 = int((rut % 10000000)/1000000)
x8 = int((rut % 100000000)/10000000) #primer digito
#Digito verificador
suma = ((x1*2)+(x2*3)+(x3*4)+(x4*5)+(x5*6)+(x6*7)+(x7*2)+(x8*3))
mod = int(suma/11)
resta = suma - (mod*11)
dig = 11 - resta
if dig == 10:
    dig = 'k'
elif dig == 11:
    dig = 0
NRut = str(rut) + str('-') + str(dig)
NDig = str(dig)
print('Dv=', NDig)      