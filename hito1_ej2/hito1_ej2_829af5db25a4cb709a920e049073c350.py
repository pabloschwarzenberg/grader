#entrada

N_telefono = (input( "ingrese numero telefonico de 8 digitos : " ))
H_llamada =  float(input  ( " ingrese hora de la llamada:"))
   

if   H_llamada >= 0.0  and H_llamada <= 7.0: 
            descriptor = "CONTESTAR " 
               
elif   H_llamada <14.0 and (N_telefono[-3:]) != 909    :
                descriptor = "CONTESTAR " 
elif  H_llamada >17.0 and H_llamada < 19.0  and   (N_telefono[3:]) != 877 :
                descriptor = " NO CONTESTAR "
elif  H_llamada < 19.0  :
                descriptor =  " CONTESTAR " 
else : 
        descriptor =  "NO CONTESTAR "
                      
 # salida
 
print( descriptor)







