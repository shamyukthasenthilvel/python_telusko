def search(list, n):
    pos=0
    for i in range(len(list)):
        if list[i]==n:
            pos =i
            return True
    return False

list=[1,2,3,4,5,6,7]
n=6
if search(list,n):
    print("found at",n)
else:
    print("not found")