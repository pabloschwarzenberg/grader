def buscarTodas(a,b):

   print ("a:",a,"b:",b)

   palabra_salida="ninguna"
   substring=""
   pos_inicial=-1
   pos_inicial_respaldo=-1
   encontre="si"
   largo_sub=0
   largo_sub=int(b)
   i=0
   while i<=(len(palabra)-largo_sub):
       substring=palabra[i:largo_sub+i]
       j=0
       encontrado=0
       pos_inicial=-1
       pos_inicial_respaldo=-1
       while j<=(len(palabra)-largo_sub):
           pos_inicial=a.find(substring,pos_inicial_respaldo+1)
           if pos_inicial==-1:
               encontre="no"
           else:
               encontrado=encontrado+1
               pos_inicial_respaldo=pos_inicial
           j=j+1
            
       if encontrado==1:
           palabra_salida=palabra_salida + " " + substring
           
       i=i+1

   return palabra_salida 
    
    
palabra=""
palabra_salida=""
string_a_encontrar=""
largo=0
palabra=input("Ingrese palabra a buscar:")
largo=input("Ingrese largo del string a buscar:")

palabra_salida=buscarTodas(palabra,largo)

print (palabra_salida)
 
    
    
    
    
    
    
    
    
    
    