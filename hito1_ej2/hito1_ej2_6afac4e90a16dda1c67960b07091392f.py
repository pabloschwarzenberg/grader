#Contestador de celular
H_dia= eval(input("Ingresa el horario de llamada: "))
n_celular= int(input("Ingresa el numero: "))
if H_dia>=00 and H_dia<= 7:
  print("Contestar")
elif H_dia<14 and n_celular%1000==909:
 print("Contestar")
elif n_celular==8770000:
  print("No Contestar")
elif H_dia>=17 and H_dia<=19:
  print("No Contestar")  
elif H_dia > 19:
  print("No contestar")       