#Zodiaco
dia=int(input("ingrese su dia de nacimiento :"))
mes=int(input("ingrese su mes de nacimiento :"))

if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=20)):
    signo = 'aries'
elif  ((mes==4) and (dia>=20)) or ((mes==5) and (dia<=21)):
    signo = 'taurus'    
elif  ((mes==5) and (dia>=21)) or ((mes==6) and (dia<=21)):
    signo = 'geminis' 
elif  ((mes==6) and (dia>=21)) or ((mes==7) and (dia<=23)):
    signo = 'cancer' 
elif  ((mes==7) and (dia>=23)) or ((mes==8) and (dia<=23)):
    signo = 'leo' 
elif  ((mes==8) and (dia>=23)) or ((mes==9) and (dia<=23)):
    signo = 'virgo' 
elif  ((mes==9) and (dia>=23)) or ((mes==10) and (dia<=23)):
    signo = 'libra' 
elif  ((mes==10) and (dia>=23)) or ((mes==11) and (dia<=22)):
    signo = 'scorpio' 
elif  ((mes==11) and (dia>=23)) or ((mes==12) and (dia<=22)):
    signo = 'sagittarius' 
elif  ((mes==12) and (dia>=22)) or ((mes==1) and (dia<=20)):
    signo = 'capricornio' 
elif  ((mes==1) and (dia>=20)) or ((mes==2) and (dia<=19)):
    signo = 'acuario' 
elif  ((mes==2) and (dia>=19)) or ((mes==3) and (dia<=21)):
    signo = 'piscis'  
print(signo)    
 