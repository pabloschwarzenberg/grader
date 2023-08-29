#Elecciones
      
Comuna_A=int(input("Votos totales comuna A: "))
Comuna_B=int(input("Votos totales comuna B: "))
Comuna_C=int(input("Votos totales comuna C: "))
Votos_a_favor_A=int(input("Votos a favor Comuna A: "))
Votos_a_favor_B=int(input("Votos a favor Comuna B: "))
Votos_a_favor_C=int(input("Votos a favor Comuna C: "))

Porcentaje_A=Votos_a_favor_A/Comuna_A#Porcentaje comuna A
Porcentaje_B=Votos_a_favor_B/Comuna_B#Porcentaje comuna B
Porcentaje_C=Votos_a_favor_C/Comuna_C#Porcentaje comuna C
Porcentaje_A_y_B=((Votos_a_favor_A+Votos_a_favor_B)/(Comuna_A+Comuna_B))#Porcentaje comuna A y B
Porcentaje_A_y_C=((Votos_a_favor_A+Votos_a_favor_C)/(Comuna_A+Comuna_C))#Porcentaje comuna A y C
Porcentaje_B_y_C=((Votos_a_favor_B+Votos_a_favor_C)/(Comuna_B+Comuna_C))#Porcentaje comuna B y C
Porcentaje_A_B_y_C=((Votos_a_favor_A+Votos_a_favor_B+Votos_a_favor_C)/(Comuna_A+Comuna_B+Comuna_C))#Porcentaje comuna A, B y C



if (Porcentaje_A>=0.8):
    print("senadora electa")
if (Porcentaje_B>=0.8):
    print("senadora electa")
if (Porcentaje_C>=0.8):
    print("senadora electa")
if (Porcentaje_A_y_B>=0.7):
    print("¿senadora electa")
if (Porcentaje_A_y_C>=0.7):
    print("senadora electa")
if (Porcentaje_B_y_C>=0.7):
    print("senadora electa")
if (Porcentaje_A_B_y_C>=0.4):
    print("senadora electa")
if (Porcentaje_A<0.8):
    print("candidate perdedora")
if (Porcentaje_B<0.8):
    print("candidate perdedora")
if (Porcentaje_C<0.8):
    print("candidate perdedora")
if (Porcentaje_A_y_B<0.7):
    print("candidate perdedora")
if (Porcentaje_A_y_C<0.7):
    print("candidate perdedora")
if (Porcentaje_B_y_C<0.7):
    print("candidate perdedora")
if (Porcentaje_A_B_y_C<0.4):
    print("candidate perdedora")
