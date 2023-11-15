n=int(input("enter number of students:"))
result={}
for i in range(n):
     print("enter the details of student no",i+1)
     rno=int(input("roll no:"))
     name=input("name:")
     age=int(input("age:"))
     marks=int(input("mark:"))
     grade=input("Grade:")
     address=input("Address:")
     result[rno]=[name,age,marks,grade,address]
     print(result)
