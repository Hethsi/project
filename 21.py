def sum1(b,c,a):
sum=0
i=0
while i<a:
 sum=sum+b
 b=b+c
 i=i+1
 return sum
a=int(input("Enter n1:"))
b=int(input("Enter n2:"))
c=int(input("Enter n3:"))
print(sum1(b,c,a))
