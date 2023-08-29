#Aprobación de créditos
print ("ingrese los datos ")

y = int(input("ingreso :"))
a = int(input(" edad :"))
n = int(input("numero de hijos :"))
o = int(input("tiempo en el banco :"))
e = str(input("estado civil ( S = soltero , C  = casado ):"))
s = str(input("si vive en campo o ciudad ( U = urbano , R = rural ) :"))

if o>10 and n>=2 :
    print (" APROBADO ")
elif e == "C" and  n > 3 and 45<a and a>56  :
    print (" APROBADO ")
elif y>2500000 and e == "S" and s == "U" :
    print (" APROBADO ")
elif y > 3500000 and o > 5 :
    print (" APROBADO ")
elif  s == "R" and e == "C" and n<2 :
    print (" APROBADO ")

else:
    print (" RECHAZADO")