class Human:
    
    def shamy(self):
        num=1
        while num<=10:
            sq = num*num
            yield sq
            num+=1
values =Human()
for i in values.shamy():
    print(i)
