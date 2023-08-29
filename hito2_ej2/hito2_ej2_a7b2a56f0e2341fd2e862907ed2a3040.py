a=input()
b=a.upper()
c=list(b)

if (c.count("A")>=1 or c.count("C")>=1 or c.count("T")>=1 or c.count("G")>=1) and (c.count("B")==0 and c.count("D")==0 and c.count("E")==0 and c.count("F")==0 and c.count("H")==0 and c.count("I")==0 and c.count("J")==0 and c.count("K")==0 and c.count("L")==0 and c.count("M")==0 and c.count("N")==0 and c.count("O")==0 and c.count("P")==0 and c.count("Q")==0 and c.count("R")==0 and c.count("S")==0 and c.count("U")==0 and c.count("V")==0 and c.count("W")==0 and c.count("X")==0 and c.count("Y")==0 and c.count("Z")==0): 
 print("secuencia correcta")
else:
 print("secuencia incorrecta")
