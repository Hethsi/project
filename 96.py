import math
def sum(a,d,b,r,n):
sum=0
for i in range(1,n+1):
sum1+=((a+(i-1)*d)*(b*math.pow(r,i-1)))
a=1
d=1
b=2
r=2
n=3
print(sum1(a,d,b,r,n))
