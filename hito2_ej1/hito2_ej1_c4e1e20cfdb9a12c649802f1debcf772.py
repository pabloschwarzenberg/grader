 def alineamiento(sec1,sec2):
   for i in range(len(sec2)):
      if sec[i] == sec2[i]:
          tempSegment += sec1[i]
      else: tempSegment = ""
  
      if len(tempSegment) > len(longestSegment):
          longestSegment = tempSegment
   return longestSegmen
