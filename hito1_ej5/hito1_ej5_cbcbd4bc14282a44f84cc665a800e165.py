import math
Rut = str(input("Ingrese su Rut :"))
Verificador = list(Rut)
numero_0 = (int(Verificador[0]))*3
numero_1 = (int(Verificador[1]))*2
numero_2 = (int(Verificador[2]))*7
numero_3 = (int(Verificador[3]))*6
numero_4 = (int(Verificador[4]))*5
numero_5 = (int(Verificador[5]))*4
numero_6 = (int(Verificador[6]))*3
numero_7 = (int(Verificador[7]))*2

Suma = (numero_0+numero_1+numero_2+numero_3+numero_4+numero_5+numero_6+numero_7)
Division = math.trunc(Suma/11)
Num_Verificador = (Suma-(11*Division))
Numero = (11-Num_Verificador)
if(Numero==11):
    print("Digito Verificador: 0")
if(Numero==10):
     print("dv=K")
if(Numero==0 or Numero==1 or Numero==2 or Numero==3 or Numero==4 or Numero==5 or Numero==6 or Numero==7 or Numero==8 or Numero==9):
    print("Digito Verificador:",Numero)
      