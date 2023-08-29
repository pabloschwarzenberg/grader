#Aprobación de créditos
print("Hola, necesitamos que, a continuación, ingrese los datos que se le solicitan")
ingr=int(input("Sus ingresos mensuales (en pesos) "))
birth=int(input("Su año de nacimiento "))
hijos=int(input("Cuantos hijos tiene "))
perten=int(input("Los años que lleva con nuestro banco "))
civil=input("Su estado civil (S: Soltero, C: Casado) ")
casa=input("Y por último, si vive en casa o campo (U: Urbano, R: Rural) ")
edad=2021-birth
if(perten>10) and (hijos>=2):
    print("CRÉDITO APROBADO")
elif(civil=="C") and (hijos>3) and (edad>=45 or edad<=55):
    print("CRÉDITO APROBADO")
elif(ingr>2500000) and (civil=="S") and (casa=="U"):
    print("CRÉDITO APROBADO")
elif(ingr>3500000) and (perten>5):
    print("CRÉDITO APROBADO")
elif(casa=="R") and (civil=="C") and (hijos<2):
    print("CRÉDITO APROBADO")
else:
    print("CRÉDITO RECHAZADO")