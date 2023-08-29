rut=(input("Escriba los digitos de su rut sin puntos y sin el digito verificador: "))
rutInvertido=list(reversed(rut))
factor=2
suma=0
Dv=0
for i in rutInvertido:
  suma+=int(i)*factor
  factor+=1
  if factor>7:
    factor=2

Dv=11-(suma%11)
if Dv==11:
    Dv=0
elif Dv==10:
    Dv="K"
print("Dv={}".format(Dv))