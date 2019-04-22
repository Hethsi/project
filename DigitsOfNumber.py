while True:
 try:
  number=int(input("Enter three digit number:"))in range(99,1000)
  break
 except valueError:
  print(Enter a three digit number:")
  continue
number=str(number)
print("Your digits are:",number[0],number[1],number[2])
