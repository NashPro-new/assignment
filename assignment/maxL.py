def max_losses_wins(team, rep):
  max_count=-1
  i=0
  while(i<len(team)):
    if(team[i] !=rep):
      i+=1
    else:
      j=i
      current_count=0
      while(j < len(team) and team[j]==rep):
        current_count+=1
        j+=1
      if(current_count > max_count):
        max_count = current_count
      i=j
  return(max_count)