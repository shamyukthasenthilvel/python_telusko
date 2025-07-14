a=10
def some():
    a=5 
    print("inside ",a)
some()
print("outside",a)

#####################

#global keyword
a=10
def some1():
    global a
    print("inside ",a)
some1()
print("outside",a)

######################

#globals()

a=10
print(id(a))
def some2():

    x=globals()['a']
    print(id(x))
    print("inside ",x)
some2()
print("outside",a)
