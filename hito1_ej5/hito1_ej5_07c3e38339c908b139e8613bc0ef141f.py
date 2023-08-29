#Cálculo del dígito verificador de un rut
rut= input("Ingrese su rut sin el digito verificador: ")
posicion1= rut[0:1:1]
posicion2= rut[1:2:1]
posicion3= rut[2:3:1]
posicion4= rut[3:4:1]
posicion5= rut[4:5:1]
posicion6= rut[5:6:1]
posicion7= rut[6:7:1]
posicion8= rut[7:8:1]
 
if len(rut)==7:
    operacion1= (int(posicion1))*2
    operacion2= (int(posicion2))*7
    operacion3= (int(posicion3))*6
    operacion4= (int(posicion4))*5
    operacion5= (int(posicion5))*4
    operacion6= (int(posicion6))*3
    operacion7= (int(posicion7))*2
  
    sumamultiplicaciones= operacion1+operacion2+operacion3+operacion4+operacion5+operacion6+operacion7
    restoporonce= (sumamultiplicaciones)%11
    
    if restoporonce!=0:
        digitoverificador= 11-restoporonce
        if digitoverificador==10:
          print("dv=k")
        else:
            print("dv=",digitoverificador)
        
    else: 
        digitoverificador=restoporonce
        print("dv=",digitoverificador)
      
if len(rut)==8:    
    operacion1= int(posicion1)*3
    operacion2= int(posicion2)*2
    operacion3= int(posicion3)*7
    operacion4= int(posicion4)*6
    operacion5= int(posicion5)*5
    operacion6= int(posicion6)*4
    operacion7= int(posicion7)*3
    operacion8= int(posicion8)*2
  
    sumamultiplicaciones= operacion1+operacion2+operacion3+operacion4+operacion5+operacion6+operacion7+operacion8
    restoporonce= (sumamultiplicaciones)%11
    if restoporonce!=0:
        digitoverificador= 11-restoporonce
        if digitoverificador==10:
          print("dv=k")
        else:
          print("dv=",digitoverificador)
        
    else: 
        digitoverificador=restoporonce
        print("dv=",digitoverificador)
    if restoporonce!=0:
        digitoverificador= 11-restoporonce
        if digitoverificador==10:
          print("dv=k")
        else:
          print("dv=",digitoverificador)
        
    else: 
        digitoverificador=restoporonce
        print("dv=",digitoverificador)
   
        
  