ingre  = int(input("¿INGRESOS?(en pesos): "))
naci   = int(input("¿AÑO DE NACIMIENTO?: "))
nhijos = int(input("¿NUMERO DE HIJOS?: "))
ab     = int(input("¿AÑOS DE PERTENENCIA AL BANCO?: "))
ecivil = str(input("¿ESTADO CIVIL?(S:soltero, C:casado): "))
vive   = str(input("¿VIVE EN CAMPO O CIUDAD?(U: urbano, R: rural): "))

 
if(ab>10)and(nhijos>=2):
    print("APROBADO")
elif(ecivil=="C")or(ecivil=="c")and(nhijos>3)and(1966>=naci<=1977):
    print("APROBADO")
elif(ingre>2500000)and(ecivil=="S")or(ecivil=="s")and(vive=="U")or(vive=="u"):
    print("APROBADO")
elif(ingre>3500000)and(ab>5):
    print("APROBADO")
elif(vive=="R")or(vive=="r")and(ecivil=="C")or(ecivil=="c")and(nhijos<2):
    print("APROBADO")

else:
    print("RECHAZADO")