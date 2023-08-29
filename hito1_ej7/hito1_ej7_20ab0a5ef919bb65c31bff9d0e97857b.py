#Zodiaco
dia=int(input("ingrese el dia: "))
mes=int(input("ingrese el mes: "))
signo=""
mesdia=int(str(mes)+str(dia))
if(mesdia>=321 and mesdia<=420):
    signo="ARIES"
if(mesdia>=421 and mesdia<=521):
    signo="TAURO"
if(mesdia>=522 and mesdia<=621):
    signo="GEMINIS"
if(mesdia>=622 and mesdia<=722):
    signo="CANCER"    
if(mesdia>=723 and mesdia<=823):
    signo="LEO"  
if(mesdia>=824 and mesdia<=923):
    signo="VIRGO"
if(mesdia>=924 and mesdia<=1023):
    signo="LIBRA"
if(mesdia>=1024 and mesdia<=1122):
    signo="ESCORPION"
if(mesdia>=1123 and mesdia<=1221):
    signo="SAGITARIO"    
if(mesdia>=1222 and mesdia<=120):
    signo="CAPRICORNO" 
if(mesdia>=121 and mesdia<=218):
    signo="ACURIO"    
if(mesdia>=219 and mesdia<=320):
    signo="PISCIS"      
print(signo)   