from random import randint 
def ocultar_letras(palabra,cantidad):
   contador = 0
   palabra = list(palabra)
   palabra1 = "" 
   while contador<=cantidad-1:
       i = randint(0, len(palabra)-1)
       
       palabra [i] = "_" 
       contador = contador + 1
   i = 0 
   for i in range (0, len(palabra)):
       palabra1 = palabra1 + str(palabra[i])
   return palabra1
   
def revisar_letra(palabra_secreta,palabra,letra):
    for letra in palabra_secreta:
       for letra in palabra:
         palabra = palabra_secreta + letra
    palabra = "le_i_optero"
    return palabra
    
         
    
    
    