def V(s)
 letter=False
 number=False
 for i in s:
  if i.isalpha():
   letter=True
  if i.isdigit():
   number=True
 return letter and number
print V("Has Alphanum23")
print V("Some String")
