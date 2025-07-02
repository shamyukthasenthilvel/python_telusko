import array as arr
my_list=arr.array('i',[12,6,9,83,85,4,53])
n=len(my_list)
for i in range(n):
    for j in range(n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
for i in my_list:
    print(i)