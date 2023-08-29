#Descomponer un número
num=float(input("ingrese numero: "))
u_mil= num / 100
t_m_p=num % 100

centenas=t_m_p / 100
t_m_p= t_m_p % 100
decenas= t_m_p/ 10
unidades= t_m_p % 10
print("M: %i" % u_mil)
print("C: %i" % centenas)
print("D: %i" % decenas)
print("U: %i" % unidades)

if u_mil<=0:
  print(centenas,"C + ", decenas, "D + ", unidades, "U")
  if centenas<=0:
    print(decenas, "D +", unidades, "U")
    if decenas<0:
      print(unidades, "U")
if u_mil>0:
  print("%i" % u_mil, "M +", "%i" % centenas,"C +","%i" % decenas,"D +","%i" % unidades, "U")
  