def max(arr,l,h):
max=arr[l]
i=l
for i in range(h+1):
if arr[i]>max:
max=arr[i]
return max
arr=[1,30,40,50,60,70,23,20]
n=len(arr)
print("The maximum element is %d"%max(arr,0,n-1))
