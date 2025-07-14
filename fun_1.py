def greet():
    print("hello malli")
greet()

def add(x,y):
    c=x+y
    #print(c)
    return c
result =add(10,20)
print("the sum is" ,result)

def add_sub(x,y):
    c=x+y
    d=x-y
    #print(c)
    return c,d
result1,result2 =add_sub(10,20)
print("the sub is" ,result2)