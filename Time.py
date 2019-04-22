def convert(minutes):
min=sec//60
sec%=60
sec=sec%(24*3600)
h=sec//3600
sec%=3600
return "%d:%02d:%02d" %(h,min,sec)
n=12345
print(convert(n))
