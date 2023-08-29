msj = input("ingrese cadena 1 --> ")
msj2= input("ingrese cadena 2 -->")
aux = ""
if(len(msj)< len(msj2)):
  a = len(msj)
else:
  a = len(msj2)
 for i in range(0,a):
   if(msj[i] != msj2[i]):
     aux.append("_")
   elif(msj[i] == msj2[i]):
     aux.append(msj[i])
#Aqui mira cual es el maor  añade el sobrante
if(len(msj) > len(msj2)):
  for k in range(a,len(msj)):
    aux.append(msj[k])
else:
  for k in range(a,len(msj2)):
    aux.append(msj2[k])
  
     