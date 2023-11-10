def power(b,e):
    if  e==0:
       return 1
    elif e==1:
       return b
    else:
       return b*power(b,e-1)
b=int(input("enter the number:  "))
e=int(input("enter the exponent:   "))
print(power(b,e))
