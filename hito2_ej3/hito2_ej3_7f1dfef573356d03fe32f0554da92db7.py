x = str(input())
x = list(x)
n = int(input())
d = []
g = []
h = []
for i in range(len(x)) :
  for j in range(n):
    d.append(x[j])
  d = ''.join(d)
  g.append(d)
  d = []
for i in range(len(g)):
  for j in range(len(g)):
    if g[i] != g[j] :
      h.append(g[i])
if h != [] :
  for i in range(len(h)):
    print(h[i])
else :
  print("ninguna")