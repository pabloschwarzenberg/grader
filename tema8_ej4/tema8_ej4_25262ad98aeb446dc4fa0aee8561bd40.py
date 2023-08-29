def rot13(palabra):
	abc = "abcdefghijklmnopqrstuvwxyz"
	abc13 = "nopqrstuvwxyzabcdefghijklm"
	out = ""
	aux = palabra
	for i in palabra:
		posicion = abc.index(i)
		pos_abc = abc13.index(i)
		print(pos_abc)
			
		out = out + abc[pos_abc]
		aux = aux[:posicion] + "_" + aux[posicion+1:]


	return out



palabra="hola"
palabra.lower()
resultado=rot13(palabra)
print("El resultado es: ",resultado)