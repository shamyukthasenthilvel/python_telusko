def binary_search(list,n):
    l=0
    u=len(list)-1
    pos=-1
    while l<=u:
        mid =(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid
    return False


list=[1,2,3,4,5,6,7]
n=6
if binary_search(list,n):
    print("found at",n)
else:
    print("not found")
