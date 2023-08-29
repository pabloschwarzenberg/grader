#Ordenar tres números

#ingrese 3 numeros enteros
numuno=int(input("ingrese el primer numero: "))
numdos=int(input("ingrese el segundo numero: "))
numtres=int(input("ingrese el tercer numero: "))
if numuno>numdos>numtres:
    print(numtres, "," ,numdos, "," ,numuno)

if numuno<numdos<numtres:
    print(numuno, "," ,numdos, "," ,numtres)
    
if numdos<numtres<numuno:
    print(numdos, "," ,numtres, "," ,numuno)

if numtres<numuno<numdos:
    print(numtres, "," ,numuno, "," ,numdos)

if numuno<numdos>numtres and numuno<numtres:
    print(numuno, "," ,numtres, "," ,numdos)
    
if numtres>numuno>numdos:
    print(numdos, "," ,numuno, "," ,numtres)

if numuno==numdos==numtres:
    print(numuno, "," ,numdos, "," ,numtres)
    
if numuno==numdos>numtres:
    print(numtres, "," ,numuno, "," ,numdos)
    
if numdos==numtres>numuno:
    print(numuno, "," ,numdos, "," ,numtres)
    
if numuno==numtres>numdos:
    print(numdos, "," ,numuno, "," ,numtres)
    
if numuno==numdos<numtres:
    print(numuno, "," ,numdos, "," ,numtres)
    
if numdos==numtres<numuno:
    print(numdos, "," ,numtres, "," ,numuno)
    
if numuno==numtres<numdos:
    print(numuno, "," ,numtres, "," ,numdos)