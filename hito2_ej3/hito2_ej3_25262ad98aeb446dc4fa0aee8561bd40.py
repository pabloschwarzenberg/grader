def subsecuencias(secuencia, n):
	ntuplas = [ ]
	ntuplas_unicas = [ ]

	contador = 0
	ntupla = ""
	
	for letra in secuencia:
		ntupla = ntupla + letra
		contador += 1
		if contador == n:
			ntuplas.append(ntupla)
			if ntupla not in ntuplas_unicas:
				ntuplas_unicas.append(ntupla)
			contador = 0
			ntupla = ""

	for i in ntuplas_unicas:
		if ntuplas.count(i) > 1:
			ntuplas_unicas.remove(i)

	if len(ntuplas_unicas) == 0:
		print("ninguna")
	else:
		for i in ntuplas_unicas:
			print(i)

	return None
  
print(subsecuencias(input("Ingresa una secuencia: "), int(input("Ingresa un valor para n: "))))