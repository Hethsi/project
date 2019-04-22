import time,random
def qu_ben(n=2**24):
 def q(a,l,h):
  if l<h:
   p=par(a,l,h)
   q(a,l,p)
   q(a,p+1,h)
def par(a,l,h):
 piv_in(=r.ran(l,h)
 piv=a[piv_in]
 i=l-1
 j=h+1
 while True:
  j-=1
  if a[j]<=piv:
   break
 if i>=j:
  return j
 temp=a[i]
 a[i]=a[j]
 a[j]=temp
start=time.time()
a=[r.ran(0,n)for i in range(0,n)]
q(a,0,len(a)-1)
end=time.time()
elapsed=end-start
return(elapsed)
