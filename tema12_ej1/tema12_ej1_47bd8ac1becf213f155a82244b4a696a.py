binario=[]
def sin(solucion):
	solucion+='0'
	return solucion
def con(solucion,n):
	if len(solucion)<n:
		solucion+="1"
		return solucion
	return
def aceptar_solucion(candidato,n):
	global binario
	if len(candidato)==n and candidato not in binario:
		binario.append(candidato)
		return True
def rechazar_solucion(candidato,n):
	if candidato in binario:
		return True
def backtracking(candidato,n):
	global binario
	if aceptar_solucion(candidato,n)==True:
		return
	if rechazar_solucion(candidato,n)==True:
		return
	solucion=sin(candidato)
	for i in range(2):
		backtracking(solucion,n)
		solucion=con(candidato,n)
	return

