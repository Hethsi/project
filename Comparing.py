s1=input("Enter the first string:")
s2=input("Enter the second string:")
c1=0
c2=0
for i in s1:
 c1=c1+1
for j in s2:
 c2=c2+1
if(c1<c2):
 print("Larger string is:")
 print(s2)
elif(c1==c2):
 print("Both are equal")
 print(c1)
else;
 print("Larger string is:")
 print(s1)
