x = int(input("ingesos(en pesos):"))
y = int(input("año de nacimiento:"))
a = int(input("numero de hijos:"))
p = int(input("años de pertenencia al banco:"))
b = input("estado civil('s':soltero, 'c':casado:")
m = input("vive en campo o ciudad('u':urbano, 'r':rural:")
año = 2020- y
if p>10 and a >= 2:
    print("APROBADO")
else:
    if b == ('C') and a>3 and 45<= años <=55:
      print("APROBADO")
    else:
         if x > 2500000 and b == ('s') and m == ('u'):
            print("APROBADO")
         else:
            if x>3500000 and p>5:
              print("APROBADO")
            else:
               if m == ('R') and b == ('C') and a<2:
                  print("APROBADO")
               else:
                  print("RECHAZADO")