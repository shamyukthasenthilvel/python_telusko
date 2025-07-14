class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1 =self.m1+other.m1
        m2 =self.m2+other.m2
        m3 =Student(m1,m2)
        return m3
    def __str__(self):
        return'() ()'.format( self.m1,self.m2)

s1=Student(50,100)
s2=Student(10,20)
sum =s1+s2
print(sum.m1,end=" \n")
print(sum.m2)
print(s2)

