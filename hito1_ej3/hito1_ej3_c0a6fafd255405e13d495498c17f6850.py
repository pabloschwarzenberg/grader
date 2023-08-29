#Aprobación de créditos
ing=int(input("Digite el ingreso: "))
adn=int(input("Digite su año de nacimiento: "))
nhijos=int(input("Digite la cantidad de hijos que usted tiene: "))
abanco=int(input("Digite por cuantos años ha sido cliente de este Banco: "))
ec=input("Cual es su estado civil? Ocupe S(Soltero) o C(Casado) para responder : ")
lgr=input("En que lugar usted recide? Utilice U(Sitio Urbano) o R(Sitio Rural) : ")
edad= (adn-2022)
if((abanco>10 and nhijos>=2) or (ec=="C" and nhijos>3 and edad>=45 and edad<=55)or (ing>2500000 and ec=="S" and lgr=="U") or (ing>3500000 and abanco>5)or (lgr=="R" and ec=="C" and nhijos<2)):

  print("Excelente! Su credito ha sido APROBADO. Gracias por confiar en Banco Computin")
else:
  print("Lo sentimos! Su credito ha sido RECHAZADO. Gracias por confiar en Banco Computin")