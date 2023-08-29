#Cálculo del dígito verificador de un rut

rut=int(input("Ingrese numero de rut"))

def verif(n):

  x = int(len(str(n)))
  
  if x == 8:
  
    a=int(str(n)[0])*3 
    b=int(str(n)[1])*2
    c=int(str(n)[2])*7
    d=int(str(n)[3])*6
    e=int(str(n)[4])*5 
    f=int(str(n)[5])*4 
    g=int(str(n)[6])*3 
    h=int(str(n)[7])*2
  else:
    a=int(str(n)[0])*2 
    b=int(str(n)[1])*7
    c=int(str(n)[2])*6
    d=int(str(n)[3])*5
    e=int(str(n)[4])*4 
    f=int(str(n)[5])*3 
    g=int(str(n)[6])*2
    h = 0
  res = ((a+b+c+d+e+f+g+h)%11)
  dig = 11 - res
  if dig == 10:
    return "k"
  elif dig == 11:
    return 0
  else:
    return dig

print ("dv=",verif(rut))