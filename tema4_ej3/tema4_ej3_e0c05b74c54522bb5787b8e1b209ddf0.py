def jerigonzo(string):
  contador_1=0
  string_1=""
  while contador_1<=len(string)-1:
    if string[contador_1]=="a":
      string_1=string_1+"apa"
      contador_1=contador_1+1
    elif string[contador_1]=="e":
      string_1=string_1+"epe"
      contador_1=contador_1+1
    elif string[contador_1]=="i":
      string_1=string_1+"ipi" 
      contador_1=contador_1+1
    elif string[contador_1]=="o":
      string_1=string_1+"opo"
      contador_1=contador_1+1     
    elif string[contador_1]=="u":
      string_1=string_1+"upu"
      contador_1=contador_1+1
    else:
      string_1=string_1+string[contador_1]
      contador_1=contador_1+1
  return string_1


