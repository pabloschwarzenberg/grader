string=input()
x=int(len(string))
q=string.replace("a", "apa")
w=q.replace("e", "epe")
e=w.replace("i", "ipi")
r=e.replace("o", "opo")
t=r.replace("u", "upu")

def jerigonzo(string):
    if string.count("a")>0:
       for a in range(0, x):
           return(t)
    if string.count("e")>0:
       for e in range(0, x):
           return(t)
    if string.count("i")>0:
       for i in range(0, x):
           return(t)
    if string.count("o")>0:
       for o in range(0, x):
           return(t)
    if string.count("u")>0:
       for u in range(0, x):
           return(t)

print(jerigonzo(string))    
