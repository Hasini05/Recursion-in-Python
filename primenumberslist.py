def prime(n,i=2):
    if n<2:
        return False
    if i*i>n:
        return True
    if n%i==0:
        return False
    return prime(n,i+1)
def fun(l,i=0):
    if i==len(l):
        return 0
    if prime(l[i]):
         print(l[i], end=' ')
    fun(l,i+1)
l=list(map(int,input().split()))
fun(l)