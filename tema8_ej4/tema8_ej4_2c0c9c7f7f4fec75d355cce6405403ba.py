def rot13(pal):
	rot=[]
	i=0
	while i<len(pal):
		if pal[i]=="a":
			rot.append("n")
		if pal[i]=="b":
			rot.append("o")
		if pal[i]=="c":
			rot.append("p")
		if pal[i]=="d":
			rot.append("q")
		if pal[i]=="e":
			rot.append("r")
		if pal[i]=="f":
			rot.append("s")
		if pal[i]=="g":
			rot.append("t")
		if pal[i]=="h":
			rot.append("u")
		if pal[i]=="i":
			rot.append("v")
		if pal[i]=="j":
			rot.append("w")
		if pal[i]=="k":
			rot.append("x")
		if pal[i]=="l":
			rot.append("y")
		if pal[i]=="m":
			rot.append("z")
		if pal[i]=="n":
			rot.append("a")
		if pal[i]=="o":
			rot.append("b")
		if pal[i]=="p":
			rot.append("c")
		if pal[i]=="q":
			rot.append("d")
		if pal[i]=="r":
			rot.append("e")
		if pal[i]=="s":
			rot.append("f")
		if pal[i]=="t":
			rot.append("g")
		if pal[i]=="u":
			rot.append("h")
		if pal[i]=="v":
			rot.append("i")
		if pal[i]=="w":
			rot.append("j")
		if pal[i]=="x":
			rot.append("k")
		if pal[i]=="y":
			rot.append("l")
		if pal[i]=="z":
			rot.append("m")
		i+=1
	rot="".join(rot)
	return rot