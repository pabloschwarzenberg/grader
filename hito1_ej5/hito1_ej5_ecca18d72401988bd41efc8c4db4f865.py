#Cálculo del dígito verificador de un rut
Rut = int(input())

mil = Rut// 1000
centena = Rut// 100 -mil*10
decena = Rut// 10 - mil*100 - centena*10
unidad = Rut// 1 - mil*1000 - centena*100 - decena*10 

print("dv=",unidad)
