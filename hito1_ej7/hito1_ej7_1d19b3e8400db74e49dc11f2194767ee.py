#Zodiaco
#Definir la funcion obtener_signo
def obtener_signo(dia_nacimiento,mes_nacimiento):
     signo=''
     if mes_nacimiento ==1:
          if dia_nacimiento<=20:
               signo="Capricornio"
          else:
               signo="Acuario" 
     elif mes_nacimiento==2:
          if dia_nacimiento <=18:
               signo="Acuario"
          else:
               signo="Piscis"
     elif mes_nacimiento==3:
          if dia_nacimiento<=20:
               signo="Piscis"
          else:
               signo="Aries"
     elif mes_nacimiento==4:
          if dia_nacimiento<=20:
               signo="Aries"
          else:
               signo="Tauro"
     elif mes_nacimiento==5:
          if dia_nacimiento<=21:
               signo="Tauro"
          else:
               signo="Geminis"
     elif mes_nacimiento==6:
          if dia_nacimiento>=21:
               signo="Geminis"
          else:
               signo="Cancer"
     elif mes_nacimiento==7:
          if dia_nacimiento<=23:
               signo="Cancer"
          else:
               signo="Leo"
     elif mes_nacimiento==8:
          if dia_nacimiento<=23:
               signo="Leo"
          else:
               signo="Virgo"
     elif mes_nacimiento==9:
          if dia_nacimiento<=23:
               signo="Virgo"
          else:
               signo="Libra"
     elif mes_nacimiento==10:
          if dia_nacimiento<=23:
               signo="Libra"
          else:
               signo="Escorpio"
     elif mes_nacimiento==11:
          if dia_nacimiento<=22:
               signo="Escorpio"
          else:
               signo="Sagitario"
     elif mes_nacimiento==12:
          if dia_nacimiento<=21:
               signo="Sagitario"
          else:
               signo="Capricornio"
     return signo

#Pedir al usuario ingresar el mes (numero) y dia de su nacimiento
dia=int(input("Ingrese el dia de su nacimiento: "))
mes=int(input("Ingrese el mes de su nacimiento: "))

signo=obtener_signo(dia,mes)

print("Su signo es: ",signo)     