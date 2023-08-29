'''
Escribe un programa que reciba como dato un número que representará un rut al que debe calcularle el dígito verificador. 
Por ejemplo al ingresar 6016740 tu programa debiera imprimir el siguiente mensaje:

dv=0

'''

rut = str(input("Ingrese su rut sin digito verificador: "))
n_serie = 2
acum = 0
for i in range(0,len(rut)):
    acum = acum + int(rut[len(rut)-1-i])*n_serie
    n_serie = n_serie+1
    if(n_serie == 8):
        n_serie = 2

print("acum",acum)
resto = acum % 11
dv = 11 - resto
if(dv == 11):
    dv = 0
elif(dv == 10):
    dv = 'k'
print("dv="+str(dv))