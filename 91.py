def cuboid(1,h,w):
return(l*h*w)
def scuboid(l,h,w):
return(2*1*w+2*w*h+2*1+h)
l=1
h=5
w=7
print("V=",cuboid(l,h,w))
print("total surface area=",scuboid(l,h,w))
