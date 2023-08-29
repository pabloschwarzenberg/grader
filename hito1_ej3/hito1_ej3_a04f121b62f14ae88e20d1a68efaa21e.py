#Aprobación de créditos
Ingr=int(input("Escriba su ingreso: "))
Edad=int(input("¿En qué año nació? "))
Hijos=int(input("¿Cuántos hijos tiene? "))
Anos=int(input("¿Hace cuántos años pertenece al banco? "))
EstC=input("S:soltero, C:casado ")
Zona=input("U:ciudad, R:campo ")

if Ingr>=0 or Edad>0 or (Hijos>=2 and Anos>10) or (EstC==S or EstC==C) or (Zona==U or Zona==C):
    print("APROBADO")
elif Ingr>=0 or (Edad>1963 and Edad<1973 and Hijos>3 and EstC==C) or (Zona==U or Zona==C):
    print("APROBADO")
elif (Ingr>2500000 and EstC==S and Zona==U) or Edad>0 or  Hijos>=0 or Anos>=0 :
    print("APROBADO")
elif (Ingr>3500000 and Anos>5) or Edad>0 or Hijos>=0 or Anos>5 or (EstC==S or EstC==C) or (Zona==U or Zona==C):
    print("APROBADO")
elif Ingr>=0 or Edad>0 or (Hijos<2 and EstC==C and Zona==C) or Años>=0 :
    print("APROBADO")
else:
    print("RECHAZADO")
