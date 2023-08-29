dia=int(input("ingrese día de nacimiento:"))
mes=input("ingrese mes de nacimiento: ")

if ((((dia>=21)or(dia<=31))and(mes=="marzo"))or((dia>=1)or(dia<=20)and(mes=="abril"))):
    print("Aries")
    
if ((((dia>=21)or(dia<=30))and(mes=="abril"))or((dia>=1)or(dia<=21)and(mes=="mayo"))):  
    print("tauro")
    
if ((((dia>=22)or(dia<=31))and(mes=="mayo"))or((dia>=1)or(dia<=21)and(mes=="junio"))):
    print("geminis")
    
if ((((dia>=22)or(dia<=30))and(mes=="junio"))or((dia>=1)or(dia<=23)and(mes=="julio"))):
    print("cancer")
    
if ((((dia>=24)or(dia<=31))and(mes=="julio"))or((dia>=1)or(dia<=23)and(mes=="agosto"))):
    print("leo")
    
if ((((dia>=24)or(dia<=31))and(mes=="agosto"))or((dia>=1)or(dia<=23)and(mes=="septiembre"))):
    print("virgo")
    
if ((((dia>=24)or(dia<=30))and(mes=="septiembre"))or((dia>=1)or(dia<=23)and(mes=="octubre"))):
    print("libra")
    
if ((((dia>=24)or(dia<=31))and(mes=="octubre"))or((dia>=1)or(dia<=22)and(mes=="noviembre"))):
    print("escorpion")
    
if ((((dia>=23)or(dia<=30))and(mes=="noviembre"))or((dia>=1)or(dia<=22)and(mes=="diciembre"))):
    print("sagitario")
    
if ((((dia>=23)or(dia<=31))and(mes=="diciembre"))or((dia>=1)or(dia<=20)and(mes=="enero"))):
    print("capricornio")
    
if ((((dia>=21)or(dia<=31))and(mes=="enero"))or((dia>=1)or(dia<=19)and(mes=="febrero"))):
    print("capricornio")
    
if ((((dia>=20)or(dia<=28))and(mes=="febrero"))or((dia>=1)or(dia<=20)and(mes=="marzo"))):
    print("piscis")
      