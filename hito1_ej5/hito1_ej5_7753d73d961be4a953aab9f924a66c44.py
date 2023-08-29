#Cálculo del dígito verificador de un rut
ingresa_rut=int(input("ingrese su rut:"))
dv_rut=ingresa_rut%10
print("dv=",{dv_rut})