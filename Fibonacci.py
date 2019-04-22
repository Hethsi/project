A=int(input("Enter the first number:"))
B=int(input("Enter the second number:"))
n=int(input("Enter the number of terms"))
print(A,B,end=" ")
while(n-2):
C=A+B
A=B
B=C
print(C,end=" ")
n=n-1
