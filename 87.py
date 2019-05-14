def g(n,m):
 if(n==0):
  return n
 else:
  return g(m,n%m)
n=int(input("Enter n:"))
m=int(input("Enter m:"))
print("The answer is:",end="")
print(g(n,m))
