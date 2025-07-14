n = int(input("enter the num"))
my_list=[0,1]
for i in range(2,n):
    element=my_list[i-1]+my_list[i-2]
    my_list.append(element)
print(my_list)

####################################

a=0
b=1
print(a)
print(b)
for i in range(2,10):
    c=a+b
    print(c)
    a=b
    b=c
#####################################

#assignment 2

a=0
b=1
print(a)
print(b)
for i in range(2,10):
    c=a+b
    if c<10:
        print(c)
        a=b
        b=c
    else:
        break


