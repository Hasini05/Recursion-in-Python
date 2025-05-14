def palindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return palindrome(s[1:-1])
n=input("Enter a string: ")
if palindrome(n):
    print("Palindrome")
else:
    print("Not a palindrome")