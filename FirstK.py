def s(N,K):
an=0
for i in range(1,N+1):
an+=(i%K)
return an
N=10
K=2
print(sum(N,K))
