
0:
1
1)
from random import
def ocultar_letras(palabra,cantidad):
acumula = []
randint
palabra = "maquina"
palabra = list
(palabra)
while cantidad !=
  
x = randint(
1,
len(palabra)-
 
if x not
in acumula:
acumula.append(x)
cantidad-=
palabra[x] =
"_"
palabra = ""
.join(palabra)
return palabra
    def revisar_letra(palabra_secreta,palabra,letra):
  x = list(palabra_secreta)
  palabra = list
(palabra)
 if letra in x:
   y = palabra_secreta.find(
"-"
)
 palabra[y] = letra
  palabra = ""
.join(palabra)
 print(palabra)
 return palabra