y=int(input("Enter The Year:"))
if(y%4==0 and y%100!=0 or y%400==0):
 print("The Year Is a Leap Year!)
else:
 print("The Year Is Not a Leap Year!")
