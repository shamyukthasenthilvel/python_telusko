def update(x):
    print(id(x))

    x=8
    print(id(x))
# its for immutable same memory location untill any change after change it will change the address does not affect the ones
a=10
print(id(a))
update(a)

#mutable -> it will not change the address just modify it
def update1(list1):
    print(id(list1))

    list1[1]=20
    print(id(list1))
list1=[1,2,3]
print(id(list1))
update1(list1)