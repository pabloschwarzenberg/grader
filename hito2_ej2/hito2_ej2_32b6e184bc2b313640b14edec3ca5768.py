
def secuencia_dna (secuencia):
   secuencia=int(input())
   bases_correctas=["A","T","C","G"]
   secuencia=secuencia.upper()
   prueba=True
   for base in secuencia:
     if base in bases_correctas:
       prueba=True
     else:
       prueba=False
       break
   if prueba==True:
     print ("secuencia correcta")
   else:
     print ("secuencia incorrecta")