def fun(i,n):
    if i>n:
        return
    print(i,end=' ')
    fun(i+1,n)
    if i!=n:
        print(i,end=' ')
n=int(input())
fun(1,n)

'''def fun(n):      #This code is for printing 5 4 3 2 1
    if n==0:
        return
    print(n,end=' ')
    fun(n-1)
n=5
fun(n)'''


'''def fun(n):      #This code is for printing 1 2 3 4 5
    if n==0:
        return
    fun(n-1)
    print(n,end=' ')
n=5
fun(n)'''