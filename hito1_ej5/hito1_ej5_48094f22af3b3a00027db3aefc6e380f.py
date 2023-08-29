#Cálculo del dígito verificador de un rut
Rut=int(input(" ingrese rut sin punto ni guión: "))
dv= Rut%(10**1)
print("dv=" + str(dv))