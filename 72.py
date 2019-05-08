def check(string):
v=set("aeiou")
s=set({})
for char in string:
if char in vowels:
s.add(char)
else:
pass
if len(s)==len(vowels):
print("Accepted")
if__name__=="__main__":
string="seequial"
string=string.lower()
check(string)
