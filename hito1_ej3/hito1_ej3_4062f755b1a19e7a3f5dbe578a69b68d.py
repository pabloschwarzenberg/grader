#Aprobación de créditos
ingreso = input ()
1000000
fecha = input ()
1998
hijos = input ()
3
banco = input ()
15
estado_civil = input ()
"C"
vive = input ()
"U"
if (banco > "10") and (hijos >= "2"): print ("APROBADO")
elif (estado_civil == "C") and (hijos >= "3") and ("45" < (2017 - int(fecha)) < "55"): print ("APROBADO")
elif (ingreso > "2500000") and (estado_civil == "S") and (vive == "U"): print ("APROBADO")
elif (ingreso > "3500000") and (banco > "5"): print ("APROBADO")
elif (vive == "R") and (estado_civil == "C") and (hijos < "2"): print ("APROBADO")
else: print ("RECHAZADO")