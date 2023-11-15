dic={}
n1=int(input("Total number of elements in dictionary: "))
for i in range(n1):
    dic[i]=input("Enter name : ")
print(" In Ascending order:")
print(sorted(dic.items(), key = lambda x:(x[1], x[0])))
print("In Descending order:")
print(sorted(dic.items(), key = lambda x:(x[1], x[0]), reverse=True))

