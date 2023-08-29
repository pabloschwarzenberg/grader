x=int(input())
y=int(input())
z=int(input())
if x!=z and z!=y and x!=y:
    if x<y and x<z and (x<y<z or z<y<x):
     print(""+str(x)+","+str(y)+","+str(z)+"")
    elif y<x and y<z and (y<x<z or z<x<y):
     print(""+str(y)+","+str(x)+","+str(z)+"")
    elif z<x and z<y and (x<y<z or z<y<x):
     print(""+str(z)+","+str(y)+","+str(x)+"")
    elif x<y and x<z and (x<z<y or y<z<x):
     print(""+str(x)+","+str(z)+","+str(y)+"")
    elif y<x and y<z and (y<z<x or x<z<y):
     print(""+str(y)+","+str(z)+","+str(x)+"")
    elif z<x and z<y and (y<x<z or z<x<y):
     print(""+str(z)+","+str(x)+","+str(y)+"")
if x==y and y!=z:
    if x<z:
        print(""+str(y)+","+str(x)+","+str(z)+"")
    if x>z:
          print(""+str(z)+","+str(y)+","+str(x)+"")
if x==z and x!=y:
    if x<y:
         print(str(z),str(x),str(y))
    if x>y:
         print(""+str(y)+","+str(x)+","+str(z)+"")
if y==z and x!=y:
    if z<x:
         print(""+str(z)+","+str(y)+","+str(x)+"")
    if z>x:
        print(""+str(x)+","+str(y)+","+str(z)+"")