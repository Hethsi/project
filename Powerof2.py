def power(N):
 if N<=0:
  return False
 else:
  return N & (N-1)==0
 N=int(input("Enter the number"))
 if power(N):
  print("Is a power of two".format(N))
 else:
  print("It is not a power of two".format(N))
