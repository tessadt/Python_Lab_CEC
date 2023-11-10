def fact(n):
  if n == 1:
     return n
  elif n==0:
     return 1
  else:
     return n*fact(n-1) 
number = int(input("User Input : "))
result=fact(number)
print("The factorial of", number, "is", fact(number))

