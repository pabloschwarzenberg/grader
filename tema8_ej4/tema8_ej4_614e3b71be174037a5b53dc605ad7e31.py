def rot13(palabra):
  x=0 
  vueltas=len(palabra)
  palabra_encriptada=""
  for i in range(vueltas):
    palabra[x]

    if(palabra[x]=="a" or palabra[x]=="n"):
      if(palabra[x]=="n"):
        palabra_encriptada=palabra_encriptada+"a"
      elif(palabra[x]=="a"):
        palabra_encriptada=palabra_encriptada+"n"       
    elif(palabra[x]=="b" or palabra[x]=="o"):
      if(palabra[x]=="b"):
        palabra_encriptada=palabra_encriptada+"o"
      elif(palabra[x]=="o"):
        palabra_encriptada=palabra_encriptada+"b"      
    elif(palabra[x]=="c" or palabra[x]=="p"):
      if(palabra[x]=="c"):
        palabra_encriptada=palabra_encriptada+"p"
      elif(palabra[x]=="p"):
        palabra_encriptada=palabra_encriptada+"c"     
    elif(palabra[x]=="d" or palabra[x]=="q"):
      if(palabra[x]=="d"):
        palabra_encriptada=palabra_encriptada+"p"
      elif(palabra[x]=="p"):
        palabra_encriptada=palabra_encriptada+"d"      
    elif(palabra[x]=="e" or palabra[x]=="r"):
      if(palabra[x]=="e"):
        palabra_encriptada=palabra_encriptada+"r"
      elif(palabra[x]=="r"):
        palabra_encriptada=palabra_encriptada+"e"     
    elif(palabra[x]=="f" or palabra[x]=="s"):
      if(palabra[x]=="f"):
        palabra_encriptada=palabra_encriptada+"s"
      elif(palabra[x]=="s"):
        palabra_encriptada=palabra_encriptada+"f"    
    elif(palabra[x]=="g" or palabra[x]=="t"):
      if(palabra[x]=="g"):
        palabra_encriptada=palabra_encriptada+"t"
      elif(palabra[x]=="t"):
        palabra_encriptada=palabra_encriptada+"g"     
    elif(palabra[x]=="u" or palabra[x]=="h"):
      if(palabra[x]=="u"):
         palabra_encriptada=palabra_encriptada+"h"
      elif(palabra[x]=="h"):
        palabra_encriptada=palabra_encriptada+"u"    
    elif(palabra[x]=="i" or palabra[x]=="v"):
      if(palabra[x]=="i"):
         palabra_encriptada=palabra_encriptada+"v"
      elif(palabra[x]=="v"):
        palabra_encriptada=palabra_encriptada+"i"    
    elif(palabra[x]=="j" or palabra[x]=="w"):
      if(palabra[x]=="j"):
        palabra_encriptada=palabra_encriptada+"w"
      elif(palabra[x]=="w"):
        palabra_encriptada=palabra_encriptada+"j"            
    elif(palabra[x]=="k" or palabra[x]=="x"):
      if(palabra[x]=="k"):
        palabra_encriptada=palabra_encriptada+"x"
      elif(palabra[x]=="x"):
        palabra_encriptada=palabra_encriptada+"k"            
    elif(palabra[x]=="l" or palabra[x]=="y"):
      if(palabra[x]=="l"):
        palabra_encriptada=palabra_encriptada+"y"
      elif(palabra[x]=="y"):
        palabra_encriptada=palabra_encriptada+"l"            
    elif(palabra[x]=="m" or palabra[x]=="z"):
      if(palabra[x]=="m"):
        palabra_encriptada=palabra_encriptada+"z"
      elif(palabra[x]=="z"):
        palabra_encriptada=palabra_encriptada+"m"
    x=x+1
  return(palabra_encriptada)