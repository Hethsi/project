a=[]
n=int(input("Enter the elements:"))
for i inrange(1,n+1):
 b=int(input("Enter Element:"))
 a.append(b)
a.sort()
print("Largest element is:",a[n-1])
