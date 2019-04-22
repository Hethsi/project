s=input("Enter the string:")
a=d=spcl=0
for i in range(len(s)):
 if(s[i].isa()):
  a=a+1
 elif(s[i].isd()):
  d=d+1
 else:
  spcl=spcl+1
print("\nTotal number of Alphabets are:",a)
print("\nTotal number of Digits are:",d)
print("\nTotal number of Special Characters are:",spcl)
