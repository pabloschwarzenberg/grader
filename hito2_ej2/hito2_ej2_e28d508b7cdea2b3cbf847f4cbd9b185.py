def val_secuencia(secuencia):
   sec_list=list(secuencia)
   sec=[]
   for s in secuencia:
       if s=="a" or s=="c" or s=="t" or s=="g":
           sec.append(s)
       else:
           continue     
   if sec==sec_list:
        return True
   else:
        return False
        
secuencia=input()
validacion=val_secuencia(secuencia)
if validacion :
    print("secuencia correcta")
elif not validacion:
    print("secuencia incorrecta")