class solution(object):
def reverse(self,a):
type a:int
negative=False
if(a<0):
a=a*-1
negative=True
else:
a=a
sum=0
dig=1
strx=str(a)
l=list(stra)
for i in l:
sum+=int(i)*dig
dig*=10
if(abs(sum)>2**32):
return 0
elif(negative==True):
return sum*-1
else:
return sum
