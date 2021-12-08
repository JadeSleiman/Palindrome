#check if palindrome or not
#1 true , 1 false, 1 wrong that replys message "Sorry, that is not a good input, we take String only, try again!"

def Palindrome(s):  #calls the function 

 return s == s[::-1]

n = (20)

#test case
s1 = "abcdefghijkjihgfedcba"
s2 = "abcdefghijklmnopqrstu"
s3 = "123"
ans = Palindrome(s1)
ans = Palindrome(s2)
ans = Palindrome(s3) 

#test
if (ans):
  print("is a palindrome")
elif n != 20:
  print("Sorry, that is not a good input, we take String only, try again!")
else:
  print("is not a palindrome")


