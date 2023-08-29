num = int(input("Ingrese rut SIN DV: ")) #20023066  
#1) Dar vuelta el número
strnum = str(num)[::-1] #eje: 66032002

#2) multiplicar cada digito por la serie 2, 3, 4, 5, 6, 7 , 2, 3, ....
uno= int(strnum[0])*2 #6*2
dos= int(strnum[1])*3 #6*3
tre= int(strnum[2])*4 #0*4
cua= int(strnum[3])*5 #3*5
cin= int(strnum[4])*6
sei= int(strnum[5])*7
sie= int(strnum[6])*2
if (len(strnum)== 8):
  och= int(strnum[7])*3  #2*3
else:
  och = 0

#3) Sumamos todos los resultados:
suma = uno + dos + tre + cua + cin + sei + sie + och


#4) Obtener el resto de la división de suma anterior por 11:
resto = suma%11


#5) a 11 le restamos el resto:
dv = 11 - resto

print(dv)
if (dv==10):
  dv = 'k'
if (dv == 11):
  dv = 0

print("dv =",dv)
      