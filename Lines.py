P=input("Enter the paragraph:")
num_lines=0
with open(P,'r')as f:
 for line in f:
  num_lines+=1
print("Number of lines in a paragraph:")
print(num_lines)
