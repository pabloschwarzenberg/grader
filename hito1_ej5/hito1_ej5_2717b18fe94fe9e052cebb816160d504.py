#Cálculo del dígito verificador de un rut
      
num = [2, 3, 4, 5, 6, 7, 2, 3]
rut = input("Ingrese rut: ")
rutlist = list(rut)
rutlist.reverse()

n =- 1
x = 0
for i in rutlist:
	i_int =int(i)

	n+=1
	num_pos=num[n]
	num_pos_int=int(num_pos)

	x+= (i_int * num_pos_int)

mdv = x % 11

dv = 11 - mdv

if(dv==10):
	dv='K'
elif(mdv==0):
	dv=mdv
else:
	pass
  
print("dv=", dv)