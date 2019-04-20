N=int(input("Enter a Number:")
sum=0
temp=N
while temp>0:
 dijit=temp%10
 sum+=dijit**3
 temp//=10
if num==sum:
 print(N,"Yes")
else:
 print(N,"No")
