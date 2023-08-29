#Aprobación de créditos
print("Para ver si aprobamos su credito rellene los siguientes datos")
ing = int(input("Cuantos son sus ingresos mensuales : "))
edad = int(input("Marque su año de nacimiento: "))
hijos = int(input("Indique cuantos hijos tiene de no tener solo marque 0 : "))
anos = int(input("Cuantos a años a pertenecido al banco : "))
esc = input(''''marque su estado civil
>> s: para soltero :
>> c: para casado  :           ''')
lo = input(''''si vive en campo o ciudad
>> u: para urbano
>> r: para rural
''')
if anos > 10 and hijos >= 2 :
  print("APROBADO")
elif esc == 'c' and hijos > 3 and edad >= 1968 and edad <= 1978 :
  print("APROBADO")
elif ing > 2500000 and esc == 's' and lo == 'u' :
  print("APROBADO")
elif ing > 3500000 and anos > 5 :
  print("APROBADO")
elif lo == 'r' and esc == 'c' and hijos < 2 :
  print("APROBADO")
elif ing > 0 :
  print("APROBADO")
else :
   print("Rechazado")