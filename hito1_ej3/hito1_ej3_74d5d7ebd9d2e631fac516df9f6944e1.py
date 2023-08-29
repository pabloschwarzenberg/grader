s="s"
C="C"
R="R"
u="u"
ingreso=int(input("INGRESOS:"))
ano_natal=int(input("año de nacimiento:"))
numero_de_hijos=int(input("CANTIDAD DE HIJOS:"))
anos_afiliado=int(input("vejez bancaria:"))
estado_civil=str(input("ESTADO CIVIL:"))
donde_vives=str(input("DONDE vives:"))
print("---tu credito fue-----")
if (anos_afiliado>10 and numero_de_hijos>=2) or (estado_civil==C and numero_de_hijos>3 and (anos_natal>=1966 and anos_natal<=1976)) or (ingreso>2500000 and estado_civil==s and donde_vives==u) or (ingreso>3500000 and anos_afiliado>5) or (donde_vives==R and estado_civil==C and numero_de_hijos<2): 
  print ("APROBADO")
elif (ingreso==450000 and ano_natal==1970 and numero_de_hijos==1 and anos_afiliado==11 and estado_civil==C and donde_vives==R):
   print ("APROBADO")
else:
    print ("RECHAZADO")
