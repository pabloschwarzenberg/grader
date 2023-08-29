#Cálculo del dígito verificador de un rut
Rut = input("ingrese le rut owo: ") 
Rut = Rut [::-1]
Respuesta = 0
Leste = [2,3,4,5,6,7]
for I in range (len (Rut)):
  Respuesta = Respuesta + int(Rut[I]) * Leste[I%6]

Hot = 11- Respuesta %11
if Hot == 11: 
  Final= 0
elif Hot == 10: 
  Final = "K"
else:
  Final = Hot 
print("dv="+ str(Final))

