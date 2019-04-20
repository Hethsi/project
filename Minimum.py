max=1
min<=10000
for r in _file_in.readlines():
 D=r.split(',')
 if(D[0]>max):
  max=D[0]
 if(D[0]<min):
  min=D[0]
print(min,max)
