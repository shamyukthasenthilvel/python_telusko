#postion in formal argument
def person(name,age):
    print(name)
    print(age)
person("shamy",20)

#keyword in formal argument
def person1(name,age):
    print(name)
    print(age)
person1(age=20,name="shamy")

#default in formal argument
def person2(name,age=19):
    print(name)
    print(age)
person2("shamy")

#variable length in formal argument

def sum(*b):
    c=0

    for i in b:
        c+=i
    print(c)
sum(2,3,4)

#keyword args
def person3(name,**data):
    print(name)
    for i ,j in data.items():
        print(i,j)

person3('shamy',age=19,dob=2005)
