N=int(input("Enter the number:"))
M=int(input("Enter the number:"))
c=N+M
root=math.sqrt(c)
if int(root+0.5)**2==c:
print("Yes")
else:
print("No")
