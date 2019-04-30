def round(n):
A=(n//10)*10
B=A+10
return(b if n-A>B-n else A)
n=4722
print(round(n))
