def R(x):
 s=len(x)
 r=[]
 for i in range(s):
  k=i+1
  for j in range(k,s):
   if x[i]==x[j] and x[i] not in r:
    r.append(x[i])
  return r
  l1=[10,20,30,20,20,30,40,50,-20,60,-20,-20]
  print(R(l1))
