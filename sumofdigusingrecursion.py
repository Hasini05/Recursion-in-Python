n=int(input())
def sum(n):
    if n==0 or n==1:
        return n
    else:
        return n%10+sum(n//10)
print(sum(n))