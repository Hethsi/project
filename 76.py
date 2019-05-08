def isComposite(N):
if (N<=1):
return False
if(n<=3):
return True
i=5
while(i*i<=N):
if(N%i==0 or N%(i+2)==0):
return True
i=i+6
return False
print("")
print("True")if(isComposite(11))else print("false")
print("True")if(isComposite(15))else print("False")
