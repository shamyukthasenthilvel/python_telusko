def count(my_list):
    even =0
    odd=0
    for i in my_list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

n=int(input("enter the size of hte list"))
my_list =[]

for i in range(n):
    element=int(input("enter the element"))
    my_list.append(element)
even , odd=count(my_list)
print(even,"   " ,odd)