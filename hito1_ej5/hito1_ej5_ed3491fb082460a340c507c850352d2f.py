def digito(rut):
   if len(str(rut)) == 7:
      a = int(str(rut)[0])*2
      b = int(str(rut)[1])*7
      c = int(str(rut)[2])*6
      d = int(str(rut)[3])*5
      e = int(str(rut)[4])*4
      f = int(str(rut)[5])*3
      g = int(str(rut)[6])*2
      h = 0
   else:
      a = int(str(rut)[0])*3
      b = int(str(rut)[1])*2
      c = int(str(rut)[2])*7
      d = int(str(rut)[3])*6
      e = int(str(rut)[4])*5
      f = int(str(rut)[5])*4
      g = int(str(rut)[6])*3
      h = int(str(rut)[7])*2
   m = a + b + c + d + e + f + g + h
   r = m % 11
   p = str(11 - r)
   if p == "10":
   	  p = "k" 
   elif p == "11":
      p = "0"
   return p 

entrada = int(input("INGRESE SU RUT SIN CODIGO VERIFICADOR"))
dv = digito(entrada)
print("dv = %s"%(dv))