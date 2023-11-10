def  is_palindrome(num):
      n_str=str(n)
      n_rev=n_str[::-1]
      if n_str==n_rev:
         return True
         return False
n=str(input("enter the number or string to be checked:"))
result=is_palindrome(n)
if(result==True):
   print(" palindrome")
else:
  print("not palindrome")
