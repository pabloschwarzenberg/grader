pesos= (input("ingreso: "))
año= (input("año de nacimiento: "))
hijos =(input ("numero de hijos: "))
permanencia =(input("años de permanencia en el banco: "))
estado_civil=(input("ingrese S o C: "))
urbano_o_rural=(input("ingrese U o R: "))
if ((str ('pesos >=3500000' )) and (str ('pesos >=2500000'))
    and (str(' año>=45')) and (str(' año <=55')) and (str ('hijos>= 2 ')) and
    (str ('hijos<=2')) and (str ('permanencia >=10')) and (str ('permanencia>=5')) and
    (str(' estado_civil == S ')) and (str ('estado_civil == C' )) and  (str ('urbano_o_rural == U ')) and
    (str(' urbano_o_rural == R '))):
   print("APROBADO")
else:
   print ("RECHAZADO")

