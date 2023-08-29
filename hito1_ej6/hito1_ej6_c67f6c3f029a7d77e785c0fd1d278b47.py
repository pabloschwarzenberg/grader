primer_numero=int(input("ingresar primer_numero: "))
segundo_numero=int(input("ingresar segundo_numero: "))
tercer_numero=int(input("ingresar tercer_numero: "))
opcion1=primer_numero<=segundo_numero<=tercer_numero
opcion2=primer_numero<=tercer_numero<=segundo_numero
opcion3=segundo_numero<=primer_numero<=tercer_numero
opcion4=segundo_numero<=tercer_numero<=primer_numero
opcion5=tercer_numero<=primer_numero<=segundo_numero
opcion6=tercer_numero<=segundo_numero<=primer_numero
orden1=primer_numero,segundo_numero,tercer_numero
orden2=primer_numero,tercer_numero,segundo_numero
orden3=segundo_numero,primer_numero,tercer_numero
orden4=segundo_numero,tercer_numero,primer_numero
orden5=tercer_numero,primer_numero,segundo_numero
orden6=tercer_numero,segundo_numero,primer_numero

if opcion1==True:
        print(orden1)
else:
	opcion1=False
	if opcion2==True:
		print(orden2)
	else:
			opcion2=False
			if opcion3==True:
				print(orden3)
			else:
					opcion3=False
					if opcion4==True:
						print(orden4)
					else:
							opcion4=False
							if opcion5==True:
								print(orden5)
							else:
									opcion5=False
									if opcion6==True:
										print(orden6)
									else:
											opcion6=False
											print("error")