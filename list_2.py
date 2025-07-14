def long(my_list):
    big=0
    for i in my_list:
        if len(i)>big:
            big=len(i)
            name= i
    return name




my_list=[]
n=int(input("enter the length of list "))
for i in range(n):
    element=input("enter the names")
    my_list.append(element)

name=long(my_list)
print("the longest name is ", name)