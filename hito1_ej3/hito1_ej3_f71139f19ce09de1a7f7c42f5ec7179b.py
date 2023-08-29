#Aprobación de créditos
edad=int(input("Ingrese su edad:"))
masa=int(input("Ingrese su masa:"))
estatura=float(input("Ingrese estatura:"))

IMC= masa/estatura**2

if IMC<22 and edad<45:
    print("Su riesgo respecto al IMC es bajo")
elif IMC<22 and edad>45:
    print("Su riesgo respecto al IMC es medio")
if IMC>22 and edad<45:
    print("Su riesgo respecto al IMC es medio")
elif IMC>22 and edad>45:
    print("Su riesgo respecto al IMC es alto")