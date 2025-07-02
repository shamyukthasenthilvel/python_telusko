import array as arr
mine = arr.array('i',[])
num = int(input("enter the no.of element"))
for i in range(num):
    x = int(input("enter the no.of element"))
    mine.append(x)
print(mine)

val=int(input("enter the value to search"))
k=0
for i in mine:
    if i == val:
        print(k)
        break

    k=k+1
print(mine.index(val))