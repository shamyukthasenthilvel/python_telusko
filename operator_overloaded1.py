class Human:
    def display(self,*args):
        if len(args) ==1:
            print("sham")
        elif len(args) == 2:
            print("abi")
        else:
            print("anu")
    def mul(self,a=None,b=None):
        if a !=None and b !=None:
            return a*b
        if a==None or b==None:
            if a==None:
                return b
            else:
                return a
obj1 =Human()
obj1.display(2)
result =obj1.mul(4,6)
print(result)
    
    