def gcd(a,b):
if(a==b):
return a
if(a>b):
 return gcd(a-b,b)
 return gcd(a,b-a)
 def lcm(a,b):
 return(a*b)/gcd(a,b)
 a=int(input("a is:"))
 b=int(input("b is:"))
 print('LCM of',a,'and',a,'is',lcm(a,b))
