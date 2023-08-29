#Aprobación de créditos
ingreso=int(input("ingreso:"))
ano1=int(input("año de nacimiento:"))
hijos=int(input("numero de hijos:"))
ano2=int(input("año de pertenencia al banco:"))
estado=input("estado civil:")
vive=input("campo o ciudad:")

def main():
  if (ano2>=10 and hijos>=2) or (estado=="c" and hijos>3 and 45<ano1<55)  or (ingreso>2500000 and estado=="S" and vive=="U") or (ingreso>3500000 and ano2>5) or (vive=="R" and estado=="C" and hijos<2):
    print ("APROBADO")
  else:
    print("RECHAZADO")

main()   