a=int(input())
if 999<a:
  m=int(a//1000)
  c=int((a-(m*1000))//100)
  d=int((a-((m*1000)+(c*100)))//10)
  u=int((a-((m*1000)+(c*100)+(d*10)))//1)
  print(str(m) + "M + " + str(c) + "C + " + str(d) + "D + " + str(u) + "U")
if 99<a:
  m=int(a//1000)
  c=int((a-(m*1000))//100)
  d=int((a-((m*1000)+(c*100)))//10)
  u=int((a-((m*1000)+(c*100)+(d*10)))//1)
  print(str(c) + "C + " + str(d) + "D + " + str(u) + "U")
if 9<a:
  m=int(a//1000)
  c=int((a-(m*1000))//100)
  d=int((a-((m*1000)+(c*100)))//10)
  u=int((a-((m*1000)+(c*100)+(d*10)))//1)
  print(str(d) + "D + " + str(u) + "U")
if 0<a:
  m=int(a//1000)
  c=int((a-(m*1000))//100)
  d=int((a-((m*1000)+(c*100)))//10)
  u=int((a-((m*1000)+(c*100)+(d*10)))//1)
  print(str(u) + "U")

      