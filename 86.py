def isogram(word):
clean_word=word.lower()
letter_list=[]
for letter in clean_word:
if letter.isalpha():
if letter in letter_list:
return False
letter_list.append(letter)
return True
if__name__=='__main__':
print(isogram("Machine"))
print(isogram("isogram"))
print(ispgram("list"))
print(isogram("Alphabet"))
