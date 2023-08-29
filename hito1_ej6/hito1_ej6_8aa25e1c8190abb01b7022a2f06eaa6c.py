Primer_Numero = eval(input("ingrese el primer numero: "))
Segundo_Numero = eval(input("ingrese el segundo numero: "))
Tercer_Numero = eval(input("ingrese el tercer numero: "))

Ma = max(Primer_Numero,Segundo_Numero,Tercer_Numero)
Mi = min(Primer_Numero,Segundo_Numero,Tercer_Numero)

G = (Primer_Numero + Segundo_Numero + Tercer_Numero)-Ma-Mi

print("De menor a mayor, el orden es: ", Mi ," , ", G , " , ", Ma) 
      