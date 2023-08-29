#Ordenar tres números
numeroa= int(input("Ingrese su primer número:"))
numerob= int(input("Ingrese su segundo número:"))
numeroc= int(input("Ingrese su tercer número:"))

if numeroa <= numerob <= numeroc:
  print(numeroa,",",numerob,",",numeroc)
elif numeroa <= numeroc <= numerob:
  print(numeroa,",",numeroc,",",numerob)
elif numeroc <= numeroa <= numerob:
  print(numeroc,",",numeroa,",",numerob)
elif numerob <= numeroa <= numeroc:
  print(numerob,",",numeroa,",",numeroc)
elif numerob <= numeroc <= numeroa:
  print(numerob,",",numeroc,",",numeroa)
elif numeroc <= numerob <= numeroa:
  print(numeroc,",",numerob,",",numeroa)