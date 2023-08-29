#Contestador Automático
celular=int(input("Ingrese numero telefonico:"))
n1=len(str(celular))
n2=8
n3=str(celular)
extraer=n3[5:8]
no_constestar1="909"
no_constestar2="877"
h1=range(0,23)

while n1>n2 or n1<n2:
    celular=int(input("Ingrese numero telefonico:"))
    n1=len(str(celular))
print("Ingresaste un celular valido")
hora=int(input("Ingrese hora de la llamada:"))
while hora<0 or hora>23:
    hora=int(input("Ingresa un horario entre 0 y 23:"))
#condiciones
if hora>=0 and hora<=7:
    print("CONTESTAR")
if hora>=7 and hora<14 :
    if extraer ==no_constestar1: 
                        print("CONTESTAR")
    else:
        print("NO CONTESTAR")    

if hora>=17 and hora<19 :
    if extraer ==no_constestar2:
                        print("CONTESTAR")         
    else:
        print("NO CONTESTAR")       
if hora>=19:
    print("NO CONTESTAR")
