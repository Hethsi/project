my_arr=arr[]
c=int(input("How many numbers you want to add:"))
for i in range(1,c+1):
my_arr.append(int(input("Enter number{}:".format(i))))
print("Input Numbers:")
print(my_arr)
min=my_arr[0]
max=my_arr[0]
for no in my_arr:
 if no<min:min=no elif no>max:
  max=no
print("Minimum number:{},Maximum number:{}".format(min,max))
