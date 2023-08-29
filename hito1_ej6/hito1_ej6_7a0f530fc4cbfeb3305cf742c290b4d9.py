var1 = int(input("var1:"))
var2 = int(input("var2:"))
var3 = int(input("var3:"))
aux = 0 

if(var1<=var2):
	if(var2<=var3):
		pass
	else:
		aux = var3
		var3 = var2
		var2 = aux
		if(var1<=var2):
			pass
		else:
			aux = var2
			var2 = var1
			var1 = aux
else:
	aux = var2
	var2 = var1
	var1 = aux
	print (var1,var2,var3)
	if(var2<=var3):
		pass
	else:
		aux = var3
		var3 = var2
		var2 = aux
		if(var1>=var2):
			aux = var2
			var2 = var1
			var1 = aux

print(var1,',' ,var2,',' ,var3)