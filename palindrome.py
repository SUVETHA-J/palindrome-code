#to check wheter the string is palindrome or not
string=input("enter a string")
rev=string[::-1]
if(string==rev):
    print("given string is palindrome:",rev)
else:
    print("given string is not a palindrome")
