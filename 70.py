def power(A):
if(A&not(A&(A-1))):
return A
while(A!=0):
A>>=1
count+=1
return 1<<cout
A=int(input("Enter the number:"))
print(power(A))
